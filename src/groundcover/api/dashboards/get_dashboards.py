from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_dashboards_response_400 import GetDashboardsResponse400
from ...models.get_dashboards_response_404 import GetDashboardsResponse404
from ...models.get_dashboards_response_500 import GetDashboardsResponse500
from ...models.view import View
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dashboards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json() if response.content else None
        if _response_200 is None:
            _response_200 = []
        for response_200_item_data in _response_200:
            response_200_item = View.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetDashboardsResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = GetDashboardsResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = GetDashboardsResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
) -> Response[GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]]:
    """Get Dashboards

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]]
    """

    kwargs = _get_kwargs(
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
) -> GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View] | None:
    """Get Dashboards

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]
    """

    return sync_detailed(
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
) -> Response[GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]]:
    """Get Dashboards

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]]
    """

    kwargs = _get_kwargs(
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
) -> GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View] | None:
    """Get Dashboards

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDashboardsResponse400 | GetDashboardsResponse404 | GetDashboardsResponse500 | list[View]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
        )
    ).parsed
