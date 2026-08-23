"""Behaviour of the sweep engine, offline.

Almost everything here is unreachable from a live run: you cannot provoke a
page-cap exhaustion, a malformed timestamp, or a truncated hard-capped listing
against a working backend without breaking it first. That is exactly why these
are the cases worth pinning -- they are the ones where a bug renders as "nothing
to clean" and nobody notices.

Each test names the sabotage that must make it fail. A test that cannot be made
to fail is not carrying its weight.
"""

from __future__ import annotations

import dataclasses
import datetime
import json
from typing import Any, Dict, List, Mapping, Optional, Sequence

import pytest
from gc_e2e_janitor import registry, sweep
from gc_e2e_janitor import report as report_mod
from gc_e2e_janitor.sweep import Limits, SweepAborted, parse_timestamp
from gc_e2e_janitor.transport import Response, TransportError

UTC = datetime.timezone.utc
UUID = "3f2504e0-4f89-11d3-9a0c-0305e82c3301"
IDENTITY = "sdk-e2e-test-service-account"


def iso(**delta: float) -> str:
    return (datetime.datetime.now(UTC) + datetime.timedelta(**delta)).isoformat().replace("+00:00", "Z")


OLD = dict(hours=-48)
FRESH = dict(minutes=-1)


@dataclasses.dataclass
class Call:
    method: str
    path: str
    json: Optional[Any]
    params: Optional[Mapping[str, Any]]


class FakeClient:
    """Records every request and serves canned responses per path.

    Deliberately the same three-argument shape as the fake in
    test_e2e_cleanup.py, so the two suites read alike.
    """

    def __init__(self) -> None:
        self.calls: List[Call] = []
        self._handlers: Dict[str, Any] = {}

    def on(self, path: str, handler: Any) -> "FakeClient":
        """handler is a Response, an exception, or f(call) -> Response."""
        self._handlers[path] = handler
        return self

    def serve_rows(
        self, spec: registry.Kind, rows: Sequence[Mapping[str, Any]], *, honour_paging: bool = True
    ) -> "FakeClient":
        route = spec.list_route

        def handler(call: Call) -> Response:
            window = dict(call.params or {})
            window.update(call.json or {})
            page = list(rows)
            if honour_paging and route.page_size:
                skip = int(window.get("skip", 0))
                page = page[skip : skip + int(window.get("limit", route.page_size))]
            payload: Any = page if route.container is None else {route.container: page}
            return Response(200, json.dumps(payload).encode())

        return self.on(route.path, handler)

    @property
    def deletes(self) -> List[Call]:
        return [c for c in self.calls if c.method == "DELETE"]

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
    ) -> Response:
        call = Call(method, path, json, params)
        self.calls.append(call)
        handler = self._handlers.get(path)
        for template, candidate in self._handlers.items():
            if handler is None and "{" not in template and path.startswith(template.rstrip("/") + "/"):
                handler = candidate
        if handler is None:
            return Response(200, b"[]")
        if isinstance(handler, Response):
            return handler
        if isinstance(handler, Exception):
            raise handler
        return handler(call)


def run_kind(client: FakeClient, kind: str, **kwargs: Any) -> sweep.SweepReport:
    params: Dict[str, Any] = dict(
        kinds=[kind],
        age_minutes=60,
        apply=True,
        identity=None,
        limits=Limits(),
        backend_id="backend-dev",
        base_url="https://api.test",
    )
    params.update(kwargs)
    return sweep.run(client, **params)


# ----------------------------------------------------------------------- timestamps


@pytest.mark.parametrize(
    "value",
    [
        None,
        "",
        "   ",
        "not-a-date",
        123,
        [],
        {},
        # Go's zero value for a non-pointer time.Time. It parses cleanly and is
        # ~2000 years old, so without the sanity floor it sails past any cutoff
        # straight into the delete list.
        "0001-01-01T00:00:00Z",
        "1970-01-01T00:00:00Z",
        # Beyond clock-skew tolerance: nonsense, therefore unknown.
        (datetime.datetime.now(UTC) + datetime.timedelta(days=2)).isoformat(),
    ],
)
def test_untrustworthy_timestamps_read_as_unknown_not_ancient(value: Any) -> None:
    """Sabotage: drop the SANITY_FLOOR check -> the zero-time cases return a
    datetime and every unset timestamp becomes a delete candidate."""
    assert parse_timestamp(value) is None


@pytest.mark.parametrize(
    "value",
    [
        "2026-08-01T10:00:00Z",
        "2026-08-01T10:00:00.123Z",
        "2026-08-01T10:00:00.123456Z",
        # Go's RFC3339Nano emits 9 fractional digits; fromisoformat takes 6.
        "2026-08-01T10:00:00.123456789Z",
        "2026-08-01T10:00:00+00:00",
        "2026-08-01T12:00:00+02:00",
    ],
)
def test_real_server_timestamp_formats_parse(value: str) -> None:
    """Sabotage: call datetime.fromisoformat directly -> every Z form and the
    9-digit fraction raise, and on 3.9 the 3-digit fraction does too."""
    parsed = parse_timestamp(value)
    assert parsed is not None and parsed.tzinfo is not None


def test_naive_timestamps_are_utc_not_runner_local(monkeypatch: pytest.MonkeyPatch) -> None:
    """A resource must not age differently depending on where the job ran.

    Sabotage: drop the tzinfo=UTC default -> this fails under TZ=America/New_York.
    """
    import time

    monkeypatch.setenv("TZ", "America/New_York")
    if hasattr(time, "tzset"):
        time.tzset()
    try:
        assert parse_timestamp("2026-08-01T10:00:00") == datetime.datetime(2026, 8, 1, 10, 0, tzinfo=UTC)
    finally:
        monkeypatch.delenv("TZ", raising=False)
        if hasattr(time, "tzset"):
            time.tzset()


def test_a_resource_exactly_at_the_cutoff_is_not_swept() -> None:
    """Strict inequality. Off-by-one here eats a live run's resources."""
    spec = registry.KINDS["dashboard"]
    report = sweep.KindReport(kind="dashboard")
    cutoff = datetime.datetime.now(UTC) - datetime.timedelta(minutes=60)
    row = {"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": cutoff.isoformat()}
    assert sweep.classify(spec, [row], cutoff, None, report) == []
    assert report.too_young == 1


def test_an_unreadable_age_is_counted_not_silently_skipped() -> None:
    """A backend that stopped emitting the timestamp would otherwise turn the
    janitor into a permanent no-op that reports success forever.

    Sabotage: skip without incrementing unknown_age -> determinate stays True and
    the run reports `ok`.
    """
    spec = registry.KINDS["dashboard"]
    report = sweep.KindReport(kind="dashboard", list_ok=True, pagination_complete=True)
    cutoff = datetime.datetime.now(UTC) - datetime.timedelta(minutes=60)
    row = {"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": "nonsense"}

    assert sweep.classify(spec, [row], cutoff, None, report) == []
    assert report.unknown_age == 1
    assert not report.determinate


def test_age_uses_the_most_recent_of_created_and_updated() -> None:
    """A resource someone is actively editing is fresh even if created long ago."""
    spec = registry.KINDS["dashboard"]
    report = sweep.KindReport(kind="dashboard")
    cutoff = datetime.datetime.now(UTC) - datetime.timedelta(minutes=60)
    row = {
        "uuid": "d1",
        "name": "e2e-test-dashboard-" + UUID,
        "createdTimestamp": iso(**OLD),
        "updatedTimestamp": iso(**FRESH),
    }
    assert sweep.classify(spec, [row], cutoff, None, report) == []
    assert report.too_young == 1


# ------------------------------------------------------------------------ paging


def test_pages_past_a_capped_list_response() -> None:
    """Sabotage: fetch one page only -> the resource on page 3 is never seen and
    the sweep reports the tenant clean."""
    spec = registry.KINDS["silence"]
    rows = [{"id": "s%d" % i, "comment": "unrelated-%d" % i, "createdAt": iso(**OLD)} for i in range(2500)]
    rows[2400] = {"id": "target", "comment": "e2e-test-silence-" + UUID, "createdAt": iso(**OLD)}
    client = FakeClient().serve_rows(spec, rows)

    report = run_kind(client, "silence", apply=False).kinds["silence"]
    assert report.listed == 2500 and report.matched == 1
    assert report.pages_fetched == 3 and report.pagination_complete


