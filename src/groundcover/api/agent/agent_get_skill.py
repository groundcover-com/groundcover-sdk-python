from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.agent_get_skill_response_200 import AgentGetSkillResponse200
from ...models.agent_get_skill_response_400 import AgentGetSkillResponse400
from ...models.agent_get_skill_response_401 import AgentGetSkillResponse401
from ...models.agent_get_skill_response_404 import AgentGetSkillResponse404
from ...models.agent_get_skill_response_500 import AgentGetSkillResponse500
from ...models.agent_get_skill_response_502 import AgentGetSkillResponse502
from ...models.agent_get_skill_response_503 import AgentGetSkillResponse503
from ..._generated_types import Response


def _get_kwargs(
    skill_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent/skills/{skill_id}".format(
            skill_id=quote(str(skill_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentGetSkillResponse200
    | AgentGetSkillResponse400
    | AgentGetSkillResponse401
    | AgentGetSkillResponse404
    | AgentGetSkillResponse500
    | AgentGetSkillResponse502
    | AgentGetSkillResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgentGetSkillResponse200.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = AgentGetSkillResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 401:
        response_401 = AgentGetSkillResponse401.from_dict(response.json()) if response.content else None

        return response_401

    if response.status_code == 404:
        response_404 = AgentGetSkillResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = AgentGetSkillResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 502:
        response_502 = AgentGetSkillResponse502.from_dict(response.json()) if response.content else None

        return response_502

    if response.status_code == 503:
        response_503 = AgentGetSkillResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentGetSkillResponse200
    | AgentGetSkillResponse400
    | AgentGetSkillResponse401
    | AgentGetSkillResponse404
    | AgentGetSkillResponse500
    | AgentGetSkillResponse502
    | AgentGetSkillResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AgentGetSkillResponse200
    | AgentGetSkillResponse400
    | AgentGetSkillResponse401
    | AgentGetSkillResponse404
    | AgentGetSkillResponse500
    | AgentGetSkillResponse502
    | AgentGetSkillResponse503
]:
    """Get Skill

     Returns a personal or organizational Skill by ID.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentGetSkillResponse200 | AgentGetSkillResponse400 | AgentGetSkillResponse401 | AgentGetSkillResponse404 | AgentGetSkillResponse500 | AgentGetSkillResponse502 | AgentGetSkillResponse503]
    """

    kwargs = _get_kwargs(
        skill_id=skill_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AgentGetSkillResponse200
    | AgentGetSkillResponse400
    | AgentGetSkillResponse401
    | AgentGetSkillResponse404
    | AgentGetSkillResponse500
    | AgentGetSkillResponse502
    | AgentGetSkillResponse503
    | None
):
    """Get Skill

     Returns a personal or organizational Skill by ID.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentGetSkillResponse200 | AgentGetSkillResponse400 | AgentGetSkillResponse401 | AgentGetSkillResponse404 | AgentGetSkillResponse500 | AgentGetSkillResponse502 | AgentGetSkillResponse503
    """

    return sync_detailed(
        skill_id=skill_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AgentGetSkillResponse200
    | AgentGetSkillResponse400
    | AgentGetSkillResponse401
    | AgentGetSkillResponse404
    | AgentGetSkillResponse500
    | AgentGetSkillResponse502
    | AgentGetSkillResponse503
]:
    """Get Skill

     Returns a personal or organizational Skill by ID.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentGetSkillResponse200 | AgentGetSkillResponse400 | AgentGetSkillResponse401 | AgentGetSkillResponse404 | AgentGetSkillResponse500 | AgentGetSkillResponse502 | AgentGetSkillResponse503]
    """

    kwargs = _get_kwargs(
        skill_id=skill_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AgentGetSkillResponse200
    | AgentGetSkillResponse400
    | AgentGetSkillResponse401
    | AgentGetSkillResponse404
    | AgentGetSkillResponse500
    | AgentGetSkillResponse502
    | AgentGetSkillResponse503
    | None
):
    """Get Skill

     Returns a personal or organizational Skill by ID.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentGetSkillResponse200 | AgentGetSkillResponse400 | AgentGetSkillResponse401 | AgentGetSkillResponse404 | AgentGetSkillResponse500 | AgentGetSkillResponse502 | AgentGetSkillResponse503
    """

    return (
        await asyncio_detailed(
            skill_id=skill_id,
            client=client,
        )
    ).parsed
