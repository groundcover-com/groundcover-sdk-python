from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.agent_create_skill_response_200 import AgentCreateSkillResponse200
from ...models.agent_create_skill_response_400 import AgentCreateSkillResponse400
from ...models.agent_create_skill_response_401 import AgentCreateSkillResponse401
from ...models.agent_create_skill_response_403 import AgentCreateSkillResponse403
from ...models.agent_create_skill_response_409 import AgentCreateSkillResponse409
from ...models.agent_create_skill_response_413 import AgentCreateSkillResponse413
from ...models.agent_create_skill_response_422 import AgentCreateSkillResponse422
from ...models.agent_create_skill_response_500 import AgentCreateSkillResponse500
from ...models.agent_create_skill_response_502 import AgentCreateSkillResponse502
from ...models.agent_create_skill_response_503 import AgentCreateSkillResponse503
from ...models.agent_skill_request_is_forwarded_to_agent_service_for_skill_creation_and_updates import (
    AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
)
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/agent/skills",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentCreateSkillResponse200
    | AgentCreateSkillResponse400
    | AgentCreateSkillResponse401
    | AgentCreateSkillResponse403
    | AgentCreateSkillResponse409
    | AgentCreateSkillResponse413
    | AgentCreateSkillResponse422
    | AgentCreateSkillResponse500
    | AgentCreateSkillResponse502
    | AgentCreateSkillResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgentCreateSkillResponse200.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = AgentCreateSkillResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 401:
        response_401 = AgentCreateSkillResponse401.from_dict(response.json()) if response.content else None

        return response_401

    if response.status_code == 403:
        response_403 = AgentCreateSkillResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 409:
        response_409 = AgentCreateSkillResponse409.from_dict(response.json()) if response.content else None

        return response_409

    if response.status_code == 413:
        response_413 = AgentCreateSkillResponse413.from_dict(response.json()) if response.content else None

        return response_413

    if response.status_code == 422:
        response_422 = AgentCreateSkillResponse422.from_dict(response.json()) if response.content else None

        return response_422

    if response.status_code == 500:
        response_500 = AgentCreateSkillResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 502:
        response_502 = AgentCreateSkillResponse502.from_dict(response.json()) if response.content else None

        return response_502

    if response.status_code == 503:
        response_503 = AgentCreateSkillResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentCreateSkillResponse200
    | AgentCreateSkillResponse400
    | AgentCreateSkillResponse401
    | AgentCreateSkillResponse403
    | AgentCreateSkillResponse409
    | AgentCreateSkillResponse413
    | AgentCreateSkillResponse422
    | AgentCreateSkillResponse500
    | AgentCreateSkillResponse502
    | AgentCreateSkillResponse503
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
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> Response[
    AgentCreateSkillResponse200
    | AgentCreateSkillResponse400
    | AgentCreateSkillResponse401
    | AgentCreateSkillResponse403
    | AgentCreateSkillResponse409
    | AgentCreateSkillResponse413
    | AgentCreateSkillResponse422
    | AgentCreateSkillResponse500
    | AgentCreateSkillResponse502
    | AgentCreateSkillResponse503
]:
    """Create Skill

     Creates a personal Skill, or an organizational Skill when is_organizational is true. Organizational
    Skills are admin only.

    Args:
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentCreateSkillResponse200 | AgentCreateSkillResponse400 | AgentCreateSkillResponse401 | AgentCreateSkillResponse403 | AgentCreateSkillResponse409 | AgentCreateSkillResponse413 | AgentCreateSkillResponse422 | AgentCreateSkillResponse500 | AgentCreateSkillResponse502 | AgentCreateSkillResponse503]
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
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> (
    AgentCreateSkillResponse200
    | AgentCreateSkillResponse400
    | AgentCreateSkillResponse401
    | AgentCreateSkillResponse403
    | AgentCreateSkillResponse409
    | AgentCreateSkillResponse413
    | AgentCreateSkillResponse422
    | AgentCreateSkillResponse500
    | AgentCreateSkillResponse502
    | AgentCreateSkillResponse503
    | None
):
    """Create Skill

     Creates a personal Skill, or an organizational Skill when is_organizational is true. Organizational
    Skills are admin only.

    Args:
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentCreateSkillResponse200 | AgentCreateSkillResponse400 | AgentCreateSkillResponse401 | AgentCreateSkillResponse403 | AgentCreateSkillResponse409 | AgentCreateSkillResponse413 | AgentCreateSkillResponse422 | AgentCreateSkillResponse500 | AgentCreateSkillResponse502 | AgentCreateSkillResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> Response[
    AgentCreateSkillResponse200
    | AgentCreateSkillResponse400
    | AgentCreateSkillResponse401
    | AgentCreateSkillResponse403
    | AgentCreateSkillResponse409
    | AgentCreateSkillResponse413
    | AgentCreateSkillResponse422
    | AgentCreateSkillResponse500
    | AgentCreateSkillResponse502
    | AgentCreateSkillResponse503
]:
    """Create Skill

     Creates a personal Skill, or an organizational Skill when is_organizational is true. Organizational
    Skills are admin only.

    Args:
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentCreateSkillResponse200 | AgentCreateSkillResponse400 | AgentCreateSkillResponse401 | AgentCreateSkillResponse403 | AgentCreateSkillResponse409 | AgentCreateSkillResponse413 | AgentCreateSkillResponse422 | AgentCreateSkillResponse500 | AgentCreateSkillResponse502 | AgentCreateSkillResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> (
    AgentCreateSkillResponse200
    | AgentCreateSkillResponse400
    | AgentCreateSkillResponse401
    | AgentCreateSkillResponse403
    | AgentCreateSkillResponse409
    | AgentCreateSkillResponse413
    | AgentCreateSkillResponse422
    | AgentCreateSkillResponse500
    | AgentCreateSkillResponse502
    | AgentCreateSkillResponse503
    | None
):
    """Create Skill

     Creates a personal Skill, or an organizational Skill when is_organizational is true. Organizational
    Skills are admin only.

    Args:
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentCreateSkillResponse200 | AgentCreateSkillResponse400 | AgentCreateSkillResponse401 | AgentCreateSkillResponse403 | AgentCreateSkillResponse409 | AgentCreateSkillResponse413 | AgentCreateSkillResponse422 | AgentCreateSkillResponse500 | AgentCreateSkillResponse502 | AgentCreateSkillResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
