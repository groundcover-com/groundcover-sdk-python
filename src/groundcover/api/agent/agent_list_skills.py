from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.agent_list_skills_response_200 import AgentListSkillsResponse200
from ...models.agent_list_skills_response_400 import AgentListSkillsResponse400
from ...models.agent_list_skills_response_401 import AgentListSkillsResponse401
from ...models.agent_list_skills_response_500 import AgentListSkillsResponse500
from ...models.agent_list_skills_response_502 import AgentListSkillsResponse502
from ...models.agent_list_skills_response_503 import AgentListSkillsResponse503
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent/skills",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentListSkillsResponse200
    | AgentListSkillsResponse400
    | AgentListSkillsResponse401
    | AgentListSkillsResponse500
    | AgentListSkillsResponse502
    | AgentListSkillsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgentListSkillsResponse200.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = AgentListSkillsResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 401:
        response_401 = AgentListSkillsResponse401.from_dict(response.json()) if response.content else None

        return response_401

    if response.status_code == 500:
        response_500 = AgentListSkillsResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 502:
        response_502 = AgentListSkillsResponse502.from_dict(response.json()) if response.content else None

        return response_502

    if response.status_code == 503:
        response_503 = AgentListSkillsResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentListSkillsResponse200
    | AgentListSkillsResponse400
    | AgentListSkillsResponse401
    | AgentListSkillsResponse500
    | AgentListSkillsResponse502
    | AgentListSkillsResponse503
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
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    AgentListSkillsResponse200
    | AgentListSkillsResponse400
    | AgentListSkillsResponse401
    | AgentListSkillsResponse500
    | AgentListSkillsResponse502
    | AgentListSkillsResponse503
]:
    """List Skills

     Returns personal and organizational Skills available to the calling user.

    Args:
        q (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentListSkillsResponse200 | AgentListSkillsResponse400 | AgentListSkillsResponse401 | AgentListSkillsResponse500 | AgentListSkillsResponse502 | AgentListSkillsResponse503]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    AgentListSkillsResponse200
    | AgentListSkillsResponse400
    | AgentListSkillsResponse401
    | AgentListSkillsResponse500
    | AgentListSkillsResponse502
    | AgentListSkillsResponse503
    | None
):
    """List Skills

     Returns personal and organizational Skills available to the calling user.

    Args:
        q (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentListSkillsResponse200 | AgentListSkillsResponse400 | AgentListSkillsResponse401 | AgentListSkillsResponse500 | AgentListSkillsResponse502 | AgentListSkillsResponse503
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    AgentListSkillsResponse200
    | AgentListSkillsResponse400
    | AgentListSkillsResponse401
    | AgentListSkillsResponse500
    | AgentListSkillsResponse502
    | AgentListSkillsResponse503
]:
    """List Skills

     Returns personal and organizational Skills available to the calling user.

    Args:
        q (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentListSkillsResponse200 | AgentListSkillsResponse400 | AgentListSkillsResponse401 | AgentListSkillsResponse500 | AgentListSkillsResponse502 | AgentListSkillsResponse503]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    AgentListSkillsResponse200
    | AgentListSkillsResponse400
    | AgentListSkillsResponse401
    | AgentListSkillsResponse500
    | AgentListSkillsResponse502
    | AgentListSkillsResponse503
    | None
):
    """List Skills

     Returns personal and organizational Skills available to the calling user.

    Args:
        q (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentListSkillsResponse200 | AgentListSkillsResponse400 | AgentListSkillsResponse401 | AgentListSkillsResponse500 | AgentListSkillsResponse502 | AgentListSkillsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
        )
    ).parsed
