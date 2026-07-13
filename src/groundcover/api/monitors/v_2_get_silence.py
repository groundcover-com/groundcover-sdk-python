from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.v2_get_silence_response_400 import V2GetSilenceResponse400
from ...models.v2_get_silence_response_404 import V2GetSilenceResponse404
from ...models.v2_get_silence_response_500 import V2GetSilenceResponse500
from ...models.v2_silence_response import V2SilenceResponse
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/monitors/v2/silences/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse | None:
    if response.status_code == 200:
        response_200 = V2SilenceResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = V2GetSilenceResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = V2GetSilenceResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = V2GetSilenceResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse]:
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
) -> Response[V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse]:
    """Get Silence by ID (V2 Unified)

     Retrieves a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse]
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
) -> V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse | None:
    """Get Silence by ID (V2 Unified)

     Retrieves a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse]:
    """Get Silence by ID (V2 Unified)

     Retrieves a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse]
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
) -> V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse | None:
    """Get Silence by ID (V2 Unified)

     Retrieves a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V2GetSilenceResponse400 | V2GetSilenceResponse404 | V2GetSilenceResponse500 | V2SilenceResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
