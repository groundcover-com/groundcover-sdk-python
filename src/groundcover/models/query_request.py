from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_request_query_type import QueryRequestQueryType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.known_pipelines import KnownPipelines
    from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
        PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
    )


T = TypeVar("T", bound="QueryRequest")


@_attrs_define
class QueryRequest:
    """QueryRequest represents a request to query metrics

    Attributes:
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Additional conditions to
            apply
        end (datetime.datetime | Unset): End time for the query
        filters (str | Unset): GCQL filters to apply
        pipeline (PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate |
            Unset):
        promql (str | Unset): Direct PromQL query string
        query_type (QueryRequestQueryType | Unset): Query type: either "range" or "instant"
            range MetricsQueryTypeRange
            instant MetricsQueryTypeInstant
        start (datetime.datetime | Unset): Start time for the query
        step (str | Unset): Step duration for range queries (e.g., "1m", "5m")
        sub_pipelines (KnownPipelines | Unset): KnownPipelines is a map of template names to pipeline templates
            We need this separate model to prevent circular references in swagger generation
    """

    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    filters: str | Unset = UNSET
    pipeline: (
        PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate | Unset
    ) = UNSET
    promql: str | Unset = UNSET
    query_type: QueryRequestQueryType | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    step: str | Unset = UNSET
    sub_pipelines: KnownPipelines | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        filters = self.filters

        pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline, Unset):
            pipeline = self.pipeline.to_dict()

        promql = self.promql

        query_type: str | Unset = UNSET
        if not isinstance(self.query_type, Unset):
            query_type = self.query_type.value

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        step = self.step

        sub_pipelines: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_pipelines, Unset):
            sub_pipelines = self.sub_pipelines.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if end is not UNSET:
            field_dict["End"] = end
        if filters is not UNSET:
            field_dict["Filters"] = filters
        if pipeline is not UNSET:
            field_dict["Pipeline"] = pipeline
        if promql is not UNSET:
            field_dict["Promql"] = promql
        if query_type is not UNSET:
            field_dict["QueryType"] = query_type
        if start is not UNSET:
            field_dict["Start"] = start
        if step is not UNSET:
            field_dict["Step"] = step
        if sub_pipelines is not UNSET:
            field_dict["SubPipelines"] = sub_pipelines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.known_pipelines import KnownPipelines
        from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
            PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
        )

        d = dict(src_dict)
        _conditions = d.pop("Conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        _end = d.pop("End", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

        filters = d.pop("Filters", UNSET)

        _pipeline = d.pop("Pipeline", UNSET)
        pipeline: (
            PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate | Unset
        )
        if isinstance(_pipeline, Unset) or _pipeline is None:
            pipeline = UNSET
        else:
            pipeline = PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate.from_dict(
                _pipeline
            )

        promql = d.pop("Promql", UNSET)

        _query_type = d.pop("QueryType", UNSET)
        query_type: QueryRequestQueryType | Unset
        if isinstance(_query_type, Unset) or _query_type is None:
            query_type = UNSET
        else:
            query_type = QueryRequestQueryType(_query_type)

        _start = d.pop("Start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset) or _start is None:
            start = UNSET
        else:
            start = parse_datetime(_start)

        step = d.pop("Step", UNSET)

        _sub_pipelines = d.pop("SubPipelines", UNSET)
        sub_pipelines: KnownPipelines | Unset
        if isinstance(_sub_pipelines, Unset) or _sub_pipelines is None:
            sub_pipelines = UNSET
        else:
            sub_pipelines = KnownPipelines.from_dict(_sub_pipelines)

        query_request = cls(
            conditions=conditions,
            end=end,
            filters=filters,
            pipeline=pipeline,
            promql=promql,
            query_type=query_type,
            start=start,
            step=step,
            sub_pipelines=sub_pipelines,
        )

        query_request.additional_properties = d
        return query_request

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
