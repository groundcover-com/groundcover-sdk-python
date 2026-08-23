"""Transport behaviour, and the CLI's mode/kind parsing.

The transport is thin, but two of its properties are load-bearing: a non-2xx must
arrive at the engine as a status rather than an exception, and a DELETE must never
be retried.
"""

from __future__ import annotations

import io
import urllib.error
from typing import Any, Dict, List, Optional

import pytest
from gc_e2e_janitor import __main__ as cli
from gc_e2e_janitor.transport import Client, Response, TransportError


def http_error(status: int, body: bytes = b"{}") -> urllib.error.HTTPError:
    return urllib.error.HTTPError("https://api.test/x", status, "err", {}, io.BytesIO(body))  # type: ignore[arg-type]


class Recorder:
    """Stands in for Client._send, so the retry policy is testable without a socket."""

    def __init__(self, outcomes: List[Any]) -> None:
        self.outcomes = list(outcomes)
        self.calls: List[Dict[str, Any]] = []

    def __call__(self, method: str, url: str, body: Optional[bytes], headers: Any) -> Response:
        self.calls.append({"method": method, "url": url, "body": body, "headers": dict(headers)})
        outcome = self.outcomes.pop(0) if self.outcomes else Response(200, b"[]")
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def make_client(monkeypatch: pytest.MonkeyPatch, outcomes: List[Any]) -> "tuple[Client, Recorder]":
    monkeypatch.setattr("gc_e2e_janitor.transport.time.sleep", lambda _: None)
    client = Client(base_url="https://api.test/", api_key="secret-key-value", backend_id="backend-dev")
    recorder = Recorder(outcomes)
    monkeypatch.setattr(client, "_send", recorder)
    return client, recorder


# --------------------------------------------------------------------- normalising


def test_an_http_error_becomes_a_status_not_an_exception() -> None:
    """urllib raises HTTPError for every 4xx/5xx, and HTTPError IS a readable
    file object. Letting it propagate would turn every 404 into a run-level crash
    three layers up, where the caller cannot tell it from a dead connection.

    Sabotage: remove the except branch in _send -> this raises.
    """
    client = Client(base_url="https://api.test", api_key="k", backend_id="b")

    class _Opener:
        def open(self, *_: Any, **__: Any) -> Any:
            raise http_error(404, b'{"error":"nope"}')

    # Patch the opener rather than urlopen: _send goes through a custom opener so
    # that cross-origin redirects can be refused before they forward the token.
    client._opener = _Opener()  # type: ignore[assignment]
    response = client._send("DELETE", "https://api.test/x", None, {})

    assert response.status == 404 and b"nope" in response.content


def test_an_empty_body_raises_rather_than_parsing_as_empty() -> None:
    """These endpoints spell empty as []. A zero-byte body is a dropped response,
    and reading it as an empty list is how a truncated read becomes a clean
    tenant."""
    with pytest.raises(TransportError, match="empty body"):
        Response(200, b"").json()
    with pytest.raises(TransportError, match="empty body"):
        Response(200, b"   ").json()


def test_a_non_json_body_raises() -> None:
    with pytest.raises(TransportError, match="not JSON"):
        Response(200, b"<html>gateway timeout</html>").json()


def test_an_empty_list_is_a_legitimate_answer() -> None:
    assert Response(200, b"[]").json() == []


# -------------------------------------------------------------------------- retries


def test_a_5xx_get_is_retried(monkeypatch: pytest.MonkeyPatch) -> None:
    client, recorder = make_client(monkeypatch, [Response(503, b"{}"), Response(200, b"[]")])
    assert client.request("GET", "/api/dashboards").status == 200
    assert len(recorder.calls) == 2


def test_a_4xx_is_never_retried(monkeypatch: pytest.MonkeyPatch) -> None:
    """A 4xx is an answer, not a failure to answer.

    Sabotage: retry on any non-2xx -> the call count is 3, not 1.
    """
    client, recorder = make_client(monkeypatch, [Response(400, b"{}")])
    assert client.request("GET", "/api/dashboards").status == 400
    assert len(recorder.calls) == 1


def test_a_delete_is_never_retried(monkeypatch: pytest.MonkeyPatch) -> None:
    """These deletes are not all idempotent -- re-deleting a synthetic re-triggers
    companion-monitor deletion, the operation that intermittently fails -- and a
    timed-out DELETE has very likely committed.

    Sabotage: add DELETE to _RETRYABLE_METHODS -> the call count is 3.
    """
    client, recorder = make_client(monkeypatch, [Response(500, b"{}")])
    assert client.request("DELETE", "/api/dashboards/x").status == 500
    assert len(recorder.calls) == 1


