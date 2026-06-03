from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_record_attributes import LogRecordAttributes
    from ..models.log_record_tags import LogRecordTags


T = TypeVar("T", bound="LogRecord")


@_attrs_define
class LogRecord:
    """
    Attributes:
        attributes (LogRecordAttributes | Unset):
        body (str | Unset):
        cluster (str | Unset):
        container_name (str | Unset):
        env (str | Unset):
        format_ (str | Unset):
        guid (str | Unset):
        level (str | Unset):
        namespace (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        tags (LogRecordTags | Unset):
        time (datetime.datetime | Unset):
        trace_id (str | Unset):
        workload (str | Unset):
    """

    attributes: LogRecordAttributes | Unset = UNSET
    body: str | Unset = UNSET
    cluster: str | Unset = UNSET
    container_name: str | Unset = UNSET
    env: str | Unset = UNSET
    format_: str | Unset = UNSET
    guid: str | Unset = UNSET
    level: str | Unset = UNSET
    namespace: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    tags: LogRecordTags | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    trace_id: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        body = self.body

        cluster = self.cluster

        container_name = self.container_name

        env = self.env

        format_ = self.format_

        guid = self.guid

        level = self.level

        namespace = self.namespace

        source = self.source

        span_id = self.span_id

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        trace_id = self.trace_id

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if body is not UNSET:
            field_dict["body"] = body
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if container_name is not UNSET:
            field_dict["container_name"] = container_name
        if env is not UNSET:
            field_dict["env"] = env
        if format_ is not UNSET:
            field_dict["format"] = format_
        if guid is not UNSET:
            field_dict["guid"] = guid
        if level is not UNSET:
            field_dict["level"] = level
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if time is not UNSET:
            field_dict["time"] = time
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_record_attributes import LogRecordAttributes
        from ..models.log_record_tags import LogRecordTags

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: LogRecordAttributes | Unset
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = LogRecordAttributes.from_dict(_attributes)

        body = d.pop("body", UNSET)

        cluster = d.pop("cluster", UNSET)

        container_name = d.pop("container_name", UNSET)

        env = d.pop("env", UNSET)

        format_ = d.pop("format", UNSET)

        guid = d.pop("guid", UNSET)

        level = d.pop("level", UNSET)

        namespace = d.pop("namespace", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("span_id", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: LogRecordTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = LogRecordTags.from_dict(_tags)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset) or _time is None:
            time = UNSET
        else:
            time = parse_datetime(_time)

        trace_id = d.pop("trace_id", UNSET)

        workload = d.pop("workload", UNSET)

        log_record = cls(
            attributes=attributes,
            body=body,
            cluster=cluster,
            container_name=container_name,
            env=env,
            format_=format_,
            guid=guid,
            level=level,
            namespace=namespace,
            source=source,
            span_id=span_id,
            tags=tags,
            time=time,
            trace_id=trace_id,
            workload=workload,
        )

        log_record.additional_properties = d
        return log_record

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
