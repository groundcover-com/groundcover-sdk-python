from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_service_account_request import CreateServiceAccountRequest
from ...models.create_service_account_response_400 import CreateServiceAccountResponse400
from ...models.create_service_account_response_409 import CreateServiceAccountResponse409
from ...models.create_service_account_response_500 import CreateServiceAccountResponse500
from ...models.service_account_create_payload import ServiceAccountCreatePayload
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateServiceAccountRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rbac/service-account/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateServiceAccountResponse400
    | CreateServiceAccountResponse409
    | CreateServiceAccountResponse500
    | ServiceAccountCreatePayload
    | None
):
    if response.status_code == 200:
        response_200 = ServiceAccountCreatePayload.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateServiceAccountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = CreateServiceAccountResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = CreateServiceAccountResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateServiceAccountResponse400
    | CreateServiceAccountResponse409
    | CreateServiceAccountResponse500
    | ServiceAccountCreatePayload
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
    body: CreateServiceAccountRequest,
) -> Response[
    CreateServiceAccountResponse400
    | CreateServiceAccountResponse409
    | CreateServiceAccountResponse500
    | ServiceAccountCreatePayload
]:
    """Create Service Account

    Args:
        body (CreateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServiceAccountResponse400 | CreateServiceAccountResponse409 | CreateServiceAccountResponse500 | ServiceAccountCreatePayload]
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
    body: CreateServiceAccountRequest,
) -> (
    CreateServiceAccountResponse400
    | CreateServiceAccountResponse409
    | CreateServiceAccountResponse500
    | ServiceAccountCreatePayload
    | None
):
    """Create Service Account

    Args:
        body (CreateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServiceAccountResponse400 | CreateServiceAccountResponse409 | CreateServiceAccountResponse500 | ServiceAccountCreatePayload
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccountRequest,
) -> Response[
    CreateServiceAccountResponse400
    | CreateServiceAccountResponse409
    | CreateServiceAccountResponse500
    | ServiceAccountCreatePayload
]:
    """Create Service Account

    Args:
        body (CreateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServiceAccountResponse400 | CreateServiceAccountResponse409 | CreateServiceAccountResponse500 | ServiceAccountCreatePayload]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccountRequest,
) -> (
    CreateServiceAccountResponse400
    | CreateServiceAccountResponse409
    | CreateServiceAccountResponse500
    | ServiceAccountCreatePayload
    | None
):
    """Create Service Account

    Args:
        body (CreateServiceAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServiceAccountResponse400 | CreateServiceAccountResponse409 | CreateServiceAccountResponse500 | ServiceAccountCreatePayload
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
