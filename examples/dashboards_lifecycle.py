"""Dashboard full CRUD lifecycle example."""

import json
import uuid

import groundcover
from groundcover.api.dashboards import (
    archive_dashboard,
    create_dashboard,
    delete_dashboard,
    get_dashboards,
    restore_dashboard,
)
from groundcover.models.create_dashboard_request import CreateDashboardRequest


def main() -> None:
    with groundcover.Client() as client:
        # Create
        dashboard_name = f"python-sdk-example-{uuid.uuid4()}"
        preset = json.dumps(
            {
                "duration": "Last 30 minutes",
                "layout": [{"id": "A", "x": 0, "y": 0, "w": 4, "h": 3, "minH": 2}],
                "widgets": [
                    {
                        "id": "A",
                        "type": "text",
                        "html": "<p>Created by Python SDK</p>",
                    }
                ],
                "variables": {},
                "schemaVersion": 3,
            }
        )

        create_dashboard.sync_detailed(
            client=client,
            body=CreateDashboardRequest(
                name=dashboard_name,
                description="Created by Python SDK example",
                preset=preset,
                is_provisioned=False,
            ),
        )

        # Find in list
        list_result = get_dashboards.sync_detailed(client=client)
        dashboards = json.loads(list_result.content)
        created = next((d for d in dashboards if d["name"] == dashboard_name), None)
        if not created:
            print("Dashboard not found after creation!")
            return

        dashboard_id = created["uuid"]
        print(f"Created dashboard: {dashboard_id}")

        # Archive
        archive_dashboard.sync_detailed(
            dashboard_id,
            client=client,
            current_revision=created["revisionNumber"],
        )
        print(f"Archived dashboard: {dashboard_id}")

        # Restore
        list_result = get_dashboards.sync_detailed(client=client)
        dashboards = json.loads(list_result.content)
        archived = next(d for d in dashboards if d["uuid"] == dashboard_id)
        restore_dashboard.sync_detailed(
            dashboard_id,
            client=client,
            current_revision=archived["revisionNumber"],
        )
        print(f"Restored dashboard: {dashboard_id}")

        # Delete
        delete_dashboard.sync_detailed(dashboard_id, client=client)
        print(f"Deleted dashboard: {dashboard_id}")


if __name__ == "__main__":
    main()
