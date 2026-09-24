from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_profiling_flamegraph_response_400 import GetProfilingFlamegraphResponse400
from ...models.get_profiling_flamegraph_response_404 import GetProfilingFlamegraphResponse404
from ...models.get_profiling_flamegraph_response_422 import GetProfilingFlamegraphResponse422
from ...models.get_profiling_flamegraph_response_500 import GetProfilingFlamegraphResponse500
from ...models.get_profiling_flamegraph_response_504 import GetProfilingFlamegraphResponse504
from ...models.profiling_flamegraph_response import ProfilingFlamegraphResponse
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    params["query"] = query

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/profiling/flamegraph",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProfilingFlamegraphResponse400
    | GetProfilingFlamegraphResponse404
    | GetProfilingFlamegraphResponse422
    | GetProfilingFlamegraphResponse500
    | GetProfilingFlamegraphResponse504
    | ProfilingFlamegraphResponse
    | None
):
    if response.status_code == 200:
        response_200 = ProfilingFlamegraphResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = GetProfilingFlamegraphResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = GetProfilingFlamegraphResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 422:
        response_422 = GetProfilingFlamegraphResponse422.from_dict(response.json()) if response.content else None

        return response_422

    if response.status_code == 500:
        response_500 = GetProfilingFlamegraphResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 504:
        response_504 = GetProfilingFlamegraphResponse504.from_dict(response.json()) if response.content else None

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProfilingFlamegraphResponse400
    | GetProfilingFlamegraphResponse404
    | GetProfilingFlamegraphResponse422
    | GetProfilingFlamegraphResponse500
    | GetProfilingFlamegraphResponse504
    | ProfilingFlamegraphResponse
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
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
) -> Response[
    GetProfilingFlamegraphResponse400
    | GetProfilingFlamegraphResponse404
    | GetProfilingFlamegraphResponse422
    | GetProfilingFlamegraphResponse500
    | GetProfilingFlamegraphResponse504
    | ProfilingFlamegraphResponse
]:
    """Fold the heaviest profiling stacks into a call tree with truncation accounting.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilingFlamegraphResponse400 | GetProfilingFlamegraphResponse404 | GetProfilingFlamegraphResponse422 | GetProfilingFlamegraphResponse500 | GetProfilingFlamegraphResponse504 | ProfilingFlamegraphResponse]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        query=query,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
) -> (
    GetProfilingFlamegraphResponse400
    | GetProfilingFlamegraphResponse404
    | GetProfilingFlamegraphResponse422
    | GetProfilingFlamegraphResponse500
    | GetProfilingFlamegraphResponse504
    | ProfilingFlamegraphResponse
    | None
):
    """Fold the heaviest profiling stacks into a call tree with truncation accounting.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilingFlamegraphResponse400 | GetProfilingFlamegraphResponse404 | GetProfilingFlamegraphResponse422 | GetProfilingFlamegraphResponse500 | GetProfilingFlamegraphResponse504 | ProfilingFlamegraphResponse
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        query=query,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
) -> Response[
    GetProfilingFlamegraphResponse400
    | GetProfilingFlamegraphResponse404
    | GetProfilingFlamegraphResponse422
    | GetProfilingFlamegraphResponse500
    | GetProfilingFlamegraphResponse504
    | ProfilingFlamegraphResponse
]:
    """Fold the heaviest profiling stacks into a call tree with truncation accounting.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilingFlamegraphResponse400 | GetProfilingFlamegraphResponse404 | GetProfilingFlamegraphResponse422 | GetProfilingFlamegraphResponse500 | GetProfilingFlamegraphResponse504 | ProfilingFlamegraphResponse]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        query=query,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
) -> (
    GetProfilingFlamegraphResponse400
    | GetProfilingFlamegraphResponse404
    | GetProfilingFlamegraphResponse422
    | GetProfilingFlamegraphResponse500
    | GetProfilingFlamegraphResponse504
    | ProfilingFlamegraphResponse
    | None
):
    """Fold the heaviest profiling stacks into a call tree with truncation accounting.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilingFlamegraphResponse400 | GetProfilingFlamegraphResponse404 | GetProfilingFlamegraphResponse422 | GetProfilingFlamegraphResponse500 | GetProfilingFlamegraphResponse504 | ProfilingFlamegraphResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            query=query,
            limit=limit,
        )
    ).parsed
