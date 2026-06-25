from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response_raw import (
        EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponseRaw,
    )


T = TypeVar("T", bound="EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse")


@_attrs_define
class EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse:
    """
    Attributes:
        cluster (str | Unset):
        created_timestamp (datetime.datetime | Unset):
        env (str | Unset):
        exit_code (str | Unset):
        instance (str | Unset):
        message (str | Unset):
        namespace (str | Unset):
        normalized_uid (str | Unset):
        object_kind (str | Unset):
        object_uid (str | Unset):
        raw (EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponseRaw | Unset):
        reason (str | Unset):
        timestamp (datetime.datetime | Unset):
        type_ (str | Unset):
        uid (str | Unset):
        workload (str | Unset):
    """

    cluster: str | Unset = UNSET
    created_timestamp: datetime.datetime | Unset = UNSET
    env: str | Unset = UNSET
    exit_code: str | Unset = UNSET
    instance: str | Unset = UNSET
    message: str | Unset = UNSET
    namespace: str | Unset = UNSET
    normalized_uid: str | Unset = UNSET
    object_kind: str | Unset = UNSET
    object_uid: str | Unset = UNSET
    raw: EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponseRaw | Unset = UNSET
    reason: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    uid: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        created_timestamp: str | Unset = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        env = self.env

        exit_code = self.exit_code

        instance = self.instance

        message = self.message

        namespace = self.namespace

        normalized_uid = self.normalized_uid

        object_kind = self.object_kind

        object_uid = self.object_uid

        raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw, Unset):
            raw = self.raw.to_dict()

        reason = self.reason

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        type_ = self.type_

        uid = self.uid

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if env is not UNSET:
            field_dict["env"] = env
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code
        if instance is not UNSET:
            field_dict["instance"] = instance
        if message is not UNSET:
            field_dict["message"] = message
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if normalized_uid is not UNSET:
            field_dict["normalized_uid"] = normalized_uid
        if object_kind is not UNSET:
            field_dict["object_kind"] = object_kind
        if object_uid is not UNSET:
            field_dict["object_uid"] = object_uid
        if raw is not UNSET:
            field_dict["raw"] = raw
        if reason is not UNSET:
            field_dict["reason"] = reason
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uid is not UNSET:
            field_dict["uid"] = uid
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response_raw import (
            EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponseRaw,
        )

        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: datetime.datetime | Unset
        if isinstance(_created_timestamp, Unset) or _created_timestamp is None:
            created_timestamp = UNSET
        else:
            created_timestamp = parse_datetime(_created_timestamp)

        env = d.pop("env", UNSET)

        exit_code = d.pop("exitCode", UNSET)

        instance = d.pop("instance", UNSET)

        message = d.pop("message", UNSET)

        namespace = d.pop("namespace", UNSET)

        normalized_uid = d.pop("normalized_uid", UNSET)

        object_kind = d.pop("object_kind", UNSET)

        object_uid = d.pop("object_uid", UNSET)

        _raw = d.pop("raw", UNSET)
        raw: EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponseRaw | Unset
        if isinstance(_raw, Unset) or _raw is None:
            raw = UNSET
        else:
            raw = EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponseRaw.from_dict(
                _raw
            )

        reason = d.pop("reason", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset) or _timestamp is None:
            timestamp = UNSET
        else:
            timestamp = parse_datetime(_timestamp)

        type_ = d.pop("type", UNSET)

        uid = d.pop("uid", UNSET)

        workload = d.pop("workload", UNSET)

        events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response = cls(
            cluster=cluster,
            created_timestamp=created_timestamp,
            env=env,
            exit_code=exit_code,
            instance=instance,
            message=message,
            namespace=namespace,
            normalized_uid=normalized_uid,
            object_kind=object_kind,
            object_uid=object_uid,
            raw=raw,
            reason=reason,
            timestamp=timestamp,
            type_=type_,
            uid=uid,
            workload=workload,
        )

        events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response.additional_properties = d
        return events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response

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
