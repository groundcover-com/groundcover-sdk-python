"""E2E tests for events endpoints. Mirrors sdk/tests/e2e/events_test.go."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.k8s import events_search
from groundcover.models.events_search_request import EventsSearchRequest


def test_events_search(gc_client: groundcover.Client) -> None:
    """Execute an events search and verify results."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours=24)

    result = events_search.sync_detailed(
        client=gc_client,
        body=EventsSearchRequest(
            start=start,
            end=now,
            query="* | stats count(*)",
        ),
    )

    assert result.status_code == 200
    payload = result.parsed
    assert isinstance(payload, list), "Events search should return a list"
    assert len(payload) > 0, "Events search should return at least one result"
    assert payload[0].get("count", 0) > 0, "Events search count should be > 0"
