from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.notification_route_response import NotificationRouteResponse
from ...models.update_notification_route_request import UpdateNotificationRouteRequest
from ...models.update_notification_route_response_400 import UpdateNotificationRouteResponse400
from ...models.update_notification_route_response_404 import UpdateNotificationRouteResponse404
from ...models.update_notification_route_response_500 import UpdateNotificationRouteResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateNotificationRouteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/notification-routes/v1/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    NotificationRouteResponse
    | UpdateNotificationRouteResponse400
    | UpdateNotificationRouteResponse404
    | UpdateNotificationRouteResponse500
    | None
):
    if response.status_code == 200:
        response_200 = NotificationRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateNotificationRouteResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = UpdateNotificationRouteResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateNotificationRouteResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    NotificationRouteResponse
    | UpdateNotificationRouteResponse400
    | UpdateNotificationRouteResponse404
    | UpdateNotificationRouteResponse500
]:
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
    body: UpdateNotificationRouteRequest,
) -> Response[
    NotificationRouteResponse
    | UpdateNotificationRouteResponse400
    | UpdateNotificationRouteResponse404
    | UpdateNotificationRouteResponse500
]:
    """Update Notification Route

     Replaces an existing notification route.

    Args:
        id (str):
        body (UpdateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationRouteResponse | UpdateNotificationRouteResponse400 | UpdateNotificationRouteResponse404 | UpdateNotificationRouteResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateNotificationRouteRequest,
) -> (
    NotificationRouteResponse
    | UpdateNotificationRouteResponse400
    | UpdateNotificationRouteResponse404
    | UpdateNotificationRouteResponse500
    | None
):
    """Update Notification Route

     Replaces an existing notification route.

    Args:
        id (str):
        body (UpdateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationRouteResponse | UpdateNotificationRouteResponse400 | UpdateNotificationRouteResponse404 | UpdateNotificationRouteResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateNotificationRouteRequest,
) -> Response[
    NotificationRouteResponse
    | UpdateNotificationRouteResponse400
    | UpdateNotificationRouteResponse404
    | UpdateNotificationRouteResponse500
]:
    """Update Notification Route

     Replaces an existing notification route.

    Args:
        id (str):
        body (UpdateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationRouteResponse | UpdateNotificationRouteResponse400 | UpdateNotificationRouteResponse404 | UpdateNotificationRouteResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateNotificationRouteRequest,
) -> (
    NotificationRouteResponse
    | UpdateNotificationRouteResponse400
    | UpdateNotificationRouteResponse404
    | UpdateNotificationRouteResponse500
    | None
):
    """Update Notification Route

     Replaces an existing notification route.

    Args:
        id (str):
        body (UpdateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationRouteResponse | UpdateNotificationRouteResponse400 | UpdateNotificationRouteResponse404 | UpdateNotificationRouteResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