def test_paging_stops_on_a_short_page() -> None:
    spec = registry.KINDS["silence"]
    rows = [{"id": "s%d" % i, "comment": "x", "createdAt": iso(**OLD)} for i in range(1500)]
    client = FakeClient().serve_rows(spec, rows)
    run_kind(client, "silence", apply=False)
    assert len([c for c in client.calls if c.path == spec.list_route.path]) == 2


def test_exhausting_the_page_cap_refuses_to_conclude_and_deletes_nothing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A server that ignores `skip` must not yield a partial listing plus a
    delete pass -- that is strictly worse than not running.

    Sabotage: set pagination_complete = True at the cap -> status becomes `ok`
    off an incomplete listing.
    """
    monkeypatch.setattr(sweep, "MAX_PAGES", 3)
    spec = registry.KINDS["silence"]
    rows = [{"id": "s%d" % i, "comment": "e2e-test-silence-" + UUID, "createdAt": iso(**OLD)} for i in range(5000)]
    client = FakeClient().serve_rows(spec, rows, honour_paging=False)

    result = run_kind(client, "silence")
    assert result.kinds["silence"].pages_fetched == 3
    assert not result.kinds["silence"].pagination_complete
    assert result.status == "partial" and result.exit_code == 2


def test_get_listers_page_in_the_query_string_and_post_listers_in_the_body() -> None:
    """Sabotage: always page in the body -> the GET handler never sees limit/skip,
    silently returns page 1 forever, and the sweep loops to the page cap."""
    silence = registry.KINDS["silence"]
    client = FakeClient().serve_rows(silence, [])
    run_kind(client, "silence", apply=False)
    call = client.calls[0]
    assert call.method == "GET" and call.params["limit"] == 1000 and call.params["skip"] == 0
    assert call.json is None


def test_a_hard_capped_listing_at_its_cap_is_not_treated_as_complete() -> None:
    """GET /api/agent/skills takes no skip or cursor, so a full-length response
    and a truncated one look identical.

    Sabotage: model hard_cap as page_size -> the sweep silently handles only the
    first 250 skills and calls it done.
    """
    spec = registry.KINDS["agent-skill"]
    rows = [{"id": "k%d" % i, "name": "x%d" % i, "created_at": iso(**OLD)} for i in range(250)]
    result = run_kind(FakeClient().serve_rows(spec, rows), "agent-skill", apply=False)
    assert not result.kinds["agent-skill"].pagination_complete
    assert result.status == "partial"


def test_a_hard_capped_listing_below_its_cap_is_complete() -> None:
    """Guards the previous test against being satisfied by 'always refuse'."""
    spec = registry.KINDS["agent-skill"]
    rows = [{"id": "k1", "name": "x", "created_at": iso(**OLD)}]
    result = run_kind(FakeClient().serve_rows(spec, rows), "agent-skill", apply=False)
    assert result.kinds["agent-skill"].pagination_complete
    assert result.status == "ok"


# ---------------------------------------------------------------- response shapes


def test_a_missing_envelope_key_raises_instead_of_looking_empty() -> None:
    """Sabotage: payload.get(container, []) -> a renamed key reads as a clean
    tenant, on every run, silently."""
    spec = registry.KINDS["synthetic"]
    client = FakeClient().on(spec.list_route.path, Response(200, b'{"items": []}'))
    result = run_kind(client, "synthetic")
    assert not result.kinds["synthetic"].list_ok
    assert "synthetics" in (result.kinds["synthetic"].list_error or "")
    assert result.status == "partial"


def test_an_incloud_only_kind_is_not_applicable_rather_than_indeterminate() -> None:
    """Ingestion-key routes 400 on every non-inCloud tenant, so on backend-dev the
    answer is "none, and there could not be" -- not "we could not tell".

    Reporting it as indeterminate would make EVERY run on the default backend
    `partial`, and a status that is always yellow is one nobody reads. Sabotage:
    treat the 400 as a plain list failure -> status becomes partial and the exit
    code stops meaning anything.
    """
    spec = registry.KINDS["ingestion-key"]
    body = b'{"message":"this endpoint is only available for inCloud backends"}'
    result = run_kind(FakeClient().on(spec.list_route.path, Response(400, body)), "ingestion-key")

    report = result.kinds["ingestion-key"]
    assert report.not_applicable and report.determinate
    assert result.status == "ok" and result.exit_code == 0
    assert "n/a on this backend" in report_mod.render_markdown(result)


def test_any_other_400_is_still_a_real_list_failure() -> None:
    """Guards the previous test against becoming "swallow every 400"."""
    spec = registry.KINDS["ingestion-key"]
    result = run_kind(
        FakeClient().on(spec.list_route.path, Response(400, b'{"message":"bad request"}')), "ingestion-key"
    )
    assert not result.kinds["ingestion-key"].list_ok
    assert result.kinds["ingestion-key"].not_applicable is None
    assert result.status == "partial"


def test_a_zero_byte_body_raises() -> None:
    """These endpoints spell empty as [] -- an empty body is a dropped response."""
    spec = registry.KINDS["synthetic"]
    result = run_kind(FakeClient().on(spec.list_route.path, Response(200, b"")), "synthetic")
    assert not result.kinds["synthetic"].list_ok


def test_a_null_container_is_a_legitimate_empty_list() -> None:
    spec = registry.KINDS["synthetic"]
    result = run_kind(FakeClient().on(spec.list_route.path, Response(200, b'{"synthetics": null}')), "synthetic")
    assert result.kinds["synthetic"].list_ok and result.kinds["synthetic"].listed == 0
    assert result.status == "ok"


def test_a_non_list_under_the_container_key_raises() -> None:
    spec = registry.KINDS["synthetic"]
    result = run_kind(FakeClient().on(spec.list_route.path, Response(200, b'{"synthetics": {"a": 1}}')), "synthetic")
    assert not result.kinds["synthetic"].list_ok


def test_a_non_object_row_raises_instead_of_being_dropped() -> None:
    """`_unwrap` refuses a bad payload, a missing key and a non-list container, so
    filtering non-dict ELEMENTS out of the list was the one hole left in it:
    `[null]` became an empty listing that was list_ok, pagination_complete and
    determinate -- "could not tell" rendered as "clean".

    Sabotage: restore `[r for r in rows if isinstance(r, dict)]`.
    """
    spec = registry.KINDS["synthetic"]
    result = run_kind(FakeClient().on(spec.list_route.path, Response(200, b'{"synthetics": [null]}')), "synthetic")

    report = result.kinds["synthetic"]
    assert not report.list_ok, "a row the janitor cannot read is not an absent row"
    assert not report.determinate
    assert result.status == "partial" and result.exit_code == 2


def test_a_partly_unreadable_page_does_not_pass_as_a_complete_one() -> None:
    """The worse half of the same defect, and the reason this is not cosmetic.

    Dropping the bad element left the GOOD rows and still reported the listing
    complete, so the sweep would delete from a silently short list while claiming
    it had seen everything. For a janitor that is "leftovers exist and we reported
    clean"; for the dependency gate in `_drop_present_in` it is worse, since
    absence would be proved from a list that had lost rows.
    """
    spec = registry.KINDS["synthetic"]
    body = b'{"synthetics": [{"id": "a", "name": "keep-me"}, null]}'
    result = run_kind(FakeClient().on(spec.list_route.path, Response(200, body)), "synthetic")

    report = result.kinds["synthetic"]
    assert not report.list_ok
    assert report.listed == 0, "no row from an unreadable page may be acted on"


def test_a_row_with_no_usable_name_is_skipped_with_a_warning(caplog: pytest.LogCaptureFixture) -> None:
    """Sabotage: str(row.get(field)) -> the name becomes the literal "None",
    which fails the pattern anyway, so assert on the warning rather than the
    absence of a delete."""
    spec = registry.KINDS["dashboard"]
    report = sweep.KindReport(kind="dashboard")
    cutoff = datetime.datetime.now(UTC)
    with caplog.at_level("WARNING"):
        assert sweep.classify(spec, [{"uuid": "d1"}], cutoff, None, report) == []
    assert any("carries none of" in r.getMessage() for r in caplog.records)


def test_name_fields_fall_back_in_order() -> None:
    """Silences carry the suite name in `comment`; monitors in `title`."""
    assert sweep.first_present({"comment": "c"}, ("comment",)) == "c"
    assert sweep.first_present({"name": "n", "title": "t"}, ("title", "name")) == "t"
    assert sweep.first_present({"name": "n"}, ("title", "name")) == "n"
    assert sweep.first_present({"title": "", "name": "n"}, ("title", "name")) == "n"


# ------------------------------------------------------------------ the five gates


def test_a_foreign_creator_is_never_swept() -> None:
    """The strongest gate: under API-key auth the backend stamps the e2e service
    account's NAME as the creator, so a human's resource cannot pass even if they
    typed an e2e-shaped name.

    Sabotage: drop the creator comparison -> the human's dashboard is deleted.
    """
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "mine", "name": "e2e-test-dashboard-" + UUID, "owner": IDENTITY, "createdTimestamp": iso(**OLD)},
        {
            "uuid": "theirs",
            "name": "e2e-test-dashboard-" + UUID,
            "owner": "someone@groundcover.com",
            "createdTimestamp": iso(**OLD),
        },
    ]
    client = FakeClient().serve_rows(spec, rows)
    result = run_kind(client, "dashboard", identity=IDENTITY)

    assert result.kinds["dashboard"].skipped_foreign_creator == 1
    assert [c.path for c in client.deletes] == ["/api/dashboards/mine"]


def test_last_active_vetoes_a_key_in_use_even_though_it_is_old() -> None:
    """This is what makes un-aged rbac sweeping safe, and it is structural: the
    middleware bumps last_used on every authenticated request, so the janitor's
    own key can never pass.

    Sabotage: drop the lastActive check -> the janitor revokes its own key.
    """
    spec = registry.KINDS["api-key"]
    rows = [
        {
            "id": "own",
            "name": "sdk-e2e-test-apikey-1712345678901234567",
            "creationDate": iso(**OLD),
            "lastActive": iso(**FRESH),
        },
        {
            "id": "stale",
            "name": "sdk-e2e-test-apikey-1712345678901234568",
            "creationDate": iso(**OLD),
            "lastActive": iso(**OLD),
        },
    ]
    client = FakeClient().serve_rows(spec, rows)
    result = run_kind(client, "api-key")

    assert result.kinds["api-key"].too_young == 1
    assert [c.path for c in client.deletes] == ["/api/rbac/apikey/stale"]


def test_synthetic_owned_monitors_are_excluded_before_the_delete_pass() -> None:
    """BE-2727: 718 of these answer 403 permanently. Excluding them is the
    difference between reporting them and issuing 718 failing DELETEs every run.

    Sabotage: drop the exclusion -> a DELETE is attempted for the companion.
    """
    spec = registry.KINDS["monitor"]
    rows = [
        {
            "uuid": "companion",
            "title": "sdk-e2e-test-monitor-12345a1-p1n1",
            "createdAt": iso(**OLD),
            "originType": "SyntheticTest",
        },
        {"uuid": "plain", "title": "sdk-e2e-test-monitor-12345a1-p1n2", "createdAt": iso(**OLD)},
    ]
    client = FakeClient().serve_rows(spec, rows)
    result = run_kind(client, "monitor")

    assert result.kinds["monitor"].excluded == 1
    assert [c.path for c in client.deletes] == ["/api/monitors/plain"]


def test_read_only_and_bound_policies_are_never_deleted() -> None:
    """readOnly policies answer 404 on delete, indistinguishable from 'gone'.
    entityCount > 0 is structural self-protection: the janitor's own policy is
    bound to its own service account."""
    spec = registry.KINDS["policy"]
    rows = [
        {"uuid": "sys", "name": "e2e-test-policy-" + UUID, "createdTimestamp": iso(**OLD), "readOnly": True},
        {"uuid": "bound", "name": "e2e-test-policy-" + UUID, "createdTimestamp": iso(**OLD), "entityCount": 2},
        {"uuid": "free", "name": "e2e-test-policy-" + UUID, "createdTimestamp": iso(**OLD), "entityCount": 0},
    ]
    client = FakeClient().serve_rows(spec, rows)
    result = run_kind(client, "policy")

    assert result.kinds["policy"].excluded == 2
    assert [c.path for c in client.deletes] == ["/api/rbac/policy/free"]


def test_unrecognised_lookalikes_are_reported_and_never_deleted() -> None:
    """The mitigation for sweeping a prefix owned by another repo: if the TS SDK
    renames, the count here grows instead of the janitor silently going quiet."""
    spec = registry.KINDS["dashboard"]
    rows = [{"uuid": "x", "name": "sdk-newlang-E2E_test-dashboard-999", "createdTimestamp": iso(**OLD)}]
    client = FakeClient().serve_rows(spec, rows)
    result = run_kind(client, "dashboard")

    assert result.kinds["dashboard"].lookalikes == ["sdk-newlang-E2E_test-dashboard-999"]
    assert client.deletes == []


# ------------------------------------------------------------------------ ordering


def test_deletion_ranks_are_a_barrier_not_merely_a_sort() -> None:
    """A live API key makes its service account's DELETE answer 400, so EVERY
    rank-10 delete must finish before the first rank-20 one is issued.

    Sabotage: flatten the phases into one sorted list interleaved by kind -> a
    service-account delete appears before the last api-key delete.
    """
    keys = registry.KINDS["api-key"]
    accounts = registry.KINDS["service-account"]
    policies = registry.KINDS["policy"]

    client = FakeClient()
    client.serve_rows(
        keys,
        [
            {"id": "k%d" % i, "name": "sdk-e2e-test-apikey-171234567890123456%d" % i, "creationDate": iso(**OLD)}
            for i in range(3)
        ],
    )
    client.serve_rows(
        accounts,
        [{"serviceAccountId": "sa%d" % i, "name": "e2e-test-sa-" + UUID} for i in range(3)],
    )
    client.serve_rows(
        policies,
        [{"uuid": "p%d" % i, "name": "e2e-test-policy-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(3)],
    )

    sweep.run(
        client,
        kinds=["policy", "service-account", "api-key"],  # deliberately worst-case order
        age_minutes=60,
        apply=True,
        identity=None,
        limits=Limits(),
        backend_id="backend-dev",
        base_url="https://api.test",
    )

    ranks = [10 if "/apikey/" in c.path else 20 if "/service-account/" in c.path else 30 for c in client.deletes]
    assert len(ranks) == 9
    assert ranks == sorted(ranks), "ranks interleaved: {}".format(ranks)


def test_one_kind_failing_to_list_does_not_stop_the_others() -> None:
    dashboards = registry.KINDS["dashboard"]
    client = FakeClient()
    client.on(registry.KINDS["synthetic"].list_route.path, Response(500, b'{"error":"boom"}'))
    client.serve_rows(
        dashboards,
        [{"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)}],
    )

    result = sweep.run(
        client,
        kinds=["synthetic", "dashboard"],
        age_minutes=60,
        apply=True,
        identity=None,
        limits=Limits(),
        backend_id="backend-dev",
        base_url="https://api.test",
    )
    assert not result.kinds["synthetic"].list_ok
    assert result.kinds["dashboard"].deleted == 1
    assert result.status == "partial"


# --------------------------------------------------------------- circuit breakers


def test_an_over_matching_pattern_trips_the_ratio_brake() -> None:
    """The realistic matcher bug is a loosened regex, and its signature is
    'suddenly almost everything matches'.

    Sabotage: remove the brake -> all 100 rows are deleted.
    """
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "d%d" % i, "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(100)
    ]
    client = FakeClient().serve_rows(spec, rows)
    result = run_kind(client, "dashboard")

    assert client.deletes == []
    assert "above the" in (result.kinds["dashboard"].aborted or "")
    assert result.status == "partial"


def test_the_ratio_brake_does_not_fire_on_a_small_tenant() -> None:
    """Two matches out of three is 66%, and perfectly normal on a tiny kind.
    Without the floor, the brake would fire constantly and be turned off."""
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)},
        {"uuid": "d2", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)},
        {"uuid": "d3", "name": "the-real-one", "createdTimestamp": iso(**OLD)},
    ]
    result = run_kind(FakeClient().serve_rows(spec, rows), "dashboard")
    assert result.kinds["dashboard"].deleted == 2 and result.status == "ok"


def test_the_per_kind_cap_aborts_rather_than_truncating() -> None:
    """Deleting the first N and calling it a day would look like success.

    Sabotage: slice the candidate list instead of raising -> deletes happen and
    the run reports ok.
    """
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "d%d" % i, "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(30)
    ] + [{"uuid": "o%d" % i, "name": "real-%d" % i, "createdTimestamp": iso(**OLD)} for i in range(200)]
    client = FakeClient().serve_rows(spec, rows)

    result = run_kind(client, "dashboard", limits=Limits(max_deletes_per_kind=10))
    assert client.deletes == []
    assert "per-kind cap" in (result.kinds["dashboard"].aborted or "")


def test_the_run_wide_cap_stops_everything() -> None:
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "d%d" % i, "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(30)
    ] + [{"uuid": "o%d" % i, "name": "real-%d" % i, "createdTimestamp": iso(**OLD)} for i in range(200)]
    client = FakeClient().serve_rows(spec, rows)

    result = run_kind(client, "dashboard", limits=Limits(max_deletes_per_kind=100, max_deletes_total=5))
    assert client.deletes == []
    assert "run cap" in (result.kinds["dashboard"].aborted or "")


def test_check_breakers_reports_the_kind_in_its_message() -> None:
    # 100 of 100 -- above the 0.95 ceiling. 90% deliberately does NOT trip it any
    # more: policies on backend-dev are legitimately 66% e2e debris, so a tighter
    # ceiling fired on correct behaviour.
    report = sweep.KindReport(kind="dashboard", listed=100, matched=100)
    candidates = [sweep.Candidate("dashboard", "d%d" % i, "n", {}) for i in range(100)]
    with pytest.raises(SweepAborted, match="dashboard"):
        sweep.check_breakers(registry.KINDS["dashboard"], candidates, report, Limits())


def test_a_legitimately_debris_heavy_kind_does_not_trip_the_ratio_brake() -> None:
    """66% of policies on backend-dev are genuine e2e debris. The old 0.60 ceiling
    fired on that -- correct behaviour reported as a suspected matcher bug."""
    report = sweep.KindReport(kind="policy", listed=450, matched=297)
    candidates = [sweep.Candidate("policy", "p%d" % i, "n", {}) for i in range(297)]
    sweep.check_breakers(registry.KINDS["policy"], candidates, report, Limits())


def test_a_large_excluded_population_does_not_trip_the_ratio_brake() -> None:
    """The brake measures CANDIDATES, not matches.

    On backend-dev, 818 of 1385 monitors are synthetic-owned companions that are
    matched and then deliberately withheld (BE-2727). Counting those would keep
    the brake permanently tripped and block the 164 monitors that genuinely can
    be deleted -- a safety limit that always fires is one that gets removed.

    Sabotage: measure report.matched instead -> this fails, and so does the real
    tenant.
    """
    spec = registry.KINDS["monitor"]
    companions = [
        {
            "uuid": "c%d" % i,
            "title": "[synthetic] - e2e-test-dns-synthetic-" + UUID,
            "createdAt": iso(**OLD),
            "originType": "SyntheticTest",
        }
        for i in range(80)
    ]
    real = [
        {"uuid": "m%d" % i, "title": "sdk-e2e-test-monitor-12345a1-p1n%d" % i, "createdAt": iso(**OLD)}
        for i in range(10)
    ]
    others = [{"uuid": "o%d" % i, "title": "prod monitor %d" % i, "createdAt": iso(**OLD)} for i in range(30)]

    client = FakeClient().serve_rows(spec, companions + real + others)
    result = run_kind(client, "monitor")
    report = result.kinds["monitor"]

    assert report.matched == 90 and report.excluded == 80
    assert report.aborted is None, report.aborted
    assert len(client.deletes) == 10


# ------------------------------------------------------------- delete classification


@pytest.mark.parametrize(
    "status,field",
    [
        (200, "deleted"),
        (204, "deleted"),
        (202, "delete_accepted"),
        (404, "already_gone"),
        (400, "failed"),
        (403, "failed"),
        (500, "failed"),
    ],
)
def test_delete_outcomes_are_classified_not_assumed(status: int, field: str) -> None:
    """400 is never 'gone' -- it is a rejection, the same rule as
    tests/e2e/_cleanup.py:54-59. And 202 is 'accepted', not done: reporting it as
    deleted would claim a completion nobody observed.

    Sabotage: fold 400 into gone_statuses -> the 400 case fails.
    """
    spec = registry.KINDS["dashboard"]
    client = FakeClient()
    client.serve_rows(spec, [{"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)}])
    client.on("/api/dashboards/d1", Response(status, b"{}"))

    report = run_kind(client, "dashboard").kinds["dashboard"]
    assert getattr(report, field) == 1


def test_an_accepted_delete_that_really_landed_is_confirmed_and_clean() -> None:
    """202 is the normal success code for api keys, service accounts and ingestion
    keys, so treating every one as indeterminate would make an ordinary apply run
    permanently yellow. Asking the server settles it."""
    spec = registry.KINDS["api-key"]
    rows = [{"id": "k1", "name": "sdk-e2e-test-apikey-1712345678901234567", "creationDate": iso(**OLD)}]
    client = FakeClient()
    client.serve_rows(spec, rows)

    def _delete(call: Call) -> Response:
        rows.clear()  # a realistic backend: gone from the next listing
        return Response(202, b"{}")

    client.on("/api/rbac/apikey/k1", _delete)

    report = run_kind(client, "api-key").kinds["api-key"]
    assert report.delete_accepted == 1 and report.delete_confirmed == 1
    assert report.delete_unconfirmed == 0 and report.determinate


def test_an_accepted_delete_that_did_not_land_is_not_reported_as_success() -> None:
    """`determinate` ignoring delete_accepted meant a queued 202 could produce
    status=ok with deleted=0 -- claiming a completion nobody observed.

    Sabotage: drop `delete_unconfirmed == 0` from determinate, or skip the
    confirmation re-list -> status becomes ok while the resource is still there.
    """
    spec = registry.KINDS["api-key"]
    client = FakeClient()
    # The backend accepts the delete and then... still lists it.
    client.serve_rows(
        spec, [{"id": "k1", "name": "sdk-e2e-test-apikey-1712345678901234567", "creationDate": iso(**OLD)}]
    )
    client.on("/api/rbac/apikey/k1", Response(202, b"{}"))

    result = run_kind(client, "api-key")
    report = result.kinds["api-key"]
    assert report.delete_accepted == 1 and report.delete_unconfirmed == 1
    assert report.delete_confirmed == 0 and not report.determinate
    assert result.status == "partial" and result.exit_code == 2
    assert "STILL LISTED" in report_mod.render_markdown(result)


def test_a_transport_failure_is_caught_per_resource() -> None:
    """One dead delete must not strand the rest."""
    spec = registry.KINDS["dashboard"]
    rows = [{"uuid": "d%d" % i, "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(3)]
    rows += [{"uuid": "o%d" % i, "name": "real-%d" % i, "createdTimestamp": iso(**OLD)} for i in range(20)]
    client = FakeClient().serve_rows(spec, rows)
    client.on("/api/dashboards/d1", TransportError("connection reset"))

    report = run_kind(client, "dashboard").kinds["dashboard"]
    assert report.deleted == 2 and report.failed == 1
    assert "connection reset" in report.failures[0]["error"]


def test_ingestion_keys_are_deleted_by_name_in_a_body() -> None:
    """The one kind cleanable with no id at all."""
    spec = registry.KINDS["ingestion-key"]
    name = "sdk-e2e-test-ingestion-key-1712345678901234567"
    client = FakeClient().serve_rows(spec, [{"id": "", "name": name}])
    client.on("/api/rbac/ingestion-keys/delete", Response(202, b"{}"))

    run_kind(client, "ingestion-key")
    delete = client.deletes[0]
    assert delete.path == "/api/rbac/ingestion-keys/delete" and delete.json == {"name": name}


def test_data_integration_deletes_carry_the_type_segment() -> None:
    spec = registry.KINDS["data-integration"]
    client = FakeClient().serve_rows(
        spec,
        [{"id": "c1", "name": "e2e-cloudwatch-" + UUID, "type": "cloudwatch", "update_timestamp": iso(**OLD)}],
    )
    run_kind(client, "data-integration")
    assert client.deletes[0].path == "/api/integrations/v1/data/config/cloudwatch/c1"


def test_a_matched_row_with_no_id_is_a_failure_not_a_silent_skip() -> None:
    spec = registry.KINDS["dashboard"]
    client = FakeClient().serve_rows(
        spec, [{"uuid": "", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)}]
    )
    report = run_kind(client, "dashboard").kinds["dashboard"]
    assert report.failed == 1 and client.deletes == []


# ------------------------------------------------------------------------- dry run


def test_report_mode_issues_no_write_of_any_kind() -> None:
    """Sabotage: any accidental delete path shows up in the recorded call log."""
    spec = registry.KINDS["dashboard"]
    client = FakeClient().serve_rows(
        spec, [{"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)}]
    )
    result = run_kind(client, "dashboard", apply=False)

    assert all(c.method in ("GET", "POST") for c in client.calls)
    assert all(c.path == "/api/dashboards" for c in client.calls)
    assert result.kinds["dashboard"].matched == 1 and result.kinds["dashboard"].deleted == 0


def test_report_mode_produces_the_same_candidate_set_apply_would_delete() -> None:
    """Otherwise the dry run is not a rehearsal and reviewing it means nothing.

    This is the offline half of the P6 live probe.
    """
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "old", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)},
        {"uuid": "new", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**FRESH)},
        {"uuid": "real", "name": "quarterly-overview", "createdTimestamp": iso(**OLD)},
    ]
    reported = run_kind(FakeClient().serve_rows(spec, rows), "dashboard", apply=False).kinds["dashboard"]
    applied_client = FakeClient().serve_rows(spec, rows)
    run_kind(applied_client, "dashboard")

    assert reported.matched == 2 and reported.too_young == 1
    assert [c.path for c in applied_client.deletes] == ["/api/dashboards/old"]


# -------------------------------------------------------------------- run reporting


def test_an_unknown_kind_is_rejected_rather_than_sweeping_nothing() -> None:
    """A typo'd kind name must not look like a clean run."""
    with pytest.raises(ValueError, match="unknown kind"):
        run_kind(FakeClient(), "dashboards")


