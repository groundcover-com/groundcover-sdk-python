from __future__ import annotations

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import _generated_errors as errors
from ..._generated_client import AuthenticatedClient, Client
from ...models.export_body import ExportBody
from ...models.export_monitors_v2_response_400 import ExportMonitorsV2Response400
from ...models.export_monitors_v2_response_500 import ExportMonitorsV2Response500
from ..._generated_types import Response


def _get_kwargs(
    *,
    body: ExportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/monitors/export",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = ExportMonitorsV2Response400.from_dict(response.json()) if response.content else None

        return response_400

    if response.status_code == 500:
        response_500 = ExportMonitorsV2Response500.from_dict(response.json()) if response.content else None

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportBody,
) -> Response[ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str]:
    """Export v2 monitors as Terraform

     One HCL document with a groundcover_monitor_v2 resource per uuid, in request
    order. A uuid that is unknown, deleted, or outside the caller's tenant and
    backend, and a monitor the resource cannot express, each become an HCL
    comment in place of the resource; the export never fails on one row. A uuid
    repeated in the request is rendered once.

    Args:
        body (ExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str]
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
    body: ExportBody,
) -> ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str | None:
    """Export v2 monitors as Terraform

     One HCL document with a groundcover_monitor_v2 resource per uuid, in request
    order. A uuid that is unknown, deleted, or outside the caller's tenant and
    backend, and a monitor the resource cannot express, each become an HCL
    comment in place of the resource; the export never fails on one row. A uuid
    repeated in the request is rendered once.

    Args:
        body (ExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportBody,
) -> Response[ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str]:
    """Export v2 monitors as Terraform

     One HCL document with a groundcover_monitor_v2 resource per uuid, in request
    order. A uuid that is unknown, deleted, or outside the caller's tenant and
    backend, and a monitor the resource cannot express, each become an HCL
    comment in place of the resource; the export never fails on one row. A uuid
    repeated in the request is rendered once.

    Args:
        body (ExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExportBody,
) -> ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str | None:
    """Export v2 monitors as Terraform

     One HCL document with a groundcover_monitor_v2 resource per uuid, in request
    order. A uuid that is unknown, deleted, or outside the caller's tenant and
    backend, and a monitor the resource cannot express, each become an HCL
    comment in place of the resource; the export never fails on one row. A uuid
    repeated in the request is rendered once.

    Args:
        body (ExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportMonitorsV2Response400 | ExportMonitorsV2Response500 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
