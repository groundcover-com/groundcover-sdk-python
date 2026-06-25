from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
        PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
    )


T = TypeVar("T", bound="PromqlFunctionRepresentsAFunctionCallInAPromQLQuery")


@_attrs_define
class PromqlFunctionRepresentsAFunctionCallInAPromQLQuery:
    """
    Attributes:
        args (list[str] | Unset):
        name (str | Unset):
        pipelines
            (list[PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate] |
            Unset):
    """

    args: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    pipelines: (
        list[PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        name = self.name

        pipelines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipelines, Unset):
            pipelines = []
            for pipelines_item_data in self.pipelines:
                pipelines_item = pipelines_item_data.to_dict()
                pipelines.append(pipelines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if name is not UNSET:
            field_dict["name"] = name
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
            PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
        )

        d = dict(src_dict)
        args = cast(list[str], d.pop("args", UNSET))

        name = d.pop("name", UNSET)

        _pipelines = d.pop("pipelines", UNSET)
        pipelines: (
            list[PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate]
            | Unset
        ) = UNSET
        if _pipelines is not UNSET:
            pipelines = []
            for pipelines_item_data in _pipelines:
                pipelines_item = PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate.from_dict(
                    pipelines_item_data
                )

                pipelines.append(pipelines_item)

        promql_function_represents_a_function_call_in_a_prom_ql_query = cls(
            args=args,
            name=name,
            pipelines=pipelines,
        )

        promql_function_represents_a_function_call_in_a_prom_ql_query.additional_properties = d
        return promql_function_represents_a_function_call_in_a_prom_ql_query

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
