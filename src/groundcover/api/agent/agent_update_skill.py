from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.agent_skill_request_is_forwarded_to_agent_service_for_skill_creation_and_updates import (
    AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
)
from ...models.agent_update_skill_response_200 import AgentUpdateSkillResponse200
from ...models.agent_update_skill_response_400 import AgentUpdateSkillResponse400
from ...models.agent_update_skill_response_401 import AgentUpdateSkillResponse401
from ...models.agent_update_skill_response_403 import AgentUpdateSkillResponse403
from ...models.agent_update_skill_response_404 import AgentUpdateSkillResponse404
from ...models.agent_update_skill_response_409 import AgentUpdateSkillResponse409
from ...models.agent_update_skill_response_413 import AgentUpdateSkillResponse413
from ...models.agent_update_skill_response_422 import AgentUpdateSkillResponse422
from ...models.agent_update_skill_response_500 import AgentUpdateSkillResponse500
from ...models.agent_update_skill_response_502 import AgentUpdateSkillResponse502
from ...models.agent_update_skill_response_503 import AgentUpdateSkillResponse503
from ..._generated_types import Response


def _get_kwargs(
    skill_id: str,
    *,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/agent/skills/{skill_id}".format(
            skill_id=quote(str(skill_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentUpdateSkillResponse200
    | AgentUpdateSkillResponse400
    | AgentUpdateSkillResponse401
    | AgentUpdateSkillResponse403
    | AgentUpdateSkillResponse404
    | AgentUpdateSkillResponse409
    | AgentUpdateSkillResponse413
    | AgentUpdateSkillResponse422
    | AgentUpdateSkillResponse500
    | AgentUpdateSkillResponse502
    | AgentUpdateSkillResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgentUpdateSkillResponse200.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = AgentUpdateSkillResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 401:
        response_401 = AgentUpdateSkillResponse401.from_dict(response.json()) if response.content else None

        return response_401

    if response.status_code == 403:
        response_403 = AgentUpdateSkillResponse403.from_dict(response.json()) if response.content else None

        return response_403

    if response.status_code == 404:
        response_404 = AgentUpdateSkillResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 409:
        response_409 = AgentUpdateSkillResponse409.from_dict(response.json()) if response.content else None

        return response_409

    if response.status_code == 413:
        response_413 = AgentUpdateSkillResponse413.from_dict(response.json()) if response.content else None

        return response_413

    if response.status_code == 422:
        response_422 = AgentUpdateSkillResponse422.from_dict(response.json()) if response.content else None

        return response_422

    if response.status_code == 500:
        response_500 = AgentUpdateSkillResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 502:
        response_502 = AgentUpdateSkillResponse502.from_dict(response.json()) if response.content else None

        return response_502

    if response.status_code == 503:
        response_503 = AgentUpdateSkillResponse503.from_dict(response.json()) if response.content else None

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgentUpdateSkillResponse200
    | AgentUpdateSkillResponse400
    | AgentUpdateSkillResponse401
    | AgentUpdateSkillResponse403
    | AgentUpdateSkillResponse404
    | AgentUpdateSkillResponse409
    | AgentUpdateSkillResponse413
    | AgentUpdateSkillResponse422
    | AgentUpdateSkillResponse500
    | AgentUpdateSkillResponse502
    | AgentUpdateSkillResponse503
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
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> Response[
    AgentUpdateSkillResponse200
    | AgentUpdateSkillResponse400
    | AgentUpdateSkillResponse401
    | AgentUpdateSkillResponse403
    | AgentUpdateSkillResponse404
    | AgentUpdateSkillResponse409
    | AgentUpdateSkillResponse413
    | AgentUpdateSkillResponse422
    | AgentUpdateSkillResponse500
    | AgentUpdateSkillResponse502
    | AgentUpdateSkillResponse503
]:
    """Update Skill

     Updates a personal or organizational Skill. Organizational Skills and org-scope changes are admin
    only.

    Args:
        skill_id (str):
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentUpdateSkillResponse200 | AgentUpdateSkillResponse400 | AgentUpdateSkillResponse401 | AgentUpdateSkillResponse403 | AgentUpdateSkillResponse404 | AgentUpdateSkillResponse409 | AgentUpdateSkillResponse413 | AgentUpdateSkillResponse422 | AgentUpdateSkillResponse500 | AgentUpdateSkillResponse502 | AgentUpdateSkillResponse503]
    """

    kwargs = _get_kwargs(
        skill_id=skill_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> (
    AgentUpdateSkillResponse200
    | AgentUpdateSkillResponse400
    | AgentUpdateSkillResponse401
    | AgentUpdateSkillResponse403
    | AgentUpdateSkillResponse404
    | AgentUpdateSkillResponse409
    | AgentUpdateSkillResponse413
    | AgentUpdateSkillResponse422
    | AgentUpdateSkillResponse500
    | AgentUpdateSkillResponse502
    | AgentUpdateSkillResponse503
    | None
):
    """Update Skill

     Updates a personal or organizational Skill. Organizational Skills and org-scope changes are admin
    only.

    Args:
        skill_id (str):
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentUpdateSkillResponse200 | AgentUpdateSkillResponse400 | AgentUpdateSkillResponse401 | AgentUpdateSkillResponse403 | AgentUpdateSkillResponse404 | AgentUpdateSkillResponse409 | AgentUpdateSkillResponse413 | AgentUpdateSkillResponse422 | AgentUpdateSkillResponse500 | AgentUpdateSkillResponse502 | AgentUpdateSkillResponse503
    """

    return sync_detailed(
        skill_id=skill_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> Response[
    AgentUpdateSkillResponse200
    | AgentUpdateSkillResponse400
    | AgentUpdateSkillResponse401
    | AgentUpdateSkillResponse403
    | AgentUpdateSkillResponse404
    | AgentUpdateSkillResponse409
    | AgentUpdateSkillResponse413
    | AgentUpdateSkillResponse422
    | AgentUpdateSkillResponse500
    | AgentUpdateSkillResponse502
    | AgentUpdateSkillResponse503
]:
    """Update Skill

     Updates a personal or organizational Skill. Organizational Skills and org-scope changes are admin
    only.

    Args:
        skill_id (str):
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentUpdateSkillResponse200 | AgentUpdateSkillResponse400 | AgentUpdateSkillResponse401 | AgentUpdateSkillResponse403 | AgentUpdateSkillResponse404 | AgentUpdateSkillResponse409 | AgentUpdateSkillResponse413 | AgentUpdateSkillResponse422 | AgentUpdateSkillResponse500 | AgentUpdateSkillResponse502 | AgentUpdateSkillResponse503]
    """

    kwargs = _get_kwargs(
        skill_id=skill_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates,
) -> (
    AgentUpdateSkillResponse200
    | AgentUpdateSkillResponse400
    | AgentUpdateSkillResponse401
    | AgentUpdateSkillResponse403
    | AgentUpdateSkillResponse404
    | AgentUpdateSkillResponse409
    | AgentUpdateSkillResponse413
    | AgentUpdateSkillResponse422
    | AgentUpdateSkillResponse500
    | AgentUpdateSkillResponse502
    | AgentUpdateSkillResponse503
    | None
):
    """Update Skill

     Updates a personal or organizational Skill. Organizational Skills and org-scope changes are admin
    only.

    Args:
        skill_id (str):
        body (AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentUpdateSkillResponse200 | AgentUpdateSkillResponse400 | AgentUpdateSkillResponse401 | AgentUpdateSkillResponse403 | AgentUpdateSkillResponse404 | AgentUpdateSkillResponse409 | AgentUpdateSkillResponse413 | AgentUpdateSkillResponse422 | AgentUpdateSkillResponse500 | AgentUpdateSkillResponse502 | AgentUpdateSkillResponse503
    """

    return (
        await asyncio_detailed(
            skill_id=skill_id,
            client=client,
            body=body,
        )
    ).parsed
