from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
        PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
    )
    from ..models.relative_timerange_defines_a_time_range_relative_to_the_evaluation_time import (
        RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime,
    )
    from ..models.rollup import Rollup
    from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import SqlPipelineDefinesAPipelineForSearchQueries


T = TypeVar("T", bound="BaseQueryIsTheBaseStructForDifferentQueryTypes")


@_attrs_define
class BaseQueryIsTheBaseStructForDifferentQueryTypes:
    """
    Attributes:
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        data_type (str | Unset):
        datasource_id (str | Unset):
        datasource_type (str | Unset):
        evaluation_delay (int | Unset):
        expression (str | Unset):
        filters (str | Unset):
        instant_rollup (str | Unset):
        name (str | Unset):
        pipeline (PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate |
            Unset):
        query_type (str | Unset):
        relative_timerange (RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset):
        rollup (Rollup | Unset):
        sql_pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
            container for the join operation ONLY.
            When Union is set, the pipeline acts as a container for the union operation ONLY.
            In these cases, no other fields should be used.
    """

    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    data_type: str | Unset = UNSET
    datasource_id: str | Unset = UNSET
    datasource_type: str | Unset = UNSET
    evaluation_delay: int | Unset = UNSET
    expression: str | Unset = UNSET
    filters: str | Unset = UNSET
    instant_rollup: str | Unset = UNSET
    name: str | Unset = UNSET
    pipeline: (
        PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate | Unset
    ) = UNSET
    query_type: str | Unset = UNSET
    relative_timerange: RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset = UNSET
    rollup: Rollup | Unset = UNSET
    sql_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        data_type = self.data_type

        datasource_id = self.datasource_id

        datasource_type = self.datasource_type

        evaluation_delay = self.evaluation_delay

        expression = self.expression

        filters = self.filters

        instant_rollup = self.instant_rollup

        name = self.name

        pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline, Unset):
            pipeline = self.pipeline.to_dict()

        query_type = self.query_type

        relative_timerange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relative_timerange, Unset):
            relative_timerange = self.relative_timerange.to_dict()

        rollup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollup, Unset):
            rollup = self.rollup.to_dict()

        sql_pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sql_pipeline, Unset):
            sql_pipeline = self.sql_pipeline.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if datasource_id is not UNSET:
            field_dict["datasourceID"] = datasource_id
        if datasource_type is not UNSET:
            field_dict["datasourceType"] = datasource_type
        if evaluation_delay is not UNSET:
            field_dict["evaluationDelay"] = evaluation_delay
        if expression is not UNSET:
            field_dict["expression"] = expression
        if filters is not UNSET:
            field_dict["filters"] = filters
        if instant_rollup is not UNSET:
            field_dict["instantRollup"] = instant_rollup
        if name is not UNSET:
            field_dict["name"] = name
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if query_type is not UNSET:
            field_dict["queryType"] = query_type
        if relative_timerange is not UNSET:
            field_dict["relativeTimerange"] = relative_timerange
        if rollup is not UNSET:
            field_dict["rollup"] = rollup
        if sql_pipeline is not UNSET:
            field_dict["sqlPipeline"] = sql_pipeline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
            PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
        )
        from ..models.relative_timerange_defines_a_time_range_relative_to_the_evaluation_time import (
            RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime,
        )
        from ..models.rollup import Rollup
        from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import (
            SqlPipelineDefinesAPipelineForSearchQueries,
        )

        d = dict(src_dict)
        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        data_type = d.pop("dataType", UNSET)

        datasource_id = d.pop("datasourceID", UNSET)

        datasource_type = d.pop("datasourceType", UNSET)

        evaluation_delay = d.pop("evaluationDelay", UNSET)

        expression = d.pop("expression", UNSET)

        filters = d.pop("filters", UNSET)

        instant_rollup = d.pop("instantRollup", UNSET)

        name = d.pop("name", UNSET)

        _pipeline = d.pop("pipeline", UNSET)
        pipeline: (
            PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate | Unset
        )
        if isinstance(_pipeline, Unset) or _pipeline is None:
            pipeline = UNSET
        else:
            pipeline = PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate.from_dict(
                _pipeline
            )

        query_type = d.pop("queryType", UNSET)

        _relative_timerange = d.pop("relativeTimerange", UNSET)
        relative_timerange: RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset
        if isinstance(_relative_timerange, Unset) or _relative_timerange is None:
            relative_timerange = UNSET
        else:
            relative_timerange = RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime.from_dict(
                _relative_timerange
            )

        _rollup = d.pop("rollup", UNSET)
        rollup: Rollup | Unset
        if isinstance(_rollup, Unset) or _rollup is None:
            rollup = UNSET
        else:
            rollup = Rollup.from_dict(_rollup)

        _sql_pipeline = d.pop("sqlPipeline", UNSET)
        sql_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset
        if isinstance(_sql_pipeline, Unset) or _sql_pipeline is None:
            sql_pipeline = UNSET
        else:
            sql_pipeline = SqlPipelineDefinesAPipelineForSearchQueries.from_dict(_sql_pipeline)

        base_query_is_the_base_struct_for_different_query_types = cls(
            conditions=conditions,
            data_type=data_type,
            datasource_id=datasource_id,
            datasource_type=datasource_type,
            evaluation_delay=evaluation_delay,
            expression=expression,
            filters=filters,
            instant_rollup=instant_rollup,
            name=name,
            pipeline=pipeline,
            query_type=query_type,
            relative_timerange=relative_timerange,
            rollup=rollup,
            sql_pipeline=sql_pipeline,
        )

        base_query_is_the_base_struct_for_different_query_types.additional_properties = d
        return base_query_is_the_base_struct_for_different_query_types

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
