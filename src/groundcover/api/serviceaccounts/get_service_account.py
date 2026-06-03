from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_service_account_response_400 import GetServiceAccountResponse400
from ...models.get_service_account_response_500 import GetServiceAccountResponse500
from ...models.service_accounts_with_policy import ServiceAccountsWithPolicy
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rbac/service-account/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy | None:
    if response.status_code == 200:
        response_200 = ServiceAccountsWithPolicy.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetServiceAccountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetServiceAccountResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy]:
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
) -> Response[GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy]:
    """Get service account by ID

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy]
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
) -> GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy | None:
    """Get service account by ID

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy]:
    """Get service account by ID

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy]
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
) -> GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy | None:
    """Get service account by ID

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServiceAccountResponse400 | GetServiceAccountResponse500 | ServiceAccountsWithPolicy
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
