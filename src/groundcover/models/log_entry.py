from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_entry_additional_columns import LogEntryAdditionalColumns
    from ..models.log_entry_metadata import LogEntryMetadata


T = TypeVar("T", bound="LogEntry")


@_attrs_define
class LogEntry:
    """
    Attributes:
        additional_columns (LogEntryAdditionalColumns | Unset):
        cluster (str | Unset):
        container (str | Unset):
        env (str | Unset):
        env_type (str | Unset):
        format_ (str | Unset):
        function_name (str | Unset):
        guid (str | Unset):
        host (str | Unset):
        instance (str | Unset):
        instance_id (str | Unset):
        instance_uid (str | Unset):
        lambda_arn (str | Unset):
        level (str | Unset):
        line (str | Unset):
        metadata (LogEntryMetadata | Unset):
        namespace (str | Unset):
        node (str | Unset):
        pod_name (str | Unset):
        pod_uid (str | Unset):
        service (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        timestamp (datetime.datetime | Unset):
        trace_id (str | Unset):
        workload (str | Unset):
    """

    additional_columns: LogEntryAdditionalColumns | Unset = UNSET
    cluster: str | Unset = UNSET
    container: str | Unset = UNSET
    env: str | Unset = UNSET
    env_type: str | Unset = UNSET
    format_: str | Unset = UNSET
    function_name: str | Unset = UNSET
    guid: str | Unset = UNSET
    host: str | Unset = UNSET
    instance: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    instance_uid: str | Unset = UNSET
    lambda_arn: str | Unset = UNSET
    level: str | Unset = UNSET
    line: str | Unset = UNSET
    metadata: LogEntryMetadata | Unset = UNSET
    namespace: str | Unset = UNSET
    node: str | Unset = UNSET
    pod_name: str | Unset = UNSET
    pod_uid: str | Unset = UNSET
    service: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    trace_id: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_columns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_columns, Unset):
            additional_columns = self.additional_columns.to_dict()

        cluster = self.cluster

        container = self.container

        env = self.env

        env_type = self.env_type

        format_ = self.format_

        function_name = self.function_name

        guid = self.guid

        host = self.host

        instance = self.instance

        instance_id = self.instance_id

        instance_uid = self.instance_uid

        lambda_arn = self.lambda_arn

        level = self.level

        line = self.line

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        namespace = self.namespace

        node = self.node

        pod_name = self.pod_name

        pod_uid = self.pod_uid

        service = self.service

        source = self.source

        span_id = self.span_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        trace_id = self.trace_id

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_columns is not UNSET:
            field_dict["additionalColumns"] = additional_columns
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if container is not UNSET:
            field_dict["container"] = container
        if env is not UNSET:
            field_dict["env"] = env
        if env_type is not UNSET:
            field_dict["envType"] = env_type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if host is not UNSET:
            field_dict["host"] = host
        if instance is not UNSET:
            field_dict["instance"] = instance
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if lambda_arn is not UNSET:
            field_dict["lambdaArn"] = lambda_arn
        if level is not UNSET:
            field_dict["level"] = level
        if line is not UNSET:
            field_dict["line"] = line
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if node is not UNSET:
            field_dict["node"] = node
        if pod_name is not UNSET:
            field_dict["pod_name"] = pod_name
        if pod_uid is not UNSET:
            field_dict["podUid"] = pod_uid
        if service is not UNSET:
            field_dict["service"] = service
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_entry_additional_columns import LogEntryAdditionalColumns
        from ..models.log_entry_metadata import LogEntryMetadata

        d = dict(src_dict)
        _additional_columns = d.pop("additionalColumns", UNSET)
        additional_columns: LogEntryAdditionalColumns | Unset
        if isinstance(_additional_columns, Unset) or _additional_columns is None:
            additional_columns = UNSET
        else:
            additional_columns = LogEntryAdditionalColumns.from_dict(_additional_columns)

        cluster = d.pop("cluster", UNSET)

        container = d.pop("container", UNSET)

        env = d.pop("env", UNSET)

        env_type = d.pop("envType", UNSET)

        format_ = d.pop("format", UNSET)

        function_name = d.pop("functionName", UNSET)

        guid = d.pop("guid", UNSET)

        host = d.pop("host", UNSET)

        instance = d.pop("instance", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        instance_uid = d.pop("instanceUid", UNSET)

        lambda_arn = d.pop("lambdaArn", UNSET)

        level = d.pop("level", UNSET)

        line = d.pop("line", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: LogEntryMetadata | Unset
        if isinstance(_metadata, Unset) or _metadata is None:
            metadata = UNSET
        else:
            metadata = LogEntryMetadata.from_dict(_metadata)

        namespace = d.pop("namespace", UNSET)

        node = d.pop("node", UNSET)

        pod_name = d.pop("pod_name", UNSET)

        pod_uid = d.pop("podUid", UNSET)

        service = d.pop("service", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("spanId", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset) or _timestamp is None:
            timestamp = UNSET
        else:
            timestamp = parse_datetime(_timestamp)

        trace_id = d.pop("traceId", UNSET)

        workload = d.pop("workload", UNSET)

        log_entry = cls(
            additional_columns=additional_columns,
            cluster=cluster,
            container=container,
            env=env,
            env_type=env_type,
            format_=format_,
            function_name=function_name,
            guid=guid,
            host=host,
            instance=instance,
            instance_id=instance_id,
            instance_uid=instance_uid,
            lambda_arn=lambda_arn,
            level=level,
            line=line,
            metadata=metadata,
            namespace=namespace,
            node=node,
            pod_name=pod_name,
            pod_uid=pod_uid,
            service=service,
            source=source,
            span_id=span_id,
            timestamp=timestamp,
            trace_id=trace_id,
            workload=workload,
        )

        log_entry.additional_properties = d
        return log_entry

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
