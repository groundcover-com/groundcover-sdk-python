from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran import (
        ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan,
    )


T = TypeVar("T", bound="FunnelAssetEntry")


@_attrs_define
class FunnelAssetEntry:
    """FunnelAssetEntry maps one asset — or one dashboard widget — to the funnel stage
    it reached, with the queries that were executed as evidence.

        Attributes:
            asset_id (str | Unset):
            asset_name (str | Unset):
            asset_type (str | Unset):
            metrics (list[str] | Unset):
            missing_keys (list[str] | Unset):
            missing_values (list[str] | Unset):
            queries (list[ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan] | Unset):
            reason (str | Unset):
            stage (str | Unset):
            widget_id (str | Unset):
            widget_title (str | Unset):
    """

    asset_id: str | Unset = UNSET
    asset_name: str | Unset = UNSET
    asset_type: str | Unset = UNSET
    metrics: list[str] | Unset = UNSET
    missing_keys: list[str] | Unset = UNSET
    missing_values: list[str] | Unset = UNSET
    queries: list[ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan] | Unset = UNSET
    reason: str | Unset = UNSET
    stage: str | Unset = UNSET
    widget_id: str | Unset = UNSET
    widget_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type = self.asset_type

        metrics: list[str] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics

        missing_keys: list[str] | Unset = UNSET
        if not isinstance(self.missing_keys, Unset):
            missing_keys = self.missing_keys

        missing_values: list[str] | Unset = UNSET
        if not isinstance(self.missing_values, Unset):
            missing_values = self.missing_values

        queries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = []
            for queries_item_data in self.queries:
                queries_item = queries_item_data.to_dict()
                queries.append(queries_item)

        reason = self.reason

        stage = self.stage

        widget_id = self.widget_id

        widget_title = self.widget_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if missing_keys is not UNSET:
            field_dict["missing_keys"] = missing_keys
        if missing_values is not UNSET:
            field_dict["missing_values"] = missing_values
        if queries is not UNSET:
            field_dict["queries"] = queries
        if reason is not UNSET:
            field_dict["reason"] = reason
        if stage is not UNSET:
            field_dict["stage"] = stage
        if widget_id is not UNSET:
            field_dict["widget_id"] = widget_id
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran import (
            ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan,
        )

        d = dict(src_dict)
        asset_id = d.pop("asset_id", UNSET)

        asset_name = d.pop("asset_name", UNSET)

        asset_type = d.pop("asset_type", UNSET)

        metrics = cast(list[str], d.pop("metrics", UNSET))

        missing_keys = cast(list[str], d.pop("missing_keys", UNSET))

        missing_values = cast(list[str], d.pop("missing_values", UNSET))

        _queries = d.pop("queries", UNSET)
        queries: list[ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan] | Unset = UNSET
        if _queries is not UNSET:
            queries = []
            for queries_item_data in _queries:
                queries_item = ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan.from_dict(queries_item_data)

                queries.append(queries_item)

        reason = d.pop("reason", UNSET)

        stage = d.pop("stage", UNSET)

        widget_id = d.pop("widget_id", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        funnel_asset_entry = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
            metrics=metrics,
            missing_keys=missing_keys,
            missing_values=missing_values,
            queries=queries,
            reason=reason,
            stage=stage,
            widget_id=widget_id,
            widget_title=widget_title,
        )

        funnel_asset_entry.additional_properties = d
        return funnel_asset_entry

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
