from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.v2_create_silence_request import V2CreateSilenceRequest
from ...models.v2_create_silence_response_400 import V2CreateSilenceResponse400
from ...models.v2_create_silence_response_500 import V2CreateSilenceResponse500
from ...models.v2_silence_response import V2SilenceResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: V2CreateSilenceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/monitors/v2/silences",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse | None:
    if response.status_code == 200:
        response_200 = V2SilenceResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = V2CreateSilenceResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = V2CreateSilenceResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V2CreateSilenceRequest,
) -> Response[V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse]:
    """Create Silence (V2 Unified)

     Creates a new silence (one-time or recurring) based on the type field.

    Args:
        body (V2CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse]
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
    body: V2CreateSilenceRequest,
) -> V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse | None:
    """Create Silence (V2 Unified)

     Creates a new silence (one-time or recurring) based on the type field.

    Args:
        body (V2CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V2CreateSilenceRequest,
) -> Response[V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse]:
    """Create Silence (V2 Unified)

     Creates a new silence (one-time or recurring) based on the type field.

    Args:
        body (V2CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: V2CreateSilenceRequest,
) -> V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse | None:
    """Create Silence (V2 Unified)

     Creates a new silence (one-time or recurring) based on the type field.

    Args:
        body (V2CreateSilenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V2CreateSilenceResponse400 | V2CreateSilenceResponse500 | V2SilenceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
