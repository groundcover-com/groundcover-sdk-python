from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.create_policy_request import CreatePolicyRequest
from ...models.create_policy_response_400 import CreatePolicyResponse400
from ...models.create_policy_response_500 import CreatePolicyResponse500
from ...models.policy_defines_an_access_control_policy import PolicyDefinesAnAccessControlPolicy
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: CreatePolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rbac/policy/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy | None:
    if response.status_code == 201:
        response_201 = PolicyDefinesAnAccessControlPolicy.from_dict(response.json()) if response.content else None

        return response_201

    if response.status_code == 400:
        response_400 = CreatePolicyResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = CreatePolicyResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePolicyRequest,
) -> Response[CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy]:
    """Create Policy

    Args:
        body (CreatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy]
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
    body: CreatePolicyRequest,
) -> CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy | None:
    """Create Policy

    Args:
        body (CreatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePolicyRequest,
) -> Response[CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy]:
    """Create Policy

    Args:
        body (CreatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePolicyRequest,
) -> CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy | None:
    """Create Policy

    Args:
        body (CreatePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePolicyResponse400 | CreatePolicyResponse500 | PolicyDefinesAnAccessControlPolicy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
