from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response import (
        EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse,
    )


T = TypeVar("T", bound="GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse")


@_attrs_define
class GetEventsOverTimeResponseDefinesTheStructureForTheEventsOverTimeAPIResponse:
    """
    Attributes:
        events (list[EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse] | Unset):
        is_limit_reached (bool | Unset):
        warning_indicator (bool | Unset):
    """

    events: list[EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse] | Unset = UNSET
    is_limit_reached: bool | Unset = UNSET
    warning_indicator: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        is_limit_reached = self.is_limit_reached

        warning_indicator = self.warning_indicator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if warning_indicator is not UNSET:
            field_dict["warningIndicator"] = warning_indicator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.events_over_time_response_defines_the_structure_for_a_single_event_in_the_events_over_time_api_response import (
            EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse,
        )

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse] | Unset = (
            UNSET
        )
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = (
                    EventsOverTimeResponseDefinesTheStructureForASingleEventInTheEventsOverTimeAPIResponse.from_dict(
                        events_item_data
                    )
                )

                events.append(events_item)

        is_limit_reached = d.pop("isLimitReached", UNSET)

        warning_indicator = d.pop("warningIndicator", UNSET)

        get_events_over_time_response_defines_the_structure_for_the_events_over_time_api_response = cls(
            events=events,
            is_limit_reached=is_limit_reached,
            warning_indicator=warning_indicator,
        )

        get_events_over_time_response_defines_the_structure_for_the_events_over_time_api_response.additional_properties = d
        return get_events_over_time_response_defines_the_structure_for_the_events_over_time_api_response

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
