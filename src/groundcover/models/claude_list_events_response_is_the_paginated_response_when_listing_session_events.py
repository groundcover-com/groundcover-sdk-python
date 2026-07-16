from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claude_inbound_event_is_a_single_event_returned_when_listing_session_events import (
        ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents,
    )


T = TypeVar("T", bound="ClaudeListEventsResponseIsThePaginatedResponseWhenListingSessionEvents")


@_attrs_define
class ClaudeListEventsResponseIsThePaginatedResponseWhenListingSessionEvents:
    """
    Attributes:
        events (list[ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents] | Unset):
        next_page (str | Unset):
    """

    events: list[ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents] | Unset = UNSET
    next_page: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        next_page = self.next_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if next_page is not UNSET:
            field_dict["next_page"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claude_inbound_event_is_a_single_event_returned_when_listing_session_events import (
            ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents,
        )

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents.from_dict(
                    events_item_data
                )

                events.append(events_item)

        next_page = d.pop("next_page", UNSET)

        claude_list_events_response_is_the_paginated_response_when_listing_session_events = cls(
            events=events,
            next_page=next_page,
        )

        claude_list_events_response_is_the_paginated_response_when_listing_session_events.additional_properties = d
        return claude_list_events_response_is_the_paginated_response_when_listing_session_events

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
