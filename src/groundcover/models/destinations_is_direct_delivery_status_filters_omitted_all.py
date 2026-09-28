from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_destination_app import V2DestinationApp


T = TypeVar("T", bound="DestinationsIsDirectDeliveryStatusFiltersOmittedAll")


@_attrs_define
class DestinationsIsDirectDeliveryStatusFiltersOmittedAll:
    """
    Attributes:
        apps (list[V2DestinationApp] | Unset):
        status_filters (list[str] | Unset):
    """

    apps: list[V2DestinationApp] | Unset = UNSET
    status_filters: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        status_filters: list[str] | Unset = UNSET
        if not isinstance(self.status_filters, Unset):
            status_filters = self.status_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if status_filters is not UNSET:
            field_dict["statusFilters"] = status_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_destination_app import V2DestinationApp

        d = dict(src_dict)
        _apps = d.pop("apps", UNSET)
        apps: list[V2DestinationApp] | Unset = UNSET
        if _apps is not UNSET:
            apps = []
            for apps_item_data in _apps:
                apps_item = V2DestinationApp.from_dict(apps_item_data)

                apps.append(apps_item)

        status_filters = cast(list[str], d.pop("statusFilters", UNSET))

        destinations_is_direct_delivery_status_filters_omitted_all = cls(
            apps=apps,
            status_filters=status_filters,
        )

        destinations_is_direct_delivery_status_filters_omitted_all.additional_properties = d
        return destinations_is_direct_delivery_status_filters_omitted_all

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
