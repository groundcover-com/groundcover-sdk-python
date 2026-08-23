from __future__ import annotations

import dataclasses
from typing import Any, Dict, List

from .sweep import KindReport, SweepReport

SCHEMA_VERSION = 1


def _cell(value: object) -> str:
    text = str(value)
    # Backticks are REMOVED rather than escaped. render_markdown wraps names in
    # code spans, and Markdown has no backslash escape inside one -- the only way
    # to include a backtick is to change the fence length, which cannot be done
    # safely for arbitrary input. A name containing one would otherwise close the
    # span and render tenant-controlled Markdown in the step summary. The JSON
    # artifact carries the byte-exact name, so nothing is lost from the record.
    text = text.replace("`", "")
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def to_dict(report: SweepReport) -> Dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "status": report.status,
        "backend_id": report.backend_id,
        "base_url": report.base_url,
        "mode": report.mode,
        "age_minutes": report.age_minutes,
        "identity": report.identity,
        "expected_kinds": list(report.expected_kinds),
        "missing_kinds": report.missing_kinds,
        "unsweepable": dict(report.unsweepable),
        "kinds": {kind: {**dataclasses.asdict(kr), "determinate": kr.determinate} for kind, kr in report.kinds.items()},
    }


def _evidence(kind_report: KindReport) -> str:
    if kind_report.not_applicable:
        # Determinate, unlike a list failure: the kind cannot exist here.
        return "n/a on this backend (inCloud-only routes)"
    if not kind_report.list_ok:
        return "**LIST FAILED** ({})".format(kind_report.list_error or "unknown")
    if kind_report.aborted:
        return "**ABORTED** (circuit breaker)"
    parts = ["ok", "{} page(s)".format(kind_report.pages_fetched)]
    if kind_report.delete_unconfirmed:
        parts.append("**{} accepted but STILL LISTED**".format(kind_report.delete_unconfirmed))
    if kind_report.creator_gate_rejected_everything:
        parts.append("**creator gate rejected ALL {} matches - stale identity?**".format(kind_report.matched))
    if not kind_report.pagination_complete:
        parts.append("**TRUNCATED**")
    if kind_report.unknown_age:
        parts.append("**{} unknown age**".format(kind_report.unknown_age))
    if kind_report.unnamed:
        # Without this the run goes red with no visible cause: `unnamed` feeds
        # `determinate` and therefore the exit code, so it has to appear in the
        # one place a human looks.
        parts.append("**{} rows had no readable name (field renamed?)**".format(kind_report.unnamed))
    return ", ".join(parts)


_COLUMNS = (
    ("listed", "listed"),
    ("matched", "matched"),
    ("skipped_foreign_creator", "other owner"),
    ("too_young", "too young"),
    ("excluded", "excluded"),
    # Zero for every kind but synthetic-companion-monitor, and it earns the column
    # there: it is the difference between "nothing to reclaim" and "we refused to
    # reclaim because the owning synthetic is still live".
    ("skipped_dependency_present", "owner live"),
    ("deleted", "deleted"),
    ("delete_accepted", "202"),
    ("delete_confirmed", "202 ok"),
    ("already_gone", "gone"),
    ("failed", "failed"),
)


def render_text(report: SweepReport) -> str:
    width = max([len(k) for k in report.expected_kinds] + [len(k) for k in report.unsweepable] + [4])
    head = "  {:<{w}}".format("kind", w=width) + "".join("{:>12}".format(label) for _, label in _COLUMNS) + "  listing"
    lines = [
        "",
        "E2E leftover sweep - {} | mode={} | age>={}m | {}".format(
            report.backend_id,
            report.mode,
            report.age_minutes,
            "identity={}".format(report.identity) if report.identity else "CREATOR GATE DISABLED",
        ),
        head,
        "  " + "-" * (len(head) - 2),
    ]

    for kind in report.expected_kinds:
        kr = report.kinds.get(kind)
        if kr is None:
            lines.append("  {:<{w}}{}  NO REPORT".format(kind, "{:>12}".format("-") * len(_COLUMNS), w=width))
            continue
        cells = "".join("{:>12}".format(getattr(kr, field)) for field, _ in _COLUMNS)
        lines.append("  {:<{w}}{}  {}".format(kind, cells, _plain(_evidence(kr)), w=width))

    for kind, reason in sorted(report.unsweepable.items()):
        dashes = "".join("{:>12}".format("-") for _ in _COLUMNS)
        lines.append("  {:<{w}}{}  NOT SWEEPABLE".format(kind, dashes, w=width))

    lines.append("")
    lines.append("  verdict: {}".format(report.status.upper()))
    if report.missing_kinds:
        lines.append("  kinds that produced no report: {}".format(", ".join(report.missing_kinds)))
    for kind, kr in sorted(report.kinds.items()):
        if kr.aborted:
            lines.append("  circuit breaker [{}]: {}".format(kind, _plain(kr.aborted)))
    total_failures = sum(len(kr.failures) for kr in report.kinds.values())
    if total_failures:
        lines.append("  delete failures: {} (details in the JSON artifact)".format(total_failures))
    lookalikes = {name for kr in report.kinds.values() for name in kr.lookalikes}
    if lookalikes:
        lines.append(
            "  unrecognised e2e-lookalike names: {} (never deleted; a growing count means a "
            "suite renamed its prefix)".format(len(lookalikes))
        )
    lines.append("")
    return "\n".join(lines)


