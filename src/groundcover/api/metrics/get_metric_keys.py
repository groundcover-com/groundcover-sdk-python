from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_metric_keys_response_400 import GetMetricKeysResponse400
from ...models.get_metric_keys_response_500 import GetMetricKeysResponse500
from ...models.metrics_keys_request import MetricsKeysRequest
from ...models.metrics_keys_response import MetricsKeysResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: MetricsKeysRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/metrics/keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse | None:
    if response.status_code == 200:
        response_200 = MetricsKeysResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetMetricKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetMetricKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsKeysRequest,
) -> Response[GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse]:
    """GetKeys retrieves metric keys based on the provided request parameters.

    Args:
        body (MetricsKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse]
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
    body: MetricsKeysRequest,
) -> GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse | None:
    """GetKeys retrieves metric keys based on the provided request parameters.

    Args:
        body (MetricsKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsKeysRequest,
) -> Response[GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse]:
    """GetKeys retrieves metric keys based on the provided request parameters.

    Args:
        body (MetricsKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MetricsKeysRequest,
) -> GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse | None:
    """GetKeys retrieves metric keys based on the provided request parameters.

    Args:
        body (MetricsKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetricKeysResponse400 | GetMetricKeysResponse500 | MetricsKeysResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
