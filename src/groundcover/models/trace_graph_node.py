from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TraceGraphNode")


@_attrs_define
class TraceGraphNode:
    """
    Attributes:
        client (str | Unset):
        client_namespace (str | Unset):
        duplication_count (int | Unset):
        id (str | Unset):
        kind (str | Unset):
        resource (str | Unset):
        server (str | Unset):
        server_namespace (str | Unset):
        span_timestamp (datetime.datetime | Unset):
    """

    client: str | Unset = UNSET
    client_namespace: str | Unset = UNSET
    duplication_count: int | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = UNSET
    resource: str | Unset = UNSET
    server: str | Unset = UNSET
    server_namespace: str | Unset = UNSET
    span_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client = self.client

        client_namespace = self.client_namespace

        duplication_count = self.duplication_count

        id = self.id

        kind = self.kind

        resource = self.resource

        server = self.server

        server_namespace = self.server_namespace

        span_timestamp: str | Unset = UNSET
        if not isinstance(self.span_timestamp, Unset):
            span_timestamp = self.span_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client
        if client_namespace is not UNSET:
            field_dict["clientNamespace"] = client_namespace
        if duplication_count is not UNSET:
            field_dict["duplicationCount"] = duplication_count
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if resource is not UNSET:
            field_dict["resource"] = resource
        if server is not UNSET:
            field_dict["server"] = server
        if server_namespace is not UNSET:
            field_dict["serverNamespace"] = server_namespace
        if span_timestamp is not UNSET:
            field_dict["spanTimestamp"] = span_timestamp

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
        client = d.pop("client", UNSET)

        client_namespace = d.pop("clientNamespace", UNSET)

        duplication_count = d.pop("duplicationCount", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        resource = d.pop("resource", UNSET)

        server = d.pop("server", UNSET)

        server_namespace = d.pop("serverNamespace", UNSET)

        _span_timestamp = d.pop("spanTimestamp", UNSET)
        span_timestamp: datetime.datetime | Unset
        if isinstance(_span_timestamp, Unset) or _span_timestamp is None:
            span_timestamp = UNSET
        else:
            span_timestamp = parse_datetime(_span_timestamp)

        trace_graph_node = cls(
            client=client,
            client_namespace=client_namespace,
            duplication_count=duplication_count,
            id=id,
            kind=kind,
            resource=resource,
            server=server,
            server_namespace=server_namespace,
            span_timestamp=span_timestamp,
        )

        trace_graph_node.additional_properties = d
        return trace_graph_node

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
