"""Keep the janitor's table from drifting away from the suites it cleans up after.

The failure this file exists to prevent has already happened once: commit
099b431aa2 widened the sweeper's regex because Go's ``TestSyntheticsEndpoints``
mints a bare ``e2e-test-synthetic-<uuid>`` with no kind infix, and those
synthetics leaked from the janitor's introduction until July 2026. Nothing failed
in the meantime -- an unrecognised name simply is not swept, and the sweep reports
success.

``tests/e2e/_names.py`` used to carry that as a warning asking the next author to
remember. Prose does not fail CI. These tests do.

They import ``tests.e2e._cleanup``, which imports generated code, so they carry
the same ``needs: [generate]`` dependency the rest of ``tests/unit`` already has.
That is fine here and deliberately not fine at runtime -- see
``test_the_janitor_never_imports_generated_code``.
"""

from __future__ import annotations

import ast
import dataclasses
import pathlib
import re
from typing import Dict, List, Set, Tuple

import pytest
from gc_e2e_janitor import registry
from gc_e2e_janitor.sweep import matches_kind


def _validate_with(spec: registry.Kind) -> None:
    """Re-run the import-time validator with one kind swapped out.

    _validate() reads the module-level table, so a malformed spec has to be put
    there to be judged. Restored in a finally: leaving a broken kind installed
    would fail unrelated tests in whatever order they happen to run.
    """
    original = registry.KINDS[spec.kind]
    registry.KINDS[spec.kind] = spec
    try:
        registry._validate()
    finally:
        registry.KINDS[spec.kind] = original


REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
JANITOR_DIR = pathlib.Path(registry.__file__).resolve().parent
GO_E2E_DIR = REPO_ROOT / "sdk" / "tests" / "e2e"

# Python's synthetic kinds all share one route and collapse to one janitor kind.
_SYNTHETIC_SUFFIX = "-synthetic"


def _collapse(kind: str) -> str:
    return "synthetic" if kind.endswith(_SYNTHETIC_SUFFIX) else kind


def go_e2e_source() -> str:
    """Every Go e2e test file, with whole-line comments removed.

    A name mentioned in a comment -- "renamed from X" -- is not a name being
    minted, and counting it either way makes both directions of the drift check
    wrong: a retired shape looks alive, and a live one could be "proved" present
    by prose alone. Trailing comments are left in place so a URL's `//` survives.
    """
    lines = []
    for path in sorted(GO_E2E_DIR.glob("*_test.go")):
        lines += [ln for ln in path.read_text().splitlines() if not ln.lstrip().startswith("//")]
    return "\n".join(lines)


# ---------------------------------------------------------------- D1: kind closure


def test_every_kind_the_suite_tracks_is_swept_or_explicitly_excluded() -> None:
    """A new resource kind must land in KINDS or UNSWEEPABLE -- never neither.

    Without this, adding a kind to the e2e suite silently creates a new class of
    leak that no janitor knows about, and nothing anywhere goes red.
    """
    from tests.e2e import _cleanup

    known = set(registry.KINDS) | set(registry.UNSWEEPABLE)
    unknown = sorted({_collapse(k) for k in _cleanup.SPECS} - known)
    assert not unknown, (
        "the e2e suite tracks {} but the janitor has never heard of them. Add each to "
        "registry.KINDS, or to registry.UNSWEEPABLE with a reason.".format(unknown)
    )


def test_unsweepable_kinds_state_why() -> None:
    for kind, reason in registry.UNSWEEPABLE.items():
        assert len(reason.strip()) > 40, "{}: needs a real reason, not {!r}".format(kind, reason)


# --------------------------------------------- D2: name coverage, all three suites


def test_python_suite_names_are_matched_for_every_kind() -> None:
    """Every name the Python suite can mint is recognised by its kind.

    Uses the real minting function rather than a transcribed literal, so renaming
    a kind token in _names.py/SPECS fails here instead of silently un-sweeping it.
    """
    from tests.e2e import _cleanup, _names

    for kind in sorted(_cleanup.SPECS):
        collapsed = _collapse(kind)
        if collapsed in registry.UNSWEEPABLE:
            continue
        name = _names.unique_name(kind)
        assert matches_kind(registry.KINDS[collapsed], name), (
            "the Python suite mints {!r} for kind {!r}, and the janitor no longer recognises it. "
            "Add the token to registry.KINDS[{!r}].name_tokens.".format(name, kind, collapsed)
        )


