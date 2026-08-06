"""E2E tests for monitors endpoints. Mirrors sdk/tests/e2e/monitors_test.go."""

from __future__ import annotations

import pytest

import groundcover
from groundcover.api.monitors import delete_monitor
from groundcover.exceptions import ConflictError

from ._cleanup import ResourceTracker

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

    def test_monitor_crud(self, gc_client: groundcover.Client, tracker: ResourceTracker) -> None:
        monitor = tracker.new("monitor")
        title = monitor.name
        header = f"{monitor.name}-header"

        monitor_yaml = MONITOR_YAML_TEMPLATE.format(title=title, header=header)

        # Create monitor (hand-written helper — YAML content-type)
        create_resp = gc_client.create_monitor(monitor_yaml)
        assert create_resp.status_code == 200
        create_payload = create_resp.json()
        monitor.resource_id = create_payload["monitorId"]
        monitor_id = monitor.resource_id

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

        # Test duplicate creation (should fail with 409). Tracked under the same
        # title so that if it unexpectedly succeeds, the extra monitor is still
        # cleaned up rather than orphaned -- the create response is discarded here,
        # so the tracker has to recover it by name.
        duplicate = tracker.new("monitor", name=title)
        with pytest.raises(ConflictError):
            gc_client.create_monitor(monitor_yaml)
        # A 409 means nothing was created, so stop tracking it. Left registered, the
        # handle never gets an id and teardown pages the entire monitor list looking
        # for a resource that by construction does not exist. If the create instead
        # succeeds, pytest.raises fails first and this line never runs, so the
        # unexpected-success case is still cleaned up.
        tracker.forget(duplicate)

        # Delete monitor (generated typed API)
        delete_monitor.sync_detailed(monitor_id, client=gc_client)
        tracker.forget(monitor)
