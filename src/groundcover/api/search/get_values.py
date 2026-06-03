from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_values_response_400 import GetValuesResponse400
from ...models.get_values_response_500 import GetValuesResponse500
from ...models.search_values_request import SearchValuesRequest
from ...models.values_response import ValuesResponse
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchValuesRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/search/values",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetValuesResponse400 | GetValuesResponse500 | ValuesResponse | None:
    if response.status_code == 200:
        response_200 = ValuesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetValuesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetValuesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetValuesResponse400 | GetValuesResponse500 | ValuesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchValuesRequest | Unset = UNSET,
) -> Response[GetValuesResponse400 | GetValuesResponse500 | ValuesResponse]:
    """GetValues retrieves search values based on the provided request parameters.

    Args:
        body (SearchValuesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetValuesResponse400 | GetValuesResponse500 | ValuesResponse]
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
    body: SearchValuesRequest | Unset = UNSET,
) -> GetValuesResponse400 | GetValuesResponse500 | ValuesResponse | None:
    """GetValues retrieves search values based on the provided request parameters.

    Args:
        body (SearchValuesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetValuesResponse400 | GetValuesResponse500 | ValuesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchValuesRequest | Unset = UNSET,
) -> Response[GetValuesResponse400 | GetValuesResponse500 | ValuesResponse]:
    """GetValues retrieves search values based on the provided request parameters.

    Args:
        body (SearchValuesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetValuesResponse400 | GetValuesResponse500 | ValuesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchValuesRequest | Unset = UNSET,
) -> GetValuesResponse400 | GetValuesResponse500 | ValuesResponse | None:
    """GetValues retrieves search values based on the provided request parameters.

    Args:
        body (SearchValuesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetValuesResponse400 | GetValuesResponse500 | ValuesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
