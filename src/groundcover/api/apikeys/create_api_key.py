from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_api_key_request import CreateApiKeyRequest
from ...models.create_api_key_response import CreateApiKeyResponse
from ...models.create_api_key_response_400 import CreateApiKeyResponse400
from ...models.create_api_key_response_409 import CreateApiKeyResponse409
from ...models.create_api_key_response_500 import CreateApiKeyResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateApiKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rbac/apikey/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = CreateApiKeyResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = CreateApiKeyResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 409:
        response_409 = CreateApiKeyResponse409.from_dict(response.json()) if response.content else None

        return response_409

    if response.status_code == 500:
        response_500 = CreateApiKeyResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateApiKeyRequest,
) -> Response[CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500]:
    """Create API Key

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500]
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
    body: CreateApiKeyRequest,
) -> CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500 | None:
    """Create API Key

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateApiKeyRequest,
) -> Response[CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500]:
    """Create API Key

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateApiKeyRequest,
) -> CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500 | None:
    """Create API Key

    Args:
        body (CreateApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateApiKeyResponse | CreateApiKeyResponse400 | CreateApiKeyResponse409 | CreateApiKeyResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
