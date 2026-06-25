from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_tenant_ai_settings_response_400 import GetTenantAISettingsResponse400
from ...models.get_tenant_ai_settings_response_500 import GetTenantAISettingsResponse500
from ...models.tenant_ai_settings_response import TenantAISettingsResponse
from ..._generated_types import Response


def _get_kwargs(
    *,
    x_backend_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Backend-Id"] = x_backend_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rbac/v2/tenant/ai-settings",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse | None:
    if response.status_code == 200:
        response_200 = TenantAISettingsResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = GetTenantAISettingsResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = GetTenantAISettingsResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_backend_id: str,
) -> Response[GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse]:
    """Get tenant AI settings

    Args:
        x_backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse]
    """

    kwargs = _get_kwargs(
        x_backend_id=x_backend_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_backend_id: str,
) -> GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse | None:
    """Get tenant AI settings

    Args:
        x_backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse
    """

    return sync_detailed(
        client=client,
        x_backend_id=x_backend_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_backend_id: str,
) -> Response[GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse]:
    """Get tenant AI settings

    Args:
        x_backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse]
    """

    kwargs = _get_kwargs(
        x_backend_id=x_backend_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_backend_id: str,
) -> GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse | None:
    """Get tenant AI settings

    Args:
        x_backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTenantAISettingsResponse400 | GetTenantAISettingsResponse500 | TenantAISettingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            x_backend_id=x_backend_id,
        )
    ).parsed
