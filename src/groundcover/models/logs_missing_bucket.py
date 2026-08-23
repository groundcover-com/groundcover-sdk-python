from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_gap_detail import AssetGapDetail


T = TypeVar("T", bound="LogsMissingBucket")


@_attrs_define
class LogsMissingBucket:
    """LogsMissingBucket covers units whose log dataset is absent, including the case
    where the log source they filter on is not ingested into groundcover at all.

        Attributes:
            assets (list[AssetGapDetail] | Unset):
            count (int | Unset):
            known_sources (list[str] | Unset):
            missing_sources (list[str] | Unset):
            source_not_ingested (int | Unset): SourceNotIngested counts units filtering on a source:<value> that
                groundcover does not ingest, which no lookback widening can fix.
    """

    assets: list[AssetGapDetail] | Unset = UNSET
    count: int | Unset = UNSET
    known_sources: list[str] | Unset = UNSET
    missing_sources: list[str] | Unset = UNSET
    source_not_ingested: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        count = self.count

        known_sources: list[str] | Unset = UNSET
        if not isinstance(self.known_sources, Unset):
            known_sources = self.known_sources

        missing_sources: list[str] | Unset = UNSET
        if not isinstance(self.missing_sources, Unset):
            missing_sources = self.missing_sources

        source_not_ingested = self.source_not_ingested

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if count is not UNSET:
            field_dict["count"] = count
        if known_sources is not UNSET:
            field_dict["known_sources"] = known_sources
        if missing_sources is not UNSET:
            field_dict["missing_sources"] = missing_sources
        if source_not_ingested is not UNSET:
            field_dict["source_not_ingested"] = source_not_ingested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_gap_detail import AssetGapDetail

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[AssetGapDetail] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = AssetGapDetail.from_dict(assets_item_data)

                assets.append(assets_item)

        count = d.pop("count", UNSET)

        known_sources = cast(list[str], d.pop("known_sources", UNSET))

        missing_sources = cast(list[str], d.pop("missing_sources", UNSET))

        source_not_ingested = d.pop("source_not_ingested", UNSET)

        logs_missing_bucket = cls(
            assets=assets,
            count=count,
            known_sources=known_sources,
            missing_sources=missing_sources,
            source_not_ingested=source_not_ingested,
        )

        logs_missing_bucket.additional_properties = d
        return logs_missing_bucket

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
