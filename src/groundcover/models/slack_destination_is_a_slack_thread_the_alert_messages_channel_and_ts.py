from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs")


@_attrs_define
class SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs:
    """
    Attributes:
        channel_id (str):
        thread_ts (str):
    """

    channel_id: str
    thread_ts: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        thread_ts = self.thread_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "threadTs": thread_ts,
            }
        )

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
        channel_id = d.pop("channelId")

        thread_ts = d.pop("threadTs")

        slack_destination_is_a_slack_thread_the_alert_messages_channel_and_ts = cls(
            channel_id=channel_id,
            thread_ts=thread_ts,
        )

        slack_destination_is_a_slack_thread_the_alert_messages_channel_and_ts.additional_properties = d
        return slack_destination_is_a_slack_thread_the_alert_messages_channel_and_ts

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
