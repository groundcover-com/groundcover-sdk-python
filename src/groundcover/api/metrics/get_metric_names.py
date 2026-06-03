from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_metric_names_response_400 import GetMetricNamesResponse400
from ...models.get_metric_names_response_500 import GetMetricNamesResponse500
from ...models.metrics_names_request import MetricsNamesRequest
from ...models.metrics_names_response import MetricsNamesResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: MetricsNamesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/metrics/names",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse | None:
    if response.status_code == 200:
        response_200 = MetricsNamesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetMetricNamesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetMetricNamesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsNamesRequest,
) -> Response[GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse]:
    """GetNames retrieves metric names based on the provided request parameters.

    Args:
        body (MetricsNamesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse]
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
    body: MetricsNamesRequest,
) -> GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse | None:
    """GetNames retrieves metric names based on the provided request parameters.

    Args:
        body (MetricsNamesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsNamesRequest,
) -> Response[GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse]:
    """GetNames retrieves metric names based on the provided request parameters.

    Args:
        body (MetricsNamesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsNamesRequest,
) -> GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse | None:
    """GetNames retrieves metric names based on the provided request parameters.

    Args:
        body (MetricsNamesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetricNamesResponse400 | GetMetricNamesResponse500 | MetricsNamesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
