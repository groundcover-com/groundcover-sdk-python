from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.policy_defines_an_access_control_policy import PolicyDefinesAnAccessControlPolicy
from ...models.update_policy_request import UpdatePolicyRequest
from ...models.update_policy_response_400 import UpdatePolicyResponse400
from ...models.update_policy_response_404 import UpdatePolicyResponse404
from ...models.update_policy_response_500 import UpdatePolicyResponse500
from ..._generated_types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdatePolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/rbac/policy/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PolicyDefinesAnAccessControlPolicy
    | UpdatePolicyResponse400
    | UpdatePolicyResponse404
    | UpdatePolicyResponse500
    | None
):
    if response.status_code == 202:
        response_202 = PolicyDefinesAnAccessControlPolicy.from_dict(response.json()) if response.content else None

        return response_202

    if response.status_code == 400:
        response_400 = UpdatePolicyResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = UpdatePolicyResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 500:
        response_500 = UpdatePolicyResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500
]:
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
    body: UpdatePolicyRequest,
) -> Response[
    PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500
]:
    """Update Policy

    Args:
        id (str):
        body (UpdatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePolicyRequest,
) -> (
    PolicyDefinesAnAccessControlPolicy
    | UpdatePolicyResponse400
    | UpdatePolicyResponse404
    | UpdatePolicyResponse500
    | None
):
    """Update Policy

    Args:
        id (str):
        body (UpdatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePolicyRequest,
) -> Response[
    PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500
]:
    """Update Policy

    Args:
        id (str):
        body (UpdatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePolicyRequest,
) -> (
    PolicyDefinesAnAccessControlPolicy
    | UpdatePolicyResponse400
    | UpdatePolicyResponse404
    | UpdatePolicyResponse500
    | None
):
    """Update Policy

    Args:
        id (str):
        body (UpdatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyDefinesAnAccessControlPolicy | UpdatePolicyResponse400 | UpdatePolicyResponse404 | UpdatePolicyResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
