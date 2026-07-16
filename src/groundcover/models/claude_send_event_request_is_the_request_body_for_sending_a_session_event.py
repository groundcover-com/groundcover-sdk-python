from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.claude_send_event_request_is_the_request_body_for_sending_a_session_event_result import (
    ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventResult,
)
from ..models.claude_send_event_request_is_the_request_body_for_sending_a_session_event_type import (
    ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventType,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEvent")


@_attrs_define
class ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEvent:
    """Type must be user.message, user.interrupt, or user.tool_confirmation, else
    the request is rejected with 400. Text carries a user.message; ToolUseID,
    Result, and Message carry a user.tool_confirmation (Message is the optional
    deny reason, forwarded upstream as deny_message).

        Attributes:
            type_ (ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventType):  Example: user.message.
            message (str | Unset): Optional reason for a deny, delivered to the agent (user.tool_confirmation only)
            result (ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventResult | Unset): Approve or deny the paused
                tool call (user.tool_confirmation only) Example: allow.
            text (str | Unset):
            tool_use_id (str | Unset): ID of the paused tool call to respond to (user.tool_confirmation only) Example:
                sevt_abc123.
    """

    type_: ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventType
    message: str | Unset = UNSET
    result: ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventResult | Unset = UNSET
    text: str | Unset = UNSET
    tool_use_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        text = self.text

        tool_use_id = self.tool_use_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if result is not UNSET:
            field_dict["result"] = result
        if text is not UNSET:
            field_dict["text"] = text
        if tool_use_id is not UNSET:
            field_dict["tool_use_id"] = tool_use_id

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
        type_ = ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventType(d.pop("type"))

        message = d.pop("message", UNSET)

        _result = d.pop("result", UNSET)
        result: ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventResult | Unset
        if isinstance(_result, Unset) or _result is None:
            result = UNSET
        else:
            result = ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventResult(_result)

        text = d.pop("text", UNSET)

        tool_use_id = d.pop("tool_use_id", UNSET)

        claude_send_event_request_is_the_request_body_for_sending_a_session_event = cls(
            type_=type_,
            message=message,
            result=result,
            text=text,
            tool_use_id=tool_use_id,
        )

        claude_send_event_request_is_the_request_body_for_sending_a_session_event.additional_properties = d
        return claude_send_event_request_is_the_request_body_for_sending_a_session_event

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
