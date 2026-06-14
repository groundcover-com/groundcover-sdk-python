"""E2E tests for logs endpoints. Mirrors sdk/tests/e2e/logs_test.go."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.logs import search_logs
from groundcover.models.logs_search_request import LogsSearchRequest


def test_logs_search(gc_client: groundcover.Client) -> None:
    """Execute a logs search and verify results."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours=24)

    result = search_logs.sync_detailed(
        client=gc_client,
        body=LogsSearchRequest(
            start=start,
            end=now,
            query="* | stats count(*)",
        ),
    )

    assert result.status_code == 200
    payload = result.parsed
    assert isinstance(payload, list), "Logs search should return a list"
    assert len(payload) > 0, "Logs search should return at least one result"
    assert payload[0].get("count", 0) > 0, "Logs search count should be > 0"
