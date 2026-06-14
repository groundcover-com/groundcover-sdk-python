"""Shared fixtures for E2E tests.

All 3 environment variables are required:
  - GC_API_KEY
  - GC_BACKEND_ID
  - GC_BASE_URL
"""

from __future__ import annotations

import os
import secrets

import pytest

import groundcover


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
def gc_async_client() -> groundcover.AsyncClient:
    """Create an async groundcover client for E2E tests."""
    api_key = _require_env("GC_API_KEY")
    backend_id = _require_env("GC_BACKEND_ID")
    base_url = _require_env("GC_BASE_URL")

    traceparent = os.environ.get("GC_TRACEPARENT") or _generate_traceparent()

    client = groundcover.AsyncClient(
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
    import asyncio

    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(client.aclose())
        else:
            loop.run_until_complete(client.aclose())
    except RuntimeError:
        asyncio.run(client.aclose())
