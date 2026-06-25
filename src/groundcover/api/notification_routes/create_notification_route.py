from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_notification_route_request import CreateNotificationRouteRequest
from ...models.create_notification_route_response import CreateNotificationRouteResponse
from ...models.create_notification_route_response_400 import CreateNotificationRouteResponse400
from ...models.create_notification_route_response_409 import CreateNotificationRouteResponse409
from ...models.create_notification_route_response_500 import CreateNotificationRouteResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateNotificationRouteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/notification-routes/v1",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateNotificationRouteResponse
    | CreateNotificationRouteResponse400
    | CreateNotificationRouteResponse409
    | CreateNotificationRouteResponse500
    | None
):
    if response.status_code == 201:
        response_201 = CreateNotificationRouteResponse.from_dict(response.json()) if response.content else None

        return response_201

    if response.status_code == 400:
        response_400 = CreateNotificationRouteResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 409:
        response_409 = CreateNotificationRouteResponse409.from_dict(response.json()) if response.content else None

        return response_409

    if response.status_code == 500:
        response_500 = CreateNotificationRouteResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateNotificationRouteResponse
    | CreateNotificationRouteResponse400
    | CreateNotificationRouteResponse409
    | CreateNotificationRouteResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNotificationRouteRequest,
) -> Response[
    CreateNotificationRouteResponse
    | CreateNotificationRouteResponse400
    | CreateNotificationRouteResponse409
    | CreateNotificationRouteResponse500
]:
    """Create Notification Route

     Creates a new notification route.

    Args:
        body (CreateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNotificationRouteResponse | CreateNotificationRouteResponse400 | CreateNotificationRouteResponse409 | CreateNotificationRouteResponse500]
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
    body: CreateNotificationRouteRequest,
) -> (
    CreateNotificationRouteResponse
    | CreateNotificationRouteResponse400
    | CreateNotificationRouteResponse409
    | CreateNotificationRouteResponse500
    | None
):
    """Create Notification Route

     Creates a new notification route.

    Args:
        body (CreateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNotificationRouteResponse | CreateNotificationRouteResponse400 | CreateNotificationRouteResponse409 | CreateNotificationRouteResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNotificationRouteRequest,
) -> Response[
    CreateNotificationRouteResponse
    | CreateNotificationRouteResponse400
    | CreateNotificationRouteResponse409
    | CreateNotificationRouteResponse500
]:
    """Create Notification Route

     Creates a new notification route.

    Args:
        body (CreateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNotificationRouteResponse | CreateNotificationRouteResponse400 | CreateNotificationRouteResponse409 | CreateNotificationRouteResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNotificationRouteRequest,
) -> (
    CreateNotificationRouteResponse
    | CreateNotificationRouteResponse400
    | CreateNotificationRouteResponse409
    | CreateNotificationRouteResponse500
    | None
):
    """Create Notification Route

     Creates a new notification route.

    Args:
        body (CreateNotificationRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNotificationRouteResponse | CreateNotificationRouteResponse400 | CreateNotificationRouteResponse409 | CreateNotificationRouteResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
