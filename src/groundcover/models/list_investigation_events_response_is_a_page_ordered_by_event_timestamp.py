from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_is_an_attributable_change_in_an_investigation_tree import (
        EventIsAnAttributableChangeInAnInvestigationTree,
    )


T = TypeVar("T", bound="ListInvestigationEventsResponseIsAPageOrderedByEventTimestamp")


@_attrs_define
class ListInvestigationEventsResponseIsAPageOrderedByEventTimestamp:
    """
    Attributes:
        done (bool):
        events (list[EventIsAnAttributableChangeInAnInvestigationTree]):
        next_after_timestamp (datetime.datetime | Unset): Last returned event's timestamp; an empty page retains
            afterTimestamp.
    """

    done: bool
    events: list[EventIsAnAttributableChangeInAnInvestigationTree]
    next_after_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        next_after_timestamp: str | Unset = UNSET
        if not isinstance(self.next_after_timestamp, Unset):
            next_after_timestamp = self.next_after_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "events": events,
            }
        )
        if next_after_timestamp is not UNSET:
            field_dict["nextAfterTimestamp"] = next_after_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_is_an_attributable_change_in_an_investigation_tree import (
            EventIsAnAttributableChangeInAnInvestigationTree,
        )

        d = dict(src_dict)
        done = d.pop("done")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = EventIsAnAttributableChangeInAnInvestigationTree.from_dict(events_item_data)

            events.append(events_item)

        _next_after_timestamp = d.pop("nextAfterTimestamp", UNSET)
        next_after_timestamp: datetime.datetime | Unset
        if isinstance(_next_after_timestamp, Unset) or _next_after_timestamp is None:
            next_after_timestamp = UNSET
        else:
            next_after_timestamp = parse_datetime(_next_after_timestamp)

        list_investigation_events_response_is_a_page_ordered_by_event_timestamp = cls(
            done=done,
            events=events,
            next_after_timestamp=next_after_timestamp,
        )

        list_investigation_events_response_is_a_page_ordered_by_event_timestamp.additional_properties = d
        return list_investigation_events_response_is_a_page_ordered_by_event_timestamp

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
