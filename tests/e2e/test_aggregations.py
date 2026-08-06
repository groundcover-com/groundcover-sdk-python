"""E2E tests for aggregations endpoints. Mirrors sdk/tests/e2e/metricsaggregator_test.go."""

from __future__ import annotations

import json

import groundcover
from groundcover.api.aggregations_metrics import (
    create_metrics_aggregator_config,
    delete_metrics_aggregator_config,
    get_metrics_aggregator_config,
    update_metrics_aggregator_config,
)
from groundcover.models.create_update_metrics_aggregator_config_request import (
    CreateUpdateMetricsAggregatorConfigRequest,
)

from . import _singletons
from ._singletons import SingletonFixture

AGGREGATOR_CONFIG = """content: |
  - ignore_old_samples: true
    match: '{__name__=~"sdk_e2e_test_metric_counter"}'
    without: [instance]
    interval: 30s
    outputs: [total_prometheus]
  - match: '{__name__=~"sdk_e2e_test_metric_latency"}'
    without: [instance]
    interval: 30s
    outputs: [avg]"""

AGGREGATOR_CONFIG_UPDATED = """content: |
  - ignore_old_samples: true
    match: '{__name__=~"sdk_e2e_test_metric_counter_updated"}'
    without: [instance]
    interval: 60s
    outputs: [total_prometheus]
  - match: '{__name__=~"sdk_e2e_test_metric_latency_updated"}'
    without: [instance]
    interval: 60s
    outputs: [avg]"""


class TestMetricsAggregatorLifecycle:
    """Full CRUD lifecycle for metrics aggregator configuration."""

    def test_metrics_aggregator_crud(self, gc_client: groundcover.Client, singleton: SingletonFixture) -> None:
        # This config is tenant-wide and has no id, so deleting it destroys the
        # tenant's real configuration rather than "our" resource. Snapshot it and
        # restore it on teardown instead.
        singleton("metrics-aggregator", markers=_singletons.SUITE_MARKERS)

        # Create
        create_result = create_metrics_aggregator_config.sync_detailed(
            client=gc_client,
            body=CreateUpdateMetricsAggregatorConfigRequest(value=AGGREGATOR_CONFIG),
        )
        assert create_result.status_code == 201
        create_data = json.loads(create_result.content)
        assert create_data["value"] == AGGREGATOR_CONFIG
        assert create_data["uuid"]
        assert create_data["created_timestamp"]
        original_timestamp = create_data["created_timestamp"]

        # Get - verify value matches
        get_result = get_metrics_aggregator_config.sync_detailed(client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["value"] == AGGREGATOR_CONFIG

        # Update
        update_result = update_metrics_aggregator_config.sync_detailed(
            client=gc_client,
            body=CreateUpdateMetricsAggregatorConfigRequest(value=AGGREGATOR_CONFIG_UPDATED),
        )
        assert update_result.status_code == 200
        update_data = json.loads(update_result.content)
        assert update_data["value"] == AGGREGATOR_CONFIG_UPDATED
        assert update_data["created_timestamp"]
        assert update_data["created_timestamp"] > original_timestamp

        # Get - verify updated value
        get_result = get_metrics_aggregator_config.sync_detailed(client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["value"] == AGGREGATOR_CONFIG_UPDATED

        # Delete - empties the value (the backend implements delete as a new
        # empty revision); the fixture restores the snapshot afterwards.
        delete_metrics_aggregator_config.sync_detailed(client=gc_client)

        get_result = get_metrics_aggregator_config.sync_detailed(client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["value"] == ""
