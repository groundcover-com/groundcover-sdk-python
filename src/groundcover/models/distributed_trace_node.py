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
        duration (float | Unset):
        hints (list[str] | Unset):
        is_error (bool | Unset):
        is_external (bool | Unset):
        operation_name (str | Unset):
        parent_span_id (str | Unset):
        resource (str | Unset):
        service_name (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        span_name (str | Unset):
        span_timestamp (datetime.datetime | Unset):
        span_type (str | Unset):
        start (float | Unset):
        status_code (str | Unset):
        trace_id (str | Unset):
        type_ (str | Unset):
    """

    children: list[DistributedTraceNode] | Unset = UNSET
    duration: float | Unset = UNSET
    hints: list[str] | Unset = UNSET
    is_error: bool | Unset = UNSET
    is_external: bool | Unset = UNSET
    operation_name: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    resource: str | Unset = UNSET
    service_name: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    span_name: str | Unset = UNSET
    span_timestamp: datetime.datetime | Unset = UNSET
    span_type: str | Unset = UNSET
    start: float | Unset = UNSET
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

        duration = self.duration

        hints: list[str] | Unset = UNSET
        if not isinstance(self.hints, Unset):
            hints = self.hints

        is_error = self.is_error

        is_external = self.is_external

        operation_name = self.operation_name

        parent_span_id = self.parent_span_id

        resource = self.resource

        service_name = self.service_name

        source = self.source

        span_id = self.span_id

        span_name = self.span_name

        span_timestamp: str | Unset = UNSET
        if not isinstance(self.span_timestamp, Unset):
            span_timestamp = self.span_timestamp.isoformat()

        span_type = self.span_type

        start = self.start

        status_code = self.status_code

        trace_id = self.trace_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if duration is not UNSET:
            field_dict["duration"] = duration
        if hints is not UNSET:
            field_dict["hints"] = hints
        if is_error is not UNSET:
            field_dict["isError"] = is_error
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if parent_span_id is not UNSET:
            field_dict["parentSpanID"] = parent_span_id
        if resource is not UNSET:
            field_dict["resource"] = resource
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

        duration = d.pop("duration", UNSET)

        hints = cast(list[str], d.pop("hints", UNSET))

        is_error = d.pop("isError", UNSET)

        is_external = d.pop("isExternal", UNSET)

        operation_name = d.pop("operationName", UNSET)

        parent_span_id = d.pop("parentSpanID", UNSET)

        resource = d.pop("resource", UNSET)

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

        status_code = d.pop("statusCode", UNSET)

        trace_id = d.pop("traceId", UNSET)

        type_ = d.pop("type", UNSET)

        distributed_trace_node = cls(
            children=children,
            duration=duration,
            hints=hints,
            is_error=is_error,
            is_external=is_external,
            operation_name=operation_name,
            parent_span_id=parent_span_id,
            resource=resource,
            service_name=service_name,
            source=source,
            span_id=span_id,
            span_name=span_name,
            span_timestamp=span_timestamp,
            span_type=span_type,
            start=start,
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
