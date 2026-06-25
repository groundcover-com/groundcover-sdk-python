from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app import (
    CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp,
)
from ...models.create_connected_app_response import CreateConnectedAppResponse
from ...models.create_connected_app_response_400 import CreateConnectedAppResponse400
from ...models.create_connected_app_response_409 import CreateConnectedAppResponse409
from ...models.create_connected_app_response_500 import CreateConnectedAppResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/connected-apps/v1",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateConnectedAppResponse
    | CreateConnectedAppResponse400
    | CreateConnectedAppResponse409
    | CreateConnectedAppResponse500
    | None
):
    if response.status_code == 201:
        response_201 = CreateConnectedAppResponse.from_dict(response.json()) if response.content else None

        return response_201

    if response.status_code == 400:
        response_400 = CreateConnectedAppResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 409:
        response_409 = CreateConnectedAppResponse409.from_dict(response.json()) if response.content else None

        return response_409

    if response.status_code == 500:
        response_500 = CreateConnectedAppResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateConnectedAppResponse
    | CreateConnectedAppResponse400
    | CreateConnectedAppResponse409
    | CreateConnectedAppResponse500
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
    body: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp,
) -> Response[
    CreateConnectedAppResponse
    | CreateConnectedAppResponse400
    | CreateConnectedAppResponse409
    | CreateConnectedAppResponse500
]:
    """Create Connected App

     Creates a new connected app for notifications.

    Args:
        body (CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConnectedAppResponse | CreateConnectedAppResponse400 | CreateConnectedAppResponse409 | CreateConnectedAppResponse500]
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
    body: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp,
) -> (
    CreateConnectedAppResponse
    | CreateConnectedAppResponse400
    | CreateConnectedAppResponse409
    | CreateConnectedAppResponse500
    | None
):
    """Create Connected App

     Creates a new connected app for notifications.

    Args:
        body (CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConnectedAppResponse | CreateConnectedAppResponse400 | CreateConnectedAppResponse409 | CreateConnectedAppResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp,
) -> Response[
    CreateConnectedAppResponse
    | CreateConnectedAppResponse400
    | CreateConnectedAppResponse409
    | CreateConnectedAppResponse500
]:
    """Create Connected App

     Creates a new connected app for notifications.

    Args:
        body (CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConnectedAppResponse | CreateConnectedAppResponse400 | CreateConnectedAppResponse409 | CreateConnectedAppResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp,
) -> (
    CreateConnectedAppResponse
    | CreateConnectedAppResponse400
    | CreateConnectedAppResponse409
    | CreateConnectedAppResponse500
    | None
):
    """Create Connected App

     Creates a new connected app for notifications.

    Args:
        body (CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConnectedAppResponse | CreateConnectedAppResponse400 | CreateConnectedAppResponse409 | CreateConnectedAppResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