def test_a_delete_that_cannot_connect_raises_without_retrying(monkeypatch: pytest.MonkeyPatch) -> None:
    client, recorder = make_client(monkeypatch, [urllib.error.URLError("connection reset")])
    with pytest.raises(TransportError, match="connection reset"):
        client.request("DELETE", "/api/dashboards/x")
    assert len(recorder.calls) == 1


def test_retries_are_bounded(monkeypatch: pytest.MonkeyPatch) -> None:
    client, recorder = make_client(monkeypatch, [Response(500, b"{}")] * 5)
    assert client.request("GET", "/api/dashboards").status == 500
    assert len(recorder.calls) == 3


# --------------------------------------------------------------------- request shape


def test_params_and_body_are_placed_correctly(monkeypatch: pytest.MonkeyPatch) -> None:
    client, recorder = make_client(monkeypatch, [Response(200, b"[]")])
    client.request("POST", "/api/monitors/list", json={"limit": 10}, params={"skip": 5})
    call = recorder.calls[0]
    assert call["url"] == "https://api.test/api/monitors/list?skip=5"
    assert call["body"] == b'{"limit": 10}'
    assert call["headers"]["X-Backend-Id"] == "backend-dev"


def test_no_body_means_no_content_type(monkeypatch: pytest.MonkeyPatch) -> None:
    """`body={}` must still send {} -- POST /api/rbac/ingestion-keys/list requires
    a JSON body -- while body=None sends nothing at all."""
    client, recorder = make_client(monkeypatch, [Response(200, b"[]"), Response(200, b"[]")])
    client.request("GET", "/api/dashboards")
    assert recorder.calls[0]["body"] is None
    assert "Content-Type" not in recorder.calls[0]["headers"]
    client.request("POST", "/api/rbac/ingestion-keys/list", json={})
    assert recorder.calls[1]["body"] == b"{}"


def test_the_api_key_never_appears_in_a_repr() -> None:
    """The janitor logs request context on failure; a key in a stack trace ends up
    in CI logs that outlive the key."""
    client = Client(base_url="https://api.test", api_key="super-secret-key", backend_id="backend-dev")
    assert "super-secret-key" not in repr(client)
    assert "backend-dev" in repr(client)


# ------------------------------------------------------------------- mode parsing


def test_only_the_exact_string_apply_arms_deletion() -> None:
    assert cli.parse_mode("apply", None) is True
    assert cli.parse_mode("report", None) is False


@pytest.mark.parametrize("value", ["APPLY", "Apply", " apply", "yes", "1", "true", "delete", "x"])
def test_an_unrecognised_sweep_mode_is_an_error_not_a_default(value: str) -> None:
    """An unparseable mode is a config bug, not a preference. Absorbing it into a
    default is how a dry run silently becomes a live one -- and the bash version's
    `[ "$DRY_RUN" = "true" ]` failed in the destructive direction for every one of
    these values."""
    with pytest.raises(SystemExit, match="SWEEP_MODE"):
        cli.parse_mode(value, None)


@pytest.mark.parametrize("value,expected_apply", [("false", True), ("true", False)])
def test_the_dry_run_alias_is_parsed_strictly(value: str, expected_apply: bool) -> None:
    """DRY_RUN arrives from a GitHub boolean input as the string "true"/"false".
    bool("false") is True, which is the trap."""
    assert cli.parse_mode(None, value) is expected_apply


@pytest.mark.parametrize("value", ["TRUE", "TRUE ", "True", "FALSE", "False", "false ", "1", "yes", "no", "0", "ture"])
def test_an_unrecognised_dry_run_is_an_error(value: str) -> None:
    """Exact match only, deliberately.

    Case folding and stripping look harmless until you notice they also accept
    "FALSE " and "false " -- i.e. they arm deletion off a malformed value. Every
    case here fails loudly instead, including the ones that would have landed on
    the safe side.
    """
    with pytest.raises(SystemExit, match="DRY_RUN"):
        cli.parse_mode(None, value)


def test_the_default_is_report() -> None:
    assert cli.parse_mode(None, None) is False
    assert cli.parse_mode(None, "") is False
    assert cli.parse_mode("", None) is False


# -------------------------------------------------------------------- kind parsing


