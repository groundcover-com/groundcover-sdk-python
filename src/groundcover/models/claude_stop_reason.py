from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ClaudeStopReason")


@_attrs_define
class ClaudeStopReason:
    """ClaudeStopReason describes why a session went idle, carried on
    session.status_idle events.

        Attributes:
            event_ids (list[str] | Unset): Event IDs that triggered the stop; for a requires_action pause these
                identify the agent tool-use event(s) awaiting a user.tool_confirmation.
            type_ (str | Unset):
    """

    event_ids: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ids: list[str] | Unset = UNSET
        if not isinstance(self.event_ids, Unset):
            event_ids = self.event_ids

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_ids is not UNSET:
            field_dict["event_ids"] = event_ids
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        event_ids = cast(list[str], d.pop("event_ids", UNSET))

        type_ = d.pop("type", UNSET)

        claude_stop_reason = cls(
            event_ids=event_ids,
            type_=type_,
        )

        claude_stop_reason.additional_properties = d
        return claude_stop_reason

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
