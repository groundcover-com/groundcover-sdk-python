from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_data_integration_config_request import CreateDataIntegrationConfigRequest
from ...models.data_integration_config import DataIntegrationConfig
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ..._generated_types import Response


def _get_kwargs(
    type_: str,
    id: str,
    *,
    body: CreateDataIntegrationConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/integrations/v1/data/config/{type_}/{id}".format(
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    if response.status_code == 200:
        response_200 = DataIntegrationConfig.from_dict(response.json()) if response.content else None

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

    if response.status_code == 500:
        response_500 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_500

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
) -> Response[DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataIntegrationConfigRequest,
) -> Response[DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    """
    Args:
        type_ (str):
        id (str):
        body (CreateDataIntegrationConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataIntegrationConfigRequest,
) -> DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    """
    Args:
        type_ (str):
        id (str):
        body (CreateDataIntegrationConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    """

    return sync_detailed(
        type_=type_,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataIntegrationConfigRequest,
) -> Response[DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    """
    Args:
        type_ (str):
        id (str):
        body (CreateDataIntegrationConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateDataIntegrationConfigRequest,
) -> DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    """
    Args:
        type_ (str):
        id (str):
        body (CreateDataIntegrationConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrationConfig | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    """

    return (
        await asyncio_detailed(
            type_=type_,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
