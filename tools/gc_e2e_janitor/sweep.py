from __future__ import annotations

import dataclasses
import datetime
import logging
import re
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from . import registry
from .registry import Kind
from .transport import Client, TransportError

logger = logging.getLogger(__name__)

UTC = datetime.timezone.utc

# Before this is treated as MISSING, not ancient: Go's non-pointer time.Time
# marshals an unset value as "0001-01-01T00:00:00Z", which parses cleanly and
# would sail past any cutoff.
SANITY_FLOOR = datetime.datetime(2020, 1, 1, tzinfo=UTC)
# Tolerance for clock skew; beyond it a timestamp is nonsense, so unknown.
FUTURE_TOLERANCE = datetime.timedelta(hours=1)

# A paginated listing will not fetch more than this, so a server that ignores
# `skip` cannot spin forever. Reaching it means the listing is INCOMPLETE.
MAX_PAGES = 100

_FRACTION_RE = re.compile(r"\.(\d+)")


class SweepAborted(RuntimeError):
    pass


class KindNotApplicable(RuntimeError):
    pass


# Keyed on the guard's fixed message (verify_incloud_backend_middleware.go:52)
# rather than a hardcoded list of inCloud backends, so a new tenant needs no
# change here.
_NOT_INCLOUD = b"only available for inCloud backends"


@dataclasses.dataclass
class Candidate:
    kind: str
    resource_id: Optional[str]
    name: str
    row: Mapping[str, Any]


@dataclasses.dataclass
class KindReport:
    kind: str
    # The field that disambiguates "clean" from "could not tell".
    list_ok: bool = False
    list_status: Optional[int] = None
    list_error: Optional[str] = None
    pages_fetched: int = 0
    # Proved by a short page, never assumed. False when the page cap or a
    # skip-less hard cap was reached.
    pagination_complete: bool = False
    listed: int = 0
    matched: int = 0
    skipped_foreign_creator: int = 0
    too_young: int = 0
    unknown_age: int = 0
    # Rows whose name field could not be read. Same failure shape as unknown_age:
    # if a backend renames a field in `name_fields`, every row takes that path,
    # `matched` stays 0, and the sweep reports a clean tenant.
    unnamed: int = 0
    excluded: int = 0
    # Withheld because requires_absent_from's listing still holds their delete id,
    # so deleting them would have taken a live resource with them. Counted rather
    # than filtered, so a run that reclaims nothing says why.
    skipped_dependency_present: int = 0
    # Present but unreadable. Feeds `determinate` like unknown_age: a malformed
    # timestamp would otherwise silently disable the freshness veto on the two
    # kinds with no age gate at all.
    unknown_last_active: int = 0
    lookalikes: List[str] = dataclasses.field(default_factory=list)
    deleted: int = 0
    delete_accepted: int = 0
    already_gone: int = 0
    failed: int = 0
    failures: List[Dict[str, Any]] = dataclasses.field(default_factory=list)
    aborted: Optional[str] = None
    # Set when the kind cannot exist on this backend at all. A determinate
    # answer -- "none here, and there never could be" -- not an unknown one.
    not_applicable: Optional[str] = None
    # Set when the creator gate rejected 100% of name matches, which usually
    # means a stale GC_E2E_IDENTITY rather than a genuinely foreign-owned tenant.
    creator_gate_rejected_everything: bool = False
    # A 202 says "accepted", not "done". These record what a confirmation re-list
    # actually observed, so an accepted-but-unconfirmed delete cannot be reported
    # as a completed one.
    delete_confirmed: int = 0
    delete_unconfirmed: int = 0
    # Both id and name, because the identity to confirm on differs by kind:
    # id-addressed routes must confirm by id, since a set of names collapses
    # duplicates and would report three surviving resources as two. Ingestion keys
    # have no meaningful id and confirm by name.
    accepted: List[Tuple[Optional[str], str]] = dataclasses.field(default_factory=list)
    # The exact set an apply run would delete, so the artifact answers "what would
    # this remove?" and a dry run is reviewable. Populated even when a breaker then
    # aborts the kind -- those are the runs most worth inspecting. Sorted so two
    # artifacts diff cleanly.
    candidates: List[Dict[str, Optional[str]]] = dataclasses.field(default_factory=list)

    @property
    def determinate(self) -> bool:
        if self.not_applicable:
            return True
        return (
            self.list_ok
            and self.pagination_complete
            and self.unknown_age == 0
            and self.unknown_last_active == 0
            and self.unnamed == 0
            and not self.creator_gate_rejected_everything
            # An accepted delete we could not confirm is an open question, not a
            # success. Reporting `ok` here would claim a completion nobody saw.
            and self.delete_unconfirmed == 0
        )


