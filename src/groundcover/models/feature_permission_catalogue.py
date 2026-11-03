from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_permission_catalogue_additional_property_item import (
    FeaturePermissionCatalogueAdditionalPropertyItem,
)

T = TypeVar("T", bound="FeaturePermissionCatalogue")


@_attrs_define
class FeaturePermissionCatalogue:
    """ """

    additional_properties: dict[str, list[FeaturePermissionCatalogueAdditionalPropertyItem]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.value
                field_dict[prop_name].append(additional_property_item)

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
        feature_permission_catalogue = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = FeaturePermissionCatalogueAdditionalPropertyItem(
                    additional_property_item_data
                )

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        feature_permission_catalogue.additional_properties = additional_properties
        return feature_permission_catalogue

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[FeaturePermissionCatalogueAdditionalPropertyItem]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[FeaturePermissionCatalogueAdditionalPropertyItem]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