# Transcribed from sdk/tests/e2e/*_test.go. Kept honest by
# test_transcribed_go_literals_still_appear_in_the_go_suite below.
GO_NAME_SAMPLES: Dict[str, List[str]] = {
    "dashboard": ["e2e-test-dashboard-3f2504e0-4f89-11d3-9a0c-0305e82c3301"],
    # monitors_test.go:51 -- title case and spaces; the trailing int is
    # rng.Intn(10_000_000), a random number and NOT a timestamp.
    "monitor": ["E2E Test - K8s Pod Not Healthy Monitor - 8461234"],
    "silence": ["e2e-test-silence-3f2504e0-4f89-11d3-9a0c-0305e82c3301"],
    "policy": [
        "e2e-test-policy-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "sdk-e2e-test-policy-for-apikey-1712345678901234567",
        "e2e-test-policy-for-sa-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
    ],
    "service-account": [
        "e2e-test-sa-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "sdk-e2e-test-sa-for-apikey-1712345678901234567",
    ],
    # Go writes "apikey", Python writes "api-key".
    "api-key": ["sdk-e2e-test-apikey-1712345678901234567"],
    "synthetic": [
        # The bare one is the 099b431aa2 case.
        "e2e-test-synthetic-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "e2e-test-tcp-synthetic-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "e2e-test-ssl-synthetic-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "e2e-test-dns-synthetic-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
    ],
    "data-integration": [
        "e2e-test-cloudwatch-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "e2e-test-cloudwatch-tags-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
        "e2e-test-cloudwatch-tags-updated-3f2504e0-4f89-11d3-9a0c-0305e82c3301",
    ],
    "ingestion-key": ["sdk-e2e-test-ingestion-key-1712345678901234567"],
    # A Go-only kind: absent from tests/e2e/_cleanup.SPECS.
    "agent-skill": ["sdk-e2e-test-skill-1712345678901234567"],
}


@pytest.mark.parametrize("kind,name", [(k, n) for k, names in sorted(GO_NAME_SAMPLES.items()) for n in names])
def test_go_suite_names_are_matched(kind: str, name: str) -> None:
    assert matches_kind(registry.KINDS[kind], name), (
        "the Go suite mints {!r} for kind {!r} and the janitor does not recognise it".format(name, kind)
    )


# The TypeScript suite lives in THIS repo (sdk-typescript/), so unlike the earlier
# assumption there is no cross-repo blind spot -- a real drift test is possible and
# these are it. `ts` in those names is `Date.now()`, i.e. 13 digits.
TS_E2E_DIR = REPO_ROOT / "sdk-typescript" / "tests" / "e2e"
_MS = "1786223057182"

# kind -> (sample name, the literal stem as it appears in the TS source)
TS_NAME_SAMPLES: Dict[str, List[Tuple[str, str]]] = {
    "dashboard": [("sdk-ts-e2e-test-dashboard-" + _MS, "sdk-ts-e2e-test-dashboard-")],
    "api-key": [("sdk-ts-e2e-test-apikey-" + _MS, "sdk-ts-e2e-test-apikey-")],
    "policy": [
        ("sdk-ts-e2e-test-policy-" + _MS, "sdk-ts-e2e-test-policy-"),
        ("sdk-ts-e2e-test-policy-for-apikey-" + _MS, "sdk-ts-e2e-test-policy-for-apikey-"),
        ("sdk-ts-e2e-test-policy-for-sa-" + _MS, "sdk-ts-e2e-test-policy-for-sa-"),
    ],
    "service-account": [
        ("sdk-ts-e2e-test-sa-" + _MS, "sdk-ts-e2e-test-sa-"),
        ("sdk-ts-e2e-test-sa-for-apikey-" + _MS, "sdk-ts-e2e-test-sa-for-apikey-"),
    ],
    "synthetic": [
        ("sdk-ts-e2e-test-http-synthetic-" + _MS, "sdk-ts-e2e-test-http-synthetic-"),
        ("sdk-ts-e2e-test-tcp-synthetic-" + _MS, "sdk-ts-e2e-test-tcp-synthetic-"),
        ("sdk-ts-e2e-test-ssl-synthetic-" + _MS, "sdk-ts-e2e-test-ssl-synthetic-"),
        ("sdk-ts-e2e-test-dns-synthetic-" + _MS, "sdk-ts-e2e-test-dns-synthetic-"),
    ],
    "data-integration": [("sdk-e2e-test-cloudwatch-" + _MS, "sdk-e2e-test-cloudwatch-")],
    "ingestion-key": [("sdk-e2e-test-ingestion-key-" + _MS, "sdk-e2e-test-ingestion-key-")],
    # The suite disagrees with itself on these two. Both shapes had debris sitting
    # unrecognised on backend-dev until sdk-typescript/ moved into this repo made
    # them visible. Fixing the suite is the better answer; matching them is what
    # reclaims what already exists.
    "silence": [("e2e-ts-test-silence-" + _MS, "e2e-ts-test-silence-")],
    "agent-skill": [("ts-sdk-e2e-test-skill-" + _MS, "ts-sdk-e2e-test-skill-")],
    # Title case and spaces; the suffix is Math.random()*10_000_000.
    "monitor": [("E2E Test - K8s Pod Not Healthy Monitor - 4821", "E2E Test - K8s Pod Not Healthy Monitor - ")],
}


