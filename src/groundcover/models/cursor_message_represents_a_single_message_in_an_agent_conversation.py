from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorMessageRepresentsASingleMessageInAnAgentConversation")


@_attrs_define
class CursorMessageRepresentsASingleMessageInAnAgentConversation:
    """
    Attributes:
        id (str | Unset):
        text (str | Unset):
        type_ (str | Unset):
    """

    id: str | Unset = UNSET
    text: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        type_ = d.pop("type", UNSET)

        cursor_message_represents_a_single_message_in_an_agent_conversation = cls(
            id=id,
            text=text,
            type_=type_,
        )

        cursor_message_represents_a_single_message_in_an_agent_conversation.additional_properties = d
        return cursor_message_represents_a_single_message_in_an_agent_conversation

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
