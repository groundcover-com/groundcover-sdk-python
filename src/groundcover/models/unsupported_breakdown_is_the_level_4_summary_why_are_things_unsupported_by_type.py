from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unsupported_asset_type_breakdown_groups_unsupported_findings_for_a_single_asset_type import (
        UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType,
    )


T = TypeVar("T", bound="UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupportedByType")


@_attrs_define
class UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupportedByType:
    """ """

    additional_properties: dict[str, UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unsupported_asset_type_breakdown_groups_unsupported_findings_for_a_single_asset_type import (
            UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType,
        )

        d = dict(src_dict)
        unsupported_breakdown_is_the_level_4_summary_why_are_things_unsupported_by_type = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        unsupported_breakdown_is_the_level_4_summary_why_are_things_unsupported_by_type.additional_properties = (
            additional_properties
        )
        return unsupported_breakdown_is_the_level_4_summary_why_are_things_unsupported_by_type

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