@pytest.mark.parametrize("kind,name", [(k, n) for k, pairs in sorted(TS_NAME_SAMPLES.items()) for n, _ in pairs])
def test_typescript_suite_names_are_matched(kind: str, name: str) -> None:
    assert matches_kind(registry.KINDS[kind], name), (
        "the TypeScript suite mints {!r} for kind {!r} and the janitor does not recognise it".format(name, kind)
    )


@pytest.mark.skipif(not TS_E2E_DIR.is_dir(), reason="sdk-typescript not present in this checkout")
@pytest.mark.parametrize("kind,stem", [(k, stem) for k, pairs in sorted(TS_NAME_SAMPLES.items()) for _, stem in pairs])
def test_transcribed_typescript_stems_still_appear_in_the_suite(kind: str, stem: str) -> None:
    """The half that makes the samples above more than a hopeful copy.

    This assertion is only possible because sdk-typescript/ is in this repo. The
    original design assumed it was not and documented the TS prefix as
    unverifiable -- which is exactly how `e2e-ts-test-silence-` and
    `ts-sdk-e2e-test-skill-` went unnoticed.
    """
    sources = "\n".join(p.read_text() for p in sorted(TS_E2E_DIR.rglob("*.ts")))
    assert stem in sources, (
        "{}: {!r} no longer appears in sdk-typescript/tests/e2e. Either the suite renamed it -- update "
        "registry.KINDS and TS_NAME_SAMPLES together -- or the literal is gone and this entry should.".format(
            kind, stem
        )
    )


# Names a person could plausibly create on a shared dev tenant. Every one of them
# would be matched by a prefix-only rule, which is why the patterns are anchored
# at both ends.
HUMAN_NAMES = [
    "e2e-test",
    "e2e-test-",
    "my-e2e-test-notes",
    "pre2e-test-dashboard-x",
    "sdk-e2e-testing-dashboard",
    "SDK-E2E-TEST-DASHBOARD-X",
    "e2e-test-dashboard-for-the-demo",
    "e2e-test-dashboard-demo",
    "e2e-cloudwatch-staging",
    "sa-test-policy for onboarding",
    "E2E Test - Prod Pod Health",
    "E2E Test - K8s Pod Not Healthy Monitor - reviewed",
    "zz-manual-do-not-delete-2026-08-06",
    "prod-dashboard",
    "",
]


@pytest.mark.parametrize("name", HUMAN_NAMES)
def test_human_names_are_matched_by_no_kind(name: str) -> None:
    matched = [k for k, spec in registry.KINDS.items() if matches_kind(spec, name)]
    assert not matched, "{!r} would be swept as {}".format(name, matched)


def test_each_suite_name_matches_exactly_one_kind() -> None:
    """No name is claimed by two kinds.

    Not a correctness bug today -- a kind only classifies rows from its own list
    endpoint, so a policy never reaches the api-key pass -- but a pattern that
    matches things it was not written for is one refactor away from mattering.
    """
    for kind, names in GO_NAME_SAMPLES.items():
        for name in names:
            owners = sorted(k for k, spec in registry.KINDS.items() if matches_kind(spec, name))
            assert owners == [kind], "{!r} matches {}, expected only {!r}".format(name, owners, kind)


