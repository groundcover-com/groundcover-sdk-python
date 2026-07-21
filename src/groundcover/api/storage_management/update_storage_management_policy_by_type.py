from __future__ import annotations

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.error_response_is_the_canonical_error_body_returned_by_http_handlers import (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers,
)
from ...models.storage_management_policy_request import StorageManagementPolicyRequest
from ...models.storage_management_policy_response_is_the_api_facing_policy_representation import (
    StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation,
)
from ..._generated_types import Response


def _get_kwargs(
    data_type: str,
    *,
    body: StorageManagementPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/storage-management/{data_type}".format(
            data_type=quote(str(data_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
    | None
):
    if response.status_code == 200:
        response_200 = (
            StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation.from_dict(response.json())
            if response.content
            else None
        )

        return response_200

    if response.status_code == 400:
        response_400 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_400

    if response.status_code == 404:
        response_404 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_404

    if response.status_code == 409:
        response_409 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_409

    if response.status_code == 500:
        response_500 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_500

    if response.status_code == 502:
        response_502 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_502

    if response.status_code == 503:
        response_503 = (
            ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers.from_dict(response.json())
            if response.content
            else None
        )

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageManagementPolicyRequest,
) -> Response[
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
]:
    """
    Args:
        data_type (str):
        body (StorageManagementPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageManagementPolicyRequest,
) -> (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
    | None
):
    """
    Args:
        data_type (str):
        body (StorageManagementPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
    """

    return sync_detailed(
        data_type=data_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageManagementPolicyRequest,
) -> Response[
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
]:
    """
    Args:
        data_type (str):
        body (StorageManagementPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageManagementPolicyRequest,
) -> (
    ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers
    | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
    | None
):
    """
    Args:
        data_type (str):
        body (StorageManagementPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlers | StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation
    """

    return (
        await asyncio_detailed(
            data_type=data_type,
            client=client,
            body=body,
        )
    ).parsed
