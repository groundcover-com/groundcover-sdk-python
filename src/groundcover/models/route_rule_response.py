from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_connected_app_response import RouteConnectedAppResponse


T = TypeVar("T", bound="RouteRuleResponse")


@_attrs_define
class RouteRuleResponse:
    """
    Attributes:
        connected_apps (list[RouteConnectedAppResponse] | Unset): The connected apps for this route
        status (list[str] | Unset): The issue statuses that trigger this route Example: ['Alerting', 'Resolved'].
    """

    connected_apps: list[RouteConnectedAppResponse] | Unset = UNSET
    status: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connected_apps, Unset):
            connected_apps = []
            for connected_apps_item_data in self.connected_apps:
                connected_apps_item = connected_apps_item_data.to_dict()
                connected_apps.append(connected_apps_item)

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_apps is not UNSET:
            field_dict["connectedApps"] = connected_apps
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_connected_app_response import RouteConnectedAppResponse

        d = dict(src_dict)
        _connected_apps = d.pop("connectedApps", UNSET)
        connected_apps: list[RouteConnectedAppResponse] | Unset = UNSET
        if _connected_apps is not UNSET:
            connected_apps = []
            for connected_apps_item_data in _connected_apps:
                connected_apps_item = RouteConnectedAppResponse.from_dict(connected_apps_item_data)

                connected_apps.append(connected_apps_item)

        status = cast(list[str], d.pop("status", UNSET))

        route_rule_response = cls(
            connected_apps=connected_apps,
            status=status,
        )

        route_rule_response.additional_properties = d
        return route_rule_response

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
