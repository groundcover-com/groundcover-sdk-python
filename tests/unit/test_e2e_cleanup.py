"""Unit tests for the E2E suite's cleanup harness (tests/e2e/_cleanup.py).

The harness itself only ever runs against a live tenant, so these offline tests
are what pin its contract: teardown order, what counts as "already gone", that a
genuine failure is loud, and that an id can be recovered from a unique name when
the create response was never seen.
"""

from __future__ import annotations

import itertools
from typing import Any, Dict, List, Optional

import pytest

from tests.e2e import _cleanup, _names, _singletons
from tests.e2e._cleanup import ResourceHandle, ResourceTracker, _Lister, _Spec


class _FakeResponse:
    def __init__(self, payload: Any, content: bytes = b"non-empty") -> None:
        self._payload = payload
        self.content = content
        self.status_code = 200

    def json(self) -> Any:
        return self._payload


class _FakeClient:
    """Stands in for groundcover.Client for the list-based id recovery path."""

    def __init__(self, payload: Any = None, content: bytes = b"non-empty") -> None:
        self.payload = payload
        self.content = content
        self.requests: List[Dict[str, Any]] = []

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: Any = None,
    ) -> _FakeResponse:
        self.requests.append({"method": method, "path": path, "json": json, "params": params})
        return _FakeResponse(self.payload, self.content)


class _PagedClient:
    """A list endpoint that caps each response, like POST /api/monitors/list."""

    def __init__(self, items: List[Dict[str, Any]], page_size: int, container: str = "monitors") -> None:
        self.items = items
        self.page_size = page_size
        self.container = container
        self.pages_served = 0

    def request(self, method: str, path: str, *, json: Any = None, params: Any = None) -> _FakeResponse:
        body = json or {}
        skip = int(body.get("skip", 0))
        limit = int(body.get("limit", self.page_size))
        self.pages_served += 1
        window = self.items[skip : skip + min(limit, self.page_size)]
        return _FakeResponse({self.container: window})


def _api_error(status_code: int) -> _cleanup.APIError:
    return _cleanup.APIError(status_code=status_code, body="boom")


@pytest.fixture
def specs(monkeypatch: pytest.MonkeyPatch) -> Dict[str, _Spec]:
    """Replace the real per-kind specs with fakes owned by the test."""
    replacement: Dict[str, _Spec] = {}
    monkeypatch.setattr(_cleanup, "SPECS", replacement)
    return replacement


def test_drain_deletes_dependents_before_what_they_reference(specs: Dict[str, _Spec]) -> None:
    deleted: List[str] = []
    for kind, rank in (("policy", 30), ("service-account", 20), ("api-key", 10)):
        specs[kind] = _Spec(delete=lambda c, h: deleted.append(h.kind), rank=rank)

    tracker = ResourceTracker(_FakeClient())
    # Created parent-first, as the real test does.
    for kind in ("policy", "service-account", "api-key"):
        tracker.new(kind).resource_id = "id-" + kind
    tracker.drain()

    assert deleted == ["api-key", "service-account", "policy"]


def test_drain_is_lifo_within_a_rank(specs: Dict[str, _Spec]) -> None:
    order: List[str] = []
    specs["secret"] = _Spec(delete=lambda c, h: order.append(h.resource_id or ""))

    tracker = ResourceTracker(_FakeClient())
    for n in ("first", "second", "third"):
        tracker.new("secret").resource_id = n
    tracker.drain()

    assert order == ["third", "second", "first"]


def test_already_gone_is_not_a_failure(specs: Dict[str, _Spec]) -> None:
    """A test that deleted its own resource must not produce a teardown error.

    404 only: 400 is a rejection unless the kind explicitly opts in, see below.
    """

    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(404)

    specs["secret"] = _Spec(delete=_delete)
    tracker = ResourceTracker(_FakeClient())
    tracker.new("secret").resource_id = "already-deleted"

    tracker.drain()  # must not raise