def test_a_kind_that_produced_no_report_is_visible_as_missing() -> None:
    """A kind dropped from the loop by a bad `continue` is otherwise
    indistinguishable from a kind that was clean."""
    result = sweep.SweepReport(
        backend_id="b",
        base_url="u",
        mode="report",
        age_minutes=60,
        identity=None,
        expected_kinds=["dashboard", "monitor"],
    )
    result.kinds["dashboard"] = sweep.KindReport(kind="dashboard", list_ok=True, pagination_complete=True)
    assert result.missing_kinds == ["monitor"]
    assert result.status == "partial" and result.exit_code == 2


def test_a_clean_determinate_run_is_ok() -> None:
    spec = registry.KINDS["dashboard"]
    result = run_kind(
        FakeClient().serve_rows(spec, [{"uuid": "x", "name": "real", "createdTimestamp": iso(**OLD)}]), "dashboard"
    )
    assert result.status == "ok" and result.exit_code == 0


def test_a_failed_delete_outranks_a_partial_listing() -> None:
    spec = registry.KINDS["dashboard"]
    client = FakeClient().serve_rows(
        spec, [{"uuid": "d1", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)}]
    )
    client.on("/api/dashboards/d1", Response(500, b"{}"))
    result = run_kind(client, "dashboard")
    assert result.status == "failed" and result.exit_code == 1


