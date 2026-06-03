"""E2E tests for metrics discovery endpoints. Mirrors sdk/tests/e2e/metrics_discovery_test.go."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

import groundcover
from groundcover.api.metrics import get_metric_keys, get_metric_names, get_metric_values
from groundcover.exceptions import APIError
from groundcover.models.metrics_keys_request import MetricsKeysRequest
from groundcover.models.metrics_names_request import MetricsNamesRequest
from groundcover.models.metrics_values_request import MetricsValuesRequest


def _time_range() -> tuple[datetime, datetime]:
    """Return start/end timestamps for the last hour."""
    end = datetime.now(timezone.utc)
    start = end - timedelta(hours=1)
    return start, end


def _extract_list(payload: object, key: str) -> list:
    """Extract a list from a parsed response, handling both typed models and raw dicts."""
    if isinstance(payload, dict):
        return payload.get(key, [])
    if isinstance(payload, list):
        return payload
    # Typed model: try attribute then additional_properties
    val = getattr(payload, key, None)
    if val is not None:
        return val
    return getattr(payload, "additional_properties", {}).get(key, [])


def test_metrics_names(gc_client: groundcover.Client) -> None:
    """List metric names."""
    start, end = _time_range()

    result = get_metric_names.sync_detailed(
        client=gc_client,
        body=MetricsNamesRequest(
            start=start,
            end=end,
            limit=10,
            filter_="",
        ),
    )
    assert result.status_code == 200
    metrics = _extract_list(result.parsed, "metrics")
    assert isinstance(metrics, list), "Metrics names should return a list"


def test_metrics_names_with_filter(gc_client: groundcover.Client) -> None:
    """List metric names filtered by a substring."""
    start, end = _time_range()

    result = get_metric_names.sync_detailed(
        client=gc_client,
        body=MetricsNamesRequest(
            start=start,
            end=end,
            limit=5,
            filter_="cpu",
        ),
    )
    assert result.status_code == 200
    metrics = _extract_list(result.parsed, "metrics")
    assert isinstance(metrics, list), "Filtered metrics names should return a list"


def test_metrics_keys(gc_client: groundcover.Client) -> None:
    """List metric label keys for an available metric."""
    start, end = _time_range()

    # First discover an available metric name
    names_result = get_metric_names.sync_detailed(
        client=gc_client,
        body=MetricsNamesRequest(
            start=start,
            end=end,
            limit=1,
            filter_="",
        ),
    )
    metrics = _extract_list(names_result.parsed, "metrics")

    if not metrics:
        pytest.skip("No metrics available to test keys")

    metric_name = metrics[0] if isinstance(metrics[0], str) else getattr(metrics[0], "name", str(metrics[0]))

    result = get_metric_keys.sync_detailed(
        client=gc_client,
        body=MetricsKeysRequest(
            name=metric_name,
            start=start,
            end=end,
            limit=10,
        ),
    )
    assert result.status_code == 200
    keys = _extract_list(result.parsed, "keys")
    assert isinstance(keys, list), "Metrics keys should return a list"


def test_metrics_values(gc_client: groundcover.Client) -> None:
    """List metric label values for an available metric and key."""
    start, end = _time_range()

    # Discover an available metric name
    names_result = get_metric_names.sync_detailed(
        client=gc_client,
        body=MetricsNamesRequest(
            start=start,
            end=end,
            limit=1,
            filter_="",
        ),
    )
    metrics = _extract_list(names_result.parsed, "metrics")

    if not metrics:
        pytest.skip("No metrics available to test values")

    metric_name = metrics[0] if isinstance(metrics[0], str) else getattr(metrics[0], "name", str(metrics[0]))

    # Discover an available key for that metric
    keys_result = get_metric_keys.sync_detailed(
        client=gc_client,
        body=MetricsKeysRequest(
            name=metric_name,
            start=start,
            end=end,
            limit=1,
        ),
    )
    keys = _extract_list(keys_result.parsed, "keys")

    if not keys:
        pytest.skip("No keys available to test values")

    key_name = keys[0]

    result = get_metric_values.sync_detailed(
        client=gc_client,
        body=MetricsValuesRequest(
            name=metric_name,
            key=key_name,
            start=start,
            end=end,
            limit=10,
        ),
    )
    assert result.status_code == 200
    values = _extract_list(result.parsed, "values")
    assert isinstance(values, list), "Metrics values should return a list"


def test_invalid_time_range(gc_client: groundcover.Client) -> None:
    """End time before start time should return an error."""
    start, end = _time_range()

    try:
        result = get_metric_names.sync_detailed(
            client=gc_client,
            body=MetricsNamesRequest(
                start=end,  # Swapped: end as start
                end=start,  # Swapped: start as end
                limit=10,
                filter_="",
            ),
        )
        # If no exception, verify non-200 status
        assert result.status_code != 200, f"Expected error for invalid time range, got {result.status_code}"
    except APIError:
        pass  # Expected


def test_nonexistent_metric_keys(gc_client: groundcover.Client) -> None:
    """Keys for a non-existent metric should return empty."""
    start, end = _time_range()

    result = get_metric_keys.sync_detailed(
        client=gc_client,
        body=MetricsKeysRequest(
            name="non_existent_metric_xyz123",
            start=start,
            end=end,
            limit=10,
        ),
    )
    # Should succeed but return empty keys
    assert result.status_code == 200
    keys = _extract_list(result.parsed, "keys")
    assert keys == [] or keys is None or len(keys) == 0, "Should return empty keys for non-existent metric"
