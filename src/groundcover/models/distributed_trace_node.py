from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DistributedTraceNode")


@_attrs_define
class DistributedTraceNode:
    """
    Attributes:
        children (list[DistributedTraceNode] | Unset):
        client (str | Unset):
        client_namespace (str | Unset):
        cluster (str | Unset):
        duration (float | Unset):
        env (str | Unset):
        hints (list[str] | Unset):
        is_encrypted (bool | Unset):
        is_error (bool | Unset):
        is_external (bool | Unset):
        is_pii (bool | Unset):
        kind (str | Unset):
        namespace (str | Unset):
        operation_name (str | Unset):
        parent_span_id (str | Unset):
        partner_is_external (bool | Unset):
        partner_namespace (str | Unset):
        partner_workload (str | Unset):
        resource (str | Unset):
        resource_truncated (bool | Unset):
        server (str | Unset):
        server_namespace (str | Unset):
        service_name (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        span_name (str | Unset):
        span_timestamp (datetime.datetime | Unset):
        span_type (str | Unset):
        start (float | Unset):
        status (str | Unset):
        status_code (str | Unset):
        trace_id (str | Unset):
        type_ (str | Unset):
    """

    children: list[DistributedTraceNode] | Unset = UNSET
    client: str | Unset = UNSET
    client_namespace: str | Unset = UNSET
    cluster: str | Unset = UNSET
    duration: float | Unset = UNSET
    env: str | Unset = UNSET
    hints: list[str] | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    is_error: bool | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_pii: bool | Unset = UNSET
    kind: str | Unset = UNSET
    namespace: str | Unset = UNSET
    operation_name: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    partner_is_external: bool | Unset = UNSET
    partner_namespace: str | Unset = UNSET
    partner_workload: str | Unset = UNSET
    resource: str | Unset = UNSET
    resource_truncated: bool | Unset = UNSET
    server: str | Unset = UNSET
    server_namespace: str | Unset = UNSET
    service_name: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    span_name: str | Unset = UNSET
    span_timestamp: datetime.datetime | Unset = UNSET
    span_type: str | Unset = UNSET
    start: float | Unset = UNSET
    status: str | Unset = UNSET
    status_code: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        client = self.client

        client_namespace = self.client_namespace

        cluster = self.cluster

        duration = self.duration

        env = self.env

        hints: list[str] | Unset = UNSET
        if not isinstance(self.hints, Unset):
            hints = self.hints

        is_encrypted = self.is_encrypted

        is_error = self.is_error

        is_external = self.is_external

        is_pii = self.is_pii

        kind = self.kind

        namespace = self.namespace

        operation_name = self.operation_name

        parent_span_id = self.parent_span_id

        partner_is_external = self.partner_is_external

        partner_namespace = self.partner_namespace

        partner_workload = self.partner_workload

        resource = self.resource

        resource_truncated = self.resource_truncated

        server = self.server

        server_namespace = self.server_namespace

        service_name = self.service_name

        source = self.source

        span_id = self.span_id

        span_name = self.span_name

        span_timestamp: str | Unset = UNSET
        if not isinstance(self.span_timestamp, Unset):
            span_timestamp = self.span_timestamp.isoformat()

        span_type = self.span_type

        start = self.start

        status = self.status

        status_code = self.status_code

        trace_id = self.trace_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if client is not UNSET:
            field_dict["client"] = client
        if client_namespace is not UNSET:
            field_dict["clientNamespace"] = client_namespace
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if duration is not UNSET:
            field_dict["duration"] = duration
        if env is not UNSET:
            field_dict["env"] = env
        if hints is not UNSET:
            field_dict["hints"] = hints
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if is_error is not UNSET:
            field_dict["isError"] = is_error
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_pii is not UNSET:
            field_dict["isPii"] = is_pii
        if kind is not UNSET:
            field_dict["kind"] = kind
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if parent_span_id is not UNSET:
            field_dict["parentSpanID"] = parent_span_id
        if partner_is_external is not UNSET:
            field_dict["partnerIsExternal"] = partner_is_external
        if partner_namespace is not UNSET:
            field_dict["partnerNamespace"] = partner_namespace
        if partner_workload is not UNSET:
            field_dict["partnerWorkload"] = partner_workload
        if resource is not UNSET:
            field_dict["resource"] = resource
        if resource_truncated is not UNSET:
            field_dict["resourceTruncated"] = resource_truncated
        if server is not UNSET:
            field_dict["server"] = server
        if server_namespace is not UNSET:
            field_dict["serverNamespace"] = server_namespace
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if span_name is not UNSET:
            field_dict["spanName"] = span_name
        if span_timestamp is not UNSET:
            field_dict["spanTimestamp"] = span_timestamp
        if span_type is not UNSET:
            field_dict["spanType"] = span_type
        if start is not UNSET:
            field_dict["start"] = start
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        _children = d.pop("children", UNSET)
        children: list[DistributedTraceNode] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = DistributedTraceNode.from_dict(children_item_data)

                children.append(children_item)

        client = d.pop("client", UNSET)

        client_namespace = d.pop("clientNamespace", UNSET)

        cluster = d.pop("cluster", UNSET)

        duration = d.pop("duration", UNSET)

        env = d.pop("env", UNSET)

        hints = cast(list[str], d.pop("hints", UNSET))

        is_encrypted = d.pop("isEncrypted", UNSET)

        is_error = d.pop("isError", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_pii = d.pop("isPii", UNSET)

        kind = d.pop("kind", UNSET)

        namespace = d.pop("namespace", UNSET)

        operation_name = d.pop("operationName", UNSET)

        parent_span_id = d.pop("parentSpanID", UNSET)

        partner_is_external = d.pop("partnerIsExternal", UNSET)

        partner_namespace = d.pop("partnerNamespace", UNSET)

        partner_workload = d.pop("partnerWorkload", UNSET)

        resource = d.pop("resource", UNSET)

        resource_truncated = d.pop("resourceTruncated", UNSET)

        server = d.pop("server", UNSET)

        server_namespace = d.pop("serverNamespace", UNSET)

        service_name = d.pop("serviceName", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("spanId", UNSET)

        span_name = d.pop("spanName", UNSET)

        _span_timestamp = d.pop("spanTimestamp", UNSET)
        span_timestamp: datetime.datetime | Unset
        if isinstance(_span_timestamp, Unset) or _span_timestamp is None:
            span_timestamp = UNSET
        else:
            span_timestamp = parse_datetime(_span_timestamp)

        span_type = d.pop("spanType", UNSET)

        start = d.pop("start", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("statusCode", UNSET)

        trace_id = d.pop("traceId", UNSET)

        type_ = d.pop("type", UNSET)

        distributed_trace_node = cls(
            children=children,
            client=client,
            client_namespace=client_namespace,
            cluster=cluster,
            duration=duration,
            env=env,
            hints=hints,
            is_encrypted=is_encrypted,
            is_error=is_error,
            is_external=is_external,
            is_pii=is_pii,
            kind=kind,
            namespace=namespace,
            operation_name=operation_name,
            parent_span_id=parent_span_id,
            partner_is_external=partner_is_external,
            partner_namespace=partner_namespace,
            partner_workload=partner_workload,
            resource=resource,
            resource_truncated=resource_truncated,
            server=server,
            server_namespace=server_namespace,
            service_name=service_name,
            source=source,
            span_id=span_id,
            span_name=span_name,
            span_timestamp=span_timestamp,
            span_type=span_type,
            start=start,
            status=status,
            status_code=status_code,
            trace_id=trace_id,
            type_=type_,
        )

        distributed_trace_node.additional_properties = d
        return distributed_trace_node

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
