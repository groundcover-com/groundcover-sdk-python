"""E2E tests for k8s endpoints. Mirrors sdk/tests/e2e/k8s_test.go."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.k8s import clusters_list, get_events_over_time, workloads_list
from groundcover.models import (
    get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time as _eot_mod,
)
from groundcover.models import (
    get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time_sort_by as _sb,
)
from groundcover.models import (
    get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time_sort_order as _so,
)
from groundcover.models.clusters_list_request import ClustersListRequest
from groundcover.models.workloads_list_request import WorkloadsListRequest

EventsOverTimeRequest = _eot_mod.GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime
SortBy = _sb.GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortBy
SortOrder = _so.GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortOrder


def test_list_clusters(gc_client: groundcover.Client) -> None:
    """List Kubernetes clusters."""
    result = clusters_list.sync_detailed(
        client=gc_client,
        body=ClustersListRequest(),
    )
    assert result.status_code == 200
    payload = result.parsed
    assert payload is not None
    assert hasattr(payload, "clusters") or "clusters" in getattr(payload, "additional_properties", {}), (
        "Response should contain 'clusters' field"
    )


def test_list_workloads(gc_client: groundcover.Client) -> None:
    """List Kubernetes workloads."""
    result = workloads_list.sync_detailed(
        client=gc_client,
        body=WorkloadsListRequest(
            sort_by="rps",
            order="desc",
        ),
    )
    assert result.status_code == 200
    payload = result.parsed
    assert payload is not None
    assert hasattr(payload, "workloads") or "workloads" in getattr(payload, "additional_properties", {}), (
        "Response should contain 'workloads' field"
    )


def test_events_over_time(gc_client: groundcover.Client) -> None:
    """Get events over time with conditions."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(minutes=15)

    result = get_events_over_time.sync_detailed(
        client=gc_client,
        body=EventsOverTimeRequest(
            start=start,
            end=now,
            sort_by=SortBy.TIMESTAMP,
            sort_order=SortOrder.DESC,
            conditions=[],
            with_raw_events=True,
        ),
    )
    assert result.status_code == 200
    payload = result.parsed
    assert payload is not None
    events = getattr(payload, "events", None)
    if events is None:
        events = getattr(payload, "additional_properties", {}).get("events", [])
    assert len(events) > 0, "Should have events in the last 15 minutes"