# ------------------------------------------- D3/D4: the Go transcription cannot rot

# The stem of each transcribed literal, as it appears in the Go source today.
GO_LITERAL_STEMS = [
    '"e2e-test-dashboard-',
    '"E2E Test - K8s Pod Not Healthy Monitor - ',
    '"e2e-test-silence-',
    '"e2e-test-policy-',
    '"sdk-e2e-test-policy-for-apikey',
    '"e2e-test-policy-for-sa-',
    '"e2e-test-sa-',
    '"sdk-e2e-test-sa-for-apikey',
    '"sdk-e2e-test-apikey-',
    '"e2e-test-synthetic-',
    '"e2e-test-tcp-synthetic-',
    # ssl and dns are in GO_NAME_SAMPLES but were missing here, so renaming either
    # in synthetics_test.go left this guard green while the janitor silently
    # stopped matching them -- the exact drift this file exists to catch.
    '"e2e-test-ssl-synthetic-',
    '"e2e-test-dns-synthetic-',
    '"e2e-test-cloudwatch-',
    '"e2e-test-cloudwatch-tags-',
    '"sdk-e2e-test-ingestion-key',
    '"sdk-e2e-test-skill-',
]

# Shapes no suite mints any more, kept because debris under them is still sitting
# on the shared tenant. Deliberately NOT in GO_LITERAL_STEMS -- they are supposed
# to be absent from the Go source now, and asserting otherwise would fail.
# Delete an entry once the backlog purge has reclaimed the last of it.
# kind -> (a sample retired name, the literal stem as it appeared in Go).
# The stem is written out rather than derived from the sample: deriving it with
# rsplit() encodes an assumption about how many hyphen-separated segments the
# prefix has, which is true for both entries today but is exactly the kind of
# incidental coupling that makes a test wrong later.
HISTORIC_NAMES = {
    # sdk/tests/e2e/serviceaccounts_test.go, before this change. No e2e token.
    "policy": ("sa-test-policy-3f2504e0-4f89-11d3-9a0c-0305e82c3301", '"sa-test-policy-'),
    # sdk/tests/e2e/dataintegrations_test.go, before this change.
    "data-integration": ("e2e-cloudwatch-3f2504e0-4f89-11d3-9a0c-0305e82c3301", '"e2e-cloudwatch-'),
}


@pytest.mark.parametrize("kind,name", [(k, v[0]) for k, v in sorted(HISTORIC_NAMES.items())])
def test_debris_under_retired_names_is_still_reclaimable(kind: str, name: str) -> None:
    assert matches_kind(registry.KINDS[kind], name)


@pytest.mark.parametrize("kind,stem", [(k, v[1]) for k, v in sorted(HISTORIC_NAMES.items())])
def test_retired_names_are_really_gone_from_the_go_suite(kind: str, stem: str) -> None:
    """The other half: if a retired shape comes BACK, its entry should move out of
    HISTORIC_NAMES, or we end up maintaining two conventions by accident."""
    if not GO_E2E_DIR.is_dir():
        pytest.skip("Go e2e suite not present in this checkout")
    assert stem not in go_e2e_source(), "{} is minting {} again; move it out of HISTORIC_NAMES".format(kind, stem)


@pytest.mark.skipif(not GO_E2E_DIR.is_dir(), reason="Go e2e suite not present in this checkout")
@pytest.mark.parametrize("stem", GO_LITERAL_STEMS)
def test_transcribed_go_literals_still_appear_in_the_go_suite(stem: str) -> None:
    """GO_NAME_SAMPLES is hand-copied from Go; make a rename loud rather than stale.

    Without this, renaming a resource in the Go suite leaves the janitor matching
    a name nothing mints any more, while the new name goes unswept -- and the
    parametrised tests above keep passing the whole time.
    """
    sources = go_e2e_source()
    assert stem in sources, (
        "{} no longer appears in sdk/tests/e2e/*_test.go. Either the Go suite renamed it -- in "
        "which case update registry.KINDS and GO_NAME_SAMPLES -- or the literal was removed and "
        "this entry should go.".format(stem)
    )


