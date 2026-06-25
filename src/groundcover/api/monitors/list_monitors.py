from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_monitors_response_400 import ListMonitorsResponse400
from ...models.list_monitors_response_500 import ListMonitorsResponse500
from ...models.monitor_list_request import MonitorListRequest
from ...models.monitor_list_response import MonitorListResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: MonitorListRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/monitors/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse | None:
    if response.status_code == 200:
        response_200 = MonitorListResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = ListMonitorsResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = ListMonitorsResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MonitorListRequest,
) -> Response[ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse]:
    """List Monitors

    Args:
        body (MonitorListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse]
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
    body: MonitorListRequest,
) -> ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse | None:
    """List Monitors

    Args:
        body (MonitorListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MonitorListRequest,
) -> Response[ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse]:
    """List Monitors

    Args:
        body (MonitorListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MonitorListRequest,
) -> ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse | None:
    """List Monitors

    Args:
        body (MonitorListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMonitorsResponse400 | ListMonitorsResponse500 | MonitorListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
