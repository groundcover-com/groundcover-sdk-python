from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_profiling_rule_response_403 import GetProfilingRuleResponse403
from ...models.get_profiling_rule_response_404 import GetProfilingRuleResponse404
from ...models.get_profiling_rule_response_500 import GetProfilingRuleResponse500
from ...models.get_profiling_rule_response_503 import GetProfilingRuleResponse503
from ...models.profiling_rule_response_is_a_stored_profiling_rule import ProfilingRuleResponseIsAStoredProfilingRule
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/profiling/v1/rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProfilingRuleResponse403
    | GetProfilingRuleResponse404
    | GetProfilingRuleResponse500
    | GetProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
    | None
):
    if response.status_code == 200:
        response_200 = (
            ProfilingRuleResponseIsAStoredProfilingRule.from_dict(response.json()) if response.content else None
        )

        return response_200

    if response.status_code == 403:
        response_403 = GetProfilingRuleResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = GetProfilingRuleResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = GetProfilingRuleResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 503:
        response_503 = GetProfilingRuleResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProfilingRuleResponse403
    | GetProfilingRuleResponse404
    | GetProfilingRuleResponse500
    | GetProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
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
    GetProfilingRuleResponse403
    | GetProfilingRuleResponse404
    | GetProfilingRuleResponse500
    | GetProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
]:
    """Get a profiling rule.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilingRuleResponse403 | GetProfilingRuleResponse404 | GetProfilingRuleResponse500 | GetProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule]
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
    GetProfilingRuleResponse403
    | GetProfilingRuleResponse404
    | GetProfilingRuleResponse500
    | GetProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
    | None
):
    """Get a profiling rule.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilingRuleResponse403 | GetProfilingRuleResponse404 | GetProfilingRuleResponse500 | GetProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule
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
    GetProfilingRuleResponse403
    | GetProfilingRuleResponse404
    | GetProfilingRuleResponse500
    | GetProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
]:
    """Get a profiling rule.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilingRuleResponse403 | GetProfilingRuleResponse404 | GetProfilingRuleResponse500 | GetProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule]
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
    GetProfilingRuleResponse403
    | GetProfilingRuleResponse404
    | GetProfilingRuleResponse500
    | GetProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
    | None
):
    """Get a profiling rule.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilingRuleResponse403 | GetProfilingRuleResponse404 | GetProfilingRuleResponse500 | GetProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
