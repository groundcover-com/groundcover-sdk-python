from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_keys_response_400 import GetKeysResponse400
from ...models.get_keys_response_500 import GetKeysResponse500
from ...models.keys_response import KeysResponse
from ...models.search_keys_request import SearchKeysRequest
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: SearchKeysRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/search/keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetKeysResponse400 | GetKeysResponse500 | KeysResponse | None:
    if response.status_code == 200:
        response_200 = KeysResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetKeysResponse400 | GetKeysResponse500 | KeysResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchKeysRequest,
) -> Response[GetKeysResponse400 | GetKeysResponse500 | KeysResponse]:
    """GetKeys retrieves search keys based on the provided request parameters.

    Args:
        body (SearchKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetKeysResponse400 | GetKeysResponse500 | KeysResponse]
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
    body: SearchKeysRequest,
) -> GetKeysResponse400 | GetKeysResponse500 | KeysResponse | None:
    """GetKeys retrieves search keys based on the provided request parameters.

    Args:
        body (SearchKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetKeysResponse400 | GetKeysResponse500 | KeysResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchKeysRequest,
) -> Response[GetKeysResponse400 | GetKeysResponse500 | KeysResponse]:
    """GetKeys retrieves search keys based on the provided request parameters.

    Args:
        body (SearchKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetKeysResponse400 | GetKeysResponse500 | KeysResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchKeysRequest,
) -> GetKeysResponse400 | GetKeysResponse500 | KeysResponse | None:
    """GetKeys retrieves search keys based on the provided request parameters.

    Args:
        body (SearchKeysRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetKeysResponse400 | GetKeysResponse500 | KeysResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
