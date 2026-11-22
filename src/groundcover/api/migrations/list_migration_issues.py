from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_issues_response_is_an_ordered_page_and_the_exact_total_under_the_filters import (
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters,
)
from ...models.list_migration_issues_asset_type import ListMigrationIssuesAssetType
from ...models.list_migration_issues_datasource import ListMigrationIssuesDatasource
from ...models.list_migration_issues_kind import ListMigrationIssuesKind
from ...models.list_migration_issues_response_400 import ListMigrationIssuesResponse400
from ...models.list_migration_issues_response_404 import ListMigrationIssuesResponse404
from ...models.list_migration_issues_response_500 import ListMigrationIssuesResponse500
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    migration_id: UUID,
    *,
    asset_type: ListMigrationIssuesAssetType | Unset = UNSET,
    asset_id: UUID | Unset = UNSET,
    kind: ListMigrationIssuesKind | Unset = UNSET,
    datasource: ListMigrationIssuesDatasource | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_type: str | Unset = UNSET
    if not isinstance(asset_type, Unset):
        json_asset_type = asset_type.value

    params["asset_type"] = json_asset_type

    json_asset_id: str | Unset = UNSET
    if not isinstance(asset_id, Unset):
        json_asset_id = str(asset_id)
    params["asset_id"] = json_asset_id

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    json_datasource: str | Unset = UNSET
    if not isinstance(datasource, Unset):
        json_datasource = datasource.value

    params["datasource"] = json_datasource

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/migrations/{migration_id}/issues".format(
            migration_id=quote(str(migration_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters
    | ListMigrationIssuesResponse400
    | ListMigrationIssuesResponse404
    | ListMigrationIssuesResponse500
    | None
):
    if response.status_code == 200:
        response_200 = (
            ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters.from_dict(response.json())
            if response.content
            else None
        )

        return response_200

    if response.status_code == 400:
        response_400 = ListMigrationIssuesResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = ListMigrationIssuesResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = ListMigrationIssuesResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters
    | ListMigrationIssuesResponse400
    | ListMigrationIssuesResponse404
    | ListMigrationIssuesResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    migration_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    asset_type: ListMigrationIssuesAssetType | Unset = UNSET,
    asset_id: UUID | Unset = UNSET,
    kind: ListMigrationIssuesKind | Unset = UNSET,
    datasource: ListMigrationIssuesDatasource | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters
    | ListMigrationIssuesResponse400
    | ListMigrationIssuesResponse404
    | ListMigrationIssuesResponse500
]:
    """List open migration issues ranked by distinct eligible assets.

     For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        asset_type (ListMigrationIssuesAssetType | Unset):
        asset_id (UUID | Unset):
        kind (ListMigrationIssuesKind | Unset):
        datasource (ListMigrationIssuesDatasource | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters | ListMigrationIssuesResponse400 | ListMigrationIssuesResponse404 | ListMigrationIssuesResponse500]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        asset_type=asset_type,
        asset_id=asset_id,
        kind=kind,
        datasource=datasource,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    migration_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    asset_type: ListMigrationIssuesAssetType | Unset = UNSET,
    asset_id: UUID | Unset = UNSET,
    kind: ListMigrationIssuesKind | Unset = UNSET,
    datasource: ListMigrationIssuesDatasource | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters
    | ListMigrationIssuesResponse400
    | ListMigrationIssuesResponse404
    | ListMigrationIssuesResponse500
    | None
):
    """List open migration issues ranked by distinct eligible assets.

     For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        asset_type (ListMigrationIssuesAssetType | Unset):
        asset_id (UUID | Unset):
        kind (ListMigrationIssuesKind | Unset):
        datasource (ListMigrationIssuesDatasource | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters | ListMigrationIssuesResponse400 | ListMigrationIssuesResponse404 | ListMigrationIssuesResponse500
    """

    return sync_detailed(
        migration_id=migration_id,
        client=client,
        asset_type=asset_type,
        asset_id=asset_id,
        kind=kind,
        datasource=datasource,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    migration_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    asset_type: ListMigrationIssuesAssetType | Unset = UNSET,
    asset_id: UUID | Unset = UNSET,
    kind: ListMigrationIssuesKind | Unset = UNSET,
    datasource: ListMigrationIssuesDatasource | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters
    | ListMigrationIssuesResponse400
    | ListMigrationIssuesResponse404
    | ListMigrationIssuesResponse500
]:
    """List open migration issues ranked by distinct eligible assets.

     For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        asset_type (ListMigrationIssuesAssetType | Unset):
        asset_id (UUID | Unset):
        kind (ListMigrationIssuesKind | Unset):
        datasource (ListMigrationIssuesDatasource | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters | ListMigrationIssuesResponse400 | ListMigrationIssuesResponse404 | ListMigrationIssuesResponse500]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        asset_type=asset_type,
        asset_id=asset_id,
        kind=kind,
        datasource=datasource,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    migration_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    asset_type: ListMigrationIssuesAssetType | Unset = UNSET,
    asset_id: UUID | Unset = UNSET,
    kind: ListMigrationIssuesKind | Unset = UNSET,
    datasource: ListMigrationIssuesDatasource | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters
    | ListMigrationIssuesResponse400
    | ListMigrationIssuesResponse404
    | ListMigrationIssuesResponse500
    | None
):
    """List open migration issues ranked by distinct eligible assets.

     For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        asset_type (ListMigrationIssuesAssetType | Unset):
        asset_id (UUID | Unset):
        kind (ListMigrationIssuesKind | Unset):
        datasource (ListMigrationIssuesDatasource | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters | ListMigrationIssuesResponse400 | ListMigrationIssuesResponse404 | ListMigrationIssuesResponse500
    """

    return (
        await asyncio_detailed(
            migration_id=migration_id,
            client=client,
            asset_type=asset_type,
            asset_id=asset_id,
            kind=kind,
            datasource=datasource,
            limit=limit,
            offset=offset,
        )
    ).parsed
