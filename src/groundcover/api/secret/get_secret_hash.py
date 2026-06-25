from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_secret_hash_response_400 import GetSecretHashResponse400
from ...models.get_secret_hash_response_404 import GetSecretHashResponse404
from ...models.get_secret_hash_response_500 import GetSecretHashResponse500
from ...models.secret_hash_response import SecretHashResponse
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/secret/{id}/hash".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse | None:
    if response.status_code == 200:
        response_200 = SecretHashResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = GetSecretHashResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = GetSecretHashResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = GetSecretHashResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse]:
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
) -> Response[GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse]:
    """Get Secret Hash

     Retrieves the FNV-1a hash of a secret's content without exposing the actual secret value.
    This is useful for Terraform/Crossplane to detect changes without retrieving the secret.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse]
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
) -> GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse | None:
    """Get Secret Hash

     Retrieves the FNV-1a hash of a secret's content without exposing the actual secret value.
    This is useful for Terraform/Crossplane to detect changes without retrieving the secret.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse]:
    """Get Secret Hash

     Retrieves the FNV-1a hash of a secret's content without exposing the actual secret value.
    This is useful for Terraform/Crossplane to detect changes without retrieving the secret.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse]
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
) -> GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse | None:
    """Get Secret Hash

     Retrieves the FNV-1a hash of a secret's content without exposing the actual secret value.
    This is useful for Terraform/Crossplane to detect changes without retrieving the secret.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSecretHashResponse400 | GetSecretHashResponse404 | GetSecretHashResponse500 | SecretHashResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
