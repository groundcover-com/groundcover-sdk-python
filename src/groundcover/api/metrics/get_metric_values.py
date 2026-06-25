from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_metric_values_response_400 import GetMetricValuesResponse400
from ...models.get_metric_values_response_500 import GetMetricValuesResponse500
from ...models.metrics_values_request import MetricsValuesRequest
from ...models.metrics_values_response import MetricsValuesResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: MetricsValuesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/metrics/values",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse | None:
    if response.status_code == 200:
        response_200 = MetricsValuesResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = GetMetricValuesResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = GetMetricValuesResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsValuesRequest,
) -> Response[GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse]:
    """GetMetricValues retrieves metric values based on the provided request parameters.

    Args:
        body (MetricsValuesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse]
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
    body: MetricsValuesRequest,
) -> GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse | None:
    """GetMetricValues retrieves metric values based on the provided request parameters.

    Args:
        body (MetricsValuesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsValuesRequest,
) -> Response[GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse]:
    """GetMetricValues retrieves metric values based on the provided request parameters.

    Args:
        body (MetricsValuesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsValuesRequest,
) -> GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse | None:
    """GetMetricValues retrieves metric values based on the provided request parameters.

    Args:
        body (MetricsValuesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetricValuesResponse400 | GetMetricValuesResponse500 | MetricsValuesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
