from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ...models.synthetic_test_create_request import SyntheticTestCreateRequest
from ...models.synthetic_test_update_response import SyntheticTestUpdateResponse
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: SyntheticTestCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/synthetics/v1/rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse | None:
    if response.status_code == 200:
        response_200 = SyntheticTestUpdateResponse.from_dict(response.json()) if response.content else None

        return response_200

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
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse]:
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
    body: SyntheticTestCreateRequest,
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse]:
    """Update Synthetic Test

     Updates a synthetic test configuration and its associated monitor.
    To create a monitor on a synthetic that currently has none, set createMonitor=true explicitly.
    Sending a monitor config block without createMonitor=true when no monitor exists returns 400.

    Args:
        id (str):
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyntheticTestCreateRequest,
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse | None:
    """Update Synthetic Test

     Updates a synthetic test configuration and its associated monitor.
    To create a monitor on a synthetic that currently has none, set createMonitor=true explicitly.
    Sending a monitor config block without createMonitor=true when no monitor exists returns 400.

    Args:
        id (str):
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyntheticTestCreateRequest,
) -> Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse]:
    """Update Synthetic Test

     Updates a synthetic test configuration and its associated monitor.
    To create a monitor on a synthetic that currently has none, set createMonitor=true explicitly.
    Sending a monitor config block without createMonitor=true when no monitor exists returns 400.

    Args:
        id (str):
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyntheticTestCreateRequest,
) -> ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse | None:
    """Update Synthetic Test

     Updates a synthetic test configuration and its associated monitor.
    To create a monitor on a synthetic that currently has none, set createMonitor=true explicitly.
    Sending a monitor config block without createMonitor=true when no monitor exists returns 400.

    Args:
        id (str):
        body (SyntheticTestCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SyntheticTestUpdateResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
