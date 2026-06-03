from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason_entry import ReasonEntry


T = TypeVar("T", bound="UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType")


@_attrs_define
class UnsupportedAssetTypeBreakdownGroupsUnsupportedFindingsForASingleAssetType:
    """
    Attributes:
        affected_assets (int | Unset):
        by_reason (list[ReasonEntry] | Unset): OrderedReasons is a list of reason→count pairs that marshals as a JSON
            object
            with keys in insertion order (preserving sort-by-count).
        count (int | Unset):
        unit (str | Unset):
    """

    affected_assets: int | Unset = UNSET
    by_reason: list[ReasonEntry] | Unset = UNSET
    count: int | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_assets = self.affected_assets

        by_reason: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_reason, Unset):
            by_reason = []
            for componentsschemas_ordered_reasons_item_data in self.by_reason:
                componentsschemas_ordered_reasons_item = componentsschemas_ordered_reasons_item_data.to_dict()
                by_reason.append(componentsschemas_ordered_reasons_item)

        count = self.count

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_assets is not UNSET:
            field_dict["affected_assets"] = affected_assets
        if by_reason is not UNSET:
            field_dict["by_reason"] = by_reason
        if count is not UNSET:
            field_dict["count"] = count
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reason_entry import ReasonEntry

        d = dict(src_dict)
        affected_assets = d.pop("affected_assets", UNSET)

        _by_reason = d.pop("by_reason", UNSET)
        by_reason: list[ReasonEntry] | Unset = UNSET
        if _by_reason is not UNSET:
            by_reason = []
            for componentsschemas_ordered_reasons_item_data in _by_reason:
                componentsschemas_ordered_reasons_item = ReasonEntry.from_dict(
                    componentsschemas_ordered_reasons_item_data
                )

                by_reason.append(componentsschemas_ordered_reasons_item)

        count = d.pop("count", UNSET)

        unit = d.pop("unit", UNSET)

        unsupported_asset_type_breakdown_groups_unsupported_findings_for_a_single_asset_type = cls(
            affected_assets=affected_assets,
            by_reason=by_reason,
            count=count,
            unit=unit,
        )

        unsupported_asset_type_breakdown_groups_unsupported_findings_for_a_single_asset_type.additional_properties = d
        return unsupported_asset_type_breakdown_groups_unsupported_findings_for_a_single_asset_type

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