def test_an_empty_extra_delete_field_is_treated_as_missing() -> None:
    """`type: ""` would build `/api/integrations/v1/data/config//c1`, which either
    404s (counted as already_gone) or hits some other route -- both reporting a
    resource as handled when it was never touched.

    Sabotage: check only `v is None` -> a malformed DELETE is issued.
    """
    spec = registry.KINDS["data-integration"]
    client = FakeClient().serve_rows(
        spec,
        [{"id": "c1", "name": "e2e-test-cloudwatch-" + UUID, "type": "", "update_timestamp": iso(**OLD)}],
    )
    report = run_kind(client, "data-integration").kinds["data-integration"]

    assert client.deletes == [], "no request should be sent with an empty path segment"
    assert report.failed == 1 and report.already_gone == 0


def test_a_truncated_confirmation_listing_does_not_confirm_anything(monkeypatch: pytest.MonkeyPatch) -> None:
    """A name missing from a TRUNCATED page is missing from the page, not from the
    tenant. Counting that as confirmed is the same absence-of-evidence mistake the
    rest of this module exists to avoid.

    Isolates the confirmation listing specifically: the FIRST listing is short and
    therefore complete, so `pagination_complete` on the main pass is True and only
    the re-list is truncated. Uses `silence`, which is the kind that can actually
    page -- an earlier version of this test used `service-account`, whose route has
    no page_size at all, so it could never truncate and passed with the guard
    removed.

    Sabotage: drop the probe.pagination_complete check -> the accepted delete is
    counted as confirmed and the run exits ok.
    """
    monkeypatch.setattr(sweep, "MAX_PAGES", 2)
    spec = registry.KINDS["silence"]
    target = {"id": "s1", "comment": "e2e-test-silence-" + UUID, "createdAt": iso(**OLD)}
    calls = {"n": 0}

    def lister(call: Call) -> Response:
        calls["n"] += 1
        if calls["n"] == 1:
            # Short page => the main listing is provably complete.
            return Response(200, json.dumps({"silences": [target]}).encode())
        # Every confirmation page comes back full, so paging never terminates and
        # the re-list is truncated. The target is absent from it -- which without
        # the guard would read as "gone".
        filler = [{"id": "x%d" % i, "comment": "unrelated-%d" % i, "createdAt": iso(**OLD)} for i in range(1000)]
        return Response(200, json.dumps({"silences": filler}).encode())

    client = FakeClient().on(spec.list_route.path, lister)
    client.on("/api/monitors/v2/silences/s1", Response(202, b"{}"))

    result = run_kind(client, "silence")
    report = result.kinds["silence"]
    assert report.pagination_complete, "the main listing must be complete so this isolates the re-list"
    assert report.delete_accepted == 1
    assert report.delete_confirmed == 0 and report.delete_unconfirmed == 1
    assert not report.determinate and result.status == "partial"


