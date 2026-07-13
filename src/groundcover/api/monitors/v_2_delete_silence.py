from __future__ import annotations

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.v2_delete_silence_response_400 import V2DeleteSilenceResponse400
from ...models.v2_delete_silence_response_404 import V2DeleteSilenceResponse404
from ...models.v2_delete_silence_response_500 import V2DeleteSilenceResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/monitors/v2/silences/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = V2DeleteSilenceResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = V2DeleteSilenceResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = V2DeleteSilenceResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500]:
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
) -> Response[Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500]:
    """Delete Silence (V2 Unified)

     Deletes a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500]
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
) -> Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500 | None:
    """Delete Silence (V2 Unified)

     Deletes a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500]:
    """Delete Silence (V2 Unified)

     Deletes a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500]
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
) -> Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500 | None:
    """Delete Silence (V2 Unified)

     Deletes a silence (one-time or recurring) by UUID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V2DeleteSilenceResponse400 | V2DeleteSilenceResponse404 | V2DeleteSilenceResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