@dataclasses.dataclass
class SweepReport:
    backend_id: str
    base_url: str
    mode: str
    age_minutes: int
    identity: Optional[str]
    expected_kinds: List[str] = dataclasses.field(default_factory=list)
    kinds: Dict[str, KindReport] = dataclasses.field(default_factory=dict)
    unsweepable: Dict[str, str] = dataclasses.field(default_factory=dict)

    @property
    def missing_kinds(self) -> List[str]:
        return [k for k in self.expected_kinds if k not in self.kinds]

    @property
    def status(self) -> str:
        if any(r.failed for r in self.kinds.values()):
            return "failed"
        if self.missing_kinds or not all(r.determinate for r in self.kinds.values()):
            return "partial"
        # A tripped breaker is work-not-done in apply mode, but in report mode
        # nothing was going to be deleted anyway -- the cap IS the survey answer.
        # Failing on it would make every report against a real backlog red.
        if self.mode == "apply" and any(r.aborted for r in self.kinds.values()):
            return "partial"
        return "ok"

    @property
    def exit_code(self) -> int:
        return {"ok": 0, "partial": 2, "failed": 1}[self.status]


def parse_timestamp(value: Any) -> Optional[datetime.datetime]:
    if not isinstance(value, str) or not value.strip():
        return None

    text = value.strip()
    if text.endswith(("Z", "z")):
        text = text[:-1] + "+00:00"
    # Go's RFC3339Nano emits up to 9 fractional digits; fromisoformat accepts at
    # most 6 (and before 3.11 requires exactly 3 or 6).
    match = _FRACTION_RE.search(text)
    if match:
        text = text[: match.start()] + "." + match.group(1)[:6].ljust(6, "0") + text[match.end() :]

    try:
        parsed = datetime.datetime.fromisoformat(text)
    except ValueError:
        return None

    if parsed.tzinfo is None:
        # Assume UTC rather than the runner's local zone, or the same resource
        # would age differently depending on where the job ran.
        parsed = parsed.replace(tzinfo=UTC)

    now = datetime.datetime.now(UTC)
    if parsed < SANITY_FLOOR or parsed > now + FUTURE_TOLERANCE:
        return None
    return parsed


def first_present(row: Mapping[str, Any], fields: Sequence[str]) -> Optional[str]:
    for field in fields:
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            return value
        if value not in (None, "", [], {}):
            return str(value)
    return None


def matches_kind(spec: Kind, name: str) -> bool:
    return any(pattern.match(name) for pattern in spec.name_patterns)


def _page_args(spec: Kind, skip: int) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    params = dict(spec.list_route.params or {})
    body = dict(spec.list_route.body) if spec.list_route.body is not None else None
    window = {"limit": spec.list_route.page_size, "skip": skip}
    if spec.list_route.page_size is not None:
        if spec.list_route.method.upper() == "GET":
            params.update(window)
        else:
            body = dict(body or {})
            body.update(window)
    return (params or None), body


