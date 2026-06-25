from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slack_chat_post_message_response_is_the_proxied_slack_chat_post_message_response_message import (
        SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponseMessage,
    )


T = TypeVar("T", bound="SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponse")


@_attrs_define
class SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponse:
    """
    Attributes:
        channel (str | Unset):
        error (str | Unset):
        message (SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponseMessage | Unset):
        ok (bool | Unset):
        ts (str | Unset):
    """

    channel: str | Unset = UNSET
    error: str | Unset = UNSET
    message: SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponseMessage | Unset = UNSET
    ok: bool | Unset = UNSET
    ts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        error = self.error

        message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        ok = self.ok

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if error is not UNSET:
            field_dict["error"] = error
        if message is not UNSET:
            field_dict["message"] = message
        if ok is not UNSET:
            field_dict["ok"] = ok
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slack_chat_post_message_response_is_the_proxied_slack_chat_post_message_response_message import (
            SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponseMessage,
        )

        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        error = d.pop("error", UNSET)

        _message = d.pop("message", UNSET)
        message: SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponseMessage | Unset
        if isinstance(_message, Unset) or _message is None:
            message = UNSET
        else:
            message = SlackChatPostMessageResponseIsTheProxiedSlackChatPostMessageResponseMessage.from_dict(_message)

        ok = d.pop("ok", UNSET)

        ts = d.pop("ts", UNSET)

        slack_chat_post_message_response_is_the_proxied_slack_chat_post_message_response = cls(
            channel=channel,
            error=error,
            message=message,
            ok=ok,
            ts=ts,
        )

        slack_chat_post_message_response_is_the_proxied_slack_chat_post_message_response.additional_properties = d
        return slack_chat_post_message_response_is_the_proxied_slack_chat_post_message_response

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
