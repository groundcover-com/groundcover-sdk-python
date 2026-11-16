from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.profiling_rule_request_creates_or_replaces_a_profiling_rule import (
    ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
)
from ...models.profiling_rule_response_is_a_stored_profiling_rule import ProfilingRuleResponseIsAStoredProfilingRule
from ...models.update_profiling_rule_response_400 import UpdateProfilingRuleResponse400
from ...models.update_profiling_rule_response_403 import UpdateProfilingRuleResponse403
from ...models.update_profiling_rule_response_404 import UpdateProfilingRuleResponse404
from ...models.update_profiling_rule_response_500 import UpdateProfilingRuleResponse500
from ...models.update_profiling_rule_response_503 import UpdateProfilingRuleResponse503
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/profiling/v1/rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfilingRuleResponseIsAStoredProfilingRule
    | UpdateProfilingRuleResponse400
    | UpdateProfilingRuleResponse403
    | UpdateProfilingRuleResponse404
    | UpdateProfilingRuleResponse500
    | UpdateProfilingRuleResponse503
    | None
):
    if response.status_code == 200:
        response_200 = (
            ProfilingRuleResponseIsAStoredProfilingRule.from_dict(response.json()) if response.content else None
        )

        return response_200

    if response.status_code == 400:
        response_400 = UpdateProfilingRuleResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 403:
        response_403 = UpdateProfilingRuleResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = UpdateProfilingRuleResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = UpdateProfilingRuleResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 503:
        response_503 = UpdateProfilingRuleResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfilingRuleResponseIsAStoredProfilingRule
    | UpdateProfilingRuleResponse400
    | UpdateProfilingRuleResponse403
    | UpdateProfilingRuleResponse404
    | UpdateProfilingRuleResponse500
    | UpdateProfilingRuleResponse503
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
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> Response[
    ProfilingRuleResponseIsAStoredProfilingRule
    | UpdateProfilingRuleResponse400
    | UpdateProfilingRuleResponse403
    | UpdateProfilingRuleResponse404
    | UpdateProfilingRuleResponse500
    | UpdateProfilingRuleResponse503
]:
    """Replace a profiling rule, keeping its ID. The scope cannot change.

    Args:
        id (str):
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfilingRuleResponseIsAStoredProfilingRule | UpdateProfilingRuleResponse400 | UpdateProfilingRuleResponse403 | UpdateProfilingRuleResponse404 | UpdateProfilingRuleResponse500 | UpdateProfilingRuleResponse503]
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
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> (
    ProfilingRuleResponseIsAStoredProfilingRule
    | UpdateProfilingRuleResponse400
    | UpdateProfilingRuleResponse403
    | UpdateProfilingRuleResponse404
    | UpdateProfilingRuleResponse500
    | UpdateProfilingRuleResponse503
    | None
):
    """Replace a profiling rule, keeping its ID. The scope cannot change.

    Args:
        id (str):
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfilingRuleResponseIsAStoredProfilingRule | UpdateProfilingRuleResponse400 | UpdateProfilingRuleResponse403 | UpdateProfilingRuleResponse404 | UpdateProfilingRuleResponse500 | UpdateProfilingRuleResponse503
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
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> Response[
    ProfilingRuleResponseIsAStoredProfilingRule
    | UpdateProfilingRuleResponse400
    | UpdateProfilingRuleResponse403
    | UpdateProfilingRuleResponse404
    | UpdateProfilingRuleResponse500
    | UpdateProfilingRuleResponse503
]:
    """Replace a profiling rule, keeping its ID. The scope cannot change.

    Args:
        id (str):
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfilingRuleResponseIsAStoredProfilingRule | UpdateProfilingRuleResponse400 | UpdateProfilingRuleResponse403 | UpdateProfilingRuleResponse404 | UpdateProfilingRuleResponse500 | UpdateProfilingRuleResponse503]
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
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> (
    ProfilingRuleResponseIsAStoredProfilingRule
    | UpdateProfilingRuleResponse400
    | UpdateProfilingRuleResponse403
    | UpdateProfilingRuleResponse404
    | UpdateProfilingRuleResponse500
    | UpdateProfilingRuleResponse503
    | None
):
    """Replace a profiling rule, keeping its ID. The scope cannot change.

    Args:
        id (str):
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfilingRuleResponseIsAStoredProfilingRule | UpdateProfilingRuleResponse400 | UpdateProfilingRuleResponse403 | UpdateProfilingRuleResponse404 | UpdateProfilingRuleResponse500 | UpdateProfilingRuleResponse503
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
