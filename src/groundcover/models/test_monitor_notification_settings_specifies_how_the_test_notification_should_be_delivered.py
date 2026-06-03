from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered")


@_attrs_define
class TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered:
    """Mirrors the monitor NotificationSettings structure.

    Attributes:
        connected_apps (list[str] | Unset): List of connected app IDs to send test notifications to directly,
            bypassing notification route matching. Example: ['app-abc-123'].
    """

    connected_apps: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_apps: list[str] | Unset = UNSET
        if not isinstance(self.connected_apps, Unset):
            connected_apps = self.connected_apps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_apps is not UNSET:
            field_dict["connectedApps"] = connected_apps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        connected_apps = cast(list[str], d.pop("connectedApps", UNSET))

        test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered = cls(
            connected_apps=connected_apps,
        )

        test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered.additional_properties = d
        return test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered

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