def _unwrap(spec: Kind, payload: Any) -> List[Mapping[str, Any]]:
    container = spec.list_route.container
    if container is None:
        rows = payload
    else:
        if not isinstance(payload, dict):
            raise TransportError(
                "{}: expected an object with a {!r} key, got {}".format(spec.kind, container, type(payload).__name__)
            )
        if container not in payload:
            raise TransportError(
                "{}: response has no {!r} key (keys: {})".format(spec.kind, container, sorted(payload))
            )
        rows = payload[container]
    # A null container is a legitimate empty list; a non-list is not.
    if rows is None:
        return []
    if not isinstance(rows, list):
        raise TransportError("{}: expected a list of rows, got {}".format(spec.kind, type(rows).__name__))
    # Every element must be an object. Filtering bad ones out instead made `[null]`
    # an empty listing that read as clean, and `[{...}, null]` return the good rows
    # while still reporting the page complete. A row we cannot read is a listing we
    # cannot trust.
    bad = [i for i, r in enumerate(rows) if not isinstance(r, dict)]
    if bad:
        raise TransportError(
            "{}: {} of {} rows are not objects (first at index {}, type {}); a row that cannot be "
            "read is not an absent row, so this listing is unusable rather than short".format(
                spec.kind, len(bad), len(rows), bad[0], type(rows[bad[0]]).__name__
            )
        )
    return rows


def _raise_for_list_status(spec: Kind, response: Any, page: Optional[int] = None) -> None:
    if response.status < 400:
        return
    if response.status == 400 and _NOT_INCLOUD in response.content:
        raise KindNotApplicable(
            "{}: these routes are inCloud-only and this backend is not inCloud, so the kind cannot exist here".format(
                spec.kind
            )
        )
    where = "list" if page is None else "list page {}".format(page)
    raise TransportError("{}: {} returned HTTP {}".format(spec.kind, where, response.status))


def list_rows(client: Client, spec: Kind, report: KindReport) -> List[Mapping[str, Any]]:
    route = spec.list_route
    rows: List[Mapping[str, Any]] = []

    if route.page_size is None:
        params, body = _page_args(spec, 0)
        response = client.request(route.method, route.path, json=body, params=params)
        report.list_status = response.status
        _raise_for_list_status(spec, response)
        rows = _unwrap(spec, response.json())
        report.pages_fetched = 1
        if route.hard_cap is not None and len(rows) >= route.hard_cap:
            # No skip, no cursor: a full-length response and a truncated one look
            # identical, so we cannot claim to have seen everything.
            report.pagination_complete = False
            logger.error(
                "%s: listing returned %d rows at its hard cap of %d and the endpoint offers no "
                "skip/cursor, so the tail is invisible -- refusing to treat this as complete",
                spec.kind,
                len(rows),
                route.hard_cap,
            )
        else:
            report.pagination_complete = True
        report.list_ok = True
        return rows

    for page in range(MAX_PAGES):
        params, body = _page_args(spec, page * route.page_size)
        response = client.request(route.method, route.path, json=body, params=params)
        report.list_status = response.status
        _raise_for_list_status(spec, response, page)
        page_rows = _unwrap(spec, response.json())
        rows.extend(page_rows)
        report.pages_fetched = page + 1
        if len(page_rows) < route.page_size:
            report.pagination_complete = True
            report.list_ok = True
            return rows

    report.list_ok = True
    report.pagination_complete = False
    logger.error(
        "%s: stopped after %d pages without reaching the end of the listing -- treating the result "
        "as incomplete rather than as the whole tenant",
        spec.kind,
        MAX_PAGES,
    )
    return rows


def _excluded_by(spec: Kind, row: Mapping[str, Any]) -> Optional[str]:
    # Checked first: when two kinds share a list route, most rows belong to the
    # other one, and reporting those as "excluded by originType" is more honest
    # than letting them fall through to a name test they were never eligible for.
    for field, wanted in spec.include_only_when:
        if row.get(field) not in wanted:
            return "{}={!r} is not one of {}".format(field, row.get(field), list(wanted))
    for field, bad_values in spec.exclude_when:
        if row.get(field) in bad_values:
            return "{}={!r}".format(field, row.get(field))
    # Structural self-protection: the janitor's own policy is bound to its own
    # service account. An e2e policy whose service account the earlier rank
    # already removed has a count of 0 by the time we look.
    if spec.kind == "policy" and isinstance(row.get("entityCount"), int) and row["entityCount"] > 0:
        return "entityCount={}".format(row["entityCount"])
    return None


