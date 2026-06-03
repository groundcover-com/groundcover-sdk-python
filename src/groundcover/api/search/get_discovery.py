from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.discovery_response import DiscoveryResponse
from ...models.get_discovery_response_400 import GetDiscoveryResponse400
from ...models.get_discovery_response_500 import GetDiscoveryResponse500
from ...models.search_discovery_request import SearchDiscoveryRequest
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: SearchDiscoveryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/search/discovery",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500 | None:
    if response.status_code == 200:
        response_200 = DiscoveryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDiscoveryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetDiscoveryResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchDiscoveryRequest,
) -> Response[DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500]:
    """GetDiscovery retrieves search discovery results based on the provided request parameters.

    Args:
        body (SearchDiscoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500]
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
    body: SearchDiscoveryRequest,
) -> DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500 | None:
    """GetDiscovery retrieves search discovery results based on the provided request parameters.

    Args:
        body (SearchDiscoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchDiscoveryRequest,
) -> Response[DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500]:
    """GetDiscovery retrieves search discovery results based on the provided request parameters.

    Args:
        body (SearchDiscoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchDiscoveryRequest,
) -> DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500 | None:
    """GetDiscovery retrieves search discovery results based on the provided request parameters.

    Args:
        body (SearchDiscoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscoveryResponse | GetDiscoveryResponse400 | GetDiscoveryResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
