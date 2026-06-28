from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered_connected_app_params import (
        TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams,
    )


T = TypeVar("T", bound="TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered")


@_attrs_define
class TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered:
    """Mirrors the monitor NotificationSettings structure.

    Attributes:
        connected_app_params
            (TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams | Unset):
            ConnectedAppParams provides per-app delivery options keyed by connected app ID.
            Slack App options supply channels; Linear options supply team_id, optional
            project_id, label_ids, assignee_id, resolved_status_id, and auto_resolve.
            Keys should reference IDs present in ConnectedApps; apps not listed here use
            default delivery. Mirrors the monitor connectedAppParams field.
        connected_apps (list[str] | Unset): List of connected app IDs to send test notifications to directly,
            bypassing notification route matching. Example: ['app-abc-123'].
    """

    connected_app_params: (
        TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams | Unset
    ) = UNSET
    connected_apps: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_app_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_app_params, Unset):
            connected_app_params = self.connected_app_params.to_dict()

        connected_apps: list[str] | Unset = UNSET
        if not isinstance(self.connected_apps, Unset):
            connected_apps = self.connected_apps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_app_params is not UNSET:
            field_dict["connectedAppParams"] = connected_app_params
        if connected_apps is not UNSET:
            field_dict["connectedApps"] = connected_apps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered_connected_app_params import (
            TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams,
        )

        d = dict(src_dict)
        _connected_app_params = d.pop("connectedAppParams", UNSET)
        connected_app_params: (
            TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams | Unset
        )
        if isinstance(_connected_app_params, Unset) or _connected_app_params is None:
            connected_app_params = UNSET
        else:
            connected_app_params = TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams.from_dict(
                _connected_app_params
            )

        connected_apps = cast(list[str], d.pop("connectedApps", UNSET))

        test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered = cls(
            connected_app_params=connected_app_params,
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
