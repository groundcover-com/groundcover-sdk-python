from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.destinations_is_direct_delivery_status_filters_omitted_all import (
        DestinationsIsDirectDeliveryStatusFiltersOmittedAll,
    )
    from ..models.no_notifications_is_the_suppress_everything_mode_marker import (
        NoNotificationsIsTheSuppressEverythingModeMarker,
    )
    from ..models.notification_routes_is_the_route_based_delivery_mode_marker import (
        NotificationRoutesIsTheRouteBasedDeliveryModeMarker,
    )


T = TypeVar("T", bound="NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault")


@_attrs_define
class NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault:
    """The renotification knobs apply to any mode.

    Attributes:
        destinations (DestinationsIsDirectDeliveryStatusFiltersOmittedAll | Unset):
        disable_renotification (bool | Unset):
        no_notifications (NoNotificationsIsTheSuppressEverythingModeMarker | Unset):
        notification_routes (NotificationRoutesIsTheRouteBasedDeliveryModeMarker | Unset):
        renotification_interval (str | Unset):
    """

    destinations: DestinationsIsDirectDeliveryStatusFiltersOmittedAll | Unset = UNSET
    disable_renotification: bool | Unset = UNSET
    no_notifications: NoNotificationsIsTheSuppressEverythingModeMarker | Unset = UNSET
    notification_routes: NotificationRoutesIsTheRouteBasedDeliveryModeMarker | Unset = UNSET
    renotification_interval: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destinations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = self.destinations.to_dict()

        disable_renotification = self.disable_renotification

        no_notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_notifications, Unset):
            no_notifications = self.no_notifications.to_dict()

        notification_routes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_routes, Unset):
            notification_routes = self.notification_routes.to_dict()

        renotification_interval = self.renotification_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if disable_renotification is not UNSET:
            field_dict["disableRenotification"] = disable_renotification
        if no_notifications is not UNSET:
            field_dict["noNotifications"] = no_notifications
        if notification_routes is not UNSET:
            field_dict["notificationRoutes"] = notification_routes
        if renotification_interval is not UNSET:
            field_dict["renotificationInterval"] = renotification_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.destinations_is_direct_delivery_status_filters_omitted_all import (
            DestinationsIsDirectDeliveryStatusFiltersOmittedAll,
        )
        from ..models.no_notifications_is_the_suppress_everything_mode_marker import (
            NoNotificationsIsTheSuppressEverythingModeMarker,
        )
        from ..models.notification_routes_is_the_route_based_delivery_mode_marker import (
            NotificationRoutesIsTheRouteBasedDeliveryModeMarker,
        )

        d = dict(src_dict)
        _destinations = d.pop("destinations", UNSET)
        destinations: DestinationsIsDirectDeliveryStatusFiltersOmittedAll | Unset
        if isinstance(_destinations, Unset) or _destinations is None:
            destinations = UNSET
        else:
            destinations = DestinationsIsDirectDeliveryStatusFiltersOmittedAll.from_dict(_destinations)

        disable_renotification = d.pop("disableRenotification", UNSET)

        _no_notifications = d.pop("noNotifications", UNSET)
        no_notifications: NoNotificationsIsTheSuppressEverythingModeMarker | Unset
        if isinstance(_no_notifications, Unset) or _no_notifications is None:
            no_notifications = UNSET
        else:
            no_notifications = NoNotificationsIsTheSuppressEverythingModeMarker.from_dict(_no_notifications)

        _notification_routes = d.pop("notificationRoutes", UNSET)
        notification_routes: NotificationRoutesIsTheRouteBasedDeliveryModeMarker | Unset
        if isinstance(_notification_routes, Unset) or _notification_routes is None:
            notification_routes = UNSET
        else:
            notification_routes = NotificationRoutesIsTheRouteBasedDeliveryModeMarker.from_dict(_notification_routes)

        renotification_interval = d.pop("renotificationInterval", UNSET)

        notification_settings_requires_exactly_one_mode_block_there_is_no_default = cls(
            destinations=destinations,
            disable_renotification=disable_renotification,
            no_notifications=no_notifications,
            notification_routes=notification_routes,
            renotification_interval=renotification_interval,
        )

        notification_settings_requires_exactly_one_mode_block_there_is_no_default.additional_properties = d
        return notification_settings_requires_exactly_one_mode_block_there_is_no_default

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
