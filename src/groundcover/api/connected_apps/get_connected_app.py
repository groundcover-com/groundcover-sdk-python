from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.connected_app_response import ConnectedAppResponse
from ...models.get_connected_app_response_404 import GetConnectedAppResponse404
from ...models.get_connected_app_response_500 import GetConnectedAppResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/connected-apps/v1/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500 | None:
    if response.status_code == 200:
        response_200 = ConnectedAppResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 404:
        response_404 = GetConnectedAppResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = GetConnectedAppResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500]:
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
) -> Response[ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500]:
    """Get Connected App

     Retrieves a single connected app by ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500 | None:
    """Get Connected App

     Retrieves a single connected app by ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500]:
    """Get Connected App

     Retrieves a single connected app by ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500 | None:
    """Get Connected App

     Retrieves a single connected app by ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppResponse | GetConnectedAppResponse404 | GetConnectedAppResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