def test_delete_error_is_not_a_leak_when_the_resource_is_verifiably_gone(
    specs: Dict[str, _Spec],
) -> None:
    """DELETE /api/monitors/silences/{id} answers 500 for an id that is already gone.

    Swallowing only 404/400 turned every self-deleted silence into a teardown
    ERROR, so a delete error is confirmed against the list before it counts.
    """

    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(500)

    specs["silence"] = _Spec(
        delete=_delete,
        lister=_Lister(method="GET", path="/api/monitors/silences", id_field="id", name_field="comment"),
    )

    # The list no longer contains it: the test's own delete already worked.
    client = _FakeClient(payload=[{"id": "other", "comment": "unrelated"}])
    tracker = ResourceTracker(client)
    tracker.new("silence").resource_id = "42"

    tracker.drain()  # must not raise


def test_delete_error_is_a_leak_when_the_resource_is_still_listed(specs: Dict[str, _Spec]) -> None:
    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(500)

    specs["silence"] = _Spec(
        delete=_delete,
        lister=_Lister(method="GET", path="/api/monitors/silences", id_field="id", name_field="comment"),
    )

    client = _FakeClient(payload=[{"id": "42", "comment": "still here"}])
    tracker = ResourceTracker(client)
    tracker.new("silence").resource_id = "42"

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_presence_check_uses_the_id_so_a_renamed_resource_is_still_seen(
    specs: Dict[str, _Spec],
) -> None:
    """test_silences renames its silence before deleting, so a name check would lie."""

    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(500)

    specs["silence"] = _Spec(
        delete=_delete,
        lister=_Lister(method="GET", path="/api/monitors/silences", id_field="id", name_field="comment"),
    )

    client = _FakeClient()
    tracker = ResourceTracker(client)
    handle = tracker.new("silence")
    handle.resource_id = "42"
    # Present under a comment that no longer matches handle.name.
    client.payload = [{"id": "42", "comment": f"{handle.name}-updated"}]

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_persistent_failure_raises_out_of_drain(specs: Dict[str, _Spec]) -> None:
    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(500)

    specs["secret"] = _Spec(delete=_delete)
    tracker = ResourceTracker(_FakeClient())
    tracker.new("secret").resource_id = "stuck"

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_one_failure_does_not_strand_the_others(specs: Dict[str, _Spec]) -> None:
    deleted: List[str] = []

    def _delete(client: Any, handle: ResourceHandle) -> None:
        if handle.resource_id == "stuck":
            raise _api_error(500)
        deleted.append(handle.resource_id or "")

    specs["secret"] = _Spec(delete=_delete)
    tracker = ResourceTracker(_FakeClient())
    for n in ("a", "stuck", "b"):
        tracker.new("secret").resource_id = n

    with pytest.raises(RuntimeError):
        tracker.drain()
    assert sorted(deleted) == ["a", "b"]


def test_second_pass_retries_a_transient_conflict(specs: Dict[str, _Spec]) -> None:
    attempts: List[str] = []

    def _delete(client: Any, handle: ResourceHandle) -> None:
        attempts.append(handle.resource_id or "")
        if len(attempts) == 1:
            # e.g. 409 "still referenced", which clears once the referrer is gone.
            raise _api_error(409)

    specs["policy"] = _Spec(delete=_delete)
    tracker = ResourceTracker(_FakeClient())
    tracker.new("policy").resource_id = "p1"

    tracker.drain()  # must not raise
    assert attempts == ["p1", "p1"]


def test_id_is_recovered_by_name_when_the_create_response_was_never_seen(
    specs: Dict[str, _Spec],
) -> None:
    """The case an after-the-fact tracker cannot catch: create committed, client errored."""
    deleted: List[Optional[str]] = []
    specs["dashboard"] = _Spec(
        delete=lambda c, h: deleted.append(h.resource_id),
        lister=_Lister(method="GET", path="/api/dashboards", id_field="uuid", name_field="name"),
    )

    client = _FakeClient()
    tracker = ResourceTracker(client)
    handle = tracker.new("dashboard")
    # Simulate the server having committed the create under our name while the
    # client saw an error, so resource_id was never assigned.
    client.payload = [
        {"uuid": "someone-else", "name": "unrelated"},
        {"uuid": "recovered-id", "name": handle.name},
    ]

    assert handle.resource_id is None
    tracker.drain()
    assert deleted == ["recovered-id"]


