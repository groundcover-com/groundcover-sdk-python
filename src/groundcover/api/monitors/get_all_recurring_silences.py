from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_all_recurring_silences_response_400 import GetAllRecurringSilencesResponse400
from ...models.get_all_recurring_silences_response_500 import GetAllRecurringSilencesResponse500
from ...models.recurring_silence_response import RecurringSilenceResponse
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    enabled_only: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["skip"] = skip

    params["enabledOnly"] = enabled_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/monitors/recurring-silences",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json() if response.content else None
        if _response_200 is None:
            _response_200 = []
        for response_200_item_data in _response_200:
            response_200_item = RecurringSilenceResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetAllRecurringSilencesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetAllRecurringSilencesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    enabled_only: bool | Unset = UNSET,
) -> Response[GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]]:
    """List Recurring Silences

     Retrieves all recurring silences.

    Args:
        limit (int | Unset):
        skip (int | Unset):
        enabled_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        skip=skip,
        enabled_only=enabled_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    enabled_only: bool | Unset = UNSET,
) -> GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse] | None:
    """List Recurring Silences

     Retrieves all recurring silences.

    Args:
        limit (int | Unset):
        skip (int | Unset):
        enabled_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        skip=skip,
        enabled_only=enabled_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    enabled_only: bool | Unset = UNSET,
) -> Response[GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]]:
    """List Recurring Silences

     Retrieves all recurring silences.

    Args:
        limit (int | Unset):
        skip (int | Unset):
        enabled_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        skip=skip,
        enabled_only=enabled_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    enabled_only: bool | Unset = UNSET,
) -> GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse] | None:
    """List Recurring Silences

     Retrieves all recurring silences.

    Args:
        limit (int | Unset):
        skip (int | Unset):
        enabled_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllRecurringSilencesResponse400 | GetAllRecurringSilencesResponse500 | list[RecurringSilenceResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            skip=skip,
            enabled_only=enabled_only,
        )
    ).parsed
