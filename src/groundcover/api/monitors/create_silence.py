from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_silence_request import CreateSilenceRequest
from ...models.create_silence_response_400 import CreateSilenceResponse400
from ...models.create_silence_response_500 import CreateSilenceResponse500
from ...models.silence import Silence
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateSilenceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/monitors/silences",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSilenceResponse400 | CreateSilenceResponse500 | Silence | None:
    if response.status_code == 200:
        response_200 = Silence.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = CreateSilenceResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = CreateSilenceResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateSilenceResponse400 | CreateSilenceResponse500 | Silence]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSilenceRequest,
) -> Response[CreateSilenceResponse400 | CreateSilenceResponse500 | Silence]:
    """Create Silence

     Creates a new silence for monitoring alerts.

    Args:
        body (CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSilenceResponse400 | CreateSilenceResponse500 | Silence]
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
    body: CreateSilenceRequest,
) -> CreateSilenceResponse400 | CreateSilenceResponse500 | Silence | None:
    """Create Silence

     Creates a new silence for monitoring alerts.

    Args:
        body (CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSilenceResponse400 | CreateSilenceResponse500 | Silence
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSilenceRequest,
) -> Response[CreateSilenceResponse400 | CreateSilenceResponse500 | Silence]:
    """Create Silence

     Creates a new silence for monitoring alerts.

    Args:
        body (CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSilenceResponse400 | CreateSilenceResponse500 | Silence]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSilenceRequest,
) -> CreateSilenceResponse400 | CreateSilenceResponse500 | Silence | None:
    """Create Silence

     Creates a new silence for monitoring alerts.

    Args:
        body (CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSilenceResponse400 | CreateSilenceResponse500 | Silence
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
