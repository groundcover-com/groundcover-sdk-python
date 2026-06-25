from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ...models.synthetic_test_list_response import SyntheticTestListResponse
from ..._generated_types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/synthetics/v1/rules",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse | None:
    if response.status_code == 200:
        response_200 = SyntheticTestListResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 500:
        response_500 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse]:
    """List Synthetic Tests

     Lists all synthetic test configurations with their status and monitor information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse | None:
    """List Synthetic Tests

     Lists all synthetic test configurations with their status and monitor information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse]:
    """List Synthetic Tests

     Lists all synthetic test configurations with their status and monitor information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse | None:
    """List Synthetic Tests

     Lists all synthetic test configurations with their status and monitor information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
