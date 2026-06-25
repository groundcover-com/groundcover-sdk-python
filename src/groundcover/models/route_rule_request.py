from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.route_connected_app_request import RouteConnectedAppRequest


T = TypeVar("T", bound="RouteRuleRequest")


@_attrs_define
class RouteRuleRequest:
    """
    Attributes:
        connected_apps (list[RouteConnectedAppRequest]): The connected apps to send notifications to
        status (list[str]): The issue statuses that trigger this route Example: ['Alerting', 'Resolved'].
    """

    connected_apps: list[RouteConnectedAppRequest]
    status: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_apps = []
        for connected_apps_item_data in self.connected_apps:
            connected_apps_item = connected_apps_item_data.to_dict()
            connected_apps.append(connected_apps_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectedApps": connected_apps,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_connected_app_request import RouteConnectedAppRequest

        d = dict(src_dict)
        connected_apps = []
        _connected_apps = d.pop("connectedApps")
        for connected_apps_item_data in _connected_apps:
            connected_apps_item = RouteConnectedAppRequest.from_dict(connected_apps_item_data)

            connected_apps.append(connected_apps_item)

        status = cast(list[str], d.pop("status"))

        route_rule_request = cls(
            connected_apps=connected_apps,
            status=status,
        )

        route_rule_request.additional_properties = d
        return route_rule_request

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
