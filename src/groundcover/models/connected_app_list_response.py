from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connected_app_list_item_response import ConnectedAppListItemResponse


T = TypeVar("T", bound="ConnectedAppListResponse")


@_attrs_define
class ConnectedAppListResponse:
    """
    Attributes:
        connected_apps (list[ConnectedAppListItemResponse] | Unset): List of connected apps
    """

    connected_apps: list[ConnectedAppListItemResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connected_apps, Unset):
            connected_apps = []
            for connected_apps_item_data in self.connected_apps:
                connected_apps_item = connected_apps_item_data.to_dict()
                connected_apps.append(connected_apps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_apps is not UNSET:
            field_dict["connectedApps"] = connected_apps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_app_list_item_response import ConnectedAppListItemResponse

        d = dict(src_dict)
        _connected_apps = d.pop("connectedApps", UNSET)
        connected_apps: list[ConnectedAppListItemResponse] | Unset = UNSET
        if _connected_apps is not UNSET:
            connected_apps = []
            for connected_apps_item_data in _connected_apps:
                connected_apps_item = ConnectedAppListItemResponse.from_dict(connected_apps_item_data)

                connected_apps.append(connected_apps_item)

        connected_app_list_response = cls(
            connected_apps=connected_apps,
        )

        connected_app_list_response.additional_properties = d
        return connected_app_list_response

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
