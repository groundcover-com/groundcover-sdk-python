from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_gap_detail import AssetGapDetail
    from ..models.not_supported_bucket_covers_unsupported_types_bucketed_by_type_by_type import (
        NotSupportedBucketCoversUnsupportedTypesBucketedByTypeByType,
    )


T = TypeVar("T", bound="NotSupportedBucketCoversUnsupportedTypesBucketedByType")


@_attrs_define
class NotSupportedBucketCoversUnsupportedTypesBucketedByType:
    """
    Attributes:
        assets (list[AssetGapDetail] | Unset):
        by_type (NotSupportedBucketCoversUnsupportedTypesBucketedByTypeByType | Unset):
        total (int | Unset):
    """

    assets: list[AssetGapDetail] | Unset = UNSET
    by_type: NotSupportedBucketCoversUnsupportedTypesBucketedByTypeByType | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        by_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = self.by_type.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if by_type is not UNSET:
            field_dict["by_type"] = by_type
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_gap_detail import AssetGapDetail
        from ..models.not_supported_bucket_covers_unsupported_types_bucketed_by_type_by_type import (
            NotSupportedBucketCoversUnsupportedTypesBucketedByTypeByType,
        )

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[AssetGapDetail] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = AssetGapDetail.from_dict(assets_item_data)

                assets.append(assets_item)

        _by_type = d.pop("by_type", UNSET)
        by_type: NotSupportedBucketCoversUnsupportedTypesBucketedByTypeByType | Unset
        if isinstance(_by_type, Unset) or _by_type is None:
            by_type = UNSET
        else:
            by_type = NotSupportedBucketCoversUnsupportedTypesBucketedByTypeByType.from_dict(_by_type)

        total = d.pop("total", UNSET)

        not_supported_bucket_covers_unsupported_types_bucketed_by_type = cls(
            assets=assets,
            by_type=by_type,
            total=total,
        )

        not_supported_bucket_covers_unsupported_types_bucketed_by_type.additional_properties = d
        return not_supported_bucket_covers_unsupported_types_bucketed_by_type

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
