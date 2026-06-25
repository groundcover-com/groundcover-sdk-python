from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog")


@_attrs_define
class CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog:
    """
    Attributes:
        category (str | Unset):
        id (str | Unset):
        tags (list[str] | Unset):
        version (int | Unset):
    """

    category: str | Unset = UNSET
    id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        id = self.id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if id is not UNSET:
            field_dict["id"] = id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if version is not UNSET:
            field_dict["version"] = version

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
        category = d.pop("category", UNSET)

        id = d.pop("id", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        version = d.pop("version", UNSET)

        catalog_model_holds_metadata_if_the_monitor_originated_from_a_catalog = cls(
            category=category,
            id=id,
            tags=tags,
            version=version,
        )

        catalog_model_holds_metadata_if_the_monitor_originated_from_a_catalog.additional_properties = d
        return catalog_model_holds_metadata_if_the_monitor_originated_from_a_catalog

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