def test_a_failed_lookup_does_not_fail_the_already_failing_test(
    specs: Dict[str, _Spec],
) -> None:
    """When the list endpoint is down too, whether the create committed is unknowable.

    Observed in CI before workflows left the SDK (AI-461): a list endpoint answering
    500 made the test fail on its own create and then produced a teardown ERROR for
    that same fault.
    """

    class _BrokenListClient:
        def request(self, method: str, path: str, **kwargs: Any) -> _FakeResponse:
            raise _api_error(500)

    specs["monitor"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(
            method="POST", path="/api/monitors/list", container="monitors", id_field="uuid", name_field="title"
        ),
    )

    tracker = ResourceTracker(_BrokenListClient())
    tracker.new("monitor")  # create failed, so no resource_id

    # Warns rather than raising: no id was ever captured, so the test already failed
    # against this same endpoint, and a second red mark for one fault helps nobody.
    tracker.drain()


def test_delete_failure_stands_when_the_presence_check_cannot_run(specs: Dict[str, _Spec]) -> None:
    """A lookup failure must not be read as proof the resource is gone."""
    calls = {"n": 0}

    def _request(method: str, path: str, **kwargs: Any) -> _FakeResponse:
        raise _api_error(503)

    class _Client:
        request = staticmethod(_request)

    def _delete(client: Any, handle: ResourceHandle) -> None:
        calls["n"] += 1
        raise _api_error(500)

    specs["silence"] = _Spec(
        delete=_delete,
        lister=_Lister(method="GET", path="/api/monitors/silences", id_field="id", name_field="comment"),
    )

    tracker = ResourceTracker(_Client())
    tracker.new("silence").resource_id = "42"

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_nothing_to_clean_when_the_create_never_committed(specs: Dict[str, _Spec]) -> None:
    deleted: List[str] = []
    specs["dashboard"] = _Spec(
        delete=lambda c, h: deleted.append(h.kind),
        lister=_Lister(method="GET", path="/api/dashboards", id_field="uuid", name_field="name"),
    )

    tracker = ResourceTracker(_FakeClient(payload=[]))
    tracker.new("dashboard")
    tracker.drain()

    assert deleted == []


def test_recovery_pages_past_a_capped_list_response(specs: Dict[str, _Spec]) -> None:
    """backend-dev holds more monitors than one page; recovery must page through.

    A single capped request made anything past the cap invisible to cleanup.
    """
    deleted: List[Optional[str]] = []
    specs["monitor"] = _Spec(
        delete=lambda c, h: deleted.append(h.resource_id),
        lister=_Lister(
            method="POST",
            path="/api/monitors/list",
            container="monitors",
            id_field="uuid",
            name_field="title",
            page_size=100,
        ),
    )

    client = _PagedClient(items=[], page_size=100)
    tracker = ResourceTracker(client)
    handle = tracker.new("monitor")
    # The target sits on the fourth page, well past a single capped response.
    client.items = [{"uuid": f"m{i}", "title": f"other-{i}"} for i in range(350)]
    client.items[320] = {"uuid": "deep-id", "title": handle.name}

    tracker.drain()

    assert deleted == ["deep-id"]
    assert client.pages_served >= 4


def test_pagination_stops_on_a_short_page(specs: Dict[str, _Spec]) -> None:
    specs["monitor"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(
            method="POST",
            path="/api/monitors/list",
            container="monitors",
            id_field="uuid",
            name_field="title",
            page_size=100,
        ),
    )

    client = _PagedClient(items=[{"uuid": f"m{i}", "title": f"other-{i}"} for i in range(150)], page_size=100)
    tracker = ResourceTracker(client)
    tracker.new("monitor")
    tracker.drain()

    # Two pages: a full one, then a short one that ends the walk.
    assert client.pages_served == 2


def test_ingestion_keys_are_declared_as_name_addressed() -> None:
    """Pins the production spec, so this cannot drift away from the test below."""
    assert _cleanup.SPECS["ingestion-key"].id_required is False


def test_name_addressed_kind_is_cleaned_without_any_id(specs: Dict[str, _Spec]) -> None:
    """A kind deleted by name must not skip cleanup just because no id was captured.

    Requiring an id here silently skipped the delete for the one kind that never
    needs one (ingestion keys) -- the case where pre-registration should pay off
    completely. Uses a synthetic kind so it tests the behaviour, not the config.
    """
    deleted: List[str] = []
    specs["name-addressed-kind"] = _Spec(
        delete=lambda c, h: deleted.append(h.name),
        id_required=False,
    )

    tracker = ResourceTracker(_FakeClient())
    handle = tracker.new("name-addressed-kind")  # no resource_id ever set
    tracker.drain()

    assert deleted == [handle.name]


