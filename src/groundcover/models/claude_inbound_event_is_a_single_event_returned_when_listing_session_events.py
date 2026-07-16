from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claude_event_content import ClaudeEventContent
    from ..models.claude_inbound_event_is_a_single_event_returned_when_listing_session_events_input import (
        ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEventsInput,
    )
    from ..models.claude_stop_reason import ClaudeStopReason


T = TypeVar("T", bound="ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents")


@_attrs_define
class ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEvents:
    """e.g. agent.message, session.status_idle, session.error, or an agent tool-use
    that paused the session awaiting a user.tool_confirmation. ID, Name, Input,
    and EvaluatedPermission are populated on tool-use events so the caller can
    render the pending tool call and echo the event ID back as tool_use_id.

        Attributes:
            content (list[ClaudeEventContent] | Unset):
            evaluated_permission (str | Unset): Evaluated permission policy for the tool call (tool-use events only)
            id (str | Unset): Event ID; on a tool-use event echo this back as tool_use_id in a
                user.tool_confirmation.
            input_ (ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEventsInput | Unset): Tool call input
                arguments (tool-use events only)
            name (str | Unset): Tool name (tool-use events only)
            stop_reason (ClaudeStopReason | Unset): ClaudeStopReason describes why a session went idle, carried on
                session.status_idle events.
            type_ (str | Unset):
    """

    content: list[ClaudeEventContent] | Unset = UNSET
    evaluated_permission: str | Unset = UNSET
    id: str | Unset = UNSET
    input_: ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEventsInput | Unset = UNSET
    name: str | Unset = UNSET
    stop_reason: ClaudeStopReason | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        evaluated_permission = self.evaluated_permission

        id = self.id

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        name = self.name

        stop_reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_reason, Unset):
            stop_reason = self.stop_reason.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if evaluated_permission is not UNSET:
            field_dict["evaluated_permission"] = evaluated_permission
        if id is not UNSET:
            field_dict["id"] = id
        if input_ is not UNSET:
            field_dict["input"] = input_
        if name is not UNSET:
            field_dict["name"] = name
        if stop_reason is not UNSET:
            field_dict["stop_reason"] = stop_reason
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claude_event_content import ClaudeEventContent
        from ..models.claude_inbound_event_is_a_single_event_returned_when_listing_session_events_input import (
            ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEventsInput,
        )
        from ..models.claude_stop_reason import ClaudeStopReason

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[ClaudeEventContent] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = ClaudeEventContent.from_dict(content_item_data)

                content.append(content_item)

        evaluated_permission = d.pop("evaluated_permission", UNSET)

        id = d.pop("id", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEventsInput | Unset
        if isinstance(_input_, Unset) or _input_ is None:
            input_ = UNSET
        else:
            input_ = ClaudeInboundEventIsASingleEventReturnedWhenListingSessionEventsInput.from_dict(_input_)

        name = d.pop("name", UNSET)

        _stop_reason = d.pop("stop_reason", UNSET)
        stop_reason: ClaudeStopReason | Unset
        if isinstance(_stop_reason, Unset) or _stop_reason is None:
            stop_reason = UNSET
        else:
            stop_reason = ClaudeStopReason.from_dict(_stop_reason)

        type_ = d.pop("type", UNSET)

        claude_inbound_event_is_a_single_event_returned_when_listing_session_events = cls(
            content=content,
            evaluated_permission=evaluated_permission,
            id=id,
            input_=input_,
            name=name,
            stop_reason=stop_reason,
            type_=type_,
        )

        claude_inbound_event_is_a_single_event_returned_when_listing_session_events.additional_properties = d
        return claude_inbound_event_is_a_single_event_returned_when_listing_session_events

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
