from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.metrics_query_response_400 import MetricsQueryResponse400
from ...models.metrics_query_response_500 import MetricsQueryResponse500
from ...models.query_request import QueryRequest
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: QueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/metrics/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MetricsQueryResponse400 | MetricsQueryResponse500 | None:
    if response.status_code == 200:
        response_200 = response.json() if response.content else None
        return response_200

    if response.status_code == 400:
        response_400 = MetricsQueryResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = MetricsQueryResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MetricsQueryResponse400 | MetricsQueryResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryRequest,
) -> Response[Any | MetricsQueryResponse400 | MetricsQueryResponse500]:
    """Execute Prometheus query.

     Executes a Prometheus query (instant or range) against the metrics server.
    Accepts either a direct 'promql' string or components ('pipeline', 'filters', 'conditions',
    'subPipelines') to build the query.

    Args:
        body (QueryRequest): QueryRequest represents a request to query metrics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetricsQueryResponse400 | MetricsQueryResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QueryRequest,
) -> Any | MetricsQueryResponse400 | MetricsQueryResponse500 | None:
    """Execute Prometheus query.

     Executes a Prometheus query (instant or range) against the metrics server.
    Accepts either a direct 'promql' string or components ('pipeline', 'filters', 'conditions',
    'subPipelines') to build the query.

    Args:
        body (QueryRequest): QueryRequest represents a request to query metrics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetricsQueryResponse400 | MetricsQueryResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryRequest,
) -> Response[Any | MetricsQueryResponse400 | MetricsQueryResponse500]:
    """Execute Prometheus query.

     Executes a Prometheus query (instant or range) against the metrics server.
    Accepts either a direct 'promql' string or components ('pipeline', 'filters', 'conditions',
    'subPipelines') to build the query.

    Args:
        body (QueryRequest): QueryRequest represents a request to query metrics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetricsQueryResponse400 | MetricsQueryResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QueryRequest,
) -> Any | MetricsQueryResponse400 | MetricsQueryResponse500 | None:
    """Execute Prometheus query.

     Executes a Prometheus query (instant or range) against the metrics server.
    Accepts either a direct 'promql' string or components ('pipeline', 'filters', 'conditions',
    'subPipelines') to build the query.

    Args:
        body (QueryRequest): QueryRequest represents a request to query metrics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetricsQueryResponse400 | MetricsQueryResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