def test_kind_without_a_lister_cannot_recover_but_does_not_fail(specs: Dict[str, _Spec]) -> None:
    """Secrets have no list route; that is a known hole, not a teardown error."""
    deleted: List[str] = []
    specs["secret"] = _Spec(delete=lambda c, h: deleted.append(h.kind), lister=None)

    tracker = ResourceTracker(_FakeClient())
    tracker.new("secret")
    tracker.drain()

    assert deleted == []


def test_finalizers_run_after_every_delete(specs: Dict[str, _Spec]) -> None:
    order: List[str] = []
    specs["secret"] = _Spec(delete=lambda c, h: order.append("delete"))

    tracker = ResourceTracker(_FakeClient())
    tracker.add_finalizer("restore config", lambda: order.append("restore"))
    tracker.new("secret").resource_id = "s1"
    tracker.drain()

    assert order == ["delete", "restore"]


def test_a_failing_finalizer_fails_the_test(specs: Dict[str, _Spec]) -> None:
    def _boom() -> None:
        raise RuntimeError("restore failed")

    tracker = ResourceTracker(_FakeClient())
    tracker.add_finalizer("restore config", _boom)

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_unknown_kind_is_rejected_at_registration() -> None:
    tracker = ResourceTracker(_FakeClient())
    with pytest.raises(KeyError, match="unknown resource kind"):
        tracker.new("not-a-real-kind")


def test_every_declared_kind_has_a_deleter() -> None:
    assert _cleanup.SPECS, "no resource kinds declared"
    for kind, spec in _cleanup.SPECS.items():
        assert callable(spec.delete), f"{kind} has no deleter"


def test_names_are_unique_and_suite_identifiable() -> None:
    names = [_names.unique_name("secret") for _ in range(50)]
    assert len(set(names)) == 50
    assert all(_names.belongs_to_suite(n) for n in names)
    assert not _names.belongs_to_suite("some-customer-dashboard")


def test_synthetic_names_are_still_recognised_by_the_janitor() -> None:
    """Guards the name-based janitor in tools/gc_e2e_janitor.

    If a rename breaks this, the janitor silently stops recognising leaked
    synthetics -- and there is no server-side TTL on them.

    This asks the real registry rather than a copy of its regex. The copy is how
    this drifted before: the sweeper's pattern lived in a bash script nothing
    imported, so widening it (099b431aa2) and renaming a kind were separate
    events that nothing tied together. tests/unit/test_janitor_registry.py now
    makes the same assertion for every kind, not just synthetics.
    """
    from gc_e2e_janitor import registry
    from gc_e2e_janitor.sweep import matches_kind

    for kind in ("http-synthetic", "tcp-synthetic", "ssl-synthetic", "dns-synthetic"):
        assert kind in _cleanup.SPECS, f"{kind} is not a declared resource kind"
        name = _names.unique_name(kind)
        assert matches_kind(registry.KINDS["synthetic"], name), f"{kind} names no longer match the janitor"


def test_run_id_prefers_an_explicit_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", "verifyx")
    monkeypatch.setenv("GITHUB_RUN_ID", "999")
    assert _names.run_id() == "verifyx"


def test_uppercase_override_is_lowercased_and_digested(monkeypatch: pytest.MonkeyPatch) -> None:
    """Uppercase is not DNS-1123-safe, so it cannot be preserved verbatim."""
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", "verifyA")
    got = _names.run_id()
    assert got.startswith("verifya") and got != "verifya"


def test_run_id_distinguishes_ci_re_runs(monkeypatch: pytest.MonkeyPatch) -> None:
    """GITHUB_RUN_ID is unchanged by a re-run, so the attempt has to be in the id.

    Without it a retried job mints the same names as the attempt that failed, and
    a duplicate monitor title is a 409 rather than a warning.
    """
    monkeypatch.delenv("GC_E2E_RUN_ID", raising=False)
    monkeypatch.setenv("GITHUB_RUN_ID", "30899699292")

    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GITHUB_RUN_ATTEMPT", "1")
    first = _names.run_id()

    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GITHUB_RUN_ATTEMPT", "2")
    second = _names.run_id()

    assert first != second
    assert first == "30899699292a1" and second == "30899699292a2"


