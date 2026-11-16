from __future__ import annotations

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.delete_profiling_rule_response_403 import DeleteProfilingRuleResponse403
from ...models.delete_profiling_rule_response_404 import DeleteProfilingRuleResponse404
from ...models.delete_profiling_rule_response_500 import DeleteProfilingRuleResponse500
from ...models.delete_profiling_rule_response_503 import DeleteProfilingRuleResponse503
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/profiling/v1/rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteProfilingRuleResponse403
    | DeleteProfilingRuleResponse404
    | DeleteProfilingRuleResponse500
    | DeleteProfilingRuleResponse503
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = DeleteProfilingRuleResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = DeleteProfilingRuleResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = DeleteProfilingRuleResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 503:
        response_503 = DeleteProfilingRuleResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteProfilingRuleResponse403
    | DeleteProfilingRuleResponse404
    | DeleteProfilingRuleResponse500
    | DeleteProfilingRuleResponse503
]:
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
) -> Response[
    Any
    | DeleteProfilingRuleResponse403
    | DeleteProfilingRuleResponse404
    | DeleteProfilingRuleResponse500
    | DeleteProfilingRuleResponse503
]:
    """Delete a profiling rule; sensors stop applying it on their next poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteProfilingRuleResponse403 | DeleteProfilingRuleResponse404 | DeleteProfilingRuleResponse500 | DeleteProfilingRuleResponse503]
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
) -> (
    Any
    | DeleteProfilingRuleResponse403
    | DeleteProfilingRuleResponse404
    | DeleteProfilingRuleResponse500
    | DeleteProfilingRuleResponse503
    | None
):
    """Delete a profiling rule; sensors stop applying it on their next poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteProfilingRuleResponse403 | DeleteProfilingRuleResponse404 | DeleteProfilingRuleResponse500 | DeleteProfilingRuleResponse503
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteProfilingRuleResponse403
    | DeleteProfilingRuleResponse404
    | DeleteProfilingRuleResponse500
    | DeleteProfilingRuleResponse503
]:
    """Delete a profiling rule; sensors stop applying it on their next poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteProfilingRuleResponse403 | DeleteProfilingRuleResponse404 | DeleteProfilingRuleResponse500 | DeleteProfilingRuleResponse503]
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
) -> (
    Any
    | DeleteProfilingRuleResponse403
    | DeleteProfilingRuleResponse404
    | DeleteProfilingRuleResponse500
    | DeleteProfilingRuleResponse503
    | None
):
    """Delete a profiling rule; sensors stop applying it on their next poll.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteProfilingRuleResponse403 | DeleteProfilingRuleResponse404 | DeleteProfilingRuleResponse500 | DeleteProfilingRuleResponse503
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
