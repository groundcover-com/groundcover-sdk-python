from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_dashboard_request import CreateDashboardRequest
from ...models.create_dashboard_response_400 import CreateDashboardResponse400
from ...models.create_dashboard_response_500 import CreateDashboardResponse500
from ...models.view import View
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreateDashboardRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/dashboards",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateDashboardResponse400 | CreateDashboardResponse500 | View | None:
    if response.status_code == 201:
        response_201 = View.from_dict(response.json()) if response.content else None

        return response_201

    if response.status_code == 400:
        response_400 = CreateDashboardResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = CreateDashboardResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateDashboardResponse400 | CreateDashboardResponse500 | View]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDashboardRequest,
) -> Response[CreateDashboardResponse400 | CreateDashboardResponse500 | View]:
    """Create Dashboard

    Args:
        body (CreateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDashboardResponse400 | CreateDashboardResponse500 | View]
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
    body: CreateDashboardRequest,
) -> CreateDashboardResponse400 | CreateDashboardResponse500 | View | None:
    """Create Dashboard

    Args:
        body (CreateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDashboardResponse400 | CreateDashboardResponse500 | View
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDashboardRequest,
) -> Response[CreateDashboardResponse400 | CreateDashboardResponse500 | View]:
    """Create Dashboard

    Args:
        body (CreateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDashboardResponse400 | CreateDashboardResponse500 | View]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateDashboardRequest,
) -> CreateDashboardResponse400 | CreateDashboardResponse500 | View | None:
    """Create Dashboard

    Args:
        body (CreateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDashboardResponse400 | CreateDashboardResponse500 | View
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
