from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.connected_app_response import ConnectedAppResponse
from ...models.update_connected_app_request_is_the_request_body_for_updating_an_existing_connected_app import (
    UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp,
)
from ...models.update_connected_app_response_400 import UpdateConnectedAppResponse400
from ...models.update_connected_app_response_404 import UpdateConnectedAppResponse404
from ...models.update_connected_app_response_500 import UpdateConnectedAppResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/connected-apps/v1/{id}".format(
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
    ConnectedAppResponse
    | UpdateConnectedAppResponse400
    | UpdateConnectedAppResponse404
    | UpdateConnectedAppResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ConnectedAppResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateConnectedAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = UpdateConnectedAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateConnectedAppResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500
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
    body: UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp,
) -> Response[
    ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500
]:
    """Update Connected App

     Replaces an existing connected app.

    Args:
        id (str):
        body (UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500]
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
    body: UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp,
) -> (
    ConnectedAppResponse
    | UpdateConnectedAppResponse400
    | UpdateConnectedAppResponse404
    | UpdateConnectedAppResponse500
    | None
):
    """Update Connected App

     Replaces an existing connected app.

    Args:
        id (str):
        body (UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500
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
    body: UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp,
) -> Response[
    ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500
]:
    """Update Connected App

     Replaces an existing connected app.

    Args:
        id (str):
        body (UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500]
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
    body: UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp,
) -> (
    ConnectedAppResponse
    | UpdateConnectedAppResponse400
    | UpdateConnectedAppResponse404
    | UpdateConnectedAppResponse500
    | None
):
    """Update Connected App

     Replaces an existing connected app.

    Args:
        id (str):
        body (UpdateConnectedAppRequestIsTheRequestBodyForUpdatingAnExistingConnectedApp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppResponse | UpdateConnectedAppResponse400 | UpdateConnectedAppResponse404 | UpdateConnectedAppResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
