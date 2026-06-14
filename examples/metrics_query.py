"""Metrics query examples — instant and range queries."""

from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.metrics import metrics_query
from groundcover.models.query_request import QueryRequest
from groundcover.models.query_request_query_type import QueryRequestQueryType


def main() -> None:
    with groundcover.Client() as client:
        now = datetime.now(timezone.utc)

        # Range query
        range_result = metrics_query.sync_detailed(
            client=client,
            body=QueryRequest(
                start=now - timedelta(minutes=30),
                end=now,
                step="1m",
                query_type=QueryRequestQueryType.RANGE,
                promql="avg(groundcover_container_cpu_limit_m_cpu)",
            ),
        )
        range_data = range_result.parsed
        print(f"Range query status: {range_data['status']}")

        # Instant query
        instant_result = metrics_query.sync_detailed(
            client=client,
            body=QueryRequest(
                start=now,
                end=now,
                query_type=QueryRequestQueryType.INSTANT,
                promql="up",
            ),
        )
        instant_data = instant_result.parsed
        print(f"Instant query status: {instant_data['status']}")


if __name__ == "__main__":
    main()
