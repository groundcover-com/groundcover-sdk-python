from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitors_catalog_item import MonitorsCatalogItem


T = TypeVar("T", bound="MonitorsCatalogItemByPack")


@_attrs_define
class MonitorsCatalogItemByPack:
    """
    Attributes:
        description (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        monitors (list[MonitorsCatalogItem] | Unset):
    """

    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    monitors: list[MonitorsCatalogItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        id = self.id

        monitors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = []
            for monitors_item_data in self.monitors:
                monitors_item = monitors_item_data.to_dict()
                monitors.append(monitors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if monitors is not UNSET:
            field_dict["monitors"] = monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitors_catalog_item import MonitorsCatalogItem

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        _monitors = d.pop("monitors", UNSET)
        monitors: list[MonitorsCatalogItem] | Unset = UNSET
        if _monitors is not UNSET:
            monitors = []
            for monitors_item_data in _monitors:
                monitors_item = MonitorsCatalogItem.from_dict(monitors_item_data)

                monitors.append(monitors_item)

        monitors_catalog_item_by_pack = cls(
            description=description,
            display_name=display_name,
            id=id,
            monitors=monitors,
        )

        monitors_catalog_item_by_pack.additional_properties = d
        return monitors_catalog_item_by_pack

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
