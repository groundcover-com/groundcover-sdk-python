from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.update_service_account_request import UpdateServiceAccountRequest
from ...models.update_service_account_response import UpdateServiceAccountResponse
from ...models.update_service_account_response_400 import UpdateServiceAccountResponse400
from ...models.update_service_account_response_404 import UpdateServiceAccountResponse404
from ...models.update_service_account_response_500 import UpdateServiceAccountResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: UpdateServiceAccountRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/rbac/service-account/update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateServiceAccountResponse
    | UpdateServiceAccountResponse400
    | UpdateServiceAccountResponse404
    | UpdateServiceAccountResponse500
    | None
):
    if response.status_code == 200:
        response_200 = UpdateServiceAccountResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateServiceAccountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = UpdateServiceAccountResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateServiceAccountResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateServiceAccountResponse
    | UpdateServiceAccountResponse400
    | UpdateServiceAccountResponse404
    | UpdateServiceAccountResponse500
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
    body: UpdateServiceAccountRequest,
) -> Response[
    UpdateServiceAccountResponse
    | UpdateServiceAccountResponse400
    | UpdateServiceAccountResponse404
    | UpdateServiceAccountResponse500
]:
    """Update Service Account

    Args:
        body (UpdateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateServiceAccountResponse | UpdateServiceAccountResponse400 | UpdateServiceAccountResponse404 | UpdateServiceAccountResponse500]
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
    body: UpdateServiceAccountRequest,
) -> (
    UpdateServiceAccountResponse
    | UpdateServiceAccountResponse400
    | UpdateServiceAccountResponse404
    | UpdateServiceAccountResponse500
    | None
):
    """Update Service Account

    Args:
        body (UpdateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateServiceAccountResponse | UpdateServiceAccountResponse400 | UpdateServiceAccountResponse404 | UpdateServiceAccountResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateServiceAccountRequest,
) -> Response[
    UpdateServiceAccountResponse
    | UpdateServiceAccountResponse400
    | UpdateServiceAccountResponse404
    | UpdateServiceAccountResponse500
]:
    """Update Service Account

    Args:
        body (UpdateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateServiceAccountResponse | UpdateServiceAccountResponse400 | UpdateServiceAccountResponse404 | UpdateServiceAccountResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateServiceAccountRequest,
) -> (
    UpdateServiceAccountResponse
    | UpdateServiceAccountResponse400
    | UpdateServiceAccountResponse404
    | UpdateServiceAccountResponse500
    | None
):
    """Update Service Account

    Args:
        body (UpdateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateServiceAccountResponse | UpdateServiceAccountResponse400 | UpdateServiceAccountResponse404 | UpdateServiceAccountResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
