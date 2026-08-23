from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel_asset_entry import FunnelAssetEntry
    from ..models.funnel_by_asset_by_stage import FunnelByAssetByStage


T = TypeVar("T", bound="FunnelByAsset")


@_attrs_define
class FunnelByAsset:
    """FunnelByAsset is the per-asset view of the funnel: every monitor and every
    dashboard widget, with the stage it terminated at.

        Attributes:
            assets (list[FunnelAssetEntry] | Unset):
            by_stage (FunnelByAssetByStage | Unset):
            total (int | Unset):
    """

    assets: list[FunnelAssetEntry] | Unset = UNSET
    by_stage: FunnelByAssetByStage | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        by_stage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_stage, Unset):
            by_stage = self.by_stage.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if by_stage is not UNSET:
            field_dict["by_stage"] = by_stage
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funnel_asset_entry import FunnelAssetEntry
        from ..models.funnel_by_asset_by_stage import FunnelByAssetByStage

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[FunnelAssetEntry] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = FunnelAssetEntry.from_dict(assets_item_data)

                assets.append(assets_item)

        _by_stage = d.pop("by_stage", UNSET)
        by_stage: FunnelByAssetByStage | Unset
        if isinstance(_by_stage, Unset) or _by_stage is None:
            by_stage = UNSET
        else:
            by_stage = FunnelByAssetByStage.from_dict(_by_stage)

        total = d.pop("total", UNSET)

        funnel_by_asset = cls(
            assets=assets,
            by_stage=by_stage,
            total=total,
        )

        funnel_by_asset.additional_properties = d
        return funnel_by_asset

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
