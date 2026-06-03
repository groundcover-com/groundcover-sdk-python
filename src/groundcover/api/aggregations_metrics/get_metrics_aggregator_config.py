from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_metrics_aggregator_config_response_204 import GetMetricsAggregatorConfigResponse204
from ...models.metrics_aggregator_config import MetricsAggregatorConfig
from ..._generated_types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/aggregations/v1/metrics/config",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig | None:
    if response.status_code == 200:
        response_200 = MetricsAggregatorConfig.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = GetMetricsAggregatorConfigResponse204.from_dict(response.json())

        return response_204

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig | None:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig | None:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetMetricsAggregatorConfigResponse204 | MetricsAggregatorConfig
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