@pytest.mark.skipif(not (GO_E2E_DIR / "setup.go").is_file(), reason="Go e2e suite not present")
def test_every_go_tracked_kind_is_known_to_the_janitor() -> None:
    """sdk/tests/e2e/setup.go enumerates what the Go suite creates and cleans up.

    A new Track* there is a new class of leak here.
    """
    source = (GO_E2E_DIR / "setup.go").read_text()
    go_kinds: Set[str] = set(re.findall(r'trackedResourceKind\s*=\s*"([^"]+)"', source))
    assert go_kinds, "could not parse trackedResourceKind constants out of setup.go"

    # setup.go's constants are human labels ("synthetic test"), not slugs.
    aliases = {
        "synthetic test": "synthetic",
        "ingestion key": "ingestion-key",
        "data integration config": "data-integration",
        "agent skill": "agent-skill",
        "api key": "api-key",
        "service account": "service-account",
    }
    known = set(registry.KINDS) | set(registry.UNSWEEPABLE)
    unknown = sorted(k for k in go_kinds if aliases.get(k, k) not in known)
    assert not unknown, (
        "the Go suite tracks {} but the janitor does not know them (after aliasing). Either add "
        "the kind, or add an alias if it is a naming difference only.".format(unknown)
    )


def test_ranks_agree_with_the_e2e_tracker() -> None:
    """Teardown order is a dependency, not a preference, so it cannot be fixed in
    one table and left wrong in the other.

    api-key -> service-account -> policy: a live API key makes its service
    account's DELETE answer 400.
    """
    from tests.e2e import _cleanup

    for kind, spec in registry.KINDS.items():
        tracker_spec = _cleanup.SPECS.get(kind)
        if tracker_spec is None:
            continue
        assert spec.rank == tracker_spec.rank, (
            "{}: janitor rank {} but tracker rank {} -- the two must agree or one of them deletes "
            "a dependency first".format(kind, spec.rank, tracker_spec.rank)
        )


def test_the_dependency_chain_is_ordered() -> None:
    ranks = registry.KINDS
    assert ranks["api-key"].rank < ranks["service-account"].rank < ranks["policy"].rank


# --------------------------------------------------------- runtime dependency guard


def test_the_janitor_never_imports_generated_code() -> None:
    """The janitor must run when `make generate` has failed.

    Its CI job is guarded by `if: always()`, which includes the run where codegen
    broke -- the run where orphans are most likely. `groundcover` cannot be
    imported then: `src/groundcover/api/`, `models/` and `_generated_client.py`
    are gitignored. httpx and the rest are only present after `uv sync`.

    AST rather than a substring grep, so a docstring mentioning groundcover does
    not fail and a function-local import does.
    """
    banned = {"groundcover", "httpx", "attrs", "tenacity", "yaml", "pytest", "respx"}
    offences = []
    for path in sorted(JANITOR_DIR.rglob("*.py")):
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                # level > 0 is a relative import, always within this package.
                names = [] if node.level else [node.module or ""]
            else:
                continue
            offences += [
                "{}:{} imports {}".format(path.name, node.lineno, name)
                for name in names
                if name.split(".")[0] in banned
            ]
    assert not offences, "the janitor must stay stdlib-only:\n  " + "\n  ".join(offences)


# ------------------------------------------------------------- table well-formedness


@pytest.mark.parametrize("kind", sorted(registry.KINDS))
def test_kind_is_internally_consistent(kind: str) -> None:
    spec = registry.KINDS[kind]
    route = spec.list_route

    assert route.method in ("GET", "POST")
    assert route.path.startswith("/api/")
    assert not (route.page_size and route.hard_cap), "page_size and hard_cap are mutually exclusive"
    assert spec.name_fields
    assert spec.name_patterns, "{}: no way to recognise its names".format(kind)
    assert (spec.age_source == registry.AGE_FROM_TIMESTAMP) == bool(spec.timestamp_fields)
    assert spec.age_source in (registry.AGE_FROM_TIMESTAMP, registry.AGE_UNGATED)

    delete = spec.delete_route
    assert bool(delete.path_template) != bool(delete.path), "exactly one addressing mode"
    allowed = {"id", "name"} | set(spec.extra_delete_fields)
    template = (delete.path_template or "") + "".join((delete.body_template or {}).values())
    assert set(re.findall(r"{(\w+)}", template)) <= allowed


