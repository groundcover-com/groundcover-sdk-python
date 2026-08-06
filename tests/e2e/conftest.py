"""Shared fixtures for E2E tests.

All 3 environment variables are required:
  - GC_API_KEY
  - GC_BACKEND_ID
  - GC_BASE_URL

These tests run against a shared live tenant, so anything a test creates must be
registered with the ``tracker`` fixture so it is deleted even when the test fails
part-way. See ``_cleanup.py``.
"""

from __future__ import annotations

import os
import secrets
from typing import Any, Callable, Optional, Sequence

import pytest

import groundcover

from . import _singletons
from ._cleanup import ResourceTracker

# The run id is pinned in tests/conftest.py, which is the root conftest and so runs
# on the controller for any invocation; doing it here only worked when tests/e2e/
# was named on the command line.


INCLOUD_REQUEST_TIMEOUT_SECONDS = 120.0


def _require_env(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        pytest.skip(f"{name} environment variable is required for E2E tests")
    return val


def _generate_traceparent() -> str:
    """Generate a random W3C traceparent header."""
    trace_id = secrets.token_hex(16)
    span_id = secrets.token_hex(8)
    return f"00-{trace_id}-{span_id}-01"


@pytest.fixture(scope="session")
def gc_client() -> groundcover.Client:
    """Create a groundcover client for E2E tests.

    All 3 env vars required, retry on 500/502/503/504/429.
    """
    api_key = _require_env("GC_API_KEY")
    backend_id = _require_env("GC_BACKEND_ID")
    base_url = _require_env("GC_BASE_URL")

    traceparent = os.environ.get("GC_TRACEPARENT") or _generate_traceparent()

    client = groundcover.Client(
        api_key=api_key,
        backend_id=backend_id,
        base_url=base_url,
        timeout=None,
        retry_count=5,
        min_retry_wait=1.0,
        max_retry_wait=10.0,
        retry_statuses=[500, 502, 503, 504, 429],
        traceparent=traceparent,
    )
    yield client
    client.close()


@pytest.fixture(scope="session")
def gc_incloud_client() -> groundcover.Client:
    """A client bound to an inCloud backend, for endpoints only served there.

    Ingestion keys sit behind ``VerifyIncloudBackend``, so on ``backend-dev`` every
    call is rejected. The Go suite handles this by pointing that one test at another
    backend (``sdk/tests/e2e/ingestionkeys_test.go:24``) rather than skipping, which
    is why its ingestion-key coverage is real and the Python one was not. Same
    default here, overridable with ``GC_INCLOUD_BACKEND_ID``.
    """
    api_key = _require_env("GC_API_KEY")
    base_url = _require_env("GC_BASE_URL")
    backend_id = os.environ.get("GC_INCLOUD_BACKEND_ID", "groundcover-staging")

    client = groundcover.Client(
        api_key=api_key,
        backend_id=backend_id,
        base_url=base_url,
        # Finite, unlike the default client below: a hung request here would stall
        # teardown indefinitely, and teardown always running is the whole point of
        # the tracker. Generous enough that a slow-but-working call still succeeds,
        # so a breach means something is actually wrong.
        timeout=INCLOUD_REQUEST_TIMEOUT_SECONDS,
        retry_count=5,
        min_retry_wait=1.0,
        max_retry_wait=10.0,
        retry_statuses=[500, 502, 503, 504, 429],
        traceparent=os.environ.get("GC_TRACEPARENT") or _generate_traceparent(),
    )
    yield client
    client.close()


@pytest.fixture
def incloud_tracker(gc_incloud_client: groundcover.Client) -> ResourceTracker:
    """Tracker bound to the inCloud client.

    Bound deliberately: a tracker built on the default client would send its deletes
    to ``backend-dev``, where the inCloud middleware rejects them -- cleanup would
    quietly do nothing.
    """
    tracked = ResourceTracker(gc_incloud_client)
    yield tracked
    tracked.drain()


@pytest.fixture
def tracker(gc_client: groundcover.Client) -> ResourceTracker:
    """Per-test registry of resources to delete on teardown.

    Function-scoped on purpose: resource lifetime is one test, a teardown failure
    is attributed to the test that caused it, and under ``-n auto`` a
    session-scoped registry would only drain once per worker (and not at all if a
    worker dies).
    """
    tracked = ResourceTracker(gc_client)
    yield tracked
    tracked.drain()


@pytest.fixture
def singleton(gc_client: groundcover.Client, tracker: ResourceTracker) -> Callable[..., Optional[Any]]:
    """Bracket a test that mutates a tenant-wide singleton config.

    Snapshots the config now and registers a restore for teardown. Returns the
    snapshot so the test can assert against the pre-existing state if it wants.
    Pass ``markers`` -- strings that appear only in this suite's own payloads --
    so a concurrent run holding the singleton is detected and this test skips
    instead of installing that run's payload as the tenant's config.
    """

    def _use(kind: str, markers: Sequence[str] = ()) -> Optional[Any]:
        snapshotted = _singletons.snapshot(gc_client, kind)
        if _singletons.looks_like_test_payload(snapshotted, markers):
            pytest.skip(
                f"{kind} currently holds an e2e test payload, so another suite run owns it; "
                "skipping rather than clobbering the tenant config"
            )
        tracker.add_finalizer(
            f"restore {kind} config",
            lambda: _singletons.restore(gc_client, kind, snapshotted, markers),
        )
        return snapshotted

    return _use
