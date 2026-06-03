from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_recurring_silence_response_400 import GetRecurringSilenceResponse400
from ...models.get_recurring_silence_response_404 import GetRecurringSilenceResponse404
from ...models.get_recurring_silence_response_500 import GetRecurringSilenceResponse500
from ...models.recurring_silence_response import RecurringSilenceResponse
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/monitors/recurring-silences/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRecurringSilenceResponse400
    | GetRecurringSilenceResponse404
    | GetRecurringSilenceResponse500
    | RecurringSilenceResponse
    | None
):
    if response.status_code == 200:
        response_200 = RecurringSilenceResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRecurringSilenceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetRecurringSilenceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetRecurringSilenceResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRecurringSilenceResponse400
    | GetRecurringSilenceResponse404
    | GetRecurringSilenceResponse500
    | RecurringSilenceResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetRecurringSilenceResponse400
    | GetRecurringSilenceResponse404
    | GetRecurringSilenceResponse500
    | RecurringSilenceResponse
]:
    """Get Recurring Silence

     Retrieves a specific recurring silence by its UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRecurringSilenceResponse400 | GetRecurringSilenceResponse404 | GetRecurringSilenceResponse500 | RecurringSilenceResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetRecurringSilenceResponse400
    | GetRecurringSilenceResponse404
    | GetRecurringSilenceResponse500
    | RecurringSilenceResponse
    | None
):
    """Get Recurring Silence

     Retrieves a specific recurring silence by its UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRecurringSilenceResponse400 | GetRecurringSilenceResponse404 | GetRecurringSilenceResponse500 | RecurringSilenceResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetRecurringSilenceResponse400
    | GetRecurringSilenceResponse404
    | GetRecurringSilenceResponse500
    | RecurringSilenceResponse
]:
    """Get Recurring Silence

     Retrieves a specific recurring silence by its UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRecurringSilenceResponse400 | GetRecurringSilenceResponse404 | GetRecurringSilenceResponse500 | RecurringSilenceResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetRecurringSilenceResponse400
    | GetRecurringSilenceResponse404
    | GetRecurringSilenceResponse500
    | RecurringSilenceResponse
    | None
):
    """Get Recurring Silence

     Retrieves a specific recurring silence by its UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRecurringSilenceResponse400 | GetRecurringSilenceResponse404 | GetRecurringSilenceResponse500 | RecurringSilenceResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
