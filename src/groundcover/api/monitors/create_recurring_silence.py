from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_recurring_silence_request import CreateRecurringSilenceRequest
from ...models.create_recurring_silence_response_400 import CreateRecurringSilenceResponse400
from ...models.create_recurring_silence_response_500 import CreateRecurringSilenceResponse500
from ...models.recurring_silence_response import RecurringSilenceResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateRecurringSilenceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/monitors/recurring-silences",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse | None:
    if response.status_code == 200:
        response_200 = RecurringSilenceResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = CreateRecurringSilenceResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = CreateRecurringSilenceResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecurringSilenceRequest,
) -> Response[CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse]:
    """Create Recurring Silence

     Creates a new recurring silence definition.

    Args:
        body (CreateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse]
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
    body: CreateRecurringSilenceRequest,
) -> CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse | None:
    """Create Recurring Silence

     Creates a new recurring silence definition.

    Args:
        body (CreateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecurringSilenceRequest,
) -> Response[CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse]:
    """Create Recurring Silence

     Creates a new recurring silence definition.

    Args:
        body (CreateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecurringSilenceRequest,
) -> CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse | None:
    """Create Recurring Silence

     Creates a new recurring silence definition.

    Args:
        body (CreateRecurringSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRecurringSilenceResponse400 | CreateRecurringSilenceResponse500 | RecurringSilenceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
