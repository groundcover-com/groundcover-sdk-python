from __future__ import annotations

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.delete_ingestion_key_request import DeleteIngestionKeyRequest
from ...models.delete_ingestion_key_response_400 import DeleteIngestionKeyResponse400
from ...models.delete_ingestion_key_response_404 import DeleteIngestionKeyResponse404
from ...models.delete_ingestion_key_response_500 import DeleteIngestionKeyResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: DeleteIngestionKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/rbac/ingestion-keys/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500 | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = DeleteIngestionKeyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = DeleteIngestionKeyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteIngestionKeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteIngestionKeyRequest,
) -> Response[Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500]:
    """Delete Ingestion Key

    Args:
        body (DeleteIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500]
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
    body: DeleteIngestionKeyRequest,
) -> Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500 | None:
    """Delete Ingestion Key

    Args:
        body (DeleteIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteIngestionKeyRequest,
) -> Response[Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500]:
    """Delete Ingestion Key

    Args:
        body (DeleteIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteIngestionKeyRequest,
) -> Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500 | None:
    """Delete Ingestion Key

    Args:
        body (DeleteIngestionKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteIngestionKeyResponse400 | DeleteIngestionKeyResponse404 | DeleteIngestionKeyResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