def classify(
    spec: Kind,
    rows: Iterable[Mapping[str, Any]],
    cutoff: datetime.datetime,
    identity: Optional[str],
    report: KindReport,
) -> List[Candidate]:
    candidates: List[Candidate] = []
    now = datetime.datetime.now(UTC)

    for row in rows:
        report.listed += 1
        name = first_present(row, spec.name_fields)
        if name is None:
            report.unnamed += 1
            logger.warning("%s: a row carries none of %s, skipping it", spec.kind, list(spec.name_fields))
            continue

        if not matches_kind(spec, name):
            if registry.LOOKALIKE_RE.search(name):
                # Debris-shaped but unrecognised. Never deleted, only counted, so a renamed
                # prefix shows up as a growing number instead of a silently shrinking sweep.
                report.lookalikes.append(name)
            continue
        report.matched += 1

        if spec.creator_field and identity is not None:
            creator = row.get(spec.creator_field)
            if creator != identity:
                report.skipped_foreign_creator += 1
                continue

        excluded = _excluded_by(spec, row)
        if excluded is not None:
            report.excluded += 1
            continue

        # A freshness veto, not an age gate: it keys off use rather than the
        # clock. The middleware bumps last_used on every authenticated request,
        # so the janitor's own key and service account can never pass it.
        if spec.last_active_field:
            raw_last_active = row.get(spec.last_active_field)
            last_active = parse_timestamp(raw_last_active)
            if last_active is not None:
                if last_active >= cutoff:
                    report.too_young += 1
                    continue
            elif raw_last_active not in (None, ""):
                # Absent means never used, which is what un-aged deletion of these kinds was
                # agreed on. Present but unreadable is a different answer, and sharing the
                # null path would silently disarm the only protection they have -- including
                # the one stopping the janitor revoking its own credentials.
                report.unknown_last_active += 1
                logger.warning(
                    "%s: %r has an unreadable %s (%r), so its freshness cannot be judged and it is left alone",
                    spec.kind,
                    name,
                    spec.last_active_field,
                    raw_last_active,
                )
                continue

        if spec.age_source == registry.AGE_FROM_TIMESTAMP:
            stamps = [parse_timestamp(row.get(f)) for f in spec.timestamp_fields]
            known = [s for s in stamps if s is not None]
            if not known:
                # Unknown is not old. Counted, because a backend that stopped
                # emitting the field would otherwise turn this into a permanent
                # silent no-op that reports success.
                report.unknown_age += 1
                logger.warning(
                    "%s: %r has no usable timestamp in %s (%s), skipping",
                    spec.kind,
                    name,
                    list(spec.timestamp_fields),
                    {f: row.get(f) for f in spec.timestamp_fields},
                )
                continue
            if max(known) >= cutoff:
                report.too_young += 1
                continue
            if max(known) > now:  # pragma: no cover - parse_timestamp bounds this
                report.unknown_age += 1
                continue

        resource_id = row.get(spec.id_field)
        candidates.append(
            Candidate(
                kind=spec.kind,
                resource_id=str(resource_id) if resource_id not in (None, "") else None,
                name=name,
                row=row,
            )
        )

    return candidates


