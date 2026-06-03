from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.recurring_silence_response import RecurringSilenceResponse
from ...models.update_recurring_silence_request import UpdateRecurringSilenceRequest
from ...models.update_recurring_silence_response_400 import UpdateRecurringSilenceResponse400
from ...models.update_recurring_silence_response_404 import UpdateRecurringSilenceResponse404
from ...models.update_recurring_silence_response_500 import UpdateRecurringSilenceResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateRecurringSilenceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/monitors/recurring-silences/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RecurringSilenceResponse
    | UpdateRecurringSilenceResponse400
    | UpdateRecurringSilenceResponse404
    | UpdateRecurringSilenceResponse500
    | None
):
    if response.status_code == 200:
        response_200 = RecurringSilenceResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateRecurringSilenceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = UpdateRecurringSilenceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateRecurringSilenceResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RecurringSilenceResponse
    | UpdateRecurringSilenceResponse400
    | UpdateRecurringSilenceResponse404
    | UpdateRecurringSilenceResponse500
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
    body: UpdateRecurringSilenceRequest,
) -> Response[
    RecurringSilenceResponse
    | UpdateRecurringSilenceResponse400
    | UpdateRecurringSilenceResponse404
    | UpdateRecurringSilenceResponse500
]:
    """Update Recurring Silence

     Updates an existing recurring silence by its UUID.

    Args:
        id (str):
        body (UpdateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecurringSilenceResponse | UpdateRecurringSilenceResponse400 | UpdateRecurringSilenceResponse404 | UpdateRecurringSilenceResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecurringSilenceRequest,
) -> (
    RecurringSilenceResponse
    | UpdateRecurringSilenceResponse400
    | UpdateRecurringSilenceResponse404
    | UpdateRecurringSilenceResponse500
    | None
):
    """Update Recurring Silence

     Updates an existing recurring silence by its UUID.

    Args:
        id (str):
        body (UpdateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecurringSilenceResponse | UpdateRecurringSilenceResponse400 | UpdateRecurringSilenceResponse404 | UpdateRecurringSilenceResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecurringSilenceRequest,
) -> Response[
    RecurringSilenceResponse
    | UpdateRecurringSilenceResponse400
    | UpdateRecurringSilenceResponse404
    | UpdateRecurringSilenceResponse500
]:
    """Update Recurring Silence

     Updates an existing recurring silence by its UUID.

    Args:
        id (str):
        body (UpdateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecurringSilenceResponse | UpdateRecurringSilenceResponse400 | UpdateRecurringSilenceResponse404 | UpdateRecurringSilenceResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecurringSilenceRequest,
) -> (
    RecurringSilenceResponse
    | UpdateRecurringSilenceResponse400
    | UpdateRecurringSilenceResponse404
    | UpdateRecurringSilenceResponse500
    | None
):
    """Update Recurring Silence

     Updates an existing recurring silence by its UUID.

    Args:
        id (str):
        body (UpdateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecurringSilenceResponse | UpdateRecurringSilenceResponse400 | UpdateRecurringSilenceResponse404 | UpdateRecurringSilenceResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
