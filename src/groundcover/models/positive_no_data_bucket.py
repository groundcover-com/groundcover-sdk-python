from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_gap_detail import AssetGapDetail
    from ..models.reason_entry import ReasonEntry


T = TypeVar("T", bound="PositiveNoDataBucket")


@_attrs_define
class PositiveNoDataBucket:
    """PositiveNoDataBucket covers units where every dependency resolves yet no data
    came back, broken down by the reason we could establish.

        Attributes:
            assets (list[AssetGapDetail] | Unset):
            by_reason (list[ReasonEntry] | Unset): OrderedReasons is a list of reason→count pairs that marshals as a JSON
                object
                with keys in insertion order (preserving sort-by-count).
            count (int | Unset):
            pct (float | Unset):
    """

    assets: list[AssetGapDetail] | Unset = UNSET
    by_reason: list[ReasonEntry] | Unset = UNSET
    count: int | Unset = UNSET
    pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        by_reason: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_reason, Unset):
            by_reason = []
            for componentsschemas_ordered_reasons_item_data in self.by_reason:
                componentsschemas_ordered_reasons_item = componentsschemas_ordered_reasons_item_data.to_dict()
                by_reason.append(componentsschemas_ordered_reasons_item)

        count = self.count

        pct = self.pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if by_reason is not UNSET:
            field_dict["by_reason"] = by_reason
        if count is not UNSET:
            field_dict["count"] = count
        if pct is not UNSET:
            field_dict["pct"] = pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_gap_detail import AssetGapDetail
        from ..models.reason_entry import ReasonEntry

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[AssetGapDetail] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = AssetGapDetail.from_dict(assets_item_data)

                assets.append(assets_item)

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

        pct = d.pop("pct", UNSET)

        positive_no_data_bucket = cls(
            assets=assets,
            by_reason=by_reason,
            count=count,
            pct=pct,
        )

        positive_no_data_bucket.additional_properties = d
        return positive_no_data_bucket

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
