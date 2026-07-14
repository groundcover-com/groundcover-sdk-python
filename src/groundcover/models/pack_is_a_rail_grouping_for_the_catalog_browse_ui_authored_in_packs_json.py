from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson")


@_attrs_define
class PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson:
    """
    Attributes:
        display (str | Unset):
        id (str | Unset):
        priority (int | Unset):
    """

    display: str | Unset = UNSET
    id: str | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display = self.display

        id = self.id

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display is not UNSET:
            field_dict["display"] = display
        if id is not UNSET:
            field_dict["id"] = id
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        display = d.pop("display", UNSET)

        id = d.pop("id", UNSET)

        priority = d.pop("priority", UNSET)

        pack_is_a_rail_grouping_for_the_catalog_browse_ui_authored_in_packs_json = cls(
            display=display,
            id=id,
            priority=priority,
        )

        pack_is_a_rail_grouping_for_the_catalog_browse_ui_authored_in_packs_json.additional_properties = d
        return pack_is_a_rail_grouping_for_the_catalog_browse_ui_authored_in_packs_json

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
