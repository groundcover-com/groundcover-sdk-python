from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_record_attributes import SpanRecordAttributes
    from ..models.span_record_query_parameters import SpanRecordQueryParameters
    from ..models.span_record_request_headers import SpanRecordRequestHeaders
    from ..models.span_record_response_headers import SpanRecordResponseHeaders
    from ..models.span_record_tags import SpanRecordTags


T = TypeVar("T", bound="SpanRecord")


@_attrs_define
class SpanRecord:
    """
    Attributes:
        attributes (SpanRecordAttributes | Unset):
        client (str | Unset):
        cluster (str | Unset):
        end_time (datetime.datetime | Unset):
        env (str | Unset):
        is_pii (bool | Unset):
        kind (str | Unset):
        namespace (str | Unset):
        parent_id (str | Unset):
        protocol_type (str | Unset):
        query_parameters (SpanRecordQueryParameters | Unset):
        request_body (str | Unset):
        request_headers (SpanRecordRequestHeaders | Unset):
        response_body (str | Unset):
        response_headers (SpanRecordResponseHeaders | Unset):
        server (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        span_name (str | Unset):
        start_time (datetime.datetime | Unset):
        status (str | Unset):
        tags (SpanRecordTags | Unset):
        trace_id (str | Unset):
        workload (str | Unset):
    """

    attributes: SpanRecordAttributes | Unset = UNSET
    client: str | Unset = UNSET
    cluster: str | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    env: str | Unset = UNSET
    is_pii: bool | Unset = UNSET
    kind: str | Unset = UNSET
    namespace: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    protocol_type: str | Unset = UNSET
    query_parameters: SpanRecordQueryParameters | Unset = UNSET
    request_body: str | Unset = UNSET
    request_headers: SpanRecordRequestHeaders | Unset = UNSET
    response_body: str | Unset = UNSET
    response_headers: SpanRecordResponseHeaders | Unset = UNSET
    server: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    span_name: str | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    tags: SpanRecordTags | Unset = UNSET
    trace_id: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        client = self.client

        cluster = self.cluster

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        env = self.env

        is_pii = self.is_pii

        kind = self.kind

        namespace = self.namespace

        parent_id = self.parent_id

        protocol_type = self.protocol_type

        query_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_parameters, Unset):
            query_parameters = self.query_parameters.to_dict()

        request_body = self.request_body

        request_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_headers, Unset):
            request_headers = self.request_headers.to_dict()

        response_body = self.response_body

        response_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_headers, Unset):
            response_headers = self.response_headers.to_dict()

        server = self.server

        source = self.source

        span_id = self.span_id

        span_name = self.span_name

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        status = self.status

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        trace_id = self.trace_id

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if client is not UNSET:
            field_dict["client"] = client
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if env is not UNSET:
            field_dict["env"] = env
        if is_pii is not UNSET:
            field_dict["is_pii"] = is_pii
        if kind is not UNSET:
            field_dict["kind"] = kind
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if protocol_type is not UNSET:
            field_dict["protocol_type"] = protocol_type
        if query_parameters is not UNSET:
            field_dict["query_parameters"] = query_parameters
        if request_body is not UNSET:
            field_dict["request_body"] = request_body
        if request_headers is not UNSET:
            field_dict["request_headers"] = request_headers
        if response_body is not UNSET:
            field_dict["response_body"] = response_body
        if response_headers is not UNSET:
            field_dict["response_headers"] = response_headers
        if server is not UNSET:
            field_dict["server"] = server
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if span_name is not UNSET:
            field_dict["span_name"] = span_name
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_record_attributes import SpanRecordAttributes
        from ..models.span_record_query_parameters import SpanRecordQueryParameters
        from ..models.span_record_request_headers import SpanRecordRequestHeaders
        from ..models.span_record_response_headers import SpanRecordResponseHeaders
        from ..models.span_record_tags import SpanRecordTags

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: SpanRecordAttributes | Unset
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = SpanRecordAttributes.from_dict(_attributes)

        client = d.pop("client", UNSET)

        cluster = d.pop("cluster", UNSET)

        _end_time = d.pop("end_time", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset) or _end_time is None:
            end_time = UNSET
        else:
            end_time = parse_datetime(_end_time)

        env = d.pop("env", UNSET)

        is_pii = d.pop("is_pii", UNSET)

        kind = d.pop("kind", UNSET)

        namespace = d.pop("namespace", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        protocol_type = d.pop("protocol_type", UNSET)

        _query_parameters = d.pop("query_parameters", UNSET)
        query_parameters: SpanRecordQueryParameters | Unset
        if isinstance(_query_parameters, Unset) or _query_parameters is None:
            query_parameters = UNSET
        else:
            query_parameters = SpanRecordQueryParameters.from_dict(_query_parameters)

        request_body = d.pop("request_body", UNSET)

        _request_headers = d.pop("request_headers", UNSET)
        request_headers: SpanRecordRequestHeaders | Unset
        if isinstance(_request_headers, Unset) or _request_headers is None:
            request_headers = UNSET
        else:
            request_headers = SpanRecordRequestHeaders.from_dict(_request_headers)

        response_body = d.pop("response_body", UNSET)

        _response_headers = d.pop("response_headers", UNSET)
        response_headers: SpanRecordResponseHeaders | Unset
        if isinstance(_response_headers, Unset) or _response_headers is None:
            response_headers = UNSET
        else:
            response_headers = SpanRecordResponseHeaders.from_dict(_response_headers)

        server = d.pop("server", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("span_id", UNSET)

        span_name = d.pop("span_name", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset) or _start_time is None:
            start_time = UNSET
        else:
            start_time = parse_datetime(_start_time)

        status = d.pop("status", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: SpanRecordTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = SpanRecordTags.from_dict(_tags)

        trace_id = d.pop("trace_id", UNSET)

        workload = d.pop("workload", UNSET)

        span_record = cls(
            attributes=attributes,
            client=client,
            cluster=cluster,
            end_time=end_time,
            env=env,
            is_pii=is_pii,
            kind=kind,
            namespace=namespace,
            parent_id=parent_id,
            protocol_type=protocol_type,
            query_parameters=query_parameters,
            request_body=request_body,
            request_headers=request_headers,
            response_body=response_body,
            response_headers=response_headers,
            server=server,
            source=source,
            span_id=span_id,
            span_name=span_name,
            start_time=start_time,
            status=status,
            tags=tags,
            trace_id=trace_id,
            workload=workload,
        )

        span_record.additional_properties = d
        return span_record

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