def _plain(text: str) -> str:
    return text.replace("**", "")


def render_markdown(report: SweepReport) -> str:
    lines: List[str] = [
        # _cell() on the heading and the identity below, not just on table cells.
        # Both are operator-controlled (backend_id can be a free-form
        # custom_backend_id; identity comes from a repo variable), and while an
        # operator corrupting their own summary is self-inflicted rather than an
        # escalation, "the rendered report cannot be corrupted by its inputs" is a
        # property worth holding uniformly -- a reader should not have to know
        # which values happened to be trusted. to_dict() keeps the raw values.
        "## E2E leftover sweep - `{}`".format(_cell(report.backend_id)),
        "",
        "**{}** | mode `{}` | age >= {}m | {}".format(
            {"ok": "OK", "partial": "PARTIAL - some results are unknown", "failed": "FAILED"}[report.status],
            report.mode,
            report.age_minutes,
            (
                "identity `{}`".format(_cell(report.identity))
                if report.identity
                # Never let a run without the second factor look like one with it.
                else "**creator gate DISABLED** (GC_E2E_IDENTITY unset)"
            ),
        ),
        "",
        "| kind | " + " | ".join(label for _, label in _COLUMNS) + " | listing |",
        "|---|" + "---:|" * len(_COLUMNS) + "---|",
    ]

    for kind in report.expected_kinds:
        kind_report = report.kinds.get(kind)
        if kind_report is None:
            lines.append("| `{}` |".format(kind) + " - |" * len(_COLUMNS) + " **NO REPORT** |")
            continue
        cells = [str(getattr(kind_report, field)) for field, _ in _COLUMNS]
        lines.append("| `{}` | {} | {} |".format(_cell(kind), " | ".join(cells), _cell(_evidence(kind_report))))

    for kind, reason in sorted(report.unsweepable.items()):
        lines.append(
            "| `{}` |".format(_cell(kind)) + " - |" * len(_COLUMNS) + " NOT SWEEPABLE - {} |".format(_cell(reason))
        )

    if report.missing_kinds:
        lines += ["", "> **Kinds that produced no report at all:** {}".format(", ".join(report.missing_kinds))]

    aborted = {k: r.aborted for k, r in report.kinds.items() if r.aborted}
    if aborted:
        lines += ["", "### Circuit breakers"] + ["- {}".format(reason) for reason in aborted.values()]

    failures = [(k, f) for k, r in report.kinds.items() for f in r.failures]
    if failures:
        lines += ["", "### Failures"] + [
            "- `{}` {}".format(_cell(kind), _cell(failure)) for kind, failure in failures[:50]
        ]
        if len(failures) > 50:
            lines.append("- ...and {} more (see the JSON artifact)".format(len(failures) - 50))

    lookalikes = sorted({name for r in report.kinds.values() for name in r.lookalikes})
    if lookalikes:
        lines += [
            "",
            "### Unrecognised e2e-lookalike names ({})".format(len(lookalikes)),
            "",
            "Never deleted. A growing count here means a suite renamed its prefix and this "
            "janitor has silently stopped recognising it.",
            "",
        ] + ["- `{}`".format(_cell(name)) for name in lookalikes[:25]]
        if len(lookalikes) > 25:
            lines.append("- ...and {} more".format(len(lookalikes) - 25))

    return "\n".join(lines) + "\n"
