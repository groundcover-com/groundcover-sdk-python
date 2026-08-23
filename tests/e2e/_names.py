"""Unique, run-scoped names for resources the E2E suite creates.

Every name this suite mints looks like::

    sdk-e2e-test-<kind>-<run_id>-p<pid>n<counter>

The ``sdk-e2e-test-`` prefix is what makes a resource identifiable as suite
debris after the fact, and it is what the name-based janitor in
``sdk-python/tools/gc_e2e_janitor`` matches on. Renaming a kind token here is
therefore not a local change: the janitor stops recognising that kind's debris,
silently, because an unmatched name is simply not swept and the sweep still
reports success. That is not a hypothetical -- Go's bare ``e2e-test-synthetic-``
names went unrecognised from the janitor's introduction until 099b431aa2.

This used to be a warning asking you to remember. It is now enforced:
``tests/unit/test_janitor_registry.py`` feeds ``unique_name()`` for every kind in
``_cleanup.SPECS`` through the janitor's real patterns, so a rename fails CI here
rather than quietly stranding resources on a shared tenant.

``run_id`` groups every resource from one test run, which is what lets you ask
"did this run leave anything behind?" and what lets a sweeper tell a finished
run's debris from a run still in flight.

Resolution order:

* ``GC_E2E_RUN_ID`` if set. ``conftest.pytest_configure`` pins this on the
  controller before xdist spawns workers, so every worker in a run agrees --
  without it each worker process would mint its own id and one run's resources
  could not be grouped together.
* else ``GITHUB_RUN_ID`` **plus** ``GITHUB_RUN_ATTEMPT``. The attempt matters:
  GitHub keeps ``GITHUB_RUN_ID`` stable when a workflow run is re-run, so
  without the attempt a retried job would mint the same names as the attempt
  that failed -- and a duplicate monitor title is a 409, not a warning.
* else a random ``r<hex>``.

``pid`` and a per-process counter disambiguate workers within one run.
"""

from __future__ import annotations

import hashlib
import itertools
import os
import re
import uuid

PREFIX = "sdk-e2e-test"

_counter = itertools.count(1)
_run_id: str = ""

_UNSAFE = re.compile(r"[^a-zA-Z0-9]+")
# Bounded so the *whole* name stays within a DNS-1123 label (63 chars), which
# ingestion-key names are validated against. Budget, worst case:
#   "sdk-e2e-test-" (13) + longest kind (16, "data-integration") + "-" (1)
#   + run id + "-p" (2) + pid (7) + "n" (1) + counter (4)  ->  44 + run id
# tests/unit/test_e2e_cleanup.py re-derives this from the real SPECS so the two
# cannot drift apart.
_MAX_RUN_ID = 19


def _sanitize(raw: str) -> str:
    """Reduce an arbitrary id to a name-safe token, keeping distinct ids distinct.

    Two ways distinct ids could collapse onto one identity, and a shared run id means
    cleanup can delete another run's resource:

    * stripping punctuation -- ``run-1`` and ``run1`` both reduce to ``run1``
    * truncating -- two long ids sharing a prefix, up to ``_MAX_RUN_ID``

    Lowercased because ingestion-key names must be DNS-1123 labels
    (``validation.IsDNS1123Label``, ingestionkeys/create_key.go:292), so an override
    like ``verifyA`` would otherwise mint a name the backend rejects.

    So whenever the token is not a faithful copy of the input, it carries a digest of
    the full value. An id that is already name-safe, lowercase and short enough (a
    numeric ``GITHUB_RUN_ID``) is left readable.
    """
    token = _UNSAFE.sub("", raw).lower()
    if not token:
        return ""
    if token == raw and len(token) <= _MAX_RUN_ID:
        return token
    digest = hashlib.sha256(raw.encode()).hexdigest()[:8]
    return token[: _MAX_RUN_ID - len(digest)] + digest


def _ci_run_id() -> str:
    """CI's identity for this run, or "" outside CI.

    Includes the attempt because GITHUB_RUN_ID is unchanged when a workflow run is
    re-run, so without it a retried job would mint the names of the attempt that
    failed -- and a duplicate monitor title is a 409, not a warning.
    """
    github_run = os.environ.get("GITHUB_RUN_ID")
    if not github_run:
        return ""
    return "{}a{}".format(github_run, os.environ.get("GITHUB_RUN_ATTEMPT", "1"))


def run_id() -> str:
    """Return this run's correlation id, generating one on first use.

    An explicit override wins over CI's id; anything that sanitizes to nothing
    (a punctuation-only value) falls back to a random id, which also keeps the
    cache above from recomputing on every call.
    """
    global _run_id
    if not _run_id:
        explicit = os.environ.get("GC_E2E_RUN_ID") or _ci_run_id()
        # 16 hex chars (64 bits), not 8: the pid and counter that follow are not
        # globally unique -- pids are reused and every worker's counter restarts at
        # 1 -- so the run token is what actually keeps names apart, including from
        # leaked resources of past runs that are still on the tenant. 32 bits is
        # thin for that once thousands of runs accumulate.
        _run_id = _sanitize(explicit) or ("r" + uuid.uuid4().hex[:16])
    return _run_id


def unique_name(kind: str) -> str:
    """Mint a unique, suite-identifiable name for a resource of ``kind``.

    The pid and counter are delimited: concatenated, pid 12 with counter 11 and pid
    121 with counter 1 both yield "1211", and every worker starts its counter at 1,
    so two workers in one run could mint the same name -- which name-based id
    recovery would then resolve to the wrong worker's resource.
    """
    return "{}-{}-{}-p{}n{}".format(PREFIX, kind, run_id(), os.getpid(), next(_counter))


def belongs_to_suite(name: str) -> bool:
    """Whether ``name`` was minted by this suite (any run, either SDK)."""
    return bool(re.match(r"^(sdk-)?e2e-test-", name or ""))
