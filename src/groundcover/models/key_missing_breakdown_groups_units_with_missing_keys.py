from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_gap_detail import AssetGapDetail
    from ..models.datasource_key_gap_aggregates_missing_field_keys_for_one_search_datasource import (
        DatasourceKeyGapAggregatesMissingFieldKeysForOneSearchDatasource,
    )
    from ..models.metric_key_gap_aggregates_missing_label_keys_for_one_metric_across_units import (
        MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits,
    )


T = TypeVar("T", bound="KeyMissingBreakdownGroupsUnitsWithMissingKeys")


@_attrs_define
class KeyMissingBreakdownGroupsUnitsWithMissingKeys:
    """Metric label gaps and search field gaps are reported separately: a log or event
    field gap has no metric to attribute it to, and folding both into a by-metric
    view produced a meaningless "unknown" bucket.

        Attributes:
            assets (list[AssetGapDetail] | Unset):
            by_datasource (list[DatasourceKeyGapAggregatesMissingFieldKeysForOneSearchDatasource] | Unset):
            by_metric (list[MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits] | Unset):
            count (int | Unset):
    """

    assets: list[AssetGapDetail] | Unset = UNSET
    by_datasource: list[DatasourceKeyGapAggregatesMissingFieldKeysForOneSearchDatasource] | Unset = UNSET
    by_metric: list[MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits] | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        by_datasource: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_datasource, Unset):
            by_datasource = []
            for by_datasource_item_data in self.by_datasource:
                by_datasource_item = by_datasource_item_data.to_dict()
                by_datasource.append(by_datasource_item)

        by_metric: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_metric, Unset):
            by_metric = []
            for by_metric_item_data in self.by_metric:
                by_metric_item = by_metric_item_data.to_dict()
                by_metric.append(by_metric_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if by_datasource is not UNSET:
            field_dict["by_datasource"] = by_datasource
        if by_metric is not UNSET:
            field_dict["by_metric"] = by_metric
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_gap_detail import AssetGapDetail
        from ..models.datasource_key_gap_aggregates_missing_field_keys_for_one_search_datasource import (
            DatasourceKeyGapAggregatesMissingFieldKeysForOneSearchDatasource,
        )
        from ..models.metric_key_gap_aggregates_missing_label_keys_for_one_metric_across_units import (
            MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits,
        )

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[AssetGapDetail] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = AssetGapDetail.from_dict(assets_item_data)

                assets.append(assets_item)

        _by_datasource = d.pop("by_datasource", UNSET)
        by_datasource: list[DatasourceKeyGapAggregatesMissingFieldKeysForOneSearchDatasource] | Unset = UNSET
        if _by_datasource is not UNSET:
            by_datasource = []
            for by_datasource_item_data in _by_datasource:
                by_datasource_item = DatasourceKeyGapAggregatesMissingFieldKeysForOneSearchDatasource.from_dict(
                    by_datasource_item_data
                )

                by_datasource.append(by_datasource_item)

        _by_metric = d.pop("by_metric", UNSET)
        by_metric: list[MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits] | Unset = UNSET
        if _by_metric is not UNSET:
            by_metric = []
            for by_metric_item_data in _by_metric:
                by_metric_item = MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits.from_dict(
                    by_metric_item_data
                )

                by_metric.append(by_metric_item)

        count = d.pop("count", UNSET)

        key_missing_breakdown_groups_units_with_missing_keys = cls(
            assets=assets,
            by_datasource=by_datasource,
            by_metric=by_metric,
            count=count,
        )

        key_missing_breakdown_groups_units_with_missing_keys.additional_properties = d
        return key_missing_breakdown_groups_units_with_missing_keys

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