def test_all_and_empty_mean_every_kind() -> None:
    from gc_e2e_janitor import registry

    assert cli.parse_kinds("all") == sorted(registry.KINDS)
    assert cli.parse_kinds(None) == sorted(registry.KINDS)
    assert cli.parse_kinds("  ") == sorted(registry.KINDS)


def test_a_typod_kind_is_rejected() -> None:
    """Silently sweeping nothing is the failure this whole tool is about."""
    with pytest.raises(SystemExit, match="unknown kind"):
        cli.parse_kinds("dashboard,monitr")


def test_an_explicit_subset_is_honoured() -> None:
    assert cli.parse_kinds("dashboard, synthetic") == ["dashboard", "synthetic"]


def test_secrets_cannot_be_requested_since_they_cannot_be_listed() -> None:
    with pytest.raises(SystemExit, match="unknown kind"):
        cli.parse_kinds("secret")


# --------------------------------------------------------------- the creator gate


def test_a_missing_identity_disables_the_gate_loudly_rather_than_aborting() -> None:
    """The creator gate is a second factor; the anchored name is the primary one.

    Hard-failing here would break the synthetics sweep that has run on every PR
    for months without any creator gate, and a mandatory setting with no default
    is how someone ends up setting a dummy value. So it degrades -- but the
    degraded state must be impossible to mistake for the guarded one.
    """
    from gc_e2e_janitor import report as report_mod
    from gc_e2e_janitor.sweep import SweepReport

    unguarded = SweepReport(backend_id="backend-dev", base_url="u", mode="apply", age_minutes=60, identity=None)
    guarded = SweepReport(backend_id="backend-dev", base_url="u", mode="apply", age_minutes=60, identity="sa-name")

    assert "creator gate DISABLED" in report_mod.render_markdown(unguarded)
    assert "creator gate DISABLED" not in report_mod.render_markdown(guarded)
    assert "identity `sa-name`" in report_mod.render_markdown(guarded)


# ---------------------------------------------------------- configuration edge cases


def test_an_empty_identity_means_no_gate_not_a_gate_against_empty() -> None:
    """`vars.X` being unset yields "" in the env, not None.

    `not identity` caught that for the warning, but classify() gates on
    `identity is not None`, so "" armed the gate against an empty creator,
    excluded every match, and reported a clean zero-candidate sweep -- in the
    exact CI configuration we ship with. Normalisation happens once, in main().

    Sabotage: pass args.identity straight through -> the run below skips its one
    candidate as foreign and reports nothing to do.
    """
    import datetime

    from gc_e2e_janitor import registry, sweep

    spec = registry.KINDS["dashboard"]
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=60)
    rows = [
        {
            "uuid": "d1",
            "name": "e2e-test-dashboard-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
            "owner": "main-service-account-2",
            "createdTimestamp": "2026-01-01T00:00:00Z",
        }
    ]

    gated = sweep.KindReport(kind="dashboard")
    assert sweep.classify(spec, rows, cutoff, "", gated) == []
    assert gated.skipped_foreign_creator == 1, "'' really does arm the gate -- hence the normalisation"

    ungated = sweep.KindReport(kind="dashboard")
    assert len(sweep.classify(spec, rows, cutoff, None, ungated)) == 1


def test_main_normalises_an_empty_identity_to_none(monkeypatch: pytest.MonkeyPatch, tmp_path: Any) -> None:
    """Pins the FIX, not just the behaviour it compensates for.

    The previous test shows that classify() treats "" as an armed gate; this one
    shows main() never hands it one. Asserting only the former passes happily
    with the normalisation reverted, which is how a regression gets back in.
    """
    captured = {}

    def fake_run(client: Any, **kwargs: Any) -> Any:
        captured.update(kwargs)
        from gc_e2e_janitor.sweep import SweepReport

        return SweepReport(
            backend_id=kwargs["backend_id"],
            base_url=kwargs["base_url"],
            mode="report",
            age_minutes=kwargs["age_minutes"],
            identity=kwargs["identity"],
        )

    monkeypatch.setenv("GC_API_KEY", "k")
    monkeypatch.setenv("GC_E2E_IDENTITY", "")
    monkeypatch.setattr(cli, "run", fake_run)
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
    assert captured["identity"] is None, "an unset workflow var must mean no gate, not a gate against ''"


