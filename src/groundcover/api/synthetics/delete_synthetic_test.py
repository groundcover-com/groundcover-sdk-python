from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.delete_synthetic_test_response import DeleteSyntheticTestResponse
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/synthetics/v1/rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    if response.status_code == 204:
        response_204 = DeleteSyntheticTestResponse.from_dict(response.json()) if response.content else None

        return response_204

    if response.status_code == 400:
        response_400 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_400

    if response.status_code == 404:
        response_404 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_404

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
) -> Response[DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
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
) -> Response[DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    """Delete Synthetic Test

     Deletes a synthetic test configuration and its associated monitor.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]
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
) -> DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    """Delete Synthetic Test

     Deletes a synthetic test configuration and its associated monitor.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    """Delete Synthetic Test

     Deletes a synthetic test configuration and its associated monitor.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]
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
) -> DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    """Delete Synthetic Test

     Deletes a synthetic test configuration and its associated monitor.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSyntheticTestResponse | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
