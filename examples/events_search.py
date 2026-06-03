"""Events search example — OOM event detection."""

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.k8s import events_search
from groundcover.models.events_search_request import EventsSearchRequest
from groundcover.utils import ConditionSet


def main() -> None:
    with groundcover.Client() as client:
        now = datetime.now(timezone.utc)

        # Search for OOM events using generated typed API
        conditions = ConditionSet().add_oom_event_conditions().build()

        # Build the request body — pass conditions via additional_properties
        # since ConditionSet returns plain dicts, not typed model objects
        body = EventsSearchRequest(
            start=now - timedelta(hours=24),
            end=now,
            query="* | stats count(*)",
        )
        body["sources"] = conditions

        result = events_search.sync_detailed(client=client, body=body)
        print(f"OOM events result: status={result.status_code}")


if __name__ == "__main__":
    main()
