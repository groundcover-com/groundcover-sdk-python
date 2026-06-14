"""E2E tests for monitors endpoints. Mirrors sdk/tests/e2e/monitors_test.go."""

from __future__ import annotations

import random

import pytest

import groundcover
from groundcover.api.monitors import delete_monitor
from groundcover.exceptions import ConflictError

MONITOR_YAML_TEMPLATE = """
title: "{title}"
display:
  header: "{header}"
  resourceHeaderLabels:
    - namespace
    - workload
  contextHeaderLabels:
    - cluster
  description: Pod has been in a non-running state for longer than 15 minutes
severity: critical
measurementType: state
model:
  queries:
    - dataType: metrics
      name: threshold_input_query
      pipeline:
        function:
          name: avg_over_time
          pipelines:
            - function:
                name: max_by
                pipelines:
                  - metric: groundcover_kube_pod_status_phase
                args:
                  - namespace
                  - workload
                  - cluster
          args:
            - "600"
  thresholds:
    - name: threshold_1
      inputName: threshold_input_query
      operator: gt
      values:
        - 0
labels:
  severity: critical
annotations:
  description: "Pod {{{{ .Labels.namespace }}}}/{{{{ .Labels.pod }}}} not running for 15m"
  summary: Kubernetes Pod not healthy
executionErrorState: OK
noDataState: OK
evaluationInterval:
  interval: 1m
  pendingFor: 0s
"""


class TestMonitorsLifecycle:
    """CRUD lifecycle for monitors with YAML content-type handling."""

    def test_monitor_crud(self, gc_client: groundcover.Client) -> None:
        random_suffix = random.randint(0, 10_000_000)
        title = f"E2E Test - K8s Pod Not Healthy Monitor - {random_suffix}"
        header = f"E2E Test - K8s Pod Not Healthy - {random_suffix}"

        monitor_yaml = MONITOR_YAML_TEMPLATE.format(title=title, header=header)

        # Create monitor (hand-written helper — YAML content-type)
        create_resp = gc_client.create_monitor(monitor_yaml)
        assert create_resp.status_code == 200
        create_payload = create_resp.json()
        monitor_id = create_payload["monitorId"]

        try:
            # Get monitor (hand-written helper — YAML response)
            monitor_data = gc_client.get_monitor(monitor_id)
            assert monitor_data["title"] == title

            # Verify pendingFor is preserved as 0s
            eval_interval = monitor_data.get("evaluationInterval", {})
            assert eval_interval.get("pendingFor") == "0s", (
                f"Expected pendingFor '0s', got '{eval_interval.get('pendingFor')}'"
            )

            # Update monitor (hand-written helper — change severity to warning)
            updated_yaml = monitor_yaml.replace("severity: critical", "severity: warning", 1)
            gc_client.update_monitor(monitor_id, updated_yaml)

            # Verify update
            updated_data = gc_client.get_monitor(monitor_id)
            assert updated_data["severity"] == "warning"
            assert updated_data["title"] == title

            # Test duplicate creation (should fail with 409)
            with pytest.raises(ConflictError):
                gc_client.create_monitor(monitor_yaml)

        finally:
            # Delete monitor (generated typed API)
            delete_monitor.sync_detailed(monitor_id, client=gc_client)
