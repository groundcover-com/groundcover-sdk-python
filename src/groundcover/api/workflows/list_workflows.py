from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.list_workflows_response_401 import ListWorkflowsResponse401
from ...models.list_workflows_response_500 import ListWorkflowsResponse500
from ...models.workflows_response import WorkflowsResponse
from ..._generated_types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/workflows/list",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse | None:
    if response.status_code == 200:
        response_200 = WorkflowsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ListWorkflowsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ListWorkflowsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse]:
    """List Workflows

     Retrieves all workflows for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse | None:
    """List Workflows

     Retrieves all workflows for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse]:
    """List Workflows

     Retrieves all workflows for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse | None:
    """List Workflows

     Retrieves all workflows for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWorkflowsResponse401 | ListWorkflowsResponse500 | WorkflowsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
