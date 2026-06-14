"""Logs search example with conditions."""

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.logs import search_logs
from groundcover.models.logs_search_request import LogsSearchRequest


def main() -> None:
    with groundcover.Client() as client:
        now = datetime.now(timezone.utc)

        # Simple log search using generated typed API
        result = search_logs.sync_detailed(
            client=client,
            body=LogsSearchRequest(
                start=now - timedelta(hours=1),
                end=now,
                query="* | stats count(*)",
            ),
        )
        payload = result.parsed or []
        if payload:
            print(f"Log count: {payload[0].get('count', 0)}")

        # Search with namespace filter
        body = LogsSearchRequest(
            start=now - timedelta(hours=1),
            end=now,
            query="* | stats count(*)",
            filters="namespace = 'default'",
        )

        result = search_logs.sync_detailed(client=client, body=body)
        payload = result.parsed or []
        if payload:
            print(f"Filtered log count: {payload[0].get('count', 0)}")


if __name__ == "__main__":
    main()
