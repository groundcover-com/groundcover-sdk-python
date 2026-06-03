from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.threshold_defines_a_condition_to_evaluate_against_a_reduced_value_operator import (
    ThresholdDefinesAConditionToEvaluateAgainstAReducedValueOperator,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_resolve_threshold_defines_a_hysteresis_recovery_condition_for_a_threshold import (
        CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold,
    )
    from ..models.relative_timerange_defines_a_time_range_relative_to_the_evaluation_time import (
        RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime,
    )


T = TypeVar("T", bound="ThresholdDefinesAConditionToEvaluateAgainstAReducedValue")


@_attrs_define
class ThresholdDefinesAConditionToEvaluateAgainstAReducedValue:
    """
    Attributes:
        input_name (str): Name of the reducer output this threshold applies to.
        name (str): Name of the threshold.
        operator (ThresholdDefinesAConditionToEvaluateAgainstAReducedValueOperator): Comparison operator.
        values (list[float]): Values to compare against (one for gt/lt, two for range operators).
        custom_resolve_threshold (CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold | Unset): The
            Operator must be the directional opposite of the parent Threshold.Operator
            and Values must not overlap the firing range (e.g. fire above 100, recover below 80).
            This maps to Grafana's "Custom recovery threshold" (unloadEvaluator) on the
            threshold expression node.
        relative_timerange (RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset):
    """

    input_name: str
    name: str
    operator: ThresholdDefinesAConditionToEvaluateAgainstAReducedValueOperator
    values: list[float]
    custom_resolve_threshold: CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold | Unset = UNSET
    relative_timerange: RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_name = self.input_name

        name = self.name

        operator = self.operator.value

        values = self.values

        custom_resolve_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_resolve_threshold, Unset):
            custom_resolve_threshold = self.custom_resolve_threshold.to_dict()

        relative_timerange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relative_timerange, Unset):
            relative_timerange = self.relative_timerange.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputName": input_name,
                "name": name,
                "operator": operator,
                "values": values,
            }
        )
        if custom_resolve_threshold is not UNSET:
            field_dict["customResolveThreshold"] = custom_resolve_threshold
        if relative_timerange is not UNSET:
            field_dict["relativeTimerange"] = relative_timerange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_resolve_threshold_defines_a_hysteresis_recovery_condition_for_a_threshold import (
            CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold,
        )
        from ..models.relative_timerange_defines_a_time_range_relative_to_the_evaluation_time import (
            RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime,
        )

        d = dict(src_dict)
        input_name = d.pop("inputName")

        name = d.pop("name")

        operator = ThresholdDefinesAConditionToEvaluateAgainstAReducedValueOperator(d.pop("operator"))

        values = cast(list[float], d.pop("values"))

        _custom_resolve_threshold = d.pop("customResolveThreshold", UNSET)
        custom_resolve_threshold: CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold | Unset
        if isinstance(_custom_resolve_threshold, Unset) or _custom_resolve_threshold is None:
            custom_resolve_threshold = UNSET
        else:
            custom_resolve_threshold = CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold.from_dict(
                _custom_resolve_threshold
            )

        _relative_timerange = d.pop("relativeTimerange", UNSET)
        relative_timerange: RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime | Unset
        if isinstance(_relative_timerange, Unset) or _relative_timerange is None:
            relative_timerange = UNSET
        else:
            relative_timerange = RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime.from_dict(
                _relative_timerange
            )

        threshold_defines_a_condition_to_evaluate_against_a_reduced_value = cls(
            input_name=input_name,
            name=name,
            operator=operator,
            values=values,
            custom_resolve_threshold=custom_resolve_threshold,
            relative_timerange=relative_timerange,
        )

        threshold_defines_a_condition_to_evaluate_against_a_reduced_value.additional_properties = d
        return threshold_defines_a_condition_to_evaluate_against_a_reduced_value

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
