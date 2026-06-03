from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_api_keys_response_400 import ListApiKeysResponse400
from ...models.list_api_keys_response_500 import ListApiKeysResponse500
from ...models.list_api_keys_response_item import ListApiKeysResponseItem
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    with_revoked: bool | Unset = UNSET,
    with_expired: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["withRevoked"] = with_revoked

    params["withExpired"] = with_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rbac/apikeys/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        if _response_200 is None:
            _response_200 = []
        for response_200_item_data in _response_200:
            response_200_item = ListApiKeysResponseItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ListApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ListApiKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    with_revoked: bool | Unset = UNSET,
    with_expired: bool | Unset = UNSET,
) -> Response[ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]]:
    """List API Keys

    Args:
        with_revoked (bool | Unset):
        with_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]]
    """

    kwargs = _get_kwargs(
        with_revoked=with_revoked,
        with_expired=with_expired,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    with_revoked: bool | Unset = UNSET,
    with_expired: bool | Unset = UNSET,
) -> ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem] | None:
    """List API Keys

    Args:
        with_revoked (bool | Unset):
        with_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]
    """

    return sync_detailed(
        client=client,
        with_revoked=with_revoked,
        with_expired=with_expired,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    with_revoked: bool | Unset = UNSET,
    with_expired: bool | Unset = UNSET,
) -> Response[ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]]:
    """List API Keys

    Args:
        with_revoked (bool | Unset):
        with_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]]
    """

    kwargs = _get_kwargs(
        with_revoked=with_revoked,
        with_expired=with_expired,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    with_revoked: bool | Unset = UNSET,
    with_expired: bool | Unset = UNSET,
) -> ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem] | None:
    """List API Keys

    Args:
        with_revoked (bool | Unset):
        with_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListApiKeysResponse400 | ListApiKeysResponse500 | list[ListApiKeysResponseItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            with_revoked=with_revoked,
            with_expired=with_expired,
        )
    ).parsed
