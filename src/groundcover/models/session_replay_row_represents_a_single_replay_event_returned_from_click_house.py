from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SessionReplayRowRepresentsASingleReplayEventReturnedFromClickHouse")


@_attrs_define
class SessionReplayRowRepresentsASingleReplayEventReturnedFromClickHouse:
    """
    Attributes:
        data (str | Unset):
        event_id (str | Unset):
        timestamp (datetime.datetime | Unset):
    """

    data: str | Unset = UNSET
    event_id: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        event_id = self.event_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if event_id is not UNSET:
            field_dict["eventID"] = event_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

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
        data = d.pop("data", UNSET)

        event_id = d.pop("eventID", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset) or _timestamp is None:
            timestamp = UNSET
        else:
            timestamp = parse_datetime(_timestamp)

        session_replay_row_represents_a_single_replay_event_returned_from_click_house = cls(
            data=data,
            event_id=event_id,
            timestamp=timestamp,
        )

        session_replay_row_represents_a_single_replay_event_returned_from_click_house.additional_properties = d
        return session_replay_row_represents_a_single_replay_event_returned_from_click_house

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
