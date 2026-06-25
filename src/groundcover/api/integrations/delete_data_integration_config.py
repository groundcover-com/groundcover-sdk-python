from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.delete_data_integration_config_response_200 import DeleteDataIntegrationConfigResponse200
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    type_: str,
    id: str,
    *,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    instance: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["env"] = env

    params["cluster"] = cluster

    params["instance"] = instance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/integrations/v1/data/config/{type_}/{id}".format(
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    if response.status_code == 200:
        response_200 = DeleteDataIntegrationConfigResponse200.from_dict(response.json()) if response.content else None

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
) -> Response[DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
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
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    instance: str | Unset = UNSET,
) -> Response[DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    """
    Args:
        type_ (str):
        id (str):
        env (str | Unset):
        cluster (str | Unset):
        instance (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
        env=env,
        cluster=cluster,
        instance=instance,
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
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    instance: str | Unset = UNSET,
) -> DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    """
    Args:
        type_ (str):
        id (str):
        env (str | Unset):
        cluster (str | Unset):
        instance (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    """

    return sync_detailed(
        type_=type_,
        id=id,
        client=client,
        env=env,
        cluster=cluster,
        instance=instance,
    ).parsed


async def asyncio_detailed(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    instance: str | Unset = UNSET,
) -> Response[DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]:
    """
    Args:
        type_ (str):
        id (str):
        env (str | Unset):
        cluster (str | Unset):
        instance (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
        env=env,
        cluster=cluster,
        instance=instance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    instance: str | Unset = UNSET,
) -> DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | None:
    """
    Args:
        type_ (str):
        id (str):
        env (str | Unset):
        cluster (str | Unset):
        instance (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDataIntegrationConfigResponse200 | ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    """

    return (
        await asyncio_detailed(
            type_=type_,
            id=id,
            client=client,
            env=env,
            cluster=cluster,
            instance=instance,
        )
    ).parsed
