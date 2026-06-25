from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_event_attributes import SpanEventAttributes


T = TypeVar("T", bound="SpanEvent")


@_attrs_define
class SpanEvent:
    """
    Attributes:
        attributes (SpanEventAttributes | Unset):
        name (str | Unset):
        timestamp (datetime.datetime | Unset):
    """

    attributes: SpanEventAttributes | Unset = UNSET
    name: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        name = self.name

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if name is not UNSET:
            field_dict["name"] = name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_event_attributes import SpanEventAttributes

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: SpanEventAttributes | Unset
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = SpanEventAttributes.from_dict(_attributes)

        name = d.pop("name", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset) or _timestamp is None:
            timestamp = UNSET
        else:
            timestamp = parse_datetime(_timestamp)

        span_event = cls(
            attributes=attributes,
            name=name,
            timestamp=timestamp,
        )

        span_event.additional_properties = d
        return span_event

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
