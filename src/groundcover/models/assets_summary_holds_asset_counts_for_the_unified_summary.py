from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_summary_holds_asset_counts_for_the_unified_summary_by_type import (
        AssetsSummaryHoldsAssetCountsForTheUnifiedSummaryByType,
    )


T = TypeVar("T", bound="AssetsSummaryHoldsAssetCountsForTheUnifiedSummary")


@_attrs_define
class AssetsSummaryHoldsAssetCountsForTheUnifiedSummary:
    """
    Attributes:
        by_type (AssetsSummaryHoldsAssetCountsForTheUnifiedSummaryByType | Unset):
        total (int | Unset):
    """

    by_type: AssetsSummaryHoldsAssetCountsForTheUnifiedSummaryByType | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = self.by_type.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_type is not UNSET:
            field_dict["by_type"] = by_type
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assets_summary_holds_asset_counts_for_the_unified_summary_by_type import (
            AssetsSummaryHoldsAssetCountsForTheUnifiedSummaryByType,
        )

        d = dict(src_dict)
        _by_type = d.pop("by_type", UNSET)
        by_type: AssetsSummaryHoldsAssetCountsForTheUnifiedSummaryByType | Unset
        if isinstance(_by_type, Unset) or _by_type is None:
            by_type = UNSET
        else:
            by_type = AssetsSummaryHoldsAssetCountsForTheUnifiedSummaryByType.from_dict(_by_type)

        total = d.pop("total", UNSET)

        assets_summary_holds_asset_counts_for_the_unified_summary = cls(
            by_type=by_type,
            total=total,
        )

        assets_summary_holds_asset_counts_for_the_unified_summary.additional_properties = d
        return assets_summary_holds_asset_counts_for_the_unified_summary

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
