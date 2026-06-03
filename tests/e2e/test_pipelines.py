"""E2E tests for pipelines endpoints.

Mirrors sdk/tests/e2e/logspipeline_test.go, tracespipeline_test.go, metricspipeline_test.go.
"""

from __future__ import annotations

import json

import groundcover
from groundcover.api.logs_pipeline import (
    create_logs_pipeline_config,
    delete_logs_pipeline_config,
    get_logs_pipeline_config,
    update_logs_pipeline_config,
)
from groundcover.api.metrics_pipeline import (
    create_metrics_pipeline_config,
    delete_metrics_pipeline_config,
    get_metrics_pipeline_config,
    update_metrics_pipeline_config,
)
from groundcover.api.traces_pipeline import (
    create_traces_pipeline_config,
    delete_traces_pipeline_config,
    get_traces_pipeline_config,
    update_traces_pipeline_config,
)
from groundcover.models.create_update_logs_pipeline_config_request import (
    CreateUpdateLogsPipelineConfigRequest,
)
from groundcover.models.create_update_metrics_pipeline_config_request import (
    CreateUpdateMetricsPipelineConfigRequest,
)
from groundcover.models.create_update_traces_pipeline_config_request import (
    CreateUpdateTracesPipelineConfigRequest,
)
from groundcover.models.relabel_config import RelabelConfig
from groundcover.models.relabel_config_add_label import RelabelConfigAddLabel

LOGS_CONFIG = """ottlRules:
- ruleName: example-rule
  conditions:
    - container_name == "nginx"
  statements:
    - set(attributes["test.key"], "test-value")"""

LOGS_CONFIG_UPDATED = """ottlRules:
- ruleName: example-rule-updated
  conditions:
    - container_name == "nginx"
  statements:
    - set(attributes["test.key"], "test-value-updated")"""

TRACES_CONFIG = """ottlRules:
- ruleName: example-rule
  conditions:
    - workload == "nginx"
  statements:
    - set(attributes["test.key"], "test-value")"""

TRACES_CONFIG_UPDATED = """ottlRules:
- ruleName: example-rule-updated
  conditions:
    - workload == "nginx"
  statements:
    - set(attributes["test.key"], "test-value-updated")"""


def _make_add_label(labels: dict[str, str]) -> RelabelConfigAddLabel:
    add_label = RelabelConfigAddLabel()
    for k, v in labels.items():
        add_label[k] = v
    return add_label


