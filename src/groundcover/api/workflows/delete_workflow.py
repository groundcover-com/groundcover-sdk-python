from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.delete_workflow_response_400 import DeleteWorkflowResponse400
from ...models.delete_workflow_response_401 import DeleteWorkflowResponse401
from ...models.delete_workflow_response_500 import DeleteWorkflowResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/workflows/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 400:
        response_400 = DeleteWorkflowResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteWorkflowResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = DeleteWorkflowResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500]:
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
) -> Response[Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500]:
    """Delete Workflow

     Deletes a workflow by its unique identifier.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500]
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
) -> Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500 | None:
    """Delete Workflow

     Deletes a workflow by its unique identifier.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500]:
    """Delete Workflow

     Deletes a workflow by its unique identifier.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500]
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
) -> Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500 | None:
    """Delete Workflow

     Deletes a workflow by its unique identifier.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteWorkflowResponse400 | DeleteWorkflowResponse401 | DeleteWorkflowResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
