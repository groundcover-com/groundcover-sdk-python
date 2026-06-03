from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_settings_defines_the_notification_settings_for_the_monitor_method import (
    NotificationSettingsDefinesTheNotificationSettingsForTheMonitorMethod,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connected_app_params_maps_each_connected_app_id_to_its_per_app_delivery_options import (
        ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions,
    )


T = TypeVar("T", bound="NotificationSettingsDefinesTheNotificationSettingsForTheMonitor")


@_attrs_define
class NotificationSettingsDefinesTheNotificationSettingsForTheMonitor:
    """
    Attributes:
        connected_app_params (ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions | Unset): Requires
            backend version >= 1.11.916; older backends reject this field with a
            validation error rather than silently dropping the configured options.
        connected_apps (list[str] | Unset):
        disable_renotification (bool | Unset):
        method (NotificationSettingsDefinesTheNotificationSettingsForTheMonitorMethod | Unset):
        renotification_interval (Any | Unset): RenotificationDuration is like Duration but marshals using model.Duration
            for cleaner output (1d instead of 24h0m0s) to match Grafana notification policy settings.
        status_filters (list[str] | Unset):
    """

    connected_app_params: ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions | Unset = UNSET
    connected_apps: list[str] | Unset = UNSET
    disable_renotification: bool | Unset = UNSET
    method: NotificationSettingsDefinesTheNotificationSettingsForTheMonitorMethod | Unset = UNSET
    renotification_interval: Any | Unset = UNSET
    status_filters: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_app_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_app_params, Unset):
            connected_app_params = self.connected_app_params.to_dict()

        connected_apps: list[str] | Unset = UNSET
        if not isinstance(self.connected_apps, Unset):
            connected_apps = self.connected_apps

        disable_renotification = self.disable_renotification

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        renotification_interval = self.renotification_interval

        status_filters: list[str] | Unset = UNSET
        if not isinstance(self.status_filters, Unset):
            status_filters = self.status_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_app_params is not UNSET:
            field_dict["connectedAppParams"] = connected_app_params
        if connected_apps is not UNSET:
            field_dict["connectedApps"] = connected_apps
        if disable_renotification is not UNSET:
            field_dict["disableRenotification"] = disable_renotification
        if method is not UNSET:
            field_dict["method"] = method
        if renotification_interval is not UNSET:
            field_dict["renotificationInterval"] = renotification_interval
        if status_filters is not UNSET:
            field_dict["statusFilters"] = status_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_app_params_maps_each_connected_app_id_to_its_per_app_delivery_options import (
            ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions,
        )

        d = dict(src_dict)
        _connected_app_params = d.pop("connectedAppParams", UNSET)
        connected_app_params: ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions | Unset
        if isinstance(_connected_app_params, Unset) or _connected_app_params is None:
            connected_app_params = UNSET
        else:
            connected_app_params = ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions.from_dict(
                _connected_app_params
            )

        connected_apps = cast(list[str], d.pop("connectedApps", UNSET))

        disable_renotification = d.pop("disableRenotification", UNSET)

        _method = d.pop("method", UNSET)
        method: NotificationSettingsDefinesTheNotificationSettingsForTheMonitorMethod | Unset
        if isinstance(_method, Unset) or _method is None:
            method = UNSET
        else:
            method = NotificationSettingsDefinesTheNotificationSettingsForTheMonitorMethod(_method)

        renotification_interval = d.pop("renotificationInterval", UNSET)

        status_filters = cast(list[str], d.pop("statusFilters", UNSET))

        notification_settings_defines_the_notification_settings_for_the_monitor = cls(
            connected_app_params=connected_app_params,
            connected_apps=connected_apps,
            disable_renotification=disable_renotification,
            method=method,
            renotification_interval=renotification_interval,
            status_filters=status_filters,
        )

        notification_settings_defines_the_notification_settings_for_the_monitor.additional_properties = d
        return notification_settings_defines_the_notification_settings_for_the_monitor

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
