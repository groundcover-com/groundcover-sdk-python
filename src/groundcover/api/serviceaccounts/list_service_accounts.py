from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_service_accounts_response_500 import ListServiceAccountsResponse500
from ...models.service_accounts_with_policy import ServiceAccountsWithPolicy
from ..._generated_types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rbac/service-accounts/list",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json() if response.content else None
        if _response_200 is None:
            _response_200 = []
        for response_200_item_data in _response_200:
            response_200_item = ServiceAccountsWithPolicy.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 500:
        response_500 = ListServiceAccountsResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]]:
    """List Service Accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy] | None:
    """List Service Accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]]:
    """List Service Accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy] | None:
    """List Service Accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListServiceAccountsResponse500 | list[ServiceAccountsWithPolicy]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
