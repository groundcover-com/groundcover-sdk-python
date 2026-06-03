from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slack_chat_post_message_request_attachments import SlackChatPostMessageRequestAttachments
    from ..models.slack_chat_post_message_request_blocks import SlackChatPostMessageRequestBlocks


T = TypeVar("T", bound="SlackChatPostMessageRequest")


@_attrs_define
class SlackChatPostMessageRequest:
    """SlackChatPostMessageRequest is the Slack chat.postMessage request payload
    accepted by the Slack provider proxy.

        Attributes:
            channel (str): Slack channel ID to send to. Example: C1234567890.
            attachments (SlackChatPostMessageRequestAttachments | Unset): Optional Slack attachments payload.
            blocks (SlackChatPostMessageRequestBlocks | Unset): Optional Slack Block Kit payload.
            text (str | Unset): Message text. Example: Alert is firing.
    """

    channel: str
    attachments: SlackChatPostMessageRequestAttachments | Unset = UNSET
    blocks: SlackChatPostMessageRequestBlocks | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        attachments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        blocks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = self.blocks.to_dict()

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slack_chat_post_message_request_attachments import SlackChatPostMessageRequestAttachments
        from ..models.slack_chat_post_message_request_blocks import SlackChatPostMessageRequestBlocks

        d = dict(src_dict)
        channel = d.pop("channel")

        _attachments = d.pop("attachments", UNSET)
        attachments: SlackChatPostMessageRequestAttachments | Unset
        if isinstance(_attachments, Unset) or _attachments is None:
            attachments = UNSET
        else:
            attachments = SlackChatPostMessageRequestAttachments.from_dict(_attachments)

        _blocks = d.pop("blocks", UNSET)
        blocks: SlackChatPostMessageRequestBlocks | Unset
        if isinstance(_blocks, Unset) or _blocks is None:
            blocks = UNSET
        else:
            blocks = SlackChatPostMessageRequestBlocks.from_dict(_blocks)

        text = d.pop("text", UNSET)

        slack_chat_post_message_request = cls(
            channel=channel,
            attachments=attachments,
            blocks=blocks,
            text=text,
        )

        slack_chat_post_message_request.additional_properties = d
        return slack_chat_post_message_request

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
