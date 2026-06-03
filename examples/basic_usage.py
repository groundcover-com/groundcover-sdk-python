"""Basic usage of the groundcover Python SDK.

Requires environment variables:
  GC_API_KEY - Your groundcover API key
  GC_BACKEND_ID - Your groundcover Backend ID
  GC_BASE_URL - Optional, defaults to https://api.groundcover.com
"""

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.metrics import metrics_query
from groundcover.models.query_request import QueryRequest
from groundcover.models.query_request_query_type import QueryRequestQueryType


def main() -> None:
    # Client reads from GC_API_KEY, GC_BACKEND_ID, GC_BASE_URL env vars
    with groundcover.Client() as client:
        # Simple metrics range query using the generated typed API
        now = datetime.now(timezone.utc)
        start = now - timedelta(minutes=15)

        result = metrics_query.sync_detailed(
            client=client,
            body=QueryRequest(
                start=start,
                end=now,
                step="1m",
                query_type=QueryRequestQueryType.RANGE,
                promql="up",
            ),
        )

        payload = result.parsed
        print(f"Query status: {payload['status']}")
        print(f"Result type: {payload['data']['resultType']}")


if __name__ == "__main__":
    main()