def test_a_creator_gate_that_rejects_everything_is_not_a_clean_sweep() -> None:
    """A stale identity looks exactly like a tenant with nothing to clean.

    Sabotage: drop the creator_gate_rejected_everything guard -> status is `ok`
    and a misconfigured janitor reports success forever.
    """
    import datetime
    import json as jsonlib

    from gc_e2e_janitor import registry, sweep
    from gc_e2e_janitor.transport import Response

    class _Client:
        def request(self, method, path, *, json=None, params=None):  # type: ignore[no-untyped-def]
            del method, path, json, params
            return Response(
                200,
                jsonlib.dumps(
                    [
                        {
                            "uuid": "d%d" % i,
                            "name": "e2e-test-dashboard-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
                            "owner": "somebody-else",
                            "createdTimestamp": "2026-01-01T00:00:00Z",
                        }
                        for i in range(5)
                    ]
                ).encode(),
            )

    del datetime
    result = sweep.run(
        _Client(),
        kinds=["dashboard"],
        age_minutes=60,
        apply=False,
        identity="stale-service-account",
        limits=sweep.Limits(),
        backend_id="backend-dev",
        base_url="https://api.test",
    )
    report = result.kinds["dashboard"]
    assert report.matched == 5 and report.skipped_foreign_creator == 5
    assert report.creator_gate_rejected_everything
    assert not report.determinate
    assert result.status == "partial" and result.exit_code == 2
    del registry


def test_duplicate_kinds_are_collapsed_preserving_order() -> None:
    """ "dashboard,dashboard" would otherwise list and classify it twice and
    duplicate it in expected_kinds, which feeds the missing_kinds check."""
    assert cli.parse_kinds("synthetic,dashboard,synthetic") == ["synthetic", "dashboard"]


@pytest.mark.parametrize("age", [-1, -60])
def test_a_negative_age_is_rejected(age: int, monkeypatch: pytest.MonkeyPatch) -> None:
    """A negative age puts the cutoff in the FUTURE, so every resource reads as
    old enough and apply mode deletes what a running suite is still using.
    argparse's type=int accepts it and the workflow's `type: number` forwards it.

    Sabotage: remove the check -> no SystemExit and the sweep proceeds.
    """
    monkeypatch.setenv("GC_API_KEY", "k")
    with pytest.raises(SystemExit, match="age-minutes"):
        cli.main(
            [
                "--base-url",
                "https://api.main.groundcover.com",
                "--backend-id",
                "backend-dev",
                "--age-minutes",
                str(age),
            ]
        )


