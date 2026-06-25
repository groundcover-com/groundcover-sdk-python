from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_ingestion_key_request import CreateIngestionKeyRequest
from ...models.create_ingestion_key_response_400 import CreateIngestionKeyResponse400
from ...models.create_ingestion_key_response_409 import CreateIngestionKeyResponse409
from ...models.create_ingestion_key_response_500 import CreateIngestionKeyResponse500
from ...models.ingestion_key_result import IngestionKeyResult
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateIngestionKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rbac/ingestion-keys/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateIngestionKeyResponse400
    | CreateIngestionKeyResponse409
    | CreateIngestionKeyResponse500
    | IngestionKeyResult
    | None
):
    if response.status_code == 201:
        response_201 = IngestionKeyResult.from_dict(response.json()) if response.content else None

        return response_201

    if response.status_code == 400:
        response_400 = CreateIngestionKeyResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 409:
        response_409 = CreateIngestionKeyResponse409.from_dict(response.json()) if response.content else None

        return response_409

    if response.status_code == 500:
        response_500 = CreateIngestionKeyResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult
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
    body: CreateIngestionKeyRequest,
) -> Response[
    CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult
]:
    """Create Ingestion Key

    Args:
        body (CreateIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult]
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
    body: CreateIngestionKeyRequest,
) -> (
    CreateIngestionKeyResponse400
    | CreateIngestionKeyResponse409
    | CreateIngestionKeyResponse500
    | IngestionKeyResult
    | None
):
    """Create Ingestion Key

    Args:
        body (CreateIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateIngestionKeyRequest,
) -> Response[
    CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult
]:
    """Create Ingestion Key

    Args:
        body (CreateIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateIngestionKeyRequest,
) -> (
    CreateIngestionKeyResponse400
    | CreateIngestionKeyResponse409
    | CreateIngestionKeyResponse500
    | IngestionKeyResult
    | None
):
    """Create Ingestion Key

    Args:
        body (CreateIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateIngestionKeyResponse400 | CreateIngestionKeyResponse409 | CreateIngestionKeyResponse500 | IngestionKeyResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
