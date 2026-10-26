from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.get_profiling_flamegraph_diff_response_400 import GetProfilingFlamegraphDiffResponse400
from ...models.get_profiling_flamegraph_diff_response_404 import GetProfilingFlamegraphDiffResponse404
from ...models.get_profiling_flamegraph_diff_response_422 import GetProfilingFlamegraphDiffResponse422
from ...models.get_profiling_flamegraph_diff_response_500 import GetProfilingFlamegraphDiffResponse500
from ...models.get_profiling_flamegraph_diff_response_504 import GetProfilingFlamegraphDiffResponse504
from ...models.profiling_flamegraph_diff_response import ProfilingFlamegraphDiffResponse
from ..._generated_types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
    focus: str | Unset = UNSET,
    frame_filter: str | Unset = UNSET,
    invert: bool | Unset = UNSET,
    base_start: datetime.datetime | Unset = UNSET,
    base_end: datetime.datetime | Unset = UNSET,
    base_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    params["query"] = query

    params["limit"] = limit

    params["focus"] = focus

    params["frameFilter"] = frame_filter

    params["invert"] = invert

    json_base_start: str | Unset = UNSET
    if not isinstance(base_start, Unset):
        json_base_start = base_start.isoformat()
    params["baseStart"] = json_base_start

    json_base_end: str | Unset = UNSET
    if not isinstance(base_end, Unset):
        json_base_end = base_end.isoformat()
    params["baseEnd"] = json_base_end

    params["baseQuery"] = base_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/profiling/v1/flamegraph-diff",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProfilingFlamegraphDiffResponse400
    | GetProfilingFlamegraphDiffResponse404
    | GetProfilingFlamegraphDiffResponse422
    | GetProfilingFlamegraphDiffResponse500
    | GetProfilingFlamegraphDiffResponse504
    | ProfilingFlamegraphDiffResponse
    | None
):
    if response.status_code == 200:
        response_200 = ProfilingFlamegraphDiffResponse.from_dict(response.json()) if response.content else None

        return response_200

    if response.status_code == 400:
        response_400 = GetProfilingFlamegraphDiffResponse400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 404:
        response_404 = GetProfilingFlamegraphDiffResponse404.from_dict(response.json()) if response.content else None

        return response_404

    if response.status_code == 422:
        response_422 = GetProfilingFlamegraphDiffResponse422.from_dict(response.json()) if response.content else None

        return response_422

    if response.status_code == 500:
        response_500 = GetProfilingFlamegraphDiffResponse500.from_dict(response.json()) if response.content else None

        return response_500

    if response.status_code == 504:
        response_504 = GetProfilingFlamegraphDiffResponse504.from_dict(response.json()) if response.content else None

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProfilingFlamegraphDiffResponse400
    | GetProfilingFlamegraphDiffResponse404
    | GetProfilingFlamegraphDiffResponse422
    | GetProfilingFlamegraphDiffResponse500
    | GetProfilingFlamegraphDiffResponse504
    | ProfilingFlamegraphDiffResponse
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
    focus: str | Unset = UNSET,
    frame_filter: str | Unset = UNSET,
    invert: bool | Unset = UNSET,
    base_start: datetime.datetime | Unset = UNSET,
    base_end: datetime.datetime | Unset = UNSET,
    base_query: str | Unset = UNSET,
) -> Response[
    GetProfilingFlamegraphDiffResponse400
    | GetProfilingFlamegraphDiffResponse404
    | GetProfilingFlamegraphDiffResponse422
    | GetProfilingFlamegraphDiffResponse500
    | GetProfilingFlamegraphDiffResponse504
    | ProfilingFlamegraphDiffResponse
]:
    """Fold the heaviest stacks of a current and a baseline selection into one call tree with weights per
    side.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):
        focus (str | Unset):
        frame_filter (str | Unset):
        invert (bool | Unset):
        base_start (datetime.datetime | Unset):
        base_end (datetime.datetime | Unset):
        base_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilingFlamegraphDiffResponse400 | GetProfilingFlamegraphDiffResponse404 | GetProfilingFlamegraphDiffResponse422 | GetProfilingFlamegraphDiffResponse500 | GetProfilingFlamegraphDiffResponse504 | ProfilingFlamegraphDiffResponse]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        query=query,
        limit=limit,
        focus=focus,
        frame_filter=frame_filter,
        invert=invert,
        base_start=base_start,
        base_end=base_end,
        base_query=base_query,
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
    focus: str | Unset = UNSET,
    frame_filter: str | Unset = UNSET,
    invert: bool | Unset = UNSET,
    base_start: datetime.datetime | Unset = UNSET,
    base_end: datetime.datetime | Unset = UNSET,
    base_query: str | Unset = UNSET,
) -> (
    GetProfilingFlamegraphDiffResponse400
    | GetProfilingFlamegraphDiffResponse404
    | GetProfilingFlamegraphDiffResponse422
    | GetProfilingFlamegraphDiffResponse500
    | GetProfilingFlamegraphDiffResponse504
    | ProfilingFlamegraphDiffResponse
    | None
):
    """Fold the heaviest stacks of a current and a baseline selection into one call tree with weights per
    side.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):
        focus (str | Unset):
        frame_filter (str | Unset):
        invert (bool | Unset):
        base_start (datetime.datetime | Unset):
        base_end (datetime.datetime | Unset):
        base_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilingFlamegraphDiffResponse400 | GetProfilingFlamegraphDiffResponse404 | GetProfilingFlamegraphDiffResponse422 | GetProfilingFlamegraphDiffResponse500 | GetProfilingFlamegraphDiffResponse504 | ProfilingFlamegraphDiffResponse
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        query=query,
        limit=limit,
        focus=focus,
        frame_filter=frame_filter,
        invert=invert,
        base_start=base_start,
        base_end=base_end,
        base_query=base_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime,
    end: datetime.datetime,
    query: str,
    limit: int | Unset = UNSET,
    focus: str | Unset = UNSET,
    frame_filter: str | Unset = UNSET,
    invert: bool | Unset = UNSET,
    base_start: datetime.datetime | Unset = UNSET,
    base_end: datetime.datetime | Unset = UNSET,
    base_query: str | Unset = UNSET,
) -> Response[
    GetProfilingFlamegraphDiffResponse400
    | GetProfilingFlamegraphDiffResponse404
    | GetProfilingFlamegraphDiffResponse422
    | GetProfilingFlamegraphDiffResponse500
    | GetProfilingFlamegraphDiffResponse504
    | ProfilingFlamegraphDiffResponse
]:
    """Fold the heaviest stacks of a current and a baseline selection into one call tree with weights per
    side.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):
        focus (str | Unset):
        frame_filter (str | Unset):
        invert (bool | Unset):
        base_start (datetime.datetime | Unset):
        base_end (datetime.datetime | Unset):
        base_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProfilingFlamegraphDiffResponse400 | GetProfilingFlamegraphDiffResponse404 | GetProfilingFlamegraphDiffResponse422 | GetProfilingFlamegraphDiffResponse500 | GetProfilingFlamegraphDiffResponse504 | ProfilingFlamegraphDiffResponse]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        query=query,
        limit=limit,
        focus=focus,
        frame_filter=frame_filter,
        invert=invert,
        base_start=base_start,
        base_end=base_end,
        base_query=base_query,
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
    focus: str | Unset = UNSET,
    frame_filter: str | Unset = UNSET,
    invert: bool | Unset = UNSET,
    base_start: datetime.datetime | Unset = UNSET,
    base_end: datetime.datetime | Unset = UNSET,
    base_query: str | Unset = UNSET,
) -> (
    GetProfilingFlamegraphDiffResponse400
    | GetProfilingFlamegraphDiffResponse404
    | GetProfilingFlamegraphDiffResponse422
    | GetProfilingFlamegraphDiffResponse500
    | GetProfilingFlamegraphDiffResponse504
    | ProfilingFlamegraphDiffResponse
    | None
):
    """Fold the heaviest stacks of a current and a baseline selection into one call tree with weights per
    side.

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        query (str):
        limit (int | Unset):
        focus (str | Unset):
        frame_filter (str | Unset):
        invert (bool | Unset):
        base_start (datetime.datetime | Unset):
        base_end (datetime.datetime | Unset):
        base_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProfilingFlamegraphDiffResponse400 | GetProfilingFlamegraphDiffResponse404 | GetProfilingFlamegraphDiffResponse422 | GetProfilingFlamegraphDiffResponse500 | GetProfilingFlamegraphDiffResponse504 | ProfilingFlamegraphDiffResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            query=query,
            limit=limit,
            focus=focus,
            frame_filter=frame_filter,
            invert=invert,
            base_start=base_start,
            base_end=base_end,
            base_query=base_query,
        )
    ).parsed
