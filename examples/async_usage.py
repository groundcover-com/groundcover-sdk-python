"""Async usage of the groundcover Python SDK."""

import asyncio
from datetime import datetime, timedelta, timezone

import groundcover
from groundcover.api.metrics import metrics_query
from groundcover.models.query_request import QueryRequest
from groundcover.models.query_request_query_type import QueryRequestQueryType


async def main() -> None:
    async with groundcover.AsyncClient() as client:
        now = datetime.now(timezone.utc)
        start = now - timedelta(minutes=15)

        result = await metrics_query.asyncio_detailed(
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


if __name__ == "__main__":
    asyncio.run(main())
