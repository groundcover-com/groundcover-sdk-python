from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_migration_issue_context_response_400 import GetMigrationIssueContextResponse400
from ...models.get_migration_issue_context_response_404 import GetMigrationIssueContextResponse404
from ...models.get_migration_issue_context_response_500 import GetMigrationIssueContextResponse500
from ...models.issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs import (
    IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs,
)
from ..._generated_types import Response


def _get_kwargs(
    migration_id: UUID,
    issue_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/migrations/{migration_id}/issues/{issue_id}/context".format(
            migration_id=quote(str(migration_id), safe=""),
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetMigrationIssueContextResponse400
    | GetMigrationIssueContextResponse404
    | GetMigrationIssueContextResponse500
    | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
    | None
):
    if response.status_code == 200:
        response_200 = (
            IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs.from_dict(response.json())
            if response.content
            else None
        )

        return response_200

    if response.status_code == 400:
        response_400 = GetMigrationIssueContextResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = GetMigrationIssueContextResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = GetMigrationIssueContextResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetMigrationIssueContextResponse400
    | GetMigrationIssueContextResponse404
    | GetMigrationIssueContextResponse500
    | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    migration_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetMigrationIssueContextResponse400
    | GetMigrationIssueContextResponse404
    | GetMigrationIssueContextResponse500
    | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
]:
    """Read an open migration issue and the stored queries for up to 3,000 of its findings.

     A query is null when its stored reference or expression is unavailable.

    For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        issue_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMigrationIssueContextResponse400 | GetMigrationIssueContextResponse404 | GetMigrationIssueContextResponse500 | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        issue_id=issue_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    migration_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetMigrationIssueContextResponse400
    | GetMigrationIssueContextResponse404
    | GetMigrationIssueContextResponse500
    | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
    | None
):
    """Read an open migration issue and the stored queries for up to 3,000 of its findings.

     A query is null when its stored reference or expression is unavailable.

    For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        issue_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMigrationIssueContextResponse400 | GetMigrationIssueContextResponse404 | GetMigrationIssueContextResponse500 | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
    """

    return sync_detailed(
        migration_id=migration_id,
        issue_id=issue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    migration_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetMigrationIssueContextResponse400
    | GetMigrationIssueContextResponse404
    | GetMigrationIssueContextResponse500
    | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
]:
    """Read an open migration issue and the stored queries for up to 3,000 of its findings.

     A query is null when its stored reference or expression is unavailable.

    For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        issue_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMigrationIssueContextResponse400 | GetMigrationIssueContextResponse404 | GetMigrationIssueContextResponse500 | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        issue_id=issue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    migration_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetMigrationIssueContextResponse400
    | GetMigrationIssueContextResponse404
    | GetMigrationIssueContextResponse500
    | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
    | None
):
    """Read an open migration issue and the stored queries for up to 3,000 of its findings.

     A query is null when its stored reference or expression is unavailable.

    For direct HTTP calls, use the X-Backend-Id header to select the backend.
    The router can infer the backend when exactly one is eligible.
    SDK callers select the backend in the client configuration.

    Args:
        migration_id (UUID):
        issue_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMigrationIssueContextResponse400 | GetMigrationIssueContextResponse404 | GetMigrationIssueContextResponse500 | IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs
    """

    return (
        await asyncio_detailed(
            migration_id=migration_id,
            issue_id=issue_id,
            client=client,
        )
    ).parsed
