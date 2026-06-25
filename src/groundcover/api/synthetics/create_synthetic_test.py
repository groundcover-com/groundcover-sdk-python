from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ...models.synthetic_test_create_request import SyntheticTestCreateRequest
from ...models.synthetic_test_create_response import SyntheticTestCreateResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: SyntheticTestCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/synthetics/v1/rules",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse | None:
    if response.status_code == 201:
        response_201 = SyntheticTestCreateResponse.from_dict(response.json()) if response.content else None

        return response_201

    if response.status_code == 400:
        response_400 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_400

    if response.status_code == 409:
        response_409 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_409

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
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyntheticTestCreateRequest,
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse]:
    """Create Synthetic Test

     Creates a new synthetic test with the provided configuration.

    Args:
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse]
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
    body: SyntheticTestCreateRequest,
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse | None:
    """Create Synthetic Test

     Creates a new synthetic test with the provided configuration.

    Args:
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyntheticTestCreateRequest,
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse]:
    """Create Synthetic Test

     Creates a new synthetic test with the provided configuration.

    Args:
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyntheticTestCreateRequest,
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse | None:
    """Create Synthetic Test

     Creates a new synthetic test with the provided configuration.

    Args:
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestCreateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
