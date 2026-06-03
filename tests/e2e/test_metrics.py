"""E2E tests for metrics endpoints. Mirrors sdk/tests/e2e/metrics_test.go."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.metrics import metrics_query
from groundcover.models.query_request import QueryRequest
from groundcover.models.query_request_query_type import QueryRequestQueryType


def test_metrics_query(gc_client: groundcover.Client) -> None:
    """Execute a metrics range query and verify the response."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(minutes=15)

    result = metrics_query.sync_detailed(
        client=gc_client,
        body=QueryRequest(
            start=start,
            end=now,
            step="1m",
            query_type=QueryRequestQueryType.RANGE,
            promql="up",
        ),
    )

    assert result.status_code == 200
    payload = result.parsed
    assert payload["status"] == "success", f"Expected status 'success', got {payload.get('status')}"
    assert "data" in payload, "Response should contain 'data' field"
    assert payload["data"] is not None, "Data field should not be None"
