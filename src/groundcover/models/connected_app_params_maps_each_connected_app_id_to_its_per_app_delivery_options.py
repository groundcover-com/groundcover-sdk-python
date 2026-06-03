from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.connected_app_delivery_options import ConnectedAppDeliveryOptions


T = TypeVar("T", bound="ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions")


@_attrs_define
class ConnectedAppParamsMapsEachConnectedAppIDToItsPerAppDeliveryOptions:
    """Requires backend version >= 1.11.916; older backends reject this field with a
    validation error rather than silently dropping the configured options.

    """

    additional_properties: dict[str, ConnectedAppDeliveryOptions] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_app_delivery_options import ConnectedAppDeliveryOptions

        d = dict(src_dict)
        connected_app_params_maps_each_connected_app_id_to_its_per_app_delivery_options = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ConnectedAppDeliveryOptions.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        connected_app_params_maps_each_connected_app_id_to_its_per_app_delivery_options.additional_properties = (
            additional_properties
        )
        return connected_app_params_maps_each_connected_app_id_to_its_per_app_delivery_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ConnectedAppDeliveryOptions:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ConnectedAppDeliveryOptions) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
