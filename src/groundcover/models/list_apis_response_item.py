from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ListApisResponseItem")


@_attrs_define
class ListApisResponseItem:
    """
    Attributes:
        cluster (str | Unset):
        container_name (str | Unset):
        env (str | Unset):
        error_rate (float | Unset):
        has_cross_az (bool | Unset):
        id (str | Unset):
        is_encrypted (bool | Unset):
        operation_name (str | Unset):
        p50 (float | Unset):
        p95 (float | Unset):
        p99 (float | Unset):
        request_rate (float | Unset):
        resource_type (str | Unset):
        server (str | Unset):
        server_is_external (bool | Unset):
        server_namespace (str | Unset):
        span_name (str | Unset):
        total_errors (int | Unset):
        total_latency_seconds (float | Unset):
        total_requests (int | Unset):
    """

    cluster: str | Unset = UNSET
    container_name: str | Unset = UNSET
    env: str | Unset = UNSET
    error_rate: float | Unset = UNSET
    has_cross_az: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    operation_name: str | Unset = UNSET
    p50: float | Unset = UNSET
    p95: float | Unset = UNSET
    p99: float | Unset = UNSET
    request_rate: float | Unset = UNSET
    resource_type: str | Unset = UNSET
    server: str | Unset = UNSET
    server_is_external: bool | Unset = UNSET
    server_namespace: str | Unset = UNSET
    span_name: str | Unset = UNSET
    total_errors: int | Unset = UNSET
    total_latency_seconds: float | Unset = UNSET
    total_requests: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        container_name = self.container_name

        env = self.env

        error_rate = self.error_rate

        has_cross_az = self.has_cross_az

        id = self.id

        is_encrypted = self.is_encrypted

        operation_name = self.operation_name

        p50 = self.p50

        p95 = self.p95

        p99 = self.p99

        request_rate = self.request_rate

        resource_type = self.resource_type

        server = self.server

        server_is_external = self.server_is_external

        server_namespace = self.server_namespace

        span_name = self.span_name

        total_errors = self.total_errors

        total_latency_seconds = self.total_latency_seconds

        total_requests = self.total_requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if container_name is not UNSET:
            field_dict["containerName"] = container_name
        if env is not UNSET:
            field_dict["env"] = env
        if error_rate is not UNSET:
            field_dict["errorRate"] = error_rate
        if has_cross_az is not UNSET:
            field_dict["hasCrossAz"] = has_cross_az
        if id is not UNSET:
            field_dict["id"] = id
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if p50 is not UNSET:
            field_dict["p50"] = p50
        if p95 is not UNSET:
            field_dict["p95"] = p95
        if p99 is not UNSET:
            field_dict["p99"] = p99
        if request_rate is not UNSET:
            field_dict["requestRate"] = request_rate
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if server is not UNSET:
            field_dict["server"] = server
        if server_is_external is not UNSET:
            field_dict["serverIsExternal"] = server_is_external
        if server_namespace is not UNSET:
            field_dict["serverNamespace"] = server_namespace
        if span_name is not UNSET:
            field_dict["spanName"] = span_name
        if total_errors is not UNSET:
            field_dict["totalErrors"] = total_errors
        if total_latency_seconds is not UNSET:
            field_dict["totalLatencySeconds"] = total_latency_seconds
        if total_requests is not UNSET:
            field_dict["totalRequests"] = total_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        container_name = d.pop("containerName", UNSET)

        env = d.pop("env", UNSET)

        error_rate = d.pop("errorRate", UNSET)

        has_cross_az = d.pop("hasCrossAz", UNSET)

        id = d.pop("id", UNSET)

        is_encrypted = d.pop("isEncrypted", UNSET)

        operation_name = d.pop("operationName", UNSET)

        p50 = d.pop("p50", UNSET)

        p95 = d.pop("p95", UNSET)

        p99 = d.pop("p99", UNSET)

        request_rate = d.pop("requestRate", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        server = d.pop("server", UNSET)

        server_is_external = d.pop("serverIsExternal", UNSET)

        server_namespace = d.pop("serverNamespace", UNSET)

        span_name = d.pop("spanName", UNSET)

        total_errors = d.pop("totalErrors", UNSET)

        total_latency_seconds = d.pop("totalLatencySeconds", UNSET)

        total_requests = d.pop("totalRequests", UNSET)

        list_apis_response_item = cls(
            cluster=cluster,
            container_name=container_name,
            env=env,
            error_rate=error_rate,
            has_cross_az=has_cross_az,
            id=id,
            is_encrypted=is_encrypted,
            operation_name=operation_name,
            p50=p50,
            p95=p95,
            p99=p99,
            request_rate=request_rate,
            resource_type=resource_type,
            server=server,
            server_is_external=server_is_external,
            server_namespace=server_namespace,
            span_name=span_name,
            total_errors=total_errors,
            total_latency_seconds=total_latency_seconds,
            total_requests=total_requests,
        )

        list_apis_response_item.additional_properties = d
        return list_apis_response_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