def test_ungated_kinds_are_the_ones_we_decided_on() -> None:
    """Sweeping without an age gate is a deliberate, reviewed exception.

    Pinned so a fourth kind cannot join them by someone forgetting to fill in
    timestamp_fields.
    """
    ungated = sorted(k for k, s in registry.KINDS.items() if s.age_source == registry.AGE_UNGATED)
    assert ungated == ["ingestion-key", "service-account"]


def test_kinds_without_an_age_gate_have_a_freshness_veto_or_a_stated_reason() -> None:
    """service-account leans on lastActive; ingestion-key has nothing and we know it.

    The veto is what makes un-aged deletion safe: the API-key middleware bumps
    last_used on every authenticated request, so the janitor's own credentials
    can never pass it.
    """
    assert registry.KINDS["service-account"].last_active_field == "lastActive"
    assert registry.KINDS["api-key"].last_active_field == "lastActive"
    assert registry.KINDS["ingestion-key"].last_active_field is None


def test_api_keys_are_not_listed_with_revoked() -> None:
    """Deleting an API key revokes it; the row stays forever.

    tests/e2e/_cleanup.py asks for revoked keys because id recovery needs to see
    what it just half-deleted. Copying that here would resurface every key the
    janitor ever deleted, on every run, forever.
    """
    params = registry.KINDS["api-key"].list_route.params or {}
    assert "withRevoked" not in params and "withExpired" not in params


def test_monitors_exclude_synthetic_owned() -> None:
    """718 synthetic-owned monitors are permanently 403 (BE-2727).

    Excluding them before the delete pass is the difference between reporting
    them and issuing 718 failing DELETEs on every run.
    """
    excludes = dict(registry.KINDS["monitor"].exclude_when)
    assert "SyntheticTest" in excludes["originType"]


# A suffix appended AFTER the machine tail. 53 of the 55 unrecognised names on
# backend-dev were this shape, invisible because the patterns anchored at the end.
SUFFIXED_NAMES = [
    ("policy", "sdk-ts-e2e-test-policy-for-sa-1786223057182-2"),
    ("policy", "sdk-e2e-test-policy-for-sa-1783928872144660122-2"),
    ("dashboard", "e2e-test-dashboard-2d2a8c0a-201a-48bd-bce7-6ba5b161d8c2-updated"),
    ("agent-skill", "ts-sdk-e2e-test-skill-1786223057182-created"),
    ("silence", "sdk-e2e-test-silence-12345a1-p4242n7-updated"),
    ("data-integration", "e2e-cloudwatch-3f2504e0-4f89-11d3-9a0c-0305e82c3301-updated"),
]


@pytest.mark.parametrize("kind,name", SUFFIXED_NAMES)
def test_a_suffix_after_the_machine_tail_is_still_recognised(kind: str, name: str) -> None:
    """Sabotage: drop _NAME_SUFFIX from _suite_regex -> every case here fails, and
    53 real resources on backend-dev go back to being invisible."""
    assert matches_kind(registry.KINDS[kind], name)


def test_the_suffix_allowance_still_requires_a_machine_tail() -> None:
    """The gate is the mandatory UUID/timestamp/pid-counter, not the end anchor.

    If the suffix allowance were written so that it could stand in for the tail,
    every one of these would match -- which is the whole false-positive risk.
    """
    for kind, name in [
        ("dashboard", "e2e-test-dashboard-for-the-demo"),
        ("dashboard", "e2e-test-dashboard-staging-copy"),
        ("policy", "e2e-test-policy-for-the-migration"),
        ("silence", "e2e-test-silence-yesterday"),
        ("data-integration", "e2e-cloudwatch-staging"),
    ]:
        assert not matches_kind(registry.KINDS[kind], name), "{!r} must not match".format(name)


def test_the_monitor_title_pattern_does_not_take_a_suffix() -> None:
    """The one pattern with no UUID or timestamp requirement, so the one a person
    could type. It must not be widened along with the others."""
    spec = registry.KINDS["monitor"]
    assert matches_kind(spec, "E2E Test - K8s Pod Not Healthy Monitor - 4821")
    for name in [
        "E2E Test - K8s Pod Not Healthy Monitor - 4821-copy",
        "E2E Test - K8s Pod Not Healthy Monitor - reviewed",
    ]:
        assert not matches_kind(spec, name), "{!r} must not match".format(name)


# --------------------------------------------- the companion-monitor kind's invariants


