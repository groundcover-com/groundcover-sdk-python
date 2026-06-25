from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_query_is_the_base_struct_for_different_query_types import (
        BaseQueryIsTheBaseStructForDifferentQueryTypes,
    )
    from ..models.reducer_model_defines_how_to_aggregate_or_transform_query_results import (
        ReducerModelDefinesHowToAggregateOrTransformQueryResults,
    )
    from ..models.threshold_defines_a_condition_to_evaluate_against_a_reduced_value import (
        ThresholdDefinesAConditionToEvaluateAgainstAReducedValue,
    )


T = TypeVar("T", bound="ThresholdDefinitions")


@_attrs_define
class ThresholdDefinitions:
    """
    Attributes:
        queries (list[BaseQueryIsTheBaseStructForDifferentQueryTypes]): List of queries defining the data sources for
            the monitor.
        reducers (list[ReducerModelDefinesHowToAggregateOrTransformQueryResults] | Unset): List of reducers to aggregate
            or transform query results.
        thresholds (list[ThresholdDefinesAConditionToEvaluateAgainstAReducedValue] | Unset): List of thresholds to
            evaluate against the final reduced value.
    """

    queries: list[BaseQueryIsTheBaseStructForDifferentQueryTypes]
    reducers: list[ReducerModelDefinesHowToAggregateOrTransformQueryResults] | Unset = UNSET
    thresholds: list[ThresholdDefinesAConditionToEvaluateAgainstAReducedValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        reducers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reducers, Unset):
            reducers = []
            for reducers_item_data in self.reducers:
                reducers_item = reducers_item_data.to_dict()
                reducers.append(reducers_item)

        thresholds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = []
            for thresholds_item_data in self.thresholds:
                thresholds_item = thresholds_item_data.to_dict()
                thresholds.append(thresholds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queries": queries,
            }
        )
        if reducers is not UNSET:
            field_dict["reducers"] = reducers
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_query_is_the_base_struct_for_different_query_types import (
            BaseQueryIsTheBaseStructForDifferentQueryTypes,
        )
        from ..models.reducer_model_defines_how_to_aggregate_or_transform_query_results import (
            ReducerModelDefinesHowToAggregateOrTransformQueryResults,
        )
        from ..models.threshold_defines_a_condition_to_evaluate_against_a_reduced_value import (
            ThresholdDefinesAConditionToEvaluateAgainstAReducedValue,
        )

        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = BaseQueryIsTheBaseStructForDifferentQueryTypes.from_dict(queries_item_data)

            queries.append(queries_item)

        _reducers = d.pop("reducers", UNSET)
        reducers: list[ReducerModelDefinesHowToAggregateOrTransformQueryResults] | Unset = UNSET
        if _reducers is not UNSET:
            reducers = []
            for reducers_item_data in _reducers:
                reducers_item = ReducerModelDefinesHowToAggregateOrTransformQueryResults.from_dict(reducers_item_data)

                reducers.append(reducers_item)

        _thresholds = d.pop("thresholds", UNSET)
        thresholds: list[ThresholdDefinesAConditionToEvaluateAgainstAReducedValue] | Unset = UNSET
        if _thresholds is not UNSET:
            thresholds = []
            for thresholds_item_data in _thresholds:
                thresholds_item = ThresholdDefinesAConditionToEvaluateAgainstAReducedValue.from_dict(
                    thresholds_item_data
                )

                thresholds.append(thresholds_item)

        threshold_definitions = cls(
            queries=queries,
            reducers=reducers,
            thresholds=thresholds,
        )

        threshold_definitions.additional_properties = d
        return threshold_definitions

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