def test_run_id_falls_back_to_a_random_id(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.delenv("GC_E2E_RUN_ID", raising=False)
    monkeypatch.delenv("GITHUB_RUN_ID", raising=False)
    generated = _names.run_id()
    assert generated.startswith("r") and len(generated) == 17


def test_pid_and_counter_cannot_collide_across_workers(monkeypatch: pytest.MonkeyPatch) -> None:
    """pid 12 + counter 11 and pid 121 + counter 1 must not produce the same name.

    Concatenated they both read "1211", and every worker starts its counter at 1, so
    two workers in one run could mint one name -- which name-based recovery would
    then resolve to the wrong worker's resource.
    """
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", "sharedrun")

    monkeypatch.setattr(_names, "_counter", itertools.count(11))
    monkeypatch.setattr(_names.os, "getpid", lambda: 12)
    worker_a = _names.unique_name("secret")

    monkeypatch.setattr(_names, "_counter", itertools.count(1))
    monkeypatch.setattr(_names.os, "getpid", lambda: 121)
    worker_b = _names.unique_name("secret")

    assert worker_a != worker_b


def test_punctuation_only_run_id_falls_back_to_random(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", "!!!///")
    generated = _names.run_id()
    assert generated.startswith("r") and len(generated) == 17


def test_long_run_ids_stay_distinct_after_truncation(monkeypatch: pytest.MonkeyPatch) -> None:
    """Truncation alone would collapse two overrides sharing a 24-char prefix."""
    shared_prefix = "a" * 30
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", shared_prefix + "-one")
    first = _names.run_id()
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", shared_prefix + "-two")
    second = _names.run_id()

    assert first != second
    assert len(first) <= 24 and len(second) <= 24


def test_recovery_skips_a_row_another_handle_already_owns(specs: Dict[str, _Spec]) -> None:
    """test_monitors registers a duplicate under the same title on purpose.

    Without excluding claimed ids, the duplicate's recovery resolves to the original
    row, deletes it twice, and leaves the duplicate on the tenant.
    """
    deleted: List[Optional[str]] = []
    specs["monitor"] = _Spec(
        delete=lambda c, h: deleted.append(h.resource_id),
        lister=_Lister(
            method="POST",
            path="/api/monitors/list",
            container="monitors",
            id_field="uuid",
            name_field="title",
        ),
    )

    client = _FakeClient()
    tracker = ResourceTracker(client)
    original = tracker.new("monitor")
    original.resource_id = "original-id"
    duplicate = tracker.new("monitor", name=original.name)  # same title, no id

    client.payload = {
        "monitors": [
            {"uuid": "original-id", "title": original.name},
            {"uuid": "duplicate-id", "title": original.name},
        ]
    }
    tracker.drain()

    assert duplicate.resource_id == "duplicate-id"
    assert sorted(d for d in deleted if d) == ["duplicate-id", "original-id"]


def test_unexpected_list_shape_raises_instead_of_looking_empty(specs: Dict[str, _Spec]) -> None:
    """A response we cannot parse must not read as 'the resource is not there'."""
    specs["dashboard"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(method="GET", path="/api/dashboards", id_field="uuid", name_field="name"),
    )

    # An envelope without the expected key: previously became [] and the resource
    # was silently skipped.
    client = _FakeClient(payload={"unexpected": [{"uuid": "x", "name": "y"}]})
    tracker = ResourceTracker(client)
    tracker.new("dashboard")

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


class _ConfigClient:
    """Stands in for the client in singleton snapshot/restore tests."""

    def __init__(self, payload: Any, status_code: int = 200, content: bytes = b"body") -> None:
        self._response = _FakeResponse(payload)
        self._response.status_code = status_code  # type: ignore[attr-defined]
        self._response.content = content  # type: ignore[attr-defined]
        self.calls: List[str] = []

    def get(self, path: str) -> Any:
        return self._response

    def put(self, path: str, *, json: Any = None) -> None:
        self.calls.append(f"PUT {json}")

    def delete(self, path: str) -> None:
        self.calls.append("DELETE")


def test_singleton_snapshot_treats_a_missing_payload_key_as_absent() -> None:
    """A deleted metrics-pipeline config answers 200 with no `rules` key at all."""
    client = _ConfigClient({"uuid": "u", "created_by": "x", "created_timestamp": "t"})
    assert _singletons.snapshot(client, "metrics-pipeline") is None


def test_singleton_snapshot_rejects_a_non_object_payload() -> None:
    """Reading a garbled response as 'no config' would DELETE a live config."""
    client = _ConfigClient(["not", "an", "object"])
    with pytest.raises(RuntimeError, match="unexpected"):
        _singletons.snapshot(client, "logs-pipeline")


def test_singleton_snapshot_preserves_a_present_value() -> None:
    client = _ConfigClient({"value": "ottlRules: []"})
    assert _singletons.snapshot(client, "logs-pipeline") == "ottlRules: []"


def test_singleton_restore_puts_back_a_non_empty_snapshot() -> None:
    client = _ConfigClient({})
    _singletons.restore(client, "logs-pipeline", "ottlRules: []")
    assert client.calls == ["PUT {'value': 'ottlRules: []'}"]


@pytest.mark.parametrize("empty", [None, "", {}])
def test_singleton_restore_deletes_when_there_was_nothing_to_restore(empty: Any) -> None:
    """An empty value cannot be PUT back: the update body requires a non-empty value."""
    client = _ConfigClient({})
    _singletons.restore(client, "metrics-pipeline", empty)
    assert client.calls == ["DELETE"]


def test_get_listers_page_via_query_params(specs: Dict[str, _Spec]) -> None:
    """GET /api/monitors/silences caps at SilencesDefaultLimit=1000 and pages by query.

    Sending limit/skip in a JSON body would be ignored by a GET handler, so a
    silence past the cap would stay invisible to recovery.
    """
    specs["silence"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(
            method="GET",
            path="/api/monitors/silences",
            id_field="id",
            name_field="comment",
            page_size=1000,
        ),
    )

    client = _FakeClient(payload=[])
    tracker = ResourceTracker(client)
    tracker.new("silence")
    tracker.drain()

    assert client.requests, "no list request was made"
    first = client.requests[0]
    assert first["params"] == {"limit": 1000, "skip": 0}
    assert first["json"] is None


def test_exhausting_the_page_cap_raises_instead_of_reading_as_absent(specs: Dict[str, _Spec]) -> None:
    """A server ignoring `skip` must not make a leak look like a clean teardown."""
    specs["monitor"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(
            method="POST",
            path="/api/monitors/list",
            container="monitors",
            id_field="uuid",
            name_field="title",
            page_size=2,
        ),
    )

    # Always returns a full page, so the walk never terminates on its own.
    client = _FakeClient(payload={"monitors": [{"uuid": "a", "title": "x"}, {"uuid": "b", "title": "y"}]})
    tracker = ResourceTracker(client)
    tracker.new("monitor")

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_400_is_not_accepted_as_gone_when_the_listing_can_check(specs: Dict[str, _Spec]) -> None:
    """A rejected delete must not read the same as a completed one."""

    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(400)

    specs["data-integration"] = _Spec(
        delete=_delete,
        lister=_Lister(method="GET", path="/api/integrations/v1/data/config", id_field="id", name_field="name"),
    )

    client = _FakeClient(payload=[{"id": "42", "name": "still-here"}])
    tracker = ResourceTracker(client)
    tracker.new("data-integration").resource_id = "42"

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_zero_byte_list_response_raises_instead_of_reading_as_empty(specs: Dict[str, _Spec]) -> None:
    """These endpoints spell an empty collection "[]"; no body at all is a surprise."""
    specs["dashboard"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(method="GET", path="/api/dashboards", id_field="uuid", name_field="name"),
    )

    tracker = ResourceTracker(_FakeClient(payload=None, content=b""))
    tracker.new("dashboard")

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_400_is_never_accepted_as_gone(specs: Dict[str, _Spec]) -> None:
    """Only 404 means gone.

    A 400 is a rejected request, including for kinds with no listing to check
    against: ingestion keys answer 404 on a real inCloud backend, so nothing needs a
    400 escape hatch, and a 400 surfacing is how a wrong-backend delete gets caught.
    """

    def _delete(client: Any, handle: ResourceHandle) -> None:
        raise _api_error(400)

    specs["secret"] = _Spec(delete=_delete, lister=None)  # accepts_400_as_gone defaults False
    tracker = ResourceTracker(_FakeClient())
    tracker.new("secret").resource_id = "secretRef::store::x"

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_an_explicit_empty_lister_body_is_still_sent(specs: Dict[str, _Spec]) -> None:
    """`body={}` means "send {}", which truthiness testing silently dropped."""
    specs["monitor"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(
            method="POST", path="/api/monitors/list", body={}, container="monitors", id_field="uuid", name_field="title"
        ),
    )

    client = _FakeClient(payload={"monitors": []})
    tracker = ResourceTracker(client)
    tracker.new("monitor")
    tracker.drain()

    assert client.requests[0]["json"] == {}


def test_markers_recognise_the_go_suites_payloads() -> None:
    """The Go e2e job writes these same four configs, in parallel with this one.

    If its payload is not recognised, the finalizer PUTs it back and it becomes the
    shared tenant's permanent config -- worse than the false skip the narrow markers
    were meant to avoid. Fixtures: sdk/tests/e2e/logspipeline_test.go:13,
    metricsaggregator_test.go:13, metricspipeline_test.go:19.
    """
    go_logs = 'ottlRules:\n- ruleName: example-rule\n  statements:\n    - set(attributes["test.key"], "test-value")'
    go_aggregator = "content: |\n  - match: '{__name__=~\"test_metric_counter\"}'"
    go_metrics_rules = {
        "keepRegex": ["http_requests_total", "process_cpu_seconds_total"],
        "addLabel": {"team": "platform"},
    }

    ours_yaml = "ottlRules:\n- ruleName: sdk-e2e-test-rule"
    ours_rules = {"addLabel": {"sdk_e2e_test": "true"}}

    for payload in (go_logs, go_aggregator, go_metrics_rules, ours_yaml, ours_rules):
        assert _singletons.looks_like_test_payload(payload, _singletons.SUITE_MARKERS), payload

    # A plausible real tenant config is still left alone.
    assert not _singletons.looks_like_test_payload(
        'ottlRules:\n- ruleName: redact-pii\n  statements:\n    - set(attributes["user.email"], "***")',
        _singletons.SUITE_MARKERS,
    )


def test_run_ids_are_dns1123_safe(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ingestion-key names must pass validation.IsDNS1123Label (create_key.go:292)."""
    import re as _re

    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", "VerifyA-UPPER")
    name = _names.unique_name("ingestion-key")

    assert _re.fullmatch(r"[a-z0-9]([-a-z0-9]*[a-z0-9])?", name), name
    assert len(name) <= 63, len(name)


def test_sanitize_layout_is_exact(monkeypatch: pytest.MonkeyPatch) -> None:
    """Pin the digest layout so a future change cannot weaken collision resistance."""
    import hashlib as _hashlib

    raw = "run-1"
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.setenv("GC_E2E_RUN_ID", raw)
    got = _names.run_id()

    expected_digest = _hashlib.sha256(raw.encode()).hexdigest()[:8]
    assert got.endswith(expected_digest)
    assert got == "run1" + expected_digest
    assert len(got) <= 24


def test_matched_row_without_a_usable_id_raises(specs: Dict[str, _Spec]) -> None:
    """The resource exists but cannot be addressed: a leak to report, not to skip."""
    specs["dashboard"] = _Spec(
        delete=lambda c, h: None,
        lister=_Lister(method="GET", path="/api/dashboards", id_field="uuid", name_field="name"),
    )

    client = _FakeClient()
    tracker = ResourceTracker(client)
    handle = tracker.new("dashboard")
    client.payload = [{"uuid": None, "name": handle.name}]

    with pytest.raises(RuntimeError, match="may have leaked"):
        tracker.drain()


def test_generated_names_fit_a_dns1123_label_for_every_kind() -> None:
    """Re-derives the run-id budget from the real SPECS, so the cap cannot drift.

    Ingestion-key names are validated as DNS-1123 labels (63 chars max,
    ingestionkeys/create_key.go:292), and the run id is only one segment of the
    name. A cap chosen without the rest of the budget in mind produced names over
    the limit.
    """
    longest_kind = max(_cleanup.SPECS, key=len)
    worst_case = (
        len(_names.PREFIX)
        + 1
        + len(longest_kind)
        + 1
        + _names._MAX_RUN_ID
        + len("-p")
        + 7  # pid, generously wide
        + 1  # the "n" separator
        + 4  # counter
    )
    assert worst_case <= 63, f"{longest_kind} can exceed a DNS-1123 label: {worst_case} chars"


def test_local_fallback_run_id_has_enough_entropy(monkeypatch: pytest.MonkeyPatch) -> None:
    """pid and counter are not globally unique, so the run token carries uniqueness.

    Leaked resources from past runs stay on the tenant, so the population a new run
    must avoid colliding with keeps growing; 32 bits was thin for that.
    """
    monkeypatch.setattr(_names, "_run_id", "")
    monkeypatch.delenv("GC_E2E_RUN_ID", raising=False)
    monkeypatch.delenv("GITHUB_RUN_ID", raising=False)
    generated = _names.run_id()

    assert generated.startswith("r")
    assert len(generated) - 1 >= 16, "expected at least 64 bits of hex in the fallback id"
    assert len(generated) <= _names._MAX_RUN_ID


class _StatefulConfigClient:
    """Config endpoint whose current value can change between snapshot and restore."""

    def __init__(self, current: Any) -> None:
        self.current = current
        self.calls: List[str] = []

    def get(self, path: str) -> Any:
        return _FakeResponse({"value": self.current} if self.current is not None else {})

    def put(self, path: str, *, json: Any = None) -> None:
        self.calls.append(f"PUT {json}")

    def delete(self, path: str) -> None:
        self.calls.append("DELETE")


def test_restore_stands_down_when_real_config_is_back() -> None:
    """No compare-and-swap exists, so a blind restore can clobber what landed since.

    If the current value is no longer a test payload, someone else's real config is
    in place and this run's stale snapshot is the wrong thing to reinstate.
    """
    client = _StatefulConfigClient(current="ottlRules:\n- ruleName: customer-redaction")

    _singletons.restore(client, "logs-pipeline", "sdk-e2e-test snapshot", _singletons.SUITE_MARKERS)

    assert client.calls == [], "should not have written anything"


def test_restore_proceeds_when_a_test_payload_is_still_in_place() -> None:
    client = _StatefulConfigClient(current="ottlRules:\n- ruleName: sdk-e2e-test-rule")

    _singletons.restore(client, "logs-pipeline", "original config", _singletons.SUITE_MARKERS)

    assert client.calls == ["PUT {'value': 'original config'}"]


def test_restore_proceeds_when_the_config_is_empty() -> None:
    """The normal path: the test deleted it, so the slot is empty and ours to refill."""
    client = _StatefulConfigClient(current=None)

    _singletons.restore(client, "logs-pipeline", "original config", _singletons.SUITE_MARKERS)

    assert client.calls == ["PUT {'value': 'original config'}"]


def test_snapshot_rejects_a_payload_of_the_wrong_type() -> None:
    """Whatever snapshot captures is replayed verbatim, so refuse odd shapes."""
    client = _ConfigClient({"rules": "should have been an object"})

    with pytest.raises(RuntimeError, match="expected dict"):
        _singletons.snapshot(client, "metrics-pipeline")


def test_forget_stops_the_redundant_delete(specs: Dict[str, _Spec]) -> None:
    """A test that deleted its own resource should not have it deleted twice.

    The second call is not a no-op server-side even though the client can ignore the
    response: the silence endpoint answers 500 for it (BE-2719), and for synthetics it
    re-triggers companion-monitor deletion. Go carries this as ``Untrack*``.
    """
    deleted: List[str] = []
    specs["silence"] = _Spec(delete=lambda c, h: deleted.append(h.resource_id or ""))

    tracker = ResourceTracker(_FakeClient())
    kept = tracker.new("silence")
    kept.resource_id = "still-tracked"
    self_deleted = tracker.new("silence")
    self_deleted.resource_id = "test-deleted-this"

    tracker.forget(self_deleted)
    tracker.drain()

    assert deleted == ["still-tracked"]


def test_forget_is_safe_for_an_untracked_handle(specs: Dict[str, _Spec]) -> None:
    specs["secret"] = _Spec(delete=lambda c, h: None)
    tracker = ResourceTracker(_FakeClient())
    handle = tracker.new("secret")
    tracker.forget(handle)
    tracker.forget(handle)  # idempotent
    tracker.drain()
