from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.update_dashboard_request import UpdateDashboardRequest
from ...models.update_dashboard_response_400 import UpdateDashboardResponse400
from ...models.update_dashboard_response_404 import UpdateDashboardResponse404
from ...models.update_dashboard_response_500 import UpdateDashboardResponse500
from ...models.view import View
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateDashboardRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/dashboards/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View | None:
    if response.status_code == 202:
        response_202 = View.from_dict(response.json()) if response.content else None

        return response_202

    if response.status_code == 400:
        response_400 = UpdateDashboardResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = UpdateDashboardResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = UpdateDashboardResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View]:
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
    body: UpdateDashboardRequest,
) -> Response[UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View]:
    """Update Dashboard

    Args:
        id (str):
        body (UpdateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View]
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
    body: UpdateDashboardRequest,
) -> UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View | None:
    """Update Dashboard

    Args:
        id (str):
        body (UpdateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View
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
    body: UpdateDashboardRequest,
) -> Response[UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View]:
    """Update Dashboard

    Args:
        id (str):
        body (UpdateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View]
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
    body: UpdateDashboardRequest,
) -> UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View | None:
    """Update Dashboard

    Args:
        id (str):
        body (UpdateDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateDashboardResponse400 | UpdateDashboardResponse404 | UpdateDashboardResponse500 | View
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
