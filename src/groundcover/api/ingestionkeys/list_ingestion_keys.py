from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.ingestion_key_result import IngestionKeyResult
from ...models.list_ingestion_keys_request import ListIngestionKeysRequest
from ...models.list_ingestion_keys_response_400 import ListIngestionKeysResponse400
from ...models.list_ingestion_keys_response_500 import ListIngestionKeysResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: ListIngestionKeysRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rbac/ingestion-keys/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json() if response.content else None
        if _response_200 is None:
            _response_200 = []
        for response_200_item_data in _response_200:
            response_200_item = IngestionKeyResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ListIngestionKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ListIngestionKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListIngestionKeysRequest,
) -> Response[ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]]:
    """List Ingestion Keys

    Args:
        body (ListIngestionKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]]
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
    body: ListIngestionKeysRequest,
) -> ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult] | None:
    """List Ingestion Keys

    Args:
        body (ListIngestionKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListIngestionKeysRequest,
) -> Response[ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]]:
    """List Ingestion Keys

    Args:
        body (ListIngestionKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListIngestionKeysRequest,
) -> ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult] | None:
    """List Ingestion Keys

    Args:
        body (ListIngestionKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListIngestionKeysResponse400 | ListIngestionKeysResponse500 | list[IngestionKeyResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