def _drop_present_in(
    client: Client,
    spec: Kind,
    candidates: Sequence[Candidate],
    report: KindReport,
) -> List[Candidate]:
    dep_kind = spec.requires_absent_from
    assert dep_kind is not None  # only called when set
    dep_spec = registry.KINDS[dep_kind]
    probe = KindReport(kind=dep_kind)

    try:
        rows = list_rows(client, dep_spec, probe)
    except KindNotApplicable:
        # The dependency cannot exist on this backend, so nothing of it can be
        # live. A determinate answer, not a doubt.
        logger.info("%s: %s is not applicable here, so no candidate can be owned by a live one", spec.kind, dep_kind)
        return list(candidates)
    except TransportError as exc:
        raise SweepAborted(
            "{}: could not list {} to prove no candidate still has a live owner ({}), so nothing "
            "was deleted -- deleting on an unread dependency risks removing live resources".format(
                spec.kind, dep_kind, exc
            )
        )

    if not probe.list_ok or not probe.pagination_complete:
        raise SweepAborted(
            "{}: the {} listing was incomplete (list_ok={}, pagination_complete={}), so absence "
            "could not be proved and nothing was deleted".format(
                spec.kind, dep_kind, probe.list_ok, probe.pagination_complete
            )
        )

    live = {str(r.get(dep_spec.id_field)) for r in rows if r.get(dep_spec.id_field) not in (None, "")}
    kept = [c for c in candidates if c.resource_id is None or str(c.resource_id) not in live]
    report.skipped_dependency_present = len(candidates) - len(kept)
    if report.skipped_dependency_present:
        logger.warning(
            "%s: withheld %d candidate(s) whose owning %s is still live -- deleting them would "
            "have removed the live %s as well",
            spec.kind,
            report.skipped_dependency_present,
            dep_kind,
            dep_kind,
        )
    return kept


def check_breakers(spec: Kind, candidates: Sequence[Candidate], report: KindReport, limits: "Limits") -> None:
    # Measured on candidates, not `matched`: whole populations are matched and then
    # withheld by design (synthetic-owned monitors, foreign creators), which would
    # keep the brake permanently tripped. An over-matching pattern still trips it,
    # since rows it wrongly matches are not what any exclusion is written for.
    if report.listed >= limits.min_matches_for_ratio and len(candidates) > report.listed * limits.max_match_ratio:
        raise SweepAborted(
            "{}: {} of {} listed resources became delete candidates ({:.0%}), above the {:.0%} "
            "ceiling -- an over-matching pattern looks exactly like this, so nothing was "
            "deleted".format(
                spec.kind,
                len(candidates),
                report.listed,
                len(candidates) / report.listed,
                limits.max_match_ratio,
            )
        )
    if len(candidates) > limits.max_deletes_per_kind:
        raise SweepAborted(
            "{}: {} candidates exceeds the per-kind cap of {} -- nothing was deleted. Re-run with "
            "a lower --max-deletes-per-kind only if you meant to be more cautious.".format(
                spec.kind, len(candidates), limits.max_deletes_per_kind
            )
        )


def delete_one(client: Client, spec: Kind, candidate: Candidate, report: KindReport) -> None:
    route = spec.delete_route
    fields: Dict[str, Any] = {"id": candidate.resource_id, "name": candidate.name}
    for field in spec.extra_delete_fields:
        fields[field] = candidate.row.get(field)

    if route.path_template:
        if candidate.resource_id is None:
            report.failed += 1
            report.failures.append({"name": candidate.name, "error": "no id on the listed row"})
            return
        # Empty counts as missing, not just None: extra_delete_fields are not
        # normalised, so a row with type="" would build `/config//c1`, which either
        # 404s as `already_gone` or hits some other route entirely.
        missing = [
            k for k, v in fields.items() if (v is None or str(v).strip() == "") and "{%s}" % k in route.path_template
        ]
        if missing:
            report.failed += 1
            report.failures.append({"name": candidate.name, "error": "missing {}".format(missing)})
            return
        path, body = route.path_template.format(**fields), None
    else:
        assert route.path and route.body_template  # guaranteed by registry._validate
        path = route.path
        body = {k: v.format(**fields) for k, v in route.body_template.items()}

    try:
        response = client.request(route.method, path, json=body)
    except TransportError as exc:
        report.failed += 1
        report.failures.append({"id": candidate.resource_id, "name": candidate.name, "error": str(exc)})
        return

    if response.status in route.unverified_statuses:
        # The request did something without saying what: for a companion monitor
        # a 404/410 means the config was already gone, which is when the monitor
        # should have been reaped a moment earlier. "Should" is not "was".
        report.delete_accepted += 1
        report.accepted.append((candidate.resource_id, candidate.name))
    elif response.status == route.accepted_status:
        # Accepted, not done. Counted apart from `deleted` so the report never
        # claims a completed deletion it has not seen; confirm_accepted_deletes()
        # then re-lists to find out which of them actually landed.
        report.delete_accepted += 1
        report.accepted.append((candidate.resource_id, candidate.name))
    elif 200 <= response.status < 300:
        report.deleted += 1
    elif response.status in route.gone_statuses:
        report.already_gone += 1
    else:
        report.failed += 1
        report.failures.append({"id": candidate.resource_id, "name": candidate.name, "http_status": response.status})