def test_accepted_deletes_are_confirmed_before_the_next_rank_issues_any() -> None:
    """The rank barrier has to order EFFECTS, not just requests.

    An api-key DELETE answers 202, so ordering the requests alone lets rank 20
    issue a service-account delete while the key is still only accepted -- and
    the backend answers 400 for a dependency that was already on its way out.

    Sabotage: move confirmation back to a single pass after all ranks -> the
    recorded call order shows the rank-20 DELETE before the api-key
    confirmation listing.
    """
    keys, accounts = registry.KINDS["api-key"], registry.KINDS["service-account"]
    client = FakeClient()
    client.serve_rows(
        keys, [{"id": "k1", "name": "sdk-e2e-test-apikey-1712345678901234567", "creationDate": iso(**OLD)}]
    )
    client.serve_rows(accounts, [{"serviceAccountId": "sa1", "name": "e2e-test-sa-" + UUID}])
    client.on("/api/rbac/apikey/k1", Response(202, b"{}"))
    client.on("/api/rbac/service-account/sa1", Response(202, b"{}"))

    sweep.run(
        client,
        kinds=["service-account", "api-key"],
        age_minutes=60,
        apply=True,
        identity=None,
        limits=Limits(),
        backend_id="backend-dev",
        base_url="https://api.test",
    )

    order = [(c.method, c.path) for c in client.calls]
    key_delete = order.index(("DELETE", "/api/rbac/apikey/k1"))
    sa_delete = order.index(("DELETE", "/api/rbac/service-account/sa1"))
    # The confirmation re-list for api keys is a GET on the key list AFTER its delete.
    key_confirm = next(i for i, c in enumerate(order) if i > key_delete and c == ("GET", "/api/rbac/apikeys/list"))
    assert key_delete < key_confirm < sa_delete, (
        "rank 20 must not issue a delete before rank 10's accepted deletes are confirmed; got {}".format(order)
    )


