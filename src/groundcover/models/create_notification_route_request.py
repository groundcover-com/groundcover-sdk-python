from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_settings_request import NotificationSettingsRequest
    from ..models.route_rule_request import RouteRuleRequest


T = TypeVar("T", bound="CreateNotificationRouteRequest")


@_attrs_define
class CreateNotificationRouteRequest:
    """
    Attributes:
        name (str): The name of the notification route Example: prod-alerts-route.
        query (str): The gcQL query to filter issues Example: env:prod AND severity:critical.
        routes (list[RouteRuleRequest]): The routing rules for notifications
        notification_settings (NotificationSettingsRequest | Unset):
    """

    name: str
    query: str
    routes: list[RouteRuleRequest]
    notification_settings: NotificationSettingsRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        query = self.query

        routes = []
        for routes_item_data in self.routes:
            routes_item = routes_item_data.to_dict()
            routes.append(routes_item)

        notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "query": query,
                "routes": routes,
            }
        )
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_settings_request import NotificationSettingsRequest
        from ..models.route_rule_request import RouteRuleRequest

        d = dict(src_dict)
        name = d.pop("name")

        query = d.pop("query")

        routes = []
        _routes = d.pop("routes")
        for routes_item_data in _routes:
            routes_item = RouteRuleRequest.from_dict(routes_item_data)

            routes.append(routes_item)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: NotificationSettingsRequest | Unset
        if isinstance(_notification_settings, Unset) or _notification_settings is None:
            notification_settings = UNSET
        else:
            notification_settings = NotificationSettingsRequest.from_dict(_notification_settings)

        create_notification_route_request = cls(
            name=name,
            query=query,
            routes=routes,
            notification_settings=notification_settings,
        )

        create_notification_route_request.additional_properties = d
        return create_notification_route_request

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
