from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TraceGraphEdge")


@_attrs_define
class TraceGraphEdge:
    """
    Attributes:
        cluster (str | Unset):
        duplication_count (int | Unset):
        id (str | Unset):
        is_error (bool | Unset):
        protocol (str | Unset):
        source (str | Unset):
        span_timestamp (datetime.datetime | Unset):
        subtype (str | Unset):
        target (str | Unset):
    """

    cluster: str | Unset = UNSET
    duplication_count: int | Unset = UNSET
    id: str | Unset = UNSET
    is_error: bool | Unset = UNSET
    protocol: str | Unset = UNSET
    source: str | Unset = UNSET
    span_timestamp: datetime.datetime | Unset = UNSET
    subtype: str | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        duplication_count = self.duplication_count

        id = self.id

        is_error = self.is_error

        protocol = self.protocol

        source = self.source

        span_timestamp: str | Unset = UNSET
        if not isinstance(self.span_timestamp, Unset):
            span_timestamp = self.span_timestamp.isoformat()

        subtype = self.subtype

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if duplication_count is not UNSET:
            field_dict["duplicationCount"] = duplication_count
        if id is not UNSET:
            field_dict["id"] = id
        if is_error is not UNSET:
            field_dict["isError"] = is_error
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if source is not UNSET:
            field_dict["source"] = source
        if span_timestamp is not UNSET:
            field_dict["spanTimestamp"] = span_timestamp
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if target is not UNSET:
            field_dict["target"] = target

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

        duplication_count = d.pop("duplicationCount", UNSET)

        id = d.pop("id", UNSET)

        is_error = d.pop("isError", UNSET)

        protocol = d.pop("protocol", UNSET)

        source = d.pop("source", UNSET)

        _span_timestamp = d.pop("spanTimestamp", UNSET)
        span_timestamp: datetime.datetime | Unset
        if isinstance(_span_timestamp, Unset) or _span_timestamp is None:
            span_timestamp = UNSET
        else:
            span_timestamp = parse_datetime(_span_timestamp)

        subtype = d.pop("subtype", UNSET)

        target = d.pop("target", UNSET)

        trace_graph_edge = cls(
            cluster=cluster,
            duplication_count=duplication_count,
            id=id,
            is_error=is_error,
            protocol=protocol,
            source=source,
            span_timestamp=span_timestamp,
            subtype=subtype,
            target=target,
        )

        trace_graph_edge.additional_properties = d
        return trace_graph_edge

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