@dataclasses.dataclass(frozen=True)
class Limits:
    max_deletes_per_kind: int = 500
    max_deletes_total: int = 2000
    # An over-matching pattern's signature is "matched essentially everything".
    # 0.60 was too tight to be usable: policies on backend-dev are legitimately
    # 66% e2e debris, so the brake fired on correct behaviour.
    max_match_ratio: float = 0.95
    # The floor stops a kind with three resources tripping on two.
    min_matches_for_ratio: int = 20


def confirm_accepted_deletes(client: Client, spec: Kind, report: KindReport) -> None:
    if not report.accepted:
        return
    probe = KindReport(kind=spec.kind)
    try:
        rows = list_rows(client, spec, probe)
    except (TransportError, KindNotApplicable) as exc:
        report.delete_unconfirmed = len(report.accepted)
        logger.warning("%s: could not confirm %d accepted delete(s): %s", spec.kind, report.delete_unconfirmed, exc)
        return

    if not probe.list_ok or not probe.pagination_complete:
        # A capped or failed re-list cannot prove absence -- a name missing from a
        # truncated page is missing from the PAGE, not the tenant.
        report.delete_unconfirmed = len(report.accepted)
        logger.warning(
            "%s: the confirmation listing was incomplete (list_ok=%s, pagination_complete=%s), so "
            "%d accepted delete(s) stay unconfirmed rather than being assumed gone",
            spec.kind,
            probe.list_ok,
            probe.pagination_complete,
            report.delete_unconfirmed,
        )
        return

    # Confirm on whatever the DELETE actually addressed. Counting per accepted
    # item rather than through a set is the point: a set of names silently
    # collapses duplicates and turns "all three still exist" into "two confirmed".
    still_there: List[Tuple[Optional[str], str]] = []
    if spec.delete_route.path_template is not None:
        surviving_ids = {str(r.get(spec.id_field)) for r in rows if r.get(spec.id_field) not in (None, "")}
        still_there = [(i, n) for i, n in report.accepted if i is not None and str(i) in surviving_ids]
    else:
        surviving_names = {n for n in (first_present(r, spec.name_fields) for r in rows) if n}
        still_there = [(i, n) for i, n in report.accepted if n in surviving_names]

    report.delete_unconfirmed = len(still_there)
    report.delete_confirmed = len(report.accepted) - report.delete_unconfirmed
    if still_there:
        logger.warning(
            "%s: %d resource(s) whose DELETE returned %d are still listed -- accepted is not the "
            "same as done, so this run is reported as indeterminate: %s",
            spec.kind,
            len(still_there),
            spec.delete_route.accepted_status,
            [n for _, n in still_there[:5]],
        )