def test_a_status_cannot_be_both_unverified_and_gone() -> None:
    """ "Gone" claims proof of absence; "unverified" says the opposite. A status in
    both makes the report's honesty depend on dict ordering."""
    spec = registry.KINDS["synthetic-companion-monitor"]
    broken = dataclasses.replace(
        spec, delete_route=dataclasses.replace(spec.delete_route, unverified_statuses=(404,), gone_statuses=(404,))
    )
    with pytest.raises(registry.RegistryError, match="both unverified and gone"):
        _validate_with(broken)


def test_include_only_when_and_exclude_when_cannot_name_the_same_field() -> None:
    spec = registry.KINDS["synthetic-companion-monitor"]
    broken = dataclasses.replace(
        spec,
        include_only_when=(("originType", ("SyntheticTest",)),),
        exclude_when=(("originType", ("Catalog",)),),
    )
    with pytest.raises(registry.RegistryError, match="contradiction"):
        _validate_with(broken)


def test_a_dependency_must_be_swept_before_its_dependent() -> None:
    """The gate is what makes this safe, but a dependency ranked after its dependent
    means the ordering intent was lost, and the gate then does redundant work every
    run while quietly withholding candidates that should have been reclaimable."""
    spec = registry.KINDS["synthetic-companion-monitor"]
    with pytest.raises(registry.RegistryError, match="must be greater"):
        _validate_with(dataclasses.replace(spec, rank=registry.KINDS["synthetic"].rank))
    with pytest.raises(registry.RegistryError, match="unknown kind"):
        _validate_with(dataclasses.replace(spec, requires_absent_from="no-such-kind"))
    with pytest.raises(registry.RegistryError, match="cannot name itself"):
        _validate_with(dataclasses.replace(spec, requires_absent_from=spec.kind))


def test_the_companion_kind_deletes_through_the_synthetics_route_not_the_monitor_one() -> None:
    """The entire reason this kind exists. DELETE /api/monitors/{id} answers 403 for
    a synthetic-owned monitor by design (internal/monitors/monitors.go:1100), so a
    regression that "simplifies" this back to the monitor route silently restores a
    kind that can never delete anything."""
    spec = registry.KINDS["synthetic-companion-monitor"]

    assert spec.delete_route.path_template == "/api/synthetics/v1/rules/{id}"
    assert spec.id_field == "originId", "the synthetics route is addressed by the config id"
    assert spec.requires_absent_from == "synthetic"
    # And the `monitor` kind must keep excluding them, or both kinds would issue a
    # delete for the same row -- one of which is guaranteed to 403.
    assert ("originType", ("SyntheticTest",)) in registry.KINDS["monitor"].exclude_when


def test_a_dependency_that_cannot_report_truncation_is_rejected() -> None:
    """The gate proving a companion's synthetic is gone reads the synthetics
    listing. list_rows() marks a route with neither page_size nor hard_cap complete
    for any 200, so such a dependency turns that proof into a dead guard -- it can
    never fail, and reports absence it never established."""
    dep = registry.KINDS["synthetic"]
    assert dep.list_route.hard_cap, "the shipped dependency must be able to report incompleteness"

    original = registry.KINDS["synthetic"]
    registry.KINDS["synthetic"] = dataclasses.replace(
        original, list_route=dataclasses.replace(original.list_route, hard_cap=None, page_size=None)
    )
    try:
        with pytest.raises(registry.RegistryError, match="never report itself incomplete"):
            registry._validate()
    finally:
        registry.KINDS["synthetic"] = original


def test_a_success_code_cannot_be_declared_unverified() -> None:
    """delete_one() tests unverified before the 2xx branch, so a success code listed
    there downgrades a completed delete to 'no idea' and then chases it with a
    pointless confirmation re-list."""
    spec = registry.KINDS["synthetic-companion-monitor"]
    for bad, match in ((200, "success code"), (204, "success code"), (202, "success code")):
        broken = dataclasses.replace(
            spec, delete_route=dataclasses.replace(spec.delete_route, unverified_statuses=(bad,))
        )
        with pytest.raises(registry.RegistryError, match=match):
            _validate_with(broken)

    clash = dataclasses.replace(
        spec, delete_route=dataclasses.replace(spec.delete_route, accepted_status=404, unverified_statuses=(404,))
    )
    with pytest.raises(registry.RegistryError, match="also accepted_status"):
        _validate_with(clash)
