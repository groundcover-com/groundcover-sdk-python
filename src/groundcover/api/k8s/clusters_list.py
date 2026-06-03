from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.clusters_list_request import ClustersListRequest
from ...models.clusters_list_response import ClustersListResponse
from ...models.clusters_list_response_400 import ClustersListResponse400
from ...models.clusters_list_response_500 import ClustersListResponse500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: ClustersListRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/k8s/v3/clusters/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClustersListResponse | ClustersListResponse400 | ClustersListResponse500 | None:
    if response.status_code == 200:
        response_200 = ClustersListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ClustersListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ClustersListResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClustersListResponse | ClustersListResponse400 | ClustersListResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ClustersListRequest,
) -> Response[ClustersListResponse | ClustersListResponse400 | ClustersListResponse500]:
    """Get clusters list.

     Retrieves a list of Kubernetes clusters based on provided source filters.

    Args:
        body (ClustersListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClustersListResponse | ClustersListResponse400 | ClustersListResponse500]
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
    body: ClustersListRequest,
) -> ClustersListResponse | ClustersListResponse400 | ClustersListResponse500 | None:
    """Get clusters list.

     Retrieves a list of Kubernetes clusters based on provided source filters.

    Args:
        body (ClustersListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClustersListResponse | ClustersListResponse400 | ClustersListResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ClustersListRequest,
) -> Response[ClustersListResponse | ClustersListResponse400 | ClustersListResponse500]:
    """Get clusters list.

     Retrieves a list of Kubernetes clusters based on provided source filters.

    Args:
        body (ClustersListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClustersListResponse | ClustersListResponse400 | ClustersListResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ClustersListRequest,
) -> ClustersListResponse | ClustersListResponse400 | ClustersListResponse500 | None:
    """Get clusters list.

     Retrieves a list of Kubernetes clusters based on provided source filters.

    Args:
        body (ClustersListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClustersListResponse | ClustersListResponse400 | ClustersListResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
