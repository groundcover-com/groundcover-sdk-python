from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.data_integration_config import DataIntegrationConfig
from ...models.error_response import ErrorResponse
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    type_: str,
    id: str,
    *,
    include_archived: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeArchived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/integrations/v1/data/config/{type_}/{id}".format(
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataIntegrationConfig | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DataIntegrationConfig.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DataIntegrationConfig | ErrorResponse]:
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
    include_archived: bool | Unset = UNSET,
) -> Response[DataIntegrationConfig | ErrorResponse]:
    """
    Args:
        type_ (str):
        id (str):
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrationConfig | ErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
        include_archived=include_archived,
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
    include_archived: bool | Unset = UNSET,
) -> DataIntegrationConfig | ErrorResponse | None:
    """
    Args:
        type_ (str):
        id (str):
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrationConfig | ErrorResponse
    """

    return sync_detailed(
        type_=type_,
        id=id,
        client=client,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> Response[DataIntegrationConfig | ErrorResponse]:
    """
    Args:
        type_ (str):
        id (str):
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrationConfig | ErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> DataIntegrationConfig | ErrorResponse | None:
    """
    Args:
        type_ (str):
        id (str):
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrationConfig | ErrorResponse
    """

    return (
        await asyncio_detailed(
            type_=type_,
            id=id,
            client=client,
            include_archived=include_archived,
        )
    ).parsed
