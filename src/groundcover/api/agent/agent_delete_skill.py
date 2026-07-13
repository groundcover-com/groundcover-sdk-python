from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.agent_delete_skill_response_200 import AgentDeleteSkillResponse200
from ...models.agent_delete_skill_response_400 import AgentDeleteSkillResponse400
from ...models.agent_delete_skill_response_401 import AgentDeleteSkillResponse401
from ...models.agent_delete_skill_response_403 import AgentDeleteSkillResponse403
from ...models.agent_delete_skill_response_404 import AgentDeleteSkillResponse404
from ...models.agent_delete_skill_response_500 import AgentDeleteSkillResponse500
from ...models.agent_delete_skill_response_502 import AgentDeleteSkillResponse502
from ...models.agent_delete_skill_response_503 import AgentDeleteSkillResponse503
from ..._generated_types import Response


def _get_kwargs(
    skill_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/agent/skills/{skill_id}".format(
            skill_id=quote(str(skill_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentDeleteSkillResponse200
    | AgentDeleteSkillResponse400
    | AgentDeleteSkillResponse401
    | AgentDeleteSkillResponse403
    | AgentDeleteSkillResponse404
    | AgentDeleteSkillResponse500
    | AgentDeleteSkillResponse502
    | AgentDeleteSkillResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgentDeleteSkillResponse200.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = AgentDeleteSkillResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 401:
        response_401 = AgentDeleteSkillResponse401.from_dict(response.json()) if response.content else None

        return response_401

    if response.status_code == 403:
        response_403 = AgentDeleteSkillResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = AgentDeleteSkillResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = AgentDeleteSkillResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 502:
        response_502 = AgentDeleteSkillResponse502.from_dict(response.json()) if response.content else None

        return response_502

    if response.status_code == 503:
        response_503 = AgentDeleteSkillResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentDeleteSkillResponse200
    | AgentDeleteSkillResponse400
    | AgentDeleteSkillResponse401
    | AgentDeleteSkillResponse403
    | AgentDeleteSkillResponse404
    | AgentDeleteSkillResponse500
    | AgentDeleteSkillResponse502
    | AgentDeleteSkillResponse503
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
    AgentDeleteSkillResponse200
    | AgentDeleteSkillResponse400
    | AgentDeleteSkillResponse401
    | AgentDeleteSkillResponse403
    | AgentDeleteSkillResponse404
    | AgentDeleteSkillResponse500
    | AgentDeleteSkillResponse502
    | AgentDeleteSkillResponse503
]:
    """Delete Skill

     Deletes a personal or organizational Skill. Organizational Skills are admin only.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDeleteSkillResponse200 | AgentDeleteSkillResponse400 | AgentDeleteSkillResponse401 | AgentDeleteSkillResponse403 | AgentDeleteSkillResponse404 | AgentDeleteSkillResponse500 | AgentDeleteSkillResponse502 | AgentDeleteSkillResponse503]
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
    AgentDeleteSkillResponse200
    | AgentDeleteSkillResponse400
    | AgentDeleteSkillResponse401
    | AgentDeleteSkillResponse403
    | AgentDeleteSkillResponse404
    | AgentDeleteSkillResponse500
    | AgentDeleteSkillResponse502
    | AgentDeleteSkillResponse503
    | None
):
    """Delete Skill

     Deletes a personal or organizational Skill. Organizational Skills are admin only.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDeleteSkillResponse200 | AgentDeleteSkillResponse400 | AgentDeleteSkillResponse401 | AgentDeleteSkillResponse403 | AgentDeleteSkillResponse404 | AgentDeleteSkillResponse500 | AgentDeleteSkillResponse502 | AgentDeleteSkillResponse503
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
    AgentDeleteSkillResponse200
    | AgentDeleteSkillResponse400
    | AgentDeleteSkillResponse401
    | AgentDeleteSkillResponse403
    | AgentDeleteSkillResponse404
    | AgentDeleteSkillResponse500
    | AgentDeleteSkillResponse502
    | AgentDeleteSkillResponse503
]:
    """Delete Skill

     Deletes a personal or organizational Skill. Organizational Skills are admin only.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDeleteSkillResponse200 | AgentDeleteSkillResponse400 | AgentDeleteSkillResponse401 | AgentDeleteSkillResponse403 | AgentDeleteSkillResponse404 | AgentDeleteSkillResponse500 | AgentDeleteSkillResponse502 | AgentDeleteSkillResponse503]
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
    AgentDeleteSkillResponse200
    | AgentDeleteSkillResponse400
    | AgentDeleteSkillResponse401
    | AgentDeleteSkillResponse403
    | AgentDeleteSkillResponse404
    | AgentDeleteSkillResponse500
    | AgentDeleteSkillResponse502
    | AgentDeleteSkillResponse503
    | None
):
    """Delete Skill

     Deletes a personal or organizational Skill. Organizational Skills are admin only.

    Args:
        skill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDeleteSkillResponse200 | AgentDeleteSkillResponse400 | AgentDeleteSkillResponse401 | AgentDeleteSkillResponse403 | AgentDeleteSkillResponse404 | AgentDeleteSkillResponse500 | AgentDeleteSkillResponse502 | AgentDeleteSkillResponse503
    """

    return (
        await asyncio_detailed(
            skill_id=skill_id,
            client=client,
        )
    ).parsed
