from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unified_summary_is_the_single_hierarchical_summary_included_in_json_output_affected_assets_by_type_additional_property import (
        UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByTypeAdditionalProperty,
    )


T = TypeVar("T", bound="UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByType")


@_attrs_define
class UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByType:
    """ """

    additional_properties: dict[
        str, UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByTypeAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unified_summary_is_the_single_hierarchical_summary_included_in_json_output_affected_assets_by_type_additional_property import (
            UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByTypeAdditionalProperty,
        )

        d = dict(src_dict)
        unified_summary_is_the_single_hierarchical_summary_included_in_json_output_affected_assets_by_type = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByTypeAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        unified_summary_is_the_single_hierarchical_summary_included_in_json_output_affected_assets_by_type.additional_properties = additional_properties
        return unified_summary_is_the_single_hierarchical_summary_included_in_json_output_affected_assets_by_type

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByTypeAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAffectedAssetsByTypeAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
