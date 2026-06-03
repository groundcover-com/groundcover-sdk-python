from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
        PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
    )


T = TypeVar("T", bound="KnownPipelines")


@_attrs_define
class KnownPipelines:
    """KnownPipelines is a map of template names to pipeline templates
    We need this separate model to prevent circular references in swagger generation

    """

    additional_properties: dict[
        str, PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promql_pipeline_represents_a_segment_of_a_prom_ql_query_which_can_be_a_metric_with_conditions_a_function_or_a_template import (
            PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
        )

        d = dict(src_dict)
        known_pipelines = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        known_pipelines.additional_properties = additional_properties
        return known_pipelines

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: PromqlPipelineRepresentsASegmentOfAPromQLQueryWhichCanBeAMetricWithConditionsAFunctionOrATemplate,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