def test_duplicate_names_do_not_collapse_when_confirming_deletes() -> None:
    """Confirmation must key on whatever the DELETE addressed.

    The delete targets an id; a set of NAMES collapses duplicates, so three
    accepted deletes sharing a name with all three still present reported
    `confirmed = 3 - 1 = 2` -- two completions nobody observed.

    Sabotage: confirm via `{first_present(row, name_fields)}` -> confirmed
    becomes 2 and the run reports partial-but-mostly-done instead of nothing done.
    """
    spec = registry.KINDS["api-key"]
    dupes = [
        {"id": "k%d" % i, "name": "sdk-e2e-test-apikey-1712345678901234567", "creationDate": iso(**OLD)}
        for i in range(3)
    ]
    client = FakeClient().serve_rows(spec, dupes)  # the backend accepts, then keeps listing them
    for i in range(3):
        client.on("/api/rbac/apikey/k%d" % i, Response(202, b"{}"))

    report = run_kind(client, "api-key").kinds["api-key"]
    assert report.delete_accepted == 3
    assert report.delete_unconfirmed == 3, "all three are still listed, so none is confirmed"
    assert report.delete_confirmed == 0


def test_a_name_addressed_kind_still_confirms_by_name() -> None:
    """Ingestion keys are deleted by name in a body and carry no meaningful id,
    so they are the one kind that must keep matching on the name."""
    spec = registry.KINDS["ingestion-key"]
    name = "sdk-e2e-test-ingestion-key-1712345678901234567"
    rows = [{"id": "", "name": name}]
    client = FakeClient().serve_rows(spec, rows)

    def _delete(call: Call) -> Response:
        rows.clear()
        return Response(202, b"{}")

    client.on("/api/rbac/ingestion-keys/delete", _delete)

    report = run_kind(client, "ingestion-key").kinds["ingestion-key"]
    assert report.delete_accepted == 1 and report.delete_confirmed == 1
    assert report.delete_unconfirmed == 0


def test_confirmation_matches_the_id_the_delete_targeted_not_a_shared_name() -> None:
    """A sibling sharing the deleted resource's name must not make it look alive.

    Two keys are named the same; only one is a candidate (the other is too young).
    Matching on the name would find the survivor and call the delete unconfirmed
    -- a false alarm rather than a false success, but still the wrong question.
    The delete addressed an id, so confirmation asks about that id.

    Sabotage: match on `spec.name_fields` instead of `spec.id_field` -> the
    surviving sibling makes this read unconfirmed.
    """
    spec = registry.KINDS["api-key"]
    shared = "sdk-e2e-test-apikey-1712345678901234567"
    rows = [
        {"id": "old", "name": shared, "creationDate": iso(**OLD)},
        {"id": "young", "name": shared, "creationDate": iso(**FRESH)},
    ]

    def _delete(call: Call) -> Response:
        rows[:] = [r for r in rows if r["id"] != "old"]
        return Response(202, b"{}")

    client = FakeClient().serve_rows(spec, rows)
    client.on("/api/rbac/apikey/old", _delete)

    report = run_kind(client, "api-key").kinds["api-key"]
    assert report.too_young == 1
    assert report.delete_accepted == 1
    assert report.delete_confirmed == 1, "the deleted id is gone; the sibling's name is irrelevant"
    assert report.delete_unconfirmed == 0


def test_rows_with_no_usable_name_are_counted_not_just_logged() -> None:
    """Same failure shape as `unknown_age`, and it was only a log line.

    If a backend renames a field in `name_fields`, every row takes that branch,
    `matched` stays 0, and the sweep reports a clean tenant. A log line does not
    change the exit code; a counter folded into `determinate` does.

    Sabotage: drop `report.unnamed += 1` (or its term in determinate) -> status
    becomes ok while the janitor could not read a single name.
    """
    spec = registry.KINDS["dashboard"]
    # The backend renamed `name` to `title`, so nothing is readable.
    rows = [{"uuid": "d%d" % i, "title": "e2e-test-dashboard-" + UUID} for i in range(5)]
    result = run_kind(FakeClient().serve_rows(spec, rows), "dashboard")
    report = result.kinds["dashboard"]

    assert report.listed == 5 and report.matched == 0
    assert report.unnamed == 5
    assert not report.determinate
    assert result.status == "partial" and result.exit_code == 2
    # The counter drives the exit code, so it has to be visible to whoever sees
    # the red run -- otherwise it is an unexplained failure.
    assert "no readable name" in report_mod.render_markdown(result)


def test_a_resource_name_cannot_corrupt_the_markdown_report() -> None:
    """The evidence column is the whole point of the report, and resource names
    come from the tenant. A `|` adds columns; a newline ends the table, so every
    row after it loses its evidence cell.

    Sabotage: interpolate the raw name -> the pipe and newline reach the output.
    """
    spec = registry.KINDS["dashboard"]
    hostile = "sdk-newlang-e2e_test-dash | evil\n| x | y | z |`code`[link](http://x)"
    client = FakeClient().serve_rows(spec, [{"uuid": "d1", "name": hostile, "createdTimestamp": iso(**OLD)}])
    markdown = report_mod.render_markdown(run_kind(client, "dashboard", apply=False))

    assert hostile not in markdown
    assert "\\|" in markdown, "the pipe must be escaped, not dropped"
    # render_markdown wraps names in code spans and Markdown cannot escape a
    # backtick inside one, so a name carrying one must not keep it.
    assert "`code`" not in markdown
    for line in markdown.splitlines():
        # No row may gain columns from a resource name.
        if line.startswith("| `dashboard`"):
            assert line.count("|") == len(report_mod._COLUMNS) + 3


def _capped_client() -> "FakeClient":
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "d%d" % i, "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(30)
    ] + [{"uuid": "o%d" % i, "name": "real-%d" % i, "createdTimestamp": iso(**OLD)} for i in range(200)]
    return FakeClient().serve_rows(spec, rows)


def test_a_circuit_breaker_in_report_mode_does_not_fail_the_run() -> None:
    """In report mode nothing was going to be deleted, so a cap is the ANSWER.

    "30 dashboards are eligible, above the automated cap" is exactly what a survey
    was asked for. Failing on it makes every report run against a tenant with a
    real backlog permanently red -- the same "always yellow, so nobody reads it"
    trap the not-applicable handling exists to avoid -- and makes the intended
    dry-run-then-review flow start from a red run.

    Sabotage: put `aborted` back into `determinate` -> this reports partial/exit 2.
    """
    result = run_kind(_capped_client(), "dashboard", apply=False, limits=Limits(max_deletes_per_kind=10))
    report = result.kinds["dashboard"]

    assert report.aborted, "the breaker must still trip and be recorded"
    assert result.status == "ok" and result.exit_code == 0
    # Visible in the rendered report even though the exit code is clean: the exit
    # code says whether the run did its job, the report says what it found.
    rendered = report_mod.render_markdown(result)
    assert "ABORTED" in rendered and "Circuit breakers" in rendered


