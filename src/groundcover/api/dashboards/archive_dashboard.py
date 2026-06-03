from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.archive_dashboard_response_400 import ArchiveDashboardResponse400
from ...models.archive_dashboard_response_404 import ArchiveDashboardResponse404
from ...models.archive_dashboard_response_500 import ArchiveDashboardResponse500
from ...models.view import View
from ..._generated_types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    current_revision: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["currentRevision"] = current_revision

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/dashboards/{id}/archive".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View | None:
    if response.status_code == 202:
        response_202 = View.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ArchiveDashboardResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ArchiveDashboardResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ArchiveDashboardResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View]:
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
    current_revision: int,
) -> Response[ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View]:
    """Archive Dashboard

    Args:
        id (str):
        current_revision (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View]
    """

    kwargs = _get_kwargs(
        id=id,
        current_revision=current_revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    current_revision: int,
) -> ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View | None:
    """Archive Dashboard

    Args:
        id (str):
        current_revision (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View
    """

    return sync_detailed(
        id=id,
        client=client,
        current_revision=current_revision,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    current_revision: int,
) -> Response[ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View]:
    """Archive Dashboard

    Args:
        id (str):
        current_revision (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View]
    """

    kwargs = _get_kwargs(
        id=id,
        current_revision=current_revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    current_revision: int,
) -> ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View | None:
    """Archive Dashboard

    Args:
        id (str):
        current_revision (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveDashboardResponse400 | ArchiveDashboardResponse404 | ArchiveDashboardResponse500 | View
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            current_revision=current_revision,
        )
    ).parsed
