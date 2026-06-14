"""Monitor CRUD lifecycle with YAML content-type handling.

Monitors use YAML content-type, so these operations use the Client helper methods.
"""

import random

import groundcover
from groundcover.api.monitors import delete_monitor

MONITOR_YAML = """
title: "Python SDK Example Monitor - {suffix}"
display:
  header: "CPU Alert"
  resourceHeaderLabels:
    - namespace
    - workload
  contextHeaderLabels:
    - cluster
  description: Pod CPU usage exceeded threshold
severity: warning
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
  severity: warning
executionErrorState: OK
noDataState: OK
evaluationInterval:
  interval: 1m
  pendingFor: 5m
"""


def main() -> None:
    with groundcover.Client() as client:
        suffix = random.randint(0, 10_000_000)
        yaml_body = MONITOR_YAML.format(suffix=suffix)

        # Create monitor (client helper — YAML content-type)
        create_resp = client.create_monitor(yaml_body)
        monitor_id = create_resp.json()["monitorId"]
        print(f"Created monitor: {monitor_id}")

        # Get monitor (client helper — returns parsed YAML)
        monitor = client.get_monitor(monitor_id)
        print(f"Monitor title: {monitor['title']}")
        print(f"Monitor severity: {monitor['severity']}")

        # Update monitor (client helper — change severity)
        updated_yaml = yaml_body.replace("severity: warning", "severity: critical", 1)
        client.update_monitor(monitor_id, updated_yaml)
        print("Updated monitor severity to critical")

        # Verify update
        updated = client.get_monitor(monitor_id)
        print(f"Updated severity: {updated['severity']}")

        # Delete (generated typed API)
        delete_monitor.sync_detailed(monitor_id, client=client)
        print(f"Deleted monitor: {monitor_id}")


if __name__ == "__main__":
    main()
