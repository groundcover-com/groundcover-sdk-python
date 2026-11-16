from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_profiling_rule_response_400 import CreateProfilingRuleResponse400
from ...models.create_profiling_rule_response_403 import CreateProfilingRuleResponse403
from ...models.create_profiling_rule_response_404 import CreateProfilingRuleResponse404
from ...models.create_profiling_rule_response_500 import CreateProfilingRuleResponse500
from ...models.create_profiling_rule_response_501 import CreateProfilingRuleResponse501
from ...models.create_profiling_rule_response_503 import CreateProfilingRuleResponse503
from ...models.profiling_rule_request_creates_or_replaces_a_profiling_rule import (
    ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
)
from ...models.profiling_rule_response_is_a_stored_profiling_rule import ProfilingRuleResponseIsAStoredProfilingRule
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/profiling/v1/rules",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProfilingRuleResponse400
    | CreateProfilingRuleResponse403
    | CreateProfilingRuleResponse404
    | CreateProfilingRuleResponse500
    | CreateProfilingRuleResponse501
    | CreateProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
    | None
):
    if response.status_code == 201:
        response_201 = (
            ProfilingRuleResponseIsAStoredProfilingRule.from_dict(response.json()) if response.content else None
        )

        return response_201

    if response.status_code == 400:
        response_400 = CreateProfilingRuleResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 403:
        response_403 = CreateProfilingRuleResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = CreateProfilingRuleResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = CreateProfilingRuleResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 501:
        response_501 = CreateProfilingRuleResponse501.from_dict(response.json()) if response.content else None

        return response_501

    if response.status_code == 503:
        response_503 = CreateProfilingRuleResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProfilingRuleResponse400
    | CreateProfilingRuleResponse403
    | CreateProfilingRuleResponse404
    | CreateProfilingRuleResponse500
    | CreateProfilingRuleResponse501
    | CreateProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> Response[
    CreateProfilingRuleResponse400
    | CreateProfilingRuleResponse403
    | CreateProfilingRuleResponse404
    | CreateProfilingRuleResponse500
    | CreateProfilingRuleResponse501
    | CreateProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
]:
    """Create a profiling rule. Sensors in its scope profile the containers its
    filter selects until it expires or is deleted.

    Args:
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProfilingRuleResponse400 | CreateProfilingRuleResponse403 | CreateProfilingRuleResponse404 | CreateProfilingRuleResponse500 | CreateProfilingRuleResponse501 | CreateProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule]
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
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> (
    CreateProfilingRuleResponse400
    | CreateProfilingRuleResponse403
    | CreateProfilingRuleResponse404
    | CreateProfilingRuleResponse500
    | CreateProfilingRuleResponse501
    | CreateProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
    | None
):
    """Create a profiling rule. Sensors in its scope profile the containers its
    filter selects until it expires or is deleted.

    Args:
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProfilingRuleResponse400 | CreateProfilingRuleResponse403 | CreateProfilingRuleResponse404 | CreateProfilingRuleResponse500 | CreateProfilingRuleResponse501 | CreateProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> Response[
    CreateProfilingRuleResponse400
    | CreateProfilingRuleResponse403
    | CreateProfilingRuleResponse404
    | CreateProfilingRuleResponse500
    | CreateProfilingRuleResponse501
    | CreateProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
]:
    """Create a profiling rule. Sensors in its scope profile the containers its
    filter selects until it expires or is deleted.

    Args:
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProfilingRuleResponse400 | CreateProfilingRuleResponse403 | CreateProfilingRuleResponse404 | CreateProfilingRuleResponse500 | CreateProfilingRuleResponse501 | CreateProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProfilingRuleRequestCreatesOrReplacesAProfilingRule,
) -> (
    CreateProfilingRuleResponse400
    | CreateProfilingRuleResponse403
    | CreateProfilingRuleResponse404
    | CreateProfilingRuleResponse500
    | CreateProfilingRuleResponse501
    | CreateProfilingRuleResponse503
    | ProfilingRuleResponseIsAStoredProfilingRule
    | None
):
    """Create a profiling rule. Sensors in its scope profile the containers its
    filter selects until it expires or is deleted.

    Args:
        body (ProfilingRuleRequestCreatesOrReplacesAProfilingRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProfilingRuleResponse400 | CreateProfilingRuleResponse403 | CreateProfilingRuleResponse404 | CreateProfilingRuleResponse500 | CreateProfilingRuleResponse501 | CreateProfilingRuleResponse503 | ProfilingRuleResponseIsAStoredProfilingRule
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
