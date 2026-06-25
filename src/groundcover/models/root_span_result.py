from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="RootSpanResult")


@_attrs_define
class RootSpanResult:
    """RootSpanResult is the scan target for GET_ROOT_SPAN_DETAILS and the item
    returned in the response. It contains only the fields consumed by the UI
    header panel; full payload data (bodies, headers) is fetched separately
    via /api/traces/v2/details when a span is selected.

        Attributes:
            cluster (str | Unset):
            env (str | Unset):
            is_encrypted (bool | Unset):
            is_external (bool | Unset):
            is_pii (bool | Unset):
            latency (float | Unset):
            namespace (str | Unset):
            resource (str | Unset):
            resource_truncated (bool | Unset):
            source (str | Unset):
            span_id (str | Unset):
            span_type (str | Unset):
            status (str | Unset):
            status_code (str | Unset):
            time (datetime.datetime | Unset):
            trace_id (str | Unset):
            workload (str | Unset):
    """

    cluster: str | Unset = UNSET
    env: str | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_pii: bool | Unset = UNSET
    latency: float | Unset = UNSET
    namespace: str | Unset = UNSET
    resource: str | Unset = UNSET
    resource_truncated: bool | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    span_type: str | Unset = UNSET
    status: str | Unset = UNSET
    status_code: str | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    trace_id: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        env = self.env

        is_encrypted = self.is_encrypted

        is_external = self.is_external

        is_pii = self.is_pii

        latency = self.latency

        namespace = self.namespace

        resource = self.resource

        resource_truncated = self.resource_truncated

        source = self.source

        span_id = self.span_id

        span_type = self.span_type

        status = self.status

        status_code = self.status_code

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        trace_id = self.trace_id

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if env is not UNSET:
            field_dict["env"] = env
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_pii is not UNSET:
            field_dict["isPii"] = is_pii
        if latency is not UNSET:
            field_dict["latency"] = latency
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if resource is not UNSET:
            field_dict["resource"] = resource
        if resource_truncated is not UNSET:
            field_dict["resourceTruncated"] = resource_truncated
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if span_type is not UNSET:
            field_dict["spanType"] = span_type
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if time is not UNSET:
            field_dict["time"] = time
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        env = d.pop("env", UNSET)

        is_encrypted = d.pop("isEncrypted", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_pii = d.pop("isPii", UNSET)

        latency = d.pop("latency", UNSET)

        namespace = d.pop("namespace", UNSET)

        resource = d.pop("resource", UNSET)

        resource_truncated = d.pop("resourceTruncated", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("spanId", UNSET)

        span_type = d.pop("spanType", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("statusCode", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset) or _time is None:
            time = UNSET
        else:
            time = parse_datetime(_time)

        trace_id = d.pop("traceId", UNSET)

        workload = d.pop("workload", UNSET)

        root_span_result = cls(
            cluster=cluster,
            env=env,
            is_encrypted=is_encrypted,
            is_external=is_external,
            is_pii=is_pii,
            latency=latency,
            namespace=namespace,
            resource=resource,
            resource_truncated=resource_truncated,
            source=source,
            span_id=span_id,
            span_type=span_type,
            status=status,
            status_code=status_code,
            time=time,
            trace_id=trace_id,
            workload=workload,
        )

        root_span_result.additional_properties = d
        return root_span_result

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