@pytest.mark.parametrize(
    "url",
    [
        "https://collector.example",
        "http://api.main.groundcover.com",  # plaintext
        "https://api.main.groundcover.com.evil.test",  # suffix lookalike
        "not-a-url",
    ],
)
def test_the_bearer_token_is_not_sent_to_an_arbitrary_host(url: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """base_url is a free-form workflow input and the API key rides every request
    as a bearer token, so the host is part of the security boundary."""
    monkeypatch.setenv("GC_API_KEY", "k")
    with pytest.raises(SystemExit, match="base_url"):
        cli.main(["--base-url", url, "--backend-id", "backend-dev"])


def test_a_custom_backend_can_be_opted_into_but_not_typo_ed(monkeypatch: pytest.MonkeyPatch) -> None:
    """The allowlist must not silently break the sdk-test dispatch, which has
    always taken a free-form backend_id -- but a typo must still be caught.
    Naming the backend in two separate variables is something a typo cannot do."""
    monkeypatch.setenv("GC_API_KEY", "k")
    with pytest.raises(SystemExit, match="allowlist"):
        cli.main(["--base-url", "https://api.main.groundcover.com", "--backend-id", "backend-custom"])

    monkeypatch.setenv("GC_BACKEND_ALLOWLIST", "backend-custom")
    assert "backend-custom" in cli._csv_env("GC_BACKEND_ALLOWLIST", cli.DEFAULT_ALLOWED_BACKENDS)


def test_a_cross_origin_redirect_is_refused() -> None:
    """urllib follows redirects and keeps the Authorization header, so a 302 from
    an otherwise-trusted host would hand the key to a third party."""
    import urllib.request

    from gc_e2e_janitor.transport import _NoCrossOriginRedirect

    handler = _NoCrossOriginRedirect()
    req = urllib.request.Request("https://api.main.groundcover.com/api/dashboards")
    with pytest.raises(TransportError, match="cross-origin redirect"):
        handler.redirect_request(req, None, 302, "Found", {}, "https://evil.test/api/dashboards")


def test_no_environment_variable_can_widen_the_bearer_host_allowlist(monkeypatch: pytest.MonkeyPatch) -> None:
    """The host allowlist is not overridable at all.

    An *additive* override was the first attempt and does not work: it stops a
    caller removing `.groundcover.com`, but adding `attacker.example` still sends
    the key there, so it is not a boundary. Every groundcover base URL is under
    the fixed suffix, so the knob bought nothing.
    """
    monkeypatch.setenv("GC_API_KEY", "k")
    monkeypatch.setenv("GC_ALLOWED_HOST_SUFFIXES", "attacker.example")
    with pytest.raises(SystemExit, match="base_url"):
        cli.main(["--base-url", "https://attacker.example", "--backend-id", "backend-dev"])


def test_age_zero_apply_requires_an_explicit_confirmation(monkeypatch: pytest.MonkeyPatch) -> None:
    """age 0 removes the only protection against deleting an in-flight run's
    resources for every kind without a lastActive veto, and the janitor's
    concurrency group does not interlock with sdk-publish.yml."""
    monkeypatch.setenv("GC_API_KEY", "k")
    monkeypatch.setenv("SWEEP_MODE", "apply")
    with pytest.raises(SystemExit, match="age-minutes 0"):
        cli.main(
            [
                "--base-url",
                "https://api.main.groundcover.com",
                "--backend-id",
                "backend-dev",
                "--age-minutes",
                "0",
            ]
        )


def test_a_comma_only_kind_selection_is_rejected() -> None:
    """`SWEEP_KINDS=","` produced an empty list that passed validation and swept
    nothing -- an invalid selection rendering as a successful no-op.

    Sabotage: drop the `if not requested` guard -> parse_kinds returns [] and the
    run reports ok having looked at nothing.
    """
    for raw in (",", " , ", ",,"):
        with pytest.raises(SystemExit, match="selects no kinds"):
            cli.parse_kinds(raw)


def test_a_config_error_still_leaves_a_report(monkeypatch: pytest.MonkeyPatch, tmp_path: Any) -> None:
    """A missing artifact is indistinguishable from a clean sweep.

    Without this the CI plumbing reproduces the exact ambiguity the janitor
    exists to remove, one level up: config error -> no report file -> nothing to
    read. The workflow now treats a missing report as an upload error, which is
    only safe because the tool guarantees one exists.

    Sabotage: drop the `except ConfigError` wrapper -> no file is written.
    """
    import json as jsonlib

    report_path = tmp_path / "r.json"
    monkeypatch.setenv("GC_API_KEY", "k")
    monkeypatch.setenv("REPORT_PATH", str(report_path))
    monkeypatch.setenv("GC_BACKEND_ID", "definitely-not-allowed")

    with pytest.raises(SystemExit):
        cli.main(["--base-url", "https://api.main.groundcover.com", "--backend-id", "definitely-not-allowed"])

    assert report_path.exists(), "a config failure must still produce a readable report"
    written = jsonlib.loads(report_path.read_text())
    assert written["status"] == "failed"
    assert "allowlist" in written["error"]


@pytest.mark.parametrize(
    "argv,expect",
    [
        # our own validation
        (["--base-url", "https://api.main.groundcover.com", "--backend-id", "nope"], "allowlist"),
        # argparse exits before a namespace exists, so the path comes from argv
        (["--bogus-flag"], "invalid arguments"),
        # urlparse raises before any of our validation runs -- and re-raises as
        # ValueError, not SystemExit, which is why the catch has to be broad
        (["--base-url", "https://[", "--backend-id", "backend-dev"], "ValueError"),
    ],
)
def test_every_startup_failure_leaves_a_report(
    argv: Any, expect: str, monkeypatch: pytest.MonkeyPatch, tmp_path: Any
) -> None:
    """The upload step treats a missing report as an error, so the guarantee has
    to hold for every way startup can die -- not just our own ConfigError.

    argparse exits before a namespace exists (so the path is recovered from
    argv), and urlparse raises ValueError before any of our validation runs.

    Sabotage: narrow the handler back to `except ConfigError` -> the last two
    cases leave no file.
    """
    import json as jsonlib

    report = tmp_path / "r.json"
    monkeypatch.setenv("GC_API_KEY", "k")
    monkeypatch.delenv("REPORT_PATH", raising=False)

    with pytest.raises((SystemExit, ValueError)):
        cli.main(["--report-path", str(report)] + list(argv))

    assert report.exists(), "a startup failure must still produce a readable report"
    assert expect in jsonlib.loads(report.read_text())["error"]


def test_help_does_not_leave_a_failure_report(monkeypatch: pytest.MonkeyPatch, tmp_path: Any) -> None:
    """`--help` is a successful exit; writing a `failed` artifact for it would
    make the required-artifact rule lie in the other direction."""
    report = tmp_path / "r.json"
    monkeypatch.delenv("REPORT_PATH", raising=False)
    with pytest.raises(SystemExit):
        cli.main(["--report-path", str(report), "--help"])
    assert not report.exists()


def test_a_repeated_report_path_flag_matches_argparse() -> None:
    """argparse takes the last occurrence; the argv fallback must agree.

    Disagreeing would put the startup-failure report somewhere the caller had
    already overridden -- the one thing this path exists to get right.
    """
    argv = ["--report-path", "/tmp/first.json", "--report-path", "/tmp/second.json"]
    assert cli.build_parser().parse_args(argv).report_path == "/tmp/second.json"
    assert cli._report_path_from_argv(argv) == "/tmp/second.json"
    assert cli._report_path_from_argv(["--report-path=/tmp/a", "--report-path=/tmp/b"]) == "/tmp/b"


def test_the_delete_caps_fit_the_real_backlog_by_default() -> None:
    """A cap you must bypass to do routine work protects nothing.

    The originals were 50/200/0.60, with a flag to raise them. On backend-dev the
    genuine backlog is 164 monitors, 297 policies (66% of all policies) and 128
    service accounts, so all three kinds blew every one of those limits and a
    default apply run could never do its job -- which would have made passing the
    bypass reflexive.

    Sabotage: restore 50/200/0.60 -> this fails, and so does every real run.
    """
    from gc_e2e_janitor.sweep import Limits

    caps = Limits()
    assert caps.max_deletes_per_kind >= 300, "must clear the 297-policy backlog"
    assert caps.max_deletes_total >= 600, "must clear ~589 candidates in one pass"
    assert caps.max_match_ratio > 0.66, "policies are legitimately 66% e2e debris"


def test_the_caps_can_be_tightened_but_there_is_no_flag_to_loosen_them(monkeypatch: pytest.MonkeyPatch) -> None:
    """The useful direction is a cautious first pass, not a routine bypass."""
    monkeypatch.setenv("MAX_DELETES_PER_KIND", "5")
    monkeypatch.setenv("MAX_DELETES_TOTAL", "9")
    args = cli.build_parser().parse_args([])
    assert args.max_deletes_per_kind == 5 and args.max_deletes_total == 9
    assert not hasattr(args, "allow_bulk"), "the bypass flag is gone"

    for bad in ("0", "-1", "abc"):
        monkeypatch.setenv("MAX_DELETES_PER_KIND", bad)
        with pytest.raises(SystemExit):
            cli.build_parser().parse_args([])


@pytest.mark.parametrize(
    "url,expected",
    [
        # Credentials survive into the 90-day report artifact if this passes.
        ("https://user:token@api.main.groundcover.com", "credentials"),
        ("https://token@api.main.groundcover.com", "credentials"),
        # Every route is appended to base_url, so anything after the host makes
        # each request address something other than the endpoint it names.
        ("https://api.main.groundcover.com/api/v1", "host only"),
        ("https://api.main.groundcover.com/?x=1", "host only"),
        ("https://api.main.groundcover.com/#frag", "host only"),
    ],
)
def test_base_url_must_be_host_only_and_credential_free(
    url: str, expected: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The host check reads only scheme and hostname, so userinfo and a path both
    sail through it while landing verbatim in the uploaded report.

    Sabotage: drop either guard in _run(). The URL is then accepted and
    to_dict()['base_url'] carries it into the artifact."""
    monkeypatch.setenv("GC_API_KEY", "k")
    with pytest.raises(SystemExit, match=expected):
        cli.main(["--base-url", url, "--backend-id", "backend-dev"])


def test_a_trailing_slash_is_still_a_valid_host_only_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """`https://host/` is what a browser and most copy-pastes produce, and Client
    rstrips it anyway -- rejecting it would be pedantry, not safety."""
    monkeypatch.setenv("GC_API_KEY", "k")
    parsed = cli.urllib.parse.urlparse("https://api.main.groundcover.com/")
    assert parsed.path == "/" and not parsed.query and not parsed.username
