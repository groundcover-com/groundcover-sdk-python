from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_profiling_rules_response_400 import ListProfilingRulesResponse400
from ...models.list_profiling_rules_response_403 import ListProfilingRulesResponse403
from ...models.list_profiling_rules_response_404 import ListProfilingRulesResponse404
from ...models.list_profiling_rules_response_500 import ListProfilingRulesResponse500
from ...models.list_profiling_rules_response_503 import ListProfilingRulesResponse503
from ...models.list_profiling_rules_status import ListProfilingRulesStatus
from ...models.profiling_rule_list_response_is_a_list_of_profiling_rules import (
    ProfilingRuleListResponseIsAListOfProfilingRules,
)
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    status: ListProfilingRulesStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["env"] = env

    params["cluster"] = cluster

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/profiling/v1/rules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListProfilingRulesResponse400
    | ListProfilingRulesResponse403
    | ListProfilingRulesResponse404
    | ListProfilingRulesResponse500
    | ListProfilingRulesResponse503
    | ProfilingRuleListResponseIsAListOfProfilingRules
    | None
):
    if response.status_code == 200:
        response_200 = (
            ProfilingRuleListResponseIsAListOfProfilingRules.from_dict(response.json()) if response.content else None
        )

        return response_200

    if response.status_code == 400:
        response_400 = ListProfilingRulesResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 403:
        response_403 = ListProfilingRulesResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = ListProfilingRulesResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = ListProfilingRulesResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 503:
        response_503 = ListProfilingRulesResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListProfilingRulesResponse400
    | ListProfilingRulesResponse403
    | ListProfilingRulesResponse404
    | ListProfilingRulesResponse500
    | ListProfilingRulesResponse503
    | ProfilingRuleListResponseIsAListOfProfilingRules
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
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    status: ListProfilingRulesStatus | Unset = UNSET,
) -> Response[
    ListProfilingRulesResponse400
    | ListProfilingRulesResponse403
    | ListProfilingRulesResponse404
    | ListProfilingRulesResponse500
    | ListProfilingRulesResponse503
    | ProfilingRuleListResponseIsAListOfProfilingRules
]:
    """List profiling rules.

    Args:
        env (str | Unset):
        cluster (str | Unset):
        status (ListProfilingRulesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProfilingRulesResponse400 | ListProfilingRulesResponse403 | ListProfilingRulesResponse404 | ListProfilingRulesResponse500 | ListProfilingRulesResponse503 | ProfilingRuleListResponseIsAListOfProfilingRules]
    """

    kwargs = _get_kwargs(
        env=env,
        cluster=cluster,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    status: ListProfilingRulesStatus | Unset = UNSET,
) -> (
    ListProfilingRulesResponse400
    | ListProfilingRulesResponse403
    | ListProfilingRulesResponse404
    | ListProfilingRulesResponse500
    | ListProfilingRulesResponse503
    | ProfilingRuleListResponseIsAListOfProfilingRules
    | None
):
    """List profiling rules.

    Args:
        env (str | Unset):
        cluster (str | Unset):
        status (ListProfilingRulesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProfilingRulesResponse400 | ListProfilingRulesResponse403 | ListProfilingRulesResponse404 | ListProfilingRulesResponse500 | ListProfilingRulesResponse503 | ProfilingRuleListResponseIsAListOfProfilingRules
    """

    return sync_detailed(
        client=client,
        env=env,
        cluster=cluster,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    status: ListProfilingRulesStatus | Unset = UNSET,
) -> Response[
    ListProfilingRulesResponse400
    | ListProfilingRulesResponse403
    | ListProfilingRulesResponse404
    | ListProfilingRulesResponse500
    | ListProfilingRulesResponse503
    | ProfilingRuleListResponseIsAListOfProfilingRules
]:
    """List profiling rules.

    Args:
        env (str | Unset):
        cluster (str | Unset):
        status (ListProfilingRulesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProfilingRulesResponse400 | ListProfilingRulesResponse403 | ListProfilingRulesResponse404 | ListProfilingRulesResponse500 | ListProfilingRulesResponse503 | ProfilingRuleListResponseIsAListOfProfilingRules]
    """

    kwargs = _get_kwargs(
        env=env,
        cluster=cluster,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    env: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    status: ListProfilingRulesStatus | Unset = UNSET,
) -> (
    ListProfilingRulesResponse400
    | ListProfilingRulesResponse403
    | ListProfilingRulesResponse404
    | ListProfilingRulesResponse500
    | ListProfilingRulesResponse503
    | ProfilingRuleListResponseIsAListOfProfilingRules
    | None
):
    """List profiling rules.

    Args:
        env (str | Unset):
        cluster (str | Unset):
        status (ListProfilingRulesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProfilingRulesResponse400 | ListProfilingRulesResponse403 | ListProfilingRulesResponse404 | ListProfilingRulesResponse500 | ListProfilingRulesResponse503 | ProfilingRuleListResponseIsAListOfProfilingRules
    """

    return (
        await asyncio_detailed(
            client=client,
            env=env,
            cluster=cluster,
            status=status,
        )
    ).parsed
