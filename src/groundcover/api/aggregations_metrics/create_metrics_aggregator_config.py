from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_update_metrics_aggregator_config_request import CreateUpdateMetricsAggregatorConfigRequest
from ...models.error_response import ErrorResponse
from ...models.metrics_aggregator_config import MetricsAggregatorConfig
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateUpdateMetricsAggregatorConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/aggregations/v1/metrics/config",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | MetricsAggregatorConfig | None:
    if response.status_code == 201:
        response_201 = MetricsAggregatorConfig.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | MetricsAggregatorConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUpdateMetricsAggregatorConfigRequest,
) -> Response[ErrorResponse | MetricsAggregatorConfig]:
    """
    Args:
        body (CreateUpdateMetricsAggregatorConfigRequest):
            CreateOrUpdateMetricsAggregatorConfigRequest defines the request structure for creating or
            updating a metrics aggregator configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MetricsAggregatorConfig]
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
    body: CreateUpdateMetricsAggregatorConfigRequest,
) -> ErrorResponse | MetricsAggregatorConfig | None:
    """
    Args:
        body (CreateUpdateMetricsAggregatorConfigRequest):
            CreateOrUpdateMetricsAggregatorConfigRequest defines the request structure for creating or
            updating a metrics aggregator configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MetricsAggregatorConfig
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUpdateMetricsAggregatorConfigRequest,
) -> Response[ErrorResponse | MetricsAggregatorConfig]:
    """
    Args:
        body (CreateUpdateMetricsAggregatorConfigRequest):
            CreateOrUpdateMetricsAggregatorConfigRequest defines the request structure for creating or
            updating a metrics aggregator configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MetricsAggregatorConfig]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateUpdateMetricsAggregatorConfigRequest,
) -> ErrorResponse | MetricsAggregatorConfig | None:
    """
    Args:
        body (CreateUpdateMetricsAggregatorConfigRequest):
            CreateOrUpdateMetricsAggregatorConfigRequest defines the request structure for creating or
            updating a metrics aggregator configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MetricsAggregatorConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
