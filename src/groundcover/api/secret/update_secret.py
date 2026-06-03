from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.secret_response import SecretResponse
from ...models.update_secret_request import UpdateSecretRequest
from ...models.update_secret_response_400 import UpdateSecretResponse400
from ...models.update_secret_response_404 import UpdateSecretResponse404
from ...models.update_secret_response_500 import UpdateSecretResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateSecretRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/secret/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500 | None:
    if response.status_code == 200:
        response_200 = SecretResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateSecretResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = UpdateSecretResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateSecretResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500]:
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
    body: UpdateSecretRequest,
) -> Response[SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500]:
    """Update Secret

    Args:
        id (str):
        body (UpdateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500]
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
    body: UpdateSecretRequest,
) -> SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500 | None:
    """Update Secret

    Args:
        id (str):
        body (UpdateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500
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
    body: UpdateSecretRequest,
) -> Response[SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500]:
    """Update Secret

    Args:
        id (str):
        body (UpdateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500]
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
    body: UpdateSecretRequest,
) -> SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500 | None:
    """Update Secret

    Args:
        id (str):
        body (UpdateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretResponse | UpdateSecretResponse400 | UpdateSecretResponse404 | UpdateSecretResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
