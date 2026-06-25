from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time import (
    GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime,
)
from ...models.get_events_over_time_response_400 import GetEventsOverTimeResponse400
from ...models.get_events_over_time_response_500 import GetEventsOverTimeResponse500
from ...models.get_events_over_time_response_defines_the_structure_for_the_events_over_time_api_response import (
    GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse,
)
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/k8s/v2/events-over-time",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetEventsOverTimeResponse400
    | GetEventsOverTimeResponse500
    | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
    | None
):
    if response.status_code == 200:
        response_200 = GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = GetEventsOverTimeResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = GetEventsOverTimeResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetEventsOverTimeResponse400
    | GetEventsOverTimeResponse500
    | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
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
    body: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime,
) -> Response[
    GetEventsOverTimeResponse400
    | GetEventsOverTimeResponse500
    | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
]:
    """Get Kubernetes events over a specified time range.

     Retrieves and filters Kubernetes events, allowing for sorting and pagination.

    Args:
        body (GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventsOverTimeResponse400 | GetEventsOverTimeResponse500 | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse]
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
    body: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime,
) -> (
    GetEventsOverTimeResponse400
    | GetEventsOverTimeResponse500
    | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
    | None
):
    """Get Kubernetes events over a specified time range.

     Retrieves and filters Kubernetes events, allowing for sorting and pagination.

    Args:
        body (GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventsOverTimeResponse400 | GetEventsOverTimeResponse500 | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime,
) -> Response[
    GetEventsOverTimeResponse400
    | GetEventsOverTimeResponse500
    | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
]:
    """Get Kubernetes events over a specified time range.

     Retrieves and filters Kubernetes events, allowing for sorting and pagination.

    Args:
        body (GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventsOverTimeResponse400 | GetEventsOverTimeResponse500 | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime,
) -> (
    GetEventsOverTimeResponse400
    | GetEventsOverTimeResponse500
    | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
    | None
):
    """Get Kubernetes events over a specified time range.

     Retrieves and filters Kubernetes events, allowing for sorting and pagination.

    Args:
        body (GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventsOverTimeResponse400 | GetEventsOverTimeResponse500 | GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
