from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_gap_detail import AssetGapDetail
    from ..models.supported_not_converted_bucket_covers_supported_types_that_failed_conversion_by_error import (
        SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversionByError,
    )


T = TypeVar("T", bound="SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion")


@_attrs_define
class SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion:
    """
    Attributes:
        assets (list[AssetGapDetail] | Unset):
        by_error (SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversionByError | Unset):
        total (int | Unset):
    """

    assets: list[AssetGapDetail] | Unset = UNSET
    by_error: SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversionByError | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        by_error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_error, Unset):
            by_error = self.by_error.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if by_error is not UNSET:
            field_dict["by_error"] = by_error
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_gap_detail import AssetGapDetail
        from ..models.supported_not_converted_bucket_covers_supported_types_that_failed_conversion_by_error import (
            SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversionByError,
        )

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[AssetGapDetail] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = AssetGapDetail.from_dict(assets_item_data)

                assets.append(assets_item)

        _by_error = d.pop("by_error", UNSET)
        by_error: SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversionByError | Unset
        if isinstance(_by_error, Unset) or _by_error is None:
            by_error = UNSET
        else:
            by_error = SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversionByError.from_dict(_by_error)

        total = d.pop("total", UNSET)

        supported_not_converted_bucket_covers_supported_types_that_failed_conversion = cls(
            assets=assets,
            by_error=by_error,
            total=total,
        )

        supported_not_converted_bucket_covers_supported_types_that_failed_conversion.additional_properties = d
        return supported_not_converted_bucket_covers_supported_types_that_failed_conversion

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