class TestLogsPipelineLifecycle:
    """Full CRUD lifecycle for logs pipeline configuration."""

    def test_logs_pipeline_crud(self, gc_client: groundcover.Client) -> None:
        try:
            # Create
            create_result = create_logs_pipeline_config.sync_detailed(
                client=gc_client,
                body=CreateUpdateLogsPipelineConfigRequest(value=LOGS_CONFIG),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            assert create_data["value"] == LOGS_CONFIG
            assert create_data["uuid"]
            assert create_data["created_timestamp"]
            original_timestamp = create_data["created_timestamp"]

            # Get - verify value matches
            get_result = get_logs_pipeline_config.sync_detailed(client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["value"] == LOGS_CONFIG

            # Update
            update_result = update_logs_pipeline_config.sync_detailed(
                client=gc_client,
                body=CreateUpdateLogsPipelineConfigRequest(value=LOGS_CONFIG_UPDATED),
            )
            assert update_result.status_code == 200
            update_data = json.loads(update_result.content)
            assert update_data["value"] == LOGS_CONFIG_UPDATED
            assert update_data["created_timestamp"]
            assert update_data["created_timestamp"] > original_timestamp

            # Get - verify updated value
            get_result = get_logs_pipeline_config.sync_detailed(client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["value"] == LOGS_CONFIG_UPDATED

        finally:
            # Delete
            delete_logs_pipeline_config.sync_detailed(client=gc_client)

        # Verify deletion - should return empty value
        get_result = get_logs_pipeline_config.sync_detailed(client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["value"] == ""


class TestTracesPipelineLifecycle:
    """Full CRUD lifecycle for traces pipeline configuration."""

    def test_traces_pipeline_crud(self, gc_client: groundcover.Client) -> None:
        try:
            # Create
            create_result = create_traces_pipeline_config.sync_detailed(
                client=gc_client,
                body=CreateUpdateTracesPipelineConfigRequest(value=TRACES_CONFIG),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            assert create_data["value"] == TRACES_CONFIG
            assert create_data["uuid"]
            assert create_data["created_timestamp"]
            original_timestamp = create_data["created_timestamp"]

            # Get - verify value matches
            get_result = get_traces_pipeline_config.sync_detailed(client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["value"] == TRACES_CONFIG

            # Update
            update_result = update_traces_pipeline_config.sync_detailed(
                client=gc_client,
                body=CreateUpdateTracesPipelineConfigRequest(value=TRACES_CONFIG_UPDATED),
            )
            assert update_result.status_code == 200
            update_data = json.loads(update_result.content)
            assert update_data["value"] == TRACES_CONFIG_UPDATED
            assert update_data["created_timestamp"]
            assert update_data["created_timestamp"] > original_timestamp

            # Get - verify updated value
            get_result = get_traces_pipeline_config.sync_detailed(client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["value"] == TRACES_CONFIG_UPDATED

        finally:
            # Delete
            delete_traces_pipeline_config.sync_detailed(client=gc_client)

        # Verify deletion - should return empty value
        get_result = get_traces_pipeline_config.sync_detailed(client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["value"] == ""


class TestMetricsPipelineLifecycle:
    """Full CRUD lifecycle for metrics pipeline configuration."""

    def test_metrics_pipeline_crud(self, gc_client: groundcover.Client) -> None:
        try:
            # Create with rules
            create_result = create_metrics_pipeline_config.sync_detailed(
                client=gc_client,
                body=CreateUpdateMetricsPipelineConfigRequest(
                    rules=RelabelConfig(
                        keep_regex=["http_requests_total", "process_cpu_seconds_total"],
                        add_label=_make_add_label({"team": "platform"}),
                    ),
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            assert create_data["rules"]["keepRegex"] == [
                "http_requests_total",
                "process_cpu_seconds_total",
            ]
            assert create_data["rules"]["addLabel"] == {"team": "platform"}
            assert create_data["uuid"]
            assert create_data["created_timestamp"]
            original_timestamp = create_data["created_timestamp"]

            # Get - verify rules
            get_result = get_metrics_pipeline_config.sync_detailed(client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["rules"]["keepRegex"] == [
                "http_requests_total",
                "process_cpu_seconds_total",
            ]
            assert get_data["rules"]["addLabel"] == {"team": "platform"}

            # Update - change keep_regex, add drop_regex, update add_label
            update_result = update_metrics_pipeline_config.sync_detailed(
                client=gc_client,
                body=CreateUpdateMetricsPipelineConfigRequest(
                    rules=RelabelConfig(
                        keep_regex=["http_requests_total", "node_cpu_seconds_total"],
                        drop_regex=["go_.*"],
                        add_label=_make_add_label({"team": "platform", "env": "staging"}),
                    ),
                ),
            )
            assert update_result.status_code == 200
            update_data = json.loads(update_result.content)
            assert update_data["rules"]["keepRegex"] == [
                "http_requests_total",
                "node_cpu_seconds_total",
            ]
            assert update_data["rules"]["dropRegex"] == ["go_.*"]
            assert update_data["rules"]["addLabel"] == {"team": "platform", "env": "staging"}
            assert update_data["created_timestamp"] > original_timestamp

            # Get - verify updated rules
            get_result = get_metrics_pipeline_config.sync_detailed(client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["rules"]["dropRegex"] == ["go_.*"]

        finally:
            # Delete
            delete_metrics_pipeline_config.sync_detailed(client=gc_client)

        # Verify deletion - should return nil/no rules
        get_result = get_metrics_pipeline_config.sync_detailed(client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data.get("rules") is None
