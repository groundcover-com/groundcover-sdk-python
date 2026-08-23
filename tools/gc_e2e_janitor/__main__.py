from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import urllib.parse
from typing import Any, Dict, List, Optional, Sequence

from . import registry
from . import report as report_mod
from .sweep import Limits, run
from .transport import Client

logger = logging.getLogger("gc_e2e_janitor")

# `backend_id` is a free-text workflow input, and pointing this at a customer
# tenant is the largest blast radius in the design. Overridable via
# GC_BACKEND_ALLOWLIST so a deliberate custom-tenant run stays possible -- the
# operator then names the backend twice, in two variables, which a typo cannot do.
DEFAULT_ALLOWED_BACKENDS = ("backend-dev", "backend-staging", "groundcover-staging")

# The bearer token rides every request, so the host is part of the security
# boundary. Deliberately NOT overridable: an additive override would let a caller
# add `attacker.example` and have the key sent there.
ALLOWED_HOST_SUFFIXES = (".groundcover.com",)


def _csv_env(name: str, default: "tuple") -> "tuple":
    raw = os.environ.get(name)
    return tuple(v.strip() for v in raw.split(",") if v.strip()) if raw else default


class ConfigError(SystemExit):
    def __init__(self, message: str) -> None:
        super().__init__("configuration error: {}".format(message))


def parse_mode(sweep_mode: Optional[str], dry_run: Optional[str]) -> bool:
    if sweep_mode:
        if sweep_mode not in ("report", "apply"):
            raise ConfigError(
                "SWEEP_MODE must be exactly 'report' or 'apply', got {!r}. Refusing to guess "
                "which side of a deletion you meant.".format(sweep_mode)
            )
        return sweep_mode == "apply"

    if dry_run is None or dry_run == "":
        return False
    if dry_run not in ("true", "false"):
        # Exact match, no case folding or stripping: leniency in the destructive
        # direction is the defect this replaces.
        raise ConfigError(
            "DRY_RUN must be exactly 'true' or 'false' (lowercase), got {!r}. A GitHub boolean "
            "input always sends one of those two; anything else means the value did not come "
            "from where you think. It is a deprecated alias for SWEEP_MODE=report|apply.".format(dry_run)
        )
    return dry_run == "false"


def parse_kinds(raw: Optional[str]) -> List[str]:
    if not raw or raw.strip() in ("", "all"):
        return sorted(registry.KINDS)
    # dict.fromkeys dedupes while preserving first-seen order: "dashboard,dashboard"
    # would otherwise list and classify the kind twice and duplicate it in
    # expected_kinds, which feeds the missing_kinds check.
    requested = list(dict.fromkeys(k.strip() for k in raw.split(",") if k.strip()))
    if not requested:
        # "," or " , " reaches here as an empty list, passes validation, and
        # sweeps nothing -- an invalid selection rendering as a successful no-op,
        # which is the failure mode this whole tool exists to remove.
        raise ConfigError(
            "SWEEP_KINDS={!r} selects no kinds. Use 'all', or a comma-separated list of: {}.".format(
                raw, sorted(registry.KINDS)
            )
        )
    unknown = sorted(set(requested) - set(registry.KINDS))
    if unknown:
        raise ConfigError(
            "unknown kind(s) {}; known: {}. A typo here would sweep nothing and look clean.".format(
                unknown, sorted(registry.KINDS)
            )
        )
    return requested


def _positive(raw: Any) -> int:
    try:
        value = int(raw)
    except (TypeError, ValueError):
        raise ConfigError("expected a whole number, got {!r}".format(raw))
    if value < 1:
        raise ConfigError("delete caps must be at least 1, got {}".format(value))
    return value


