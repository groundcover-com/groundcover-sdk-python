from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_secret_request import CreateSecretRequest
from ...models.create_secret_response_400 import CreateSecretResponse400
from ...models.create_secret_response_500 import CreateSecretResponse500
from ...models.secret_response import SecretResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateSecretRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/secret",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse | None:
    if response.status_code == 201:
        response_201 = SecretResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateSecretResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = CreateSecretResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
) -> Response[CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse]:
    """Create Secret

    Args:
        body (CreateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse]
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
    body: CreateSecretRequest,
) -> CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse | None:
    """Create Secret

    Args:
        body (CreateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
) -> Response[CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse]:
    """Create Secret

    Args:
        body (CreateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
) -> CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse | None:
    """Create Secret

    Args:
        body (CreateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSecretResponse400 | CreateSecretResponse500 | SecretResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
