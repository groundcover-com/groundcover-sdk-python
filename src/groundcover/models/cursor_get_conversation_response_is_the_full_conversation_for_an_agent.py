from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_message_represents_a_single_message_in_an_agent_conversation import (
        CursorMessageRepresentsASingleMessageInAnAgentConversation,
    )


T = TypeVar("T", bound="CursorGetConversationResponseIsTheFullConversationForAnAgent")


@_attrs_define
class CursorGetConversationResponseIsTheFullConversationForAnAgent:
    """
    Attributes:
        id (str | Unset):
        messages (list[CursorMessageRepresentsASingleMessageInAnAgentConversation] | Unset):
    """

    id: str | Unset = UNSET
    messages: list[CursorMessageRepresentsASingleMessageInAnAgentConversation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_message_represents_a_single_message_in_an_agent_conversation import (
            CursorMessageRepresentsASingleMessageInAnAgentConversation,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: list[CursorMessageRepresentsASingleMessageInAnAgentConversation] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = CursorMessageRepresentsASingleMessageInAnAgentConversation.from_dict(messages_item_data)

                messages.append(messages_item)

        cursor_get_conversation_response_is_the_full_conversation_for_an_agent = cls(
            id=id,
            messages=messages,
        )

        cursor_get_conversation_response_is_the_full_conversation_for_an_agent.additional_properties = d
        return cursor_get_conversation_response_is_the_full_conversation_for_an_agent

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
