from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_all_silences_response_400 import GetAllSilencesResponse400
from ...models.get_all_silences_response_500 import GetAllSilencesResponse500
from ...models.silence import Silence
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["includeRecurring"] = include_recurring

    params["limit"] = limit

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/monitors/silences",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json() if response.content else None
        if _response_200 is None:
            _response_200 = []
        for response_200_item_data in _response_200:
            response_200_item = Silence.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetAllSilencesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetAllSilencesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> Response[GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]]:
    """Get All Silences

     Retrieves all silences with optional filtering.

    Args:
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]]
    """

    kwargs = _get_kwargs(
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
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence] | None:
    """Get All Silences

     Retrieves all silences with optional filtering.

    Args:
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]
    """

    return sync_detailed(
        client=client,
        active=active,
        include_recurring=include_recurring,
        limit=limit,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> Response[GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]]:
    """Get All Silences

     Retrieves all silences with optional filtering.

    Args:
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]]
    """

    kwargs = _get_kwargs(
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
    active: bool | Unset = UNSET,
    include_recurring: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
) -> GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence] | None:
    """Get All Silences

     Retrieves all silences with optional filtering.

    Args:
        active (bool | Unset):
        include_recurring (bool | Unset):
        limit (int | Unset):
        skip (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllSilencesResponse400 | GetAllSilencesResponse500 | list[Silence]
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            include_recurring=include_recurring,
            limit=limit,
            skip=skip,
        )
    ).parsed
