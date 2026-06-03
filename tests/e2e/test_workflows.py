"""E2E tests for workflows endpoints. Mirrors sdk/tests/e2e/workflows_test.go."""

from __future__ import annotations

import uuid

import groundcover
from groundcover.api.workflows import delete_workflow, list_workflows


class TestWorkflowsLifecycle:
    """CRUD lifecycle for workflows with text/plain content-type."""

    def test_workflow_crud(self, gc_client: groundcover.Client) -> None:
        workflow_uuid = uuid.uuid4()

        workflow_definition = f"""workflow:
  id: e2e-test-simple-{workflow_uuid}
  description: Simple e2e test workflow
  triggers:
    - type: alert
  actions:
    - name: test-action
      provider:
        type: slack
        config: ' {{{{ providers.slack_test }}}} '
        with:
          message: 'Test message'"""

        # Create workflow (hand-written helper — text/plain content-type)
        create_resp = gc_client.create_workflow(workflow_definition)
        assert create_resp.status_code == 202
        create_payload = create_resp.json()
        workflow_id = create_payload["workflow_id"]
        assert workflow_id, "Workflow ID should not be empty"
        assert create_payload.get("status"), "Workflow status should not be empty"
        assert create_payload.get("revision", 0) > 0, "Workflow revision should be > 0"

        try:
            # List workflows (generated typed API)
            list_result = list_workflows.sync_detailed(client=gc_client)
            assert list_result.status_code == 200
            list_parsed = list_result.parsed
            workflows = getattr(list_parsed, "workflows", None)
            if workflows is None:
                workflows = getattr(list_parsed, "additional_properties", {}).get("workflows", [])

            workflows = workflows or []
            found = None
            for w in workflows:
                w_id = w.get("id") if isinstance(w, dict) else getattr(w, "id", None)
                if w_id == workflow_id:
                    found = w
                    break
            assert found is not None, f"Created workflow {workflow_id} not found in list"
            found_name = found.get("name") if isinstance(found, dict) else getattr(found, "name", "")
            assert "e2e-test-simple" in found_name

        finally:
            # Delete workflow (generated typed API)
            delete_result = delete_workflow.sync_detailed(workflow_id, client=gc_client)
            assert delete_result.status_code == 200

        # Verify deletion
        list_result = list_workflows.sync_detailed(client=gc_client)
        assert list_result.status_code == 200
        list_parsed = list_result.parsed
        workflows = getattr(list_parsed, "workflows", None)
        if workflows is None:
            workflows = getattr(list_parsed, "additional_properties", {}).get("workflows", [])
        workflows = workflows or []
        for w in workflows:
            w_id = w.get("id") if isinstance(w, dict) else getattr(w, "id", None)
            assert w_id != workflow_id, f"Deleted workflow {workflow_id} should not be in list"
