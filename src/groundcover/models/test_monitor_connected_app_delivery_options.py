from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_monitor_connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery import (
        TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery,
    )


T = TypeVar("T", bound="TestMonitorConnectedAppDeliveryOptions")


@_attrs_define
class TestMonitorConnectedAppDeliveryOptions:
    """TestMonitorConnectedAppDeliveryOptions carries per-app delivery options for a direct
    connected-app test notification. Fields are app-type specific; unrelated fields are ignored.

        Attributes:
            channels (list[TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery] | Unset): Channels
                lists the Slack channels to post to (slack-app connected apps).
                Multiple channels result in one test notification per channel.
    """

    channels: list[TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_monitor_connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery import (
            TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery,
        )

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: list[TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery.from_dict(
                    channels_item_data
                )

                channels.append(channels_item)

        test_monitor_connected_app_delivery_options = cls(
            channels=channels,
        )

        test_monitor_connected_app_delivery_options.additional_properties = d
        return test_monitor_connected_app_delivery_options

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
