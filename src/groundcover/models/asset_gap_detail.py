from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_gap_detail_keys_by_datasource import AssetGapDetailKeysByDatasource
    from ..models.asset_gap_detail_keys_by_metric import AssetGapDetailKeysByMetric
    from ..models.asset_gap_detail_values_by_metric import AssetGapDetailValuesByMetric
    from ..models.executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran import (
        ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan,
    )


T = TypeVar("T", bound="AssetGapDetail")


@_attrs_define
class AssetGapDetail:
    """AssetGapDetail describes one unit's gaps, counted once regardless of how many
    findings produced it.

        Attributes:
            asset_id (str | Unset):
            asset_name (str | Unset):
            datasources (list[str] | Unset):
            keys (list[str] | Unset):
            keys_by_datasource (AssetGapDetailKeysByDatasource | Unset):
            keys_by_metric (AssetGapDetailKeysByMetric | Unset): KeysByMetric and KeysByDatasource preserve which owner each
                missing key
                belongs to. Without them a unit missing a metric label and a log field
                reported both keys under the metric *and* under logs.
            metrics (list[str] | Unset):
            queries (list[ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan] | Unset):
            reason (str | Unset):
            some_queries_returned_data (bool | Unset): SomeQueriesReturnedData distinguishes a unit where every query came
                back
                empty from one where only some did. Without it, a widget with nine working
                series and one broken one is indistinguishable from a wholly dead widget.
            values (list[str] | Unset):
            values_by_metric (AssetGapDetailValuesByMetric | Unset):
            widget_id (str | Unset):
            widget_title (str | Unset):
    """

    asset_id: str | Unset = UNSET
    asset_name: str | Unset = UNSET
    datasources: list[str] | Unset = UNSET
    keys: list[str] | Unset = UNSET
    keys_by_datasource: AssetGapDetailKeysByDatasource | Unset = UNSET
    keys_by_metric: AssetGapDetailKeysByMetric | Unset = UNSET
    metrics: list[str] | Unset = UNSET
    queries: list[ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan] | Unset = UNSET
    reason: str | Unset = UNSET
    some_queries_returned_data: bool | Unset = UNSET
    values: list[str] | Unset = UNSET
    values_by_metric: AssetGapDetailValuesByMetric | Unset = UNSET
    widget_id: str | Unset = UNSET
    widget_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        datasources: list[str] | Unset = UNSET
        if not isinstance(self.datasources, Unset):
            datasources = self.datasources

        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        keys_by_datasource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keys_by_datasource, Unset):
            keys_by_datasource = self.keys_by_datasource.to_dict()

        keys_by_metric: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keys_by_metric, Unset):
            keys_by_metric = self.keys_by_metric.to_dict()

        metrics: list[str] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics

        queries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = []
            for queries_item_data in self.queries:
                queries_item = queries_item_data.to_dict()
                queries.append(queries_item)

        reason = self.reason

        some_queries_returned_data = self.some_queries_returned_data

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        values_by_metric: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values_by_metric, Unset):
            values_by_metric = self.values_by_metric.to_dict()

        widget_id = self.widget_id

        widget_title = self.widget_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if datasources is not UNSET:
            field_dict["datasources"] = datasources
        if keys is not UNSET:
            field_dict["keys"] = keys
        if keys_by_datasource is not UNSET:
            field_dict["keys_by_datasource"] = keys_by_datasource
        if keys_by_metric is not UNSET:
            field_dict["keys_by_metric"] = keys_by_metric
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if queries is not UNSET:
            field_dict["queries"] = queries
        if reason is not UNSET:
            field_dict["reason"] = reason
        if some_queries_returned_data is not UNSET:
            field_dict["some_queries_returned_data"] = some_queries_returned_data
        if values is not UNSET:
            field_dict["values"] = values
        if values_by_metric is not UNSET:
            field_dict["values_by_metric"] = values_by_metric
        if widget_id is not UNSET:
            field_dict["widget_id"] = widget_id
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_gap_detail_keys_by_datasource import AssetGapDetailKeysByDatasource
        from ..models.asset_gap_detail_keys_by_metric import AssetGapDetailKeysByMetric
        from ..models.asset_gap_detail_values_by_metric import AssetGapDetailValuesByMetric
        from ..models.executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran import (
            ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan,
        )

        d = dict(src_dict)
        asset_id = d.pop("asset_id", UNSET)

        asset_name = d.pop("asset_name", UNSET)

        datasources = cast(list[str], d.pop("datasources", UNSET))

        keys = cast(list[str], d.pop("keys", UNSET))

        _keys_by_datasource = d.pop("keys_by_datasource", UNSET)
        keys_by_datasource: AssetGapDetailKeysByDatasource | Unset
        if isinstance(_keys_by_datasource, Unset) or _keys_by_datasource is None:
            keys_by_datasource = UNSET
        else:
            keys_by_datasource = AssetGapDetailKeysByDatasource.from_dict(_keys_by_datasource)

        _keys_by_metric = d.pop("keys_by_metric", UNSET)
        keys_by_metric: AssetGapDetailKeysByMetric | Unset
        if isinstance(_keys_by_metric, Unset) or _keys_by_metric is None:
            keys_by_metric = UNSET
        else:
            keys_by_metric = AssetGapDetailKeysByMetric.from_dict(_keys_by_metric)

        metrics = cast(list[str], d.pop("metrics", UNSET))

        _queries = d.pop("queries", UNSET)
        queries: list[ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan] | Unset = UNSET
        if _queries is not UNSET:
            queries = []
            for queries_item_data in _queries:
                queries_item = ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan.from_dict(queries_item_data)

                queries.append(queries_item)

        reason = d.pop("reason", UNSET)

        some_queries_returned_data = d.pop("some_queries_returned_data", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        _values_by_metric = d.pop("values_by_metric", UNSET)
        values_by_metric: AssetGapDetailValuesByMetric | Unset
        if isinstance(_values_by_metric, Unset) or _values_by_metric is None:
            values_by_metric = UNSET
        else:
            values_by_metric = AssetGapDetailValuesByMetric.from_dict(_values_by_metric)

        widget_id = d.pop("widget_id", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        asset_gap_detail = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            datasources=datasources,
            keys=keys,
            keys_by_datasource=keys_by_datasource,
            keys_by_metric=keys_by_metric,
            metrics=metrics,
            queries=queries,
            reason=reason,
            some_queries_returned_data=some_queries_returned_data,
            values=values,
            values_by_metric=values_by_metric,
            widget_id=widget_id,
            widget_title=widget_title,
        )

        asset_gap_detail.additional_properties = d
        return asset_gap_detail

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
