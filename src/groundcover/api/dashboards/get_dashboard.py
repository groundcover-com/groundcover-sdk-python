from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_dashboard_response_400 import GetDashboardResponse400
from ...models.get_dashboard_response_404 import GetDashboardResponse404
from ...models.get_dashboard_response_500 import GetDashboardResponse500
from ...models.view import View
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    exclude_preset: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["excludePreset"] = exclude_preset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dashboards/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View | None:
    if response.status_code == 200:
        response_200 = View.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = GetDashboardResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = GetDashboardResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = GetDashboardResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_preset: bool | Unset = UNSET,
) -> Response[GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View]:
    """Get Dashboard by ID

    Args:
        id (str):
        exclude_preset (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View]
    """

    kwargs = _get_kwargs(
        id=id,
        exclude_preset=exclude_preset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_preset: bool | Unset = UNSET,
) -> GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View | None:
    """Get Dashboard by ID

    Args:
        id (str):
        exclude_preset (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View
    """

    return sync_detailed(
        id=id,
        client=client,
        exclude_preset=exclude_preset,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_preset: bool | Unset = UNSET,
) -> Response[GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View]:
    """Get Dashboard by ID

    Args:
        id (str):
        exclude_preset (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View]
    """

    kwargs = _get_kwargs(
        id=id,
        exclude_preset=exclude_preset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_preset: bool | Unset = UNSET,
) -> GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View | None:
    """Get Dashboard by ID

    Args:
        id (str):
        exclude_preset (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDashboardResponse400 | GetDashboardResponse404 | GetDashboardResponse500 | View
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            exclude_preset=exclude_preset,
        )
    ).parsed
