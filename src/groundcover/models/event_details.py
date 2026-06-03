from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_details_event_attributes import EventDetailsEventAttributes


T = TypeVar("T", bound="EventDetails")


@_attrs_define
class EventDetails:
    """
    Attributes:
        event_attributes (EventDetailsEventAttributes | Unset):
        event_id (str | Unset):
        event_type (str | Unset):
        timestamp (datetime.datetime | Unset):
    """

    event_attributes: EventDetailsEventAttributes | Unset = UNSET
    event_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_attributes, Unset):
            event_attributes = self.event_attributes.to_dict()

        event_id = self.event_id

        event_type = self.event_type

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_attributes is not UNSET:
            field_dict["eventAttributes"] = event_attributes
        if event_id is not UNSET:
            field_dict["eventID"] = event_id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_details_event_attributes import EventDetailsEventAttributes

        d = dict(src_dict)
        _event_attributes = d.pop("eventAttributes", UNSET)
        event_attributes: EventDetailsEventAttributes | Unset
        if isinstance(_event_attributes, Unset) or _event_attributes is None:
            event_attributes = UNSET
        else:
            event_attributes = EventDetailsEventAttributes.from_dict(_event_attributes)

        event_id = d.pop("eventID", UNSET)

        event_type = d.pop("eventType", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset) or _timestamp is None:
            timestamp = UNSET
        else:
            timestamp = parse_datetime(_timestamp)

        event_details = cls(
            event_attributes=event_attributes,
            event_id=event_id,
            event_type=event_type,
            timestamp=timestamp,
        )

        event_details.additional_properties = d
        return event_details

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
