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
    from ..models.promql_function_represents_a_function_call_in_a_prom_ql_query import (
        PromqlFunctionRepresentsAFunctionCallInAPromQLQuery,
    )


T = TypeVar(
    "T", bound="PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate"
)


@_attrs_define
class PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate:
    """
    Attributes:
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        function (PromqlFunctionRepresentsAFunctionCallInAPromQLQuery | Unset):
        metric (str | Unset): Pipeline can either have a metric OR a function OR a template
        template (str | Unset):
    """

    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    function: PromqlFunctionRepresentsAFunctionCallInAPromQLQuery | Unset = UNSET
    metric: str | Unset = UNSET
    template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        function: dict[str, Any] | Unset = UNSET
        if not isinstance(self.function, Unset):
            function = self.function.to_dict()

        metric = self.metric

        template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if function is not UNSET:
            field_dict["function"] = function
        if metric is not UNSET:
            field_dict["metric"] = metric
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.promql_function_represents_a_function_call_in_a_prom_ql_query import (
            PromqlFunctionRepresentsAFunctionCallInAPromQLQuery,
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

        _function = d.pop("function", UNSET)
        function: PromqlFunctionRepresentsAFunctionCallInAPromQLQuery | Unset
        if isinstance(_function, Unset) or _function is None:
            function = UNSET
        else:
            function = PromqlFunctionRepresentsAFunctionCallInAPromQLQuery.from_dict(_function)

        metric = d.pop("metric", UNSET)

        template = d.pop("template", UNSET)

        promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template = cls(
            conditions=conditions,
            function=function,
            metric=metric,
            template=template,
        )

        promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template.additional_properties = d
        return promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template

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