def run(
    client: Client,
    *,
    kinds: Sequence[str],
    age_minutes: int,
    apply: bool,
    identity: Optional[str],
    limits: Limits,
    backend_id: str,
    base_url: str,
) -> SweepReport:
    unknown = [k for k in kinds if k not in registry.KINDS]
    if unknown:
        # A typo'd kind name must not silently sweep nothing.
        raise ValueError("unknown kind(s) {}; known: {}".format(sorted(unknown), sorted(registry.KINDS)))

    report = SweepReport(
        backend_id=backend_id,
        base_url=base_url,
        mode="apply" if apply else "report",
        age_minutes=age_minutes,
        identity=identity,
        expected_kinds=list(kinds),
        unsweepable=dict(registry.UNSWEEPABLE),
    )
    cutoff = datetime.datetime.now(UTC) - datetime.timedelta(minutes=age_minutes)
    pending: Dict[str, List[Candidate]] = {}

    # Phase 1: enumerate everything. Read-only, so one kind's failure never stops
    # another from being surveyed.
    for kind in kinds:
        spec = registry.KINDS[kind]
        kind_report = KindReport(kind=kind)
        report.kinds[kind] = kind_report
        try:
            rows = list_rows(client, spec, kind_report)
        except KindNotApplicable as exc:
            kind_report.not_applicable = str(exc)
            logger.info("%s", exc)
            continue
        except TransportError as exc:
            kind_report.list_ok = False
            kind_report.list_error = str(exc)
            logger.error("%s: could not be listed, so its result is unknown, not clean: %s", kind, exc)
            continue

        candidates = classify(spec, rows, cutoff, identity, kind_report)

        if spec.requires_absent_from is not None:
            try:
                candidates = _drop_present_in(client, spec, candidates, kind_report)
            except SweepAborted as exc:
                kind_report.aborted = str(exc)
                logger.error("%s", exc)
                continue

        # A stale identity is otherwise invisible: every match is skipped as
        # foreign and the kind reports zero candidates, which looks exactly like a
        # correctly-configured sweep with nothing to do.
        if kind_report.matched and kind_report.skipped_foreign_creator == kind_report.matched:
            kind_report.creator_gate_rejected_everything = True
            logger.error(
                "%s: all %d name matches were rejected by the creator gate (identity=%r). Either "
                "the identity is stale or every match belongs to another account -- this is "
                "reported as indeterminate rather than as a clean sweep.",
                kind,
                kind_report.matched,
                identity,
            )

        kind_report.candidates = sorted(
            ({"id": c.resource_id, "name": c.name} for c in candidates),
            key=lambda c: (c["name"] or "", c["id"] or ""),
        )

        try:
            check_breakers(spec, candidates, kind_report, limits)
        except SweepAborted as exc:
            kind_report.aborted = str(exc)
            logger.error("%s", exc)
            continue
        pending[kind] = candidates

    total = sum(len(c) for c in pending.values())
    if total > limits.max_deletes_total:
        for kind in pending:
            report.kinds[
                kind
            ].aborted = "{} candidates across all kinds exceeds the run cap of {} -- nothing was deleted".format(
                total, limits.max_deletes_total
            )
        logger.error("%s candidates exceeds the run cap of %s; nothing deleted", total, limits.max_deletes_total)
        return report

    if not apply:
        return report

    # Phase 2: delete in rank order, as a barrier on EFFECTS rather than requests.
    # A live API key makes its service account's DELETE answer 400, and these
    # routes answer 202, so ordering the requests is not enough -- each rank's
    # accepted deletes are confirmed before the next rank starts.
    for rank in sorted({registry.KINDS[k].rank for k in pending}):
        kinds_at_rank = [k for k in pending if registry.KINDS[k].rank == rank]
        for kind in kinds_at_rank:
            spec = registry.KINDS[kind]
            for candidate in pending[kind]:
                delete_one(client, spec, candidate, report.kinds[kind])

        for kind in kinds_at_rank:
            confirm_accepted_deletes(client, registry.KINDS[kind], report.kinds[kind])

        unconfirmed = {
            k: report.kinds[k].delete_unconfirmed for k in kinds_at_rank if report.kinds[k].delete_unconfirmed
        }
        if unconfirmed:
            # Continue rather than skipping dependent ranks: unconfirmed is not
            # known-failed, and a dependent delete that really does hit the 400 is
            # reported as `failed` right under this warning.
            logger.warning(
                "rank %d finished with unconfirmed deletes %s; later ranks may see dependency "
                "errors from resources that are still on their way out",
                rank,
                unconfirmed,
            )

    return report
