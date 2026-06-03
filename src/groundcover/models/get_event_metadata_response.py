from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_event_metadata_response_string_attributes import GetEventMetadataResponseStringAttributes


T = TypeVar("T", bound="GetEventMetadataResponse")


@_attrs_define
class GetEventMetadataResponse:
    """
    Attributes:
        count (int | Unset):
        first_seen (datetime.datetime | Unset):
        last_seen (datetime.datetime | Unset):
        string_attributes (GetEventMetadataResponseStringAttributes | Unset):
    """

    count: int | Unset = UNSET
    first_seen: datetime.datetime | Unset = UNSET
    last_seen: datetime.datetime | Unset = UNSET
    string_attributes: GetEventMetadataResponseStringAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        first_seen: str | Unset = UNSET
        if not isinstance(self.first_seen, Unset):
            first_seen = self.first_seen.isoformat()

        last_seen: str | Unset = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        string_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.string_attributes, Unset):
            string_attributes = self.string_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if first_seen is not UNSET:
            field_dict["firstSeen"] = first_seen
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if string_attributes is not UNSET:
            field_dict["string_attributes"] = string_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_event_metadata_response_string_attributes import GetEventMetadataResponseStringAttributes

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _first_seen = d.pop("firstSeen", UNSET)
        first_seen: datetime.datetime | Unset
        if isinstance(_first_seen, Unset) or _first_seen is None:
            first_seen = UNSET
        else:
            first_seen = parse_datetime(_first_seen)

        _last_seen = d.pop("lastSeen", UNSET)
        last_seen: datetime.datetime | Unset
        if isinstance(_last_seen, Unset) or _last_seen is None:
            last_seen = UNSET
        else:
            last_seen = parse_datetime(_last_seen)

        _string_attributes = d.pop("string_attributes", UNSET)
        string_attributes: GetEventMetadataResponseStringAttributes | Unset
        if isinstance(_string_attributes, Unset) or _string_attributes is None:
            string_attributes = UNSET
        else:
            string_attributes = GetEventMetadataResponseStringAttributes.from_dict(_string_attributes)

        get_event_metadata_response = cls(
            count=count,
            first_seen=first_seen,
            last_seen=last_seen,
            string_attributes=string_attributes,
        )

        get_event_metadata_response.additional_properties = d
        return get_event_metadata_response

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
