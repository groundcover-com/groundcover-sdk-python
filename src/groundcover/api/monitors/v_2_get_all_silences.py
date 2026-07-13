from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.v2_get_all_silences_response_400 import V2GetAllSilencesResponse400
from ...models.v2_get_all_silences_response_500 import V2GetAllSilencesResponse500
from ...models.v2_get_all_silences_type import V2GetAllSilencesType
from ...models.v2_silences_list_response import V2SilencesListResponse
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: V2GetAllSilencesType | Unset = UNSET,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["active"] = active

    params["includeRecurring"] = include_recurring

    params["limit"] = limit

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/monitors/v2/silences",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse | None:
    if response.status_code == 200:
        response_200 = V2SilencesListResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = V2GetAllSilencesResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = V2GetAllSilencesResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: V2GetAllSilencesType | Unset = UNSET,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> Response[V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse]:
    """List All Silences (V2 Unified)

     Returns both one-time and recurring silences in a single list.

    Args:
        type_ (V2GetAllSilencesType | Unset):
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        active=active,
        include_recurring=include_recurring,
        limit=limit,
        skip=skip,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: V2GetAllSilencesType | Unset = UNSET,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse | None:
    """List All Silences (V2 Unified)

     Returns both one-time and recurring silences in a single list.

    Args:
        type_ (V2GetAllSilencesType | Unset):
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
        active=active,
        include_recurring=include_recurring,
        limit=limit,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: V2GetAllSilencesType | Unset = UNSET,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> Response[V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse]:
    """List All Silences (V2 Unified)

     Returns both one-time and recurring silences in a single list.

    Args:
        type_ (V2GetAllSilencesType | Unset):
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        active=active,
        include_recurring=include_recurring,
        limit=limit,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: V2GetAllSilencesType | Unset = UNSET,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse | None:
    """List All Silences (V2 Unified)

     Returns both one-time and recurring silences in a single list.

    Args:
        type_ (V2GetAllSilencesType | Unset):
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V2GetAllSilencesResponse400 | V2GetAllSilencesResponse500 | V2SilencesListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            active=active,
            include_recurring=include_recurring,
            limit=limit,
            skip=skip,
        )
    ).parsed