def test_a_circuit_breaker_in_apply_mode_still_fails_the_run() -> None:
    """In apply mode a breaker means work was refused, so the run is not clean.

    Sabotage: drop the `mode == "apply"` clause from status -> this reports ok
    while 30 resources the run was asked to delete are still there.
    """
    result = run_kind(_capped_client(), "dashboard", apply=True, limits=Limits(max_deletes_per_kind=10))
    assert result.kinds["dashboard"].aborted
    assert result.status == "partial" and result.exit_code == 2


def test_a_real_unknown_still_fails_even_in_report_mode() -> None:
    """Relaxing breakers must not relax genuine unknowns. A truncated listing is
    still indeterminate in report mode, because the counts themselves are wrong."""
    spec = registry.KINDS["agent-skill"]
    rows = [{"id": "k%d" % i, "name": "x%d" % i, "created_at": iso(**OLD)} for i in range(250)]
    result = run_kind(FakeClient().serve_rows(spec, rows), "agent-skill", apply=False)
    assert not result.kinds["agent-skill"].pagination_complete
    assert result.status == "partial"


def test_the_report_reaches_the_job_log_not_only_the_step_summary(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Any, capsys: Any
) -> None:
    """A clean run used to log two lines.

    The table was written to $GITHUB_STEP_SUMMARY *instead of* stdout, so a sweep
    over ten kinds and thousands of resources produced "ingestion-key is n/a" and
    "sweep ok" in the log, with every number only in a file you had to download.
    A tool whose whole argument is "make the outcome legible" has to be legible
    where people actually look.

    Sabotage: restore the if/else so the summary path suppresses the log output ->
    the captured stderr no longer contains the table.
    """
    from gc_e2e_janitor import __main__ as cli

    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GC_API_KEY", "k")
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    monkeypatch.setattr(
        cli,
        "run",
        lambda client, **kw: sweep.SweepReport(
            backend_id=kw["backend_id"],
            base_url=kw["base_url"],
            mode="report",
            age_minutes=kw["age_minutes"],
            identity=None,
            expected_kinds=["dashboard"],
            kinds={"dashboard": sweep.KindReport(kind="dashboard", list_ok=True, pagination_complete=True, listed=7)},
        ),
    )

    cli.main(
        [
            "--base-url",
            "https://api.main.groundcover.com",
            "--backend-id",
            "backend-dev",
            "--kinds",
            "dashboard",
            "--report-path",
            str(tmp_path / "r.json"),
        ]
    )

    logged = capsys.readouterr().err
    assert "E2E leftover sweep" in logged and "dashboard" in logged and "verdict: OK" in logged
    # ...and the step summary still gets its markdown version.
    assert "## E2E leftover sweep" in summary.read_text()


def test_the_artifact_names_every_resource_that_would_be_deleted() -> None:
    """Counts alone cannot be reviewed. The artifact has to say WHICH resources.

    Sabotage: stop populating kind_report.candidates -> the report says "2
    candidates" and a reviewer has no way to check what they are before approving
    an apply run.
    """
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "keep", "name": "quarterly-overview", "createdTimestamp": iso(**OLD)},
        {"uuid": "d-b", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)},
        {"uuid": "d-a", "name": "e2e-test-dashboard-" + UUID + "-updated", "createdTimestamp": iso(**OLD)},
        {"uuid": "young", "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**FRESH)},
    ]
    result = run_kind(FakeClient().serve_rows(spec, rows), "dashboard", apply=False)
    listed = result.kinds["dashboard"].candidates

    # The complete records, not just ids plus a shared prefix: a mispaired
    # {id, name} is exactly the corruption an artifact reader could not detect.
    assert listed == [
        {"id": "d-b", "name": "e2e-test-dashboard-" + UUID},
        {"id": "d-a", "name": "e2e-test-dashboard-" + UUID + "-updated"},
    ], "sorted by name, correctly paired, and only the eligible ones"
    # It survives serialisation -- the artifact is what a reviewer reads.
    assert report_mod.to_dict(result)["kinds"]["dashboard"]["candidates"] == listed


def test_an_aborted_kind_still_names_its_candidates() -> None:
    """A tripped breaker is exactly when you want to see the list: the run refused
    to act precisely because the set was large or suspicious."""
    spec = registry.KINDS["dashboard"]
    rows = [
        {"uuid": "d%d" % i, "name": "e2e-test-dashboard-" + UUID, "createdTimestamp": iso(**OLD)} for i in range(30)
    ] + [{"uuid": "o%d" % i, "name": "real-%d" % i, "createdTimestamp": iso(**OLD)} for i in range(200)]
    result = run_kind(FakeClient().serve_rows(spec, rows), "dashboard", limits=Limits(max_deletes_per_kind=10))
    report = result.kinds["dashboard"]

    assert report.aborted
    # Compare the whole serialized set: a count alone passes even if sweep.py
    # dropped, duplicated or mispaired records while still emitting 30 of them.
    assert report_mod.to_dict(result)["kinds"]["dashboard"]["candidates"] == sorted(
        ({"id": "d%d" % i, "name": "e2e-test-dashboard-" + UUID} for i in range(30)),
        key=lambda c: (c["name"], c["id"]),
    )


# ------------------------------------------- synthetic companion monitors (BE-2727)
#
# This kind deletes a MONITOR through the SYNTHETICS route, because no monitor
# route can touch it (403 by design). Its success signal is an error status, and
# its safety depends on the owning synthetic being gone. Both of those are exactly
# the kind of thing that decays silently, so all of it is pinned here.

COMPANION = "synthetic-companion-monitor"
SYNTH_LIST = "/api/synthetics/v1/rules"


def companion_row(origin_id: str, *, name: str = "e2e-test-synthetic-" + UUID, **over: Any) -> Dict[str, Any]:
    row: Dict[str, Any] = {
        "uuid": "mon-" + origin_id,
        "originId": origin_id,
        "originType": "SyntheticTest",
        "title": "[synthetic] - " + name,
        "createdAt": iso(**OLD),
        "updatedAt": iso(**OLD),
    }
    row.update(over)
    return row


def companion_client(rows: Sequence[Mapping[str, Any]], *, synthetics: Any = ()) -> FakeClient:
    """Serves the monitor listing plus the synthetics listing the gate consults."""
    client = FakeClient().serve_rows(registry.KINDS[COMPANION], rows)
    if isinstance(synthetics, (list, tuple)):
        client.on(SYNTH_LIST, Response(200, json.dumps({"synthetics": list(synthetics)}).encode()))
    else:
        client.on(SYNTH_LIST, synthetics)
    return client


def test_only_synthetic_owned_monitors_are_candidates() -> None:
    """A title alone must not qualify a monitor for deletion through this route.

    The `[synthetic] - ...` name pattern is the primary selector, and it already
    keeps an ordinary `e2e-test-monitor-<uuid>` out. What include_only_when adds is
    the case the name cannot judge: a monitor CARRYING that title while not being a
    companion at all. Its originId then means something else, or nothing, and
    handing it to the synthetics delete route addresses an unrelated resource.

    Sabotage: drop include_only_when. The impostor becomes a candidate."""
    rows = [
        companion_row("s1"),
        # Right title, not a companion -- originId points at another kind's id.
        companion_row("someone-elses-config-id", originType="Monitor"),
        # Belongs to the `monitor` kind; excluded by the name pattern, not by type.
        {
            "uuid": "plain",
            "originType": None,
            "title": "e2e-test-monitor-" + UUID,
            "createdAt": iso(**OLD),
            "updatedAt": iso(**OLD),
        },
    ]
    client = companion_client(rows)
    report = run_kind(client, COMPANION).kinds[COMPANION]

    assert [c["id"] for c in report.candidates] == ["s1"]
    assert report.excluded == 1, "the impostor is reported as excluded, not silently dropped"
    assert [c.path for c in client.deletes] == [SYNTH_LIST + "/s1"]


