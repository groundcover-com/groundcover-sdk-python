from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reducer_model_defines_how_to_aggregate_or_transform_query_results_type import (
    ReducerModelDefinesHowToAggregateOrTransformQueryResultsType,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relative_timerange_defines_a_time_range_relative_to_the_evaluation_time import (
        RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime,
    )


T = TypeVar("T", bound="ReducerModelDefinesHowToAggregateOrTransformQueryResults")


@_attrs_define
class ReducerModelDefinesHowToAggregateOrTransformQueryResults:
    """
    Attributes:
        name (str): Name of the reducer output.
        type_ (ReducerModelDefinesHowToAggregateOrTransformQueryResultsType): Type of the reducer.
        expression (str | Unset): Math expression (if type is 'math').
        input_name (str | Unset): Name of the query or reducer output to use as input.
        relative_timerange (RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset):
    """

    name: str
    type_: ReducerModelDefinesHowToAggregateOrTransformQueryResultsType
    expression: str | Unset = UNSET
    input_name: str | Unset = UNSET
    relative_timerange: RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        expression = self.expression

        input_name = self.input_name

        relative_timerange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relative_timerange, Unset):
            relative_timerange = self.relative_timerange.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if expression is not UNSET:
            field_dict["expression"] = expression
        if input_name is not UNSET:
            field_dict["inputName"] = input_name
        if relative_timerange is not UNSET:
            field_dict["relativeTimerange"] = relative_timerange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relative_timerange_defines_a_time_range_relative_to_the_evaluation_time import (
            RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = ReducerModelDefinesHowToAggregateOrTransformQueryResultsType(d.pop("type"))

        expression = d.pop("expression", UNSET)

        input_name = d.pop("inputName", UNSET)

        _relative_timerange = d.pop("relativeTimerange", UNSET)
        relative_timerange: RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset
        if isinstance(_relative_timerange, Unset) or _relative_timerange is None:
            relative_timerange = UNSET
        else:
            relative_timerange = RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime.from_dict(
                _relative_timerange
            )

        reducer_model_defines_how_to_aggregate_or_transform_query_results = cls(
            name=name,
            type_=type_,
            expression=expression,
            input_name=input_name,
            relative_timerange=relative_timerange,
        )

        reducer_model_defines_how_to_aggregate_or_transform_query_results.additional_properties = d
        return reducer_model_defines_how_to_aggregate_or_transform_query_results

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
