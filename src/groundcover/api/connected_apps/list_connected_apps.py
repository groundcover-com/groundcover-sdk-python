from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_connected_apps_request import ListConnectedAppsRequest
from ...models.list_connected_apps_response import ListConnectedAppsResponse
from ...models.list_connected_apps_response_400 import ListConnectedAppsResponse400
from ...models.list_connected_apps_response_500 import ListConnectedAppsResponse500
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ListConnectedAppsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/connected-apps/v1/list",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500 | None:
    if response.status_code == 200:
        response_200 = ListConnectedAppsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListConnectedAppsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ListConnectedAppsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListConnectedAppsRequest | Unset = UNSET,
) -> Response[ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500]:
    """List Connected Apps

     Returns a list of connected apps filtered by the gcQL query.
    Supports freetext search on name, type:<type>, and notification_route:<route-name>.

    Args:
        body (ListConnectedAppsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500]
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
    body: ListConnectedAppsRequest | Unset = UNSET,
) -> ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500 | None:
    """List Connected Apps

     Returns a list of connected apps filtered by the gcQL query.
    Supports freetext search on name, type:<type>, and notification_route:<route-name>.

    Args:
        body (ListConnectedAppsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListConnectedAppsRequest | Unset = UNSET,
) -> Response[ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500]:
    """List Connected Apps

     Returns a list of connected apps filtered by the gcQL query.
    Supports freetext search on name, type:<type>, and notification_route:<route-name>.

    Args:
        body (ListConnectedAppsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListConnectedAppsRequest | Unset = UNSET,
) -> ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500 | None:
    """List Connected Apps

     Returns a list of connected apps filtered by the gcQL query.
    Supports freetext search on name, type:<type>, and notification_route:<route-name>.

    Args:
        body (ListConnectedAppsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListConnectedAppsResponse | ListConnectedAppsResponse400 | ListConnectedAppsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
