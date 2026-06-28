from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.test_monitor_connected_app_delivery_options import TestMonitorConnectedAppDeliveryOptions


T = TypeVar(
    "T", bound="TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams"
)


@_attrs_define
class TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDeliveredConnectedAppParams:
    """ConnectedAppParams provides per-app delivery options keyed by connected app ID.
    Slack App options supply channels; Linear options supply team_id, optional
    project_id, label_ids, assignee_id, resolved_status_id, and auto_resolve.
    Keys should reference IDs present in ConnectedApps; apps not listed here use
    default delivery. Mirrors the monitor connectedAppParams field.

    """

    additional_properties: dict[str, TestMonitorConnectedAppDeliveryOptions] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_monitor_connected_app_delivery_options import TestMonitorConnectedAppDeliveryOptions

        d = dict(src_dict)
        test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered_connected_app_params = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TestMonitorConnectedAppDeliveryOptions.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered_connected_app_params.additional_properties = additional_properties
        return test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered_connected_app_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> TestMonitorConnectedAppDeliveryOptions:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: TestMonitorConnectedAppDeliveryOptions) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
