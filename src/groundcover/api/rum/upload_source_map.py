from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ...models.source_map_upload_response_is_the_json_success_body_returned_by_the_upload_handler import (
    SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler,
)
from ..._generated_types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rum/sourcemaps",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
    | None
):
    if response.status_code == 201:
        response_201 = (
            SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler.from_dict(response.json())
            if response.content
            else None
        )

        return response_201

    if response.status_code == 400:
        response_400 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_400

    if response.status_code == 413:
        response_413 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_413

    if response.status_code == 500:
        response_500 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_500

    if response.status_code == 502:
        response_502 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_502

    if response.status_code == 503:
        response_503 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
]:
    """Upload a sourcemap

     Accepts multipart/form-data with app_id, release_id, and file fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
    | None
):
    """Upload a sourcemap

     Accepts multipart/form-data with app_id, release_id, and file fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
]:
    """Upload a sourcemap

     Accepts multipart/form-data with app_id, release_id, and file fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
    | None
):
    """Upload a sourcemap

     Accepts multipart/form-data with app_id, release_id, and file fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