def test_a_companion_whose_synthetic_is_still_live_is_withheld() -> None:
    """Sabotage: drop requires_absent_from. The delete then removes a LIVE synthetic
    as collateral -- the one failure mode that is not recoverable by re-running."""
    rows = [companion_row("gone-1"), companion_row("live-1")]
    client = companion_client(rows, synthetics=[{"id": "live-1", "name": "e2e-test-synthetic-" + UUID}])
    report = run_kind(client, COMPANION).kinds[COMPANION]

    assert report.skipped_dependency_present == 1
    assert [c["id"] for c in report.candidates] == ["gone-1"], "the artifact names only what is reclaimable"
    assert [c.path for c in client.deletes] == [SYNTH_LIST + "/gone-1"]


def test_an_unreadable_synthetics_listing_aborts_instead_of_deleting() -> None:
    """Sabotage: make _drop_present_in fall through to `return list(candidates)` when
    the probe fails. Absence would then be inferred from a listing nobody read."""
    for synthetics in (TransportError("connection reset"), Response(500, b'{"error":"boom"}')):
        client = companion_client([companion_row("s1")], synthetics=synthetics)
        report = run_kind(client, COMPANION).kinds[COMPANION]

        assert report.aborted, "an unusable dependency listing must stop the kind: %r" % synthetics
        assert client.deletes == [], "nothing may be deleted on the strength of an unread listing"


def test_a_truncated_synthetics_listing_aborts() -> None:
    """A hard-capped listing that comes back full proves nothing about absence.

    Sabotage: drop the pagination_complete check from _drop_present_in."""
    cap = registry.KINDS["synthetic"].list_route.hard_cap
    assert cap, "the dependency needs a cap or this check can never fire -- see _validate"
    client = FakeClient().serve_rows(registry.KINDS[COMPANION], [companion_row("s1")])
    # A response AT the cap is indistinguishable from a truncated one, so the
    # listing cannot claim completeness and absence cannot be proved.
    at_cap = [{"id": "other-%d" % i, "name": "whatever"} for i in range(cap)]
    client.on(SYNTH_LIST, Response(200, json.dumps({"synthetics": at_cap}).encode()))

    report = run_kind(client, COMPANION).kinds[COMPANION]

    assert report.aborted and client.deletes == []


@pytest.mark.parametrize("status", [404, 410])
def test_the_config_gone_statuses_count_as_unverified_not_as_deleted(status: int) -> None:
    """404/410 mean the CONFIG was already gone. That is when the companion monitor
    should have been reaped a moment earlier -- 'should have been' is not 'was'.

    Sabotage: move 404 into gone_statuses, or treat these as 2xx. Either one claims
    a completed deletion the response never reported."""
    rows = [companion_row("s1")]
    client = companion_client(rows)
    # Reclaimed: the monitor is absent from the confirmation listing.
    served = {"n": 0}

    def monitors_handler(call: Call) -> Response:
        served["n"] += 1
        remaining = [] if served["n"] > 1 else list(rows)
        return Response(200, json.dumps({"results": remaining}).encode())

    client.on("/api/monitors/summary/query", monitors_handler)
    client.on(SYNTH_LIST + "/s1", Response(status, b'{"error":"gone"}'))

    report = run_kind(client, COMPANION).kinds[COMPANION]

    assert report.deleted == 0, "the route never said the monitor was deleted"
    assert report.already_gone == 0, "nothing here was proved absent by the status alone"
    assert report.delete_accepted == 1
    # The re-list is what turns it into a real answer.
    assert report.delete_confirmed == 1 and report.delete_unconfirmed == 0
    assert report.determinate


def test_a_companion_still_listed_after_its_delete_stays_unconfirmed() -> None:
    """The whole safety argument is 'the re-list proves it'. If the monitor is still
    there, the run must say so rather than counting a reclaim.

    Sabotage: have confirm_accepted_deletes treat every accepted delete as done."""
    rows = [companion_row("s1")]
    client = companion_client(rows)
    client.on(SYNTH_LIST + "/s1", Response(410, b'{"error":"archived"}'))

    report = run_kind(client, COMPANION).kinds[COMPANION]

    assert report.delete_accepted == 1
    assert report.delete_unconfirmed == 1 and report.delete_confirmed == 0
    assert not report.determinate, "an unproven reclaim must not read as a clean sweep"


def test_a_failed_monitor_delete_is_a_failure_not_a_reclaim() -> None:
    """500 from this route means DeleteMonitorByOrigin itself failed, which is the
    one outcome that must never be absorbed.

    Sabotage: add 500 to unverified_statuses."""
    client = companion_client([companion_row("s1")])
    client.on(SYNTH_LIST + "/s1", Response(500, b'{"message":"Failed to delete associated monitor"}'))

    report = run_kind(client, COMPANION).kinds[COMPANION]

    assert report.failed == 1 and report.delete_accepted == 0
    assert report.failures[0]["http_status"] == 500


def test_human_named_synthetic_companions_are_never_matched() -> None:
    """The 111 non-e2e companions on backend-dev are somebody's real synthetics."""
    rows = [companion_row("h%d" % i, name=n) for i, n in enumerate(["asdf", "clickhouse", "TEST", "test-synth-1234"])]
    report = run_kind(companion_client(rows), COMPANION, apply=False).kinds[COMPANION]

    assert report.matched == 0 and report.candidates == []


# ------------------------------------------------------- the lastActive freshness veto


@pytest.mark.parametrize("raw", ["not-a-date", iso(days=400), "", None])
def test_an_unreadable_last_active_never_reads_as_never_used(raw: Any) -> None:
    """`lastActive: null` means never used, and un-aged deletion of api keys and
    service accounts was agreed on that basis. A value that is PRESENT but
    unreadable is a different answer, and sharing the null path would silently
    disarm the only protection these kinds have -- including the one that stops
    the janitor revoking its own credentials.

    Sabotage: restore `if last_active is not None and last_active >= cutoff`. A
    future or malformed timestamp then falls straight through to deletable."""
    spec = registry.KINDS["api-key"]
    rows = [
        {
            "id": "k1",
            "name": "sdk-e2e-test-apikey-1712345678901234567",
            "creationDate": iso(**OLD),
            "lastActive": raw,
        }
    ]
    client = FakeClient().serve_rows(spec, rows)

    report = run_kind(client, "api-key").kinds["api-key"]

    if raw in ("", None):
        # Genuinely absent: the agreed decision stands, it is swept.
        assert report.unknown_last_active == 0
        assert [c.path for c in client.deletes] == ["/api/rbac/apikey/k1"]
    else:
        assert report.unknown_last_active == 1, "an unreadable timestamp is unknown, not unused"
        assert client.deletes == [], "nothing may be deleted on a freshness signal nobody could read"
        assert not report.determinate, "and the run must not report itself clean"


def test_the_step_summary_cannot_be_corrupted_by_the_backend_or_identity() -> None:
    """These are operator-controlled rather than tenant-controlled, so corrupting
    them is self-inflicted -- but "the rendered report cannot be broken by its own
    inputs" should not depend on a reader knowing which values were trusted.

    Sabotage: drop either _cell() from render_markdown's header. The backtick then
    closes the code span and the newline splits the heading."""
    result = sweep.SweepReport(
        backend_id="backend-dev`\n## Injected heading",
        base_url="https://api.test",
        mode="report",
        age_minutes=60,
        identity="acct`\n- injected bullet",
    )
    md = report_mod.render_markdown(result)
    header = md.splitlines()[0]

    assert header.startswith("## E2E leftover sweep - `")
    assert header.count("`") == 2, "the code span must open and close on one line"
    # The payload is allowed to survive as inert literal text inside the span --
    # what must not happen is it becoming structure. Markdown is line-oriented, so
    # the test is that no line STARTS with the injected syntax.
    starts = [ln.lstrip() for ln in md.splitlines()]
    assert not any(ln.startswith("## Injected") for ln in starts), "a newline became a heading"
    assert not any(ln.startswith("- injected") for ln in starts), "a newline became a list item"
    # The record keeps the bytes exactly as they were.
    assert report_mod.to_dict(result)["backend_id"] == "backend-dev`\n## Injected heading"
