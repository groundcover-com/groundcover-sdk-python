from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_resolve_threshold_defines_a_hysteresis_recovery_condition_for_a_threshold_operator import (
    CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThresholdOperator,
)

T = TypeVar("T", bound="CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold")


@_attrs_define
class CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThreshold:
    """The Operator must be the directional opposite of the parent Threshold.Operator
    and Values must not overlap the firing range (e.g. fire above 100, recover below 80).
    This maps to Grafana's "Custom recovery threshold" (unloadEvaluator) on the
    threshold expression node.

        Attributes:
            operator (CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThresholdOperator): Comparison operator
                for recovery. Must be the directional opposite of the
                parent threshold's Operator.
            values (list[float]): Resolve values (one for gt/lt, two for range operators). Must not overlap
                the firing values — see validateCustomResolveThreshold for the exact rules.
    """

    operator: CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThresholdOperator
    values: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        operator = CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThresholdOperator(d.pop("operator"))

        values = cast(list[float], d.pop("values"))

        custom_resolve_threshold_defines_a_hysteresis_recovery_condition_for_a_threshold = cls(
            operator=operator,
            values=values,
        )

        custom_resolve_threshold_defines_a_hysteresis_recovery_condition_for_a_threshold.additional_properties = d
        return custom_resolve_threshold_defines_a_hysteresis_recovery_condition_for_a_threshold

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