def _age_minutes(raw: Any) -> int:
    try:
        return int(raw)
    except (TypeError, ValueError):
        raise ConfigError("AGE_MINUTES / --age-minutes must be a whole number of minutes, got {!r}".format(raw))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gc_e2e_janitor",
        description="Reconcile e2e test resources stranded on a shared tenant, by name.",
        epilog=(
            "exit codes: 0 = ran, every kind proved its listing complete, nothing indeterminate. "
            "2 = partial; a kind could not be listed, a listing was truncated, or a timestamp "
            "could not be read -- NOT the same as clean. 1 = deletes were attempted and failed. "
            "A tripped circuit breaker exits 2 in apply mode and 0 in report mode, where the cap "
            "is the survey answer; read kinds[*].aborted rather than the exit code there."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--base-url", default=os.environ.get("GC_BASE_URL"))
    parser.add_argument("--backend-id", default=os.environ.get("GC_BACKEND_ID"))
    parser.add_argument("--kinds", default=os.environ.get("SWEEP_KINDS"))
    parser.add_argument("--age-minutes", type=_age_minutes, default=os.environ.get("AGE_MINUTES") or 60)
    parser.add_argument(
        "--identity",
        default=os.environ.get("GC_E2E_IDENTITY"),
        help=(
            "The e2e service account's NAME. Under API-key auth the backend records it as the "
            "creator of everything the suites make. On backend-dev that account is shared with "
            "other automation, so this proves 'not a human's' rather than 'definitely e2e's' -- "
            "it is a conjunct with the name pattern, not a substitute. Required to apply to any "
            "kind that exposes a creator."
        ),
    )
    parser.add_argument("--report-path", default=os.environ.get("REPORT_PATH"))
    # Named for what it actually authorises. It used to be --allow-bulk and did
    # two unrelated jobs: raise the delete caps, and waive the age gate. The caps
    # now fit routine work, so only the age waiver is left.
    parser.add_argument(
        "--confirm-no-age-gate",
        action="store_true",
        default=os.environ.get("CONFIRM_NO_AGE_GATE") == "true",
        help="Permit --age-minutes 0 with apply, which removes the only protection "
        "against deleting an in-flight run's resources.",
    )
    # Lowerable per run for a deliberately cautious pass; the defaults are sized
    # for the real backlog.
    parser.add_argument(
        "--max-deletes-per-kind",
        type=_positive,
        default=os.environ.get("MAX_DELETES_PER_KIND") or Limits.max_deletes_per_kind,
    )
    parser.add_argument(
        "--max-deletes-total", type=_positive, default=os.environ.get("MAX_DELETES_TOTAL") or Limits.max_deletes_total
    )
    parser.add_argument("--max-pages-override", type=int, default=None, help=argparse.SUPPRESS)
    return parser


def _report_path_from_argv(argv: Optional[Sequence[str]]) -> Optional[str]:
    if not argv:
        return None
    # Reversed because argparse takes the last occurrence of a repeated option.
    for i in range(len(argv) - 1, -1, -1):
        item = argv[i]
        if item.startswith("--report-path="):
            return item.split("=", 1)[1]
        if item == "--report-path" and i + 1 < len(argv):
            return argv[i + 1]
    return None


def _write_early_failure_report(
    message: str,
    args: Optional[argparse.Namespace] = None,
    argv: Optional[Sequence[str]] = None,
) -> None:
    path = getattr(args, "report_path", None) or _report_path_from_argv(argv) or os.environ.get("REPORT_PATH")
    if not path:
        return

    payload: Dict[str, Any] = {
        "schema_version": report_mod.SCHEMA_VERSION,
        "status": "failed",
        "error": message,
        "backend_id": getattr(args, "backend_id", None) or os.environ.get("GC_BACKEND_ID"),
        "base_url": getattr(args, "base_url", None) or os.environ.get("GC_BASE_URL"),
        "age_minutes": getattr(args, "age_minutes", None),
        "mode": os.environ.get("SWEEP_MODE") or "report",
        "kinds": {},
        "expected_kinds": [],
        "missing_kinds": [],
        "note": "the run failed during startup, before any listing was attempted",
    }

    # Atomic via a sibling temp file: the upload step treats a missing report as an
    # error, which makes a half-written one worse than none.
    tmp = "{}.{}.tmp".format(path, os.getpid())
    try:
        with open(tmp, "w") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except OSError as exc:
        logger.warning("could not write the startup-failure report to %s: %s", path, exc)
        try:
            os.unlink(tmp)
        except OSError:
            pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    # Normalise once. argparse falls back to sys.argv internally when argv is
    # None, but the failure-report path scans this list itself and would
    # otherwise see nothing for the ordinary `python -m gc_e2e_janitor` call.
    argv = list(argv) if argv is not None else sys.argv[1:]
    parsed: Optional[argparse.Namespace] = None
    try:
        parsed = build_parser().parse_args(argv)
        return _run(parsed)
    except ConfigError as exc:
        _write_early_failure_report(str(exc), parsed, argv)
        raise
    except SystemExit as exc:
        # argparse exits here for a usage error (code 2) and for --help (code 0).
        # Only the former is a failure worth reporting; --help must not leave a
        # "failed" artifact behind.
        if exc.code not in (0, None):
            _write_early_failure_report("invalid arguments: {}".format(exc.code), parsed, argv)
        raise
    except Exception as exc:
        # urlparse("https://[") raises before our own validation runs, and a death
        # with no report leaves the required artifact absent with no diagnostic.
        _write_early_failure_report("{}: {}".format(type(exc).__name__, exc), parsed, argv)
        raise


def _run(args: argparse.Namespace) -> int:

    api_key = os.environ.get("GC_API_KEY")
    if not (api_key and args.base_url and args.backend_id):
        raise ConfigError("GC_API_KEY, GC_BASE_URL and GC_BACKEND_ID are all required")

    allowed_backends = _csv_env("GC_BACKEND_ALLOWLIST", DEFAULT_ALLOWED_BACKENDS)
    if args.backend_id not in allowed_backends:
        raise ConfigError(
            "backend {!r} is not in the allowlist {}. This tool deletes data; pointing it at an "
            "unlisted tenant is never intentional. If it IS intentional, name it in "
            "GC_BACKEND_ALLOWLIST too.".format(args.backend_id, list(allowed_backends))
        )

    # The API key travels as `Authorization: Bearer` on every request, so a wrong
    # base_url does not just fail -- it hands the e2e key to whoever owns that
    # host. base_url is a free-form workflow input, so it is validated like one.
    parsed = urllib.parse.urlparse(args.base_url)
    suffixes = ALLOWED_HOST_SUFFIXES
    host = parsed.hostname or ""
    if parsed.scheme != "https" or not any(host == s.lstrip(".") or host.endswith(s) for s in suffixes):
        raise ConfigError(
            "base_url {!r} must be https and its host must end with one of {}. The API key is "
            "sent as a bearer token on every request, so the host is part of the security "
            "boundary.".format(args.base_url, list(suffixes))
        )

    # The check above reads only scheme and hostname, so `https://user:token@host`
    # would pass -- and base_url is copied verbatim into a 90-day artifact.
    # Rejects rather than strips: silently rewriting an operator's endpoint is the
    # worse surprise. A path or query is refused too, since every route is built
    # by appending to base_url.
    if parsed.username or parsed.password:
        raise ConfigError(
            "base_url must not embed credentials. The value is written verbatim into the report "
            "artifact, which is retained for 90 days, so a token in the URL outlives the run. "
            "Pass the key via GC_API_KEY."
        )
    if parsed.path not in ("", "/") or parsed.query or parsed.fragment or parsed.params:
        raise ConfigError(
            "base_url {!r} must be scheme and host only -- every route is appended to it, so a "
            "path, query or fragment corrupts every request rather than prefixing "
            "it.".format(args.base_url)
        )

    # argparse type=int accepts -5, and the workflow's `type: number` forwards it
    # unchanged. A negative age puts the cutoff in the future, making everything
    # eligible.
    if args.age_minutes < 0:
        raise ConfigError(
            "--age-minutes / AGE_MINUTES must be >= 0, got {}. A negative age puts the cutoff in "
            "the future, which makes every resource eligible.".format(args.age_minutes)
        )

    apply = parse_mode(os.environ.get("SWEEP_MODE"), os.environ.get("DRY_RUN"))

    if apply and args.age_minutes == 0 and not args.confirm_no_age_gate:
        # The sweep does not interlock with sdk-publish.yml, which runs the Go
        # e2e suite against the same tenant on every push to main -- a shared
        # concurrency group would let a sweep cancel a queued release. For every
        # kind without a `lastActive` veto the age cutoff is the only thing
        # keeping this off an in-flight run's resources, and age 0 removes it.
        raise ConfigError(
            "--age-minutes 0 with apply removes the only protection against deleting an in-flight "
            "e2e run's resources (sdk-publish.yml runs the Go suite against this tenant and does "
            "not share a concurrency group). Set CONFIRM_NO_AGE_GATE=true if you mean it."
        )
    kinds = parse_kinds(args.kinds)

    # The creator gate is a second factor; the anchored name is the primary one.
    # A missing identity disables it loudly -- the state goes in the report header
    # and the log -- rather than aborting.
    #
    # Normalised here because an unset workflow variable arrives as "" while
    # classify() gates on `is not None`: an empty string would arm the gate
    # against an empty creator, reject every match, and report a clean sweep.
    identity = args.identity or None

    gated = sorted(k for k in kinds if registry.KINDS[k].creator_field)
    if apply and gated and not identity:
        logger.warning(
            "GC_E2E_IDENTITY is not set, so the creator gate is DISABLED for %s. Deletion for "
            "those kinds rests on the anchored name pattern and the age cutoff alone. Set it to "
            "the e2e service account's NAME -- the backend records that as the creator under "
            "API-key auth, not an email.",
            gated,
        )

    if args.max_pages_override is not None:
        # Test hook for the P0 calibration probe: force a truncated listing and
        # confirm the tool reports `partial` rather than a smaller number as fact.
        from . import sweep as sweep_mod

        sweep_mod.MAX_PAGES = args.max_pages_override

    limits = Limits(
        max_deletes_per_kind=args.max_deletes_per_kind,
        max_deletes_total=args.max_deletes_total,
    )

    client = Client(base_url=args.base_url, api_key=api_key, backend_id=args.backend_id)
    result = run(
        client,
        kinds=kinds,
        age_minutes=args.age_minutes,
        apply=apply,
        identity=identity,
        limits=limits,
        backend_id=args.backend_id,
        base_url=args.base_url,
    )

    payload = report_mod.to_dict(result)
    if args.report_path:
        with open(args.report_path, "w") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))

    # Always to the log, in addition to (not instead of) the step summary. These
    # used to be alternatives, so in CI the numbers went only to a file you had to
    # download and the log carried two lines.
    print(report_mod.render_text(result), file=sys.stderr)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as handle:
            handle.write(report_mod.render_markdown(result))

    logger.info("sweep %s (exit %d)", result.status, result.exit_code)
    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
