"""E2E tests for dashboards endpoints. Mirrors sdk/tests/e2e/dashboards_test.go."""

from __future__ import annotations

import json
import uuid

import groundcover
from groundcover.api.dashboards import (
    archive_dashboard,
    create_dashboard,
    delete_dashboard,
    get_dashboard,
    get_dashboards,
    restore_dashboard,
    update_dashboard,
)
from groundcover.models.create_dashboard_request import CreateDashboardRequest
from groundcover.models.update_dashboard_request import UpdateDashboardRequest

DASHBOARD_PRESET = json.dumps(
    {
        "duration": "Last 30 minutes",
        "layout": [
            {"id": "A", "x": 0, "y": 0, "w": 4, "h": 3, "minH": 2},
            {"id": "B", "x": 0, "y": 3, "w": 4, "h": 3, "minH": 1},
        ],
        "widgets": [
            {
                "id": "A",
                "type": "widget",
                "name": "avg(groundcover_node_rt_disk_space_used_percent{})",
                "queries": [
                    {
                        "id": "A",
                        "expr": "avg(groundcover_node_rt_disk_space_used_percent{})",
                        "dataType": "metrics",
                        "step": None,
                        "editorMode": "builder",
                    }
                ],
                "visualizationConfig": {"type": "time-series"},
            },
            {"id": "B", "type": "text", "html": "<p>SDK Test Widget</p>"},
        ],
        "variables": {},
        "schemaVersion": 3,
    }
)

UPDATED_PRESET = json.dumps(
    {
        "duration": "Last 1 hour",
        "layout": [
            {"id": "A", "x": 0, "y": 0, "w": 6, "h": 4, "minH": 2},
            {"id": "B", "x": 0, "y": 4, "w": 6, "h": 2, "minH": 1},
        ],
        "widgets": [
            {
                "id": "A",
                "type": "widget",
                "name": "Updated: avg(groundcover_node_rt_disk_space_used_percent{})",
                "queries": [
                    {
                        "id": "A",
                        "expr": "avg(groundcover_node_rt_disk_space_used_percent{})",
                        "dataType": "metrics",
                        "step": None,
                        "editorMode": "builder",
                    }
                ],
                "visualizationConfig": {"type": "time-series"},
            },
            {"id": "B", "type": "text", "html": "<p>Updated SDK Test Widget</p>"},
        ],
        "variables": {},
        "schemaVersion": 3,
    }
)


def _find_dashboard(gc_client: groundcover.Client, dashboard_id: str) -> dict | None:
    """Find a dashboard by ID in the list."""
    result = get_dashboards.sync_detailed(client=gc_client)
    dashboards = json.loads(result.content) if result.content else []
    if isinstance(dashboards, dict):
        dashboards = dashboards.get("dashboards", dashboards.get("items", []))
    for view in dashboards:
        if view.get("uuid") == dashboard_id:
            return view
    return None


class TestDashboardsLifecycle:
    """Full CRUD lifecycle for dashboards."""

    def test_dashboard_crud(self, gc_client: groundcover.Client) -> None:
        dashboard_name = f"e2e-test-dashboard-{uuid.uuid4()}"
        description = "Dashboard created during E2E testing"

        # Create
        create_result = create_dashboard.sync_detailed(
            client=gc_client,
            body=CreateDashboardRequest(
                name=dashboard_name,
                description=description,
                preset=DASHBOARD_PRESET,
                is_provisioned=False,
            ),
        )
        assert create_result.status_code == 201

        # Find in list
        list_result = get_dashboards.sync_detailed(client=gc_client)
        dashboards = json.loads(list_result.content) if list_result.content else []
        if isinstance(dashboards, dict):
            dashboards = dashboards.get("dashboards", dashboards.get("items", []))
        created = None
        for d in dashboards:
            if d.get("name") == dashboard_name:
                created = d
                break
        assert created is not None, "Created dashboard not found in list"
        dashboard_id = created["uuid"]
        assert created["status"] == "active"

        try:
            # Get
            get_result = get_dashboard.sync_detailed(dashboard_id, client=gc_client)
            assert get_result.status_code == 200

            # Update
            updated_name = f"{dashboard_name}-updated"
            update_dashboard.sync_detailed(
                dashboard_id,
                client=gc_client,
                body=UpdateDashboardRequest(
                    name=updated_name,
                    description="Updated dashboard description",
                    preset=UPDATED_PRESET,
                    current_revision=created["revisionNumber"],
                    override=False,
                    is_provisioned=False,
                ),
            )
            updated = _find_dashboard(gc_client, dashboard_id)
            assert updated is not None
            assert updated["name"] == updated_name
            assert updated["revisionNumber"] > created["revisionNumber"]

            # Archive
            archive_dashboard.sync_detailed(
                dashboard_id,
                client=gc_client,
                current_revision=updated["revisionNumber"],
            )
            archived = _find_dashboard(gc_client, dashboard_id)
            assert archived is not None
            assert archived["status"] == "archived"

            # Restore
            restore_dashboard.sync_detailed(
                dashboard_id,
                client=gc_client,
                current_revision=archived["revisionNumber"],
            )
            restored = _find_dashboard(gc_client, dashboard_id)
            assert restored is not None
            assert restored["status"] == "active"

        finally:
            # Delete (cleanup)
            delete_dashboard.sync_detailed(dashboard_id, client=gc_client)

        # Verify deleted
        deleted = _find_dashboard(gc_client, dashboard_id)
        assert deleted is None, "Deleted dashboard should not be in list"
