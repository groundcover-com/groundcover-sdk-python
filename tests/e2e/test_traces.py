"""E2E tests for traces endpoints. Mirrors sdk/tests/e2e/traces_test.go."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.traces import search_traces
from groundcover.models.traces_search_request import TracesSearchRequest


def test_traces_search(gc_client: groundcover.Client) -> None:
    """Execute a traces search and verify results."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours=24)

    result = search_traces.sync_detailed(
        client=gc_client,
        body=TracesSearchRequest(
            start=start,
            end=now,
            query="* | stats count(*)",
        ),
    )

    assert result.status_code == 200
    payload = result.parsed
    assert isinstance(payload, list), "Traces search should return a list"
    assert len(payload) > 0, "Traces search should return at least one result"
    assert payload[0].get("count", 0) > 0, "Traces search count should be > 0"
