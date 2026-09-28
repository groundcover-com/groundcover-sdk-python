from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies")


@_attrs_define
class QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies:
    """
    Attributes:
        evaluation_delay (str | Unset): Shifts the eval window back, length unchanged. Whole seconds, at most 7d.
            Rejected where Rollup is.
        expression (str | Unset):
        rollup (str | Unset): Lookback window: whole seconds, positive. Required when the type has a
            time axis, rejected otherwise (sql, timeless datasets).
        rollup_function (str | Unset): Required iff metrics, rejected otherwise.
    """

    evaluation_delay: str | Unset = UNSET
    expression: str | Unset = UNSET
    rollup: str | Unset = UNSET
    rollup_function: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluation_delay = self.evaluation_delay

        expression = self.expression

        rollup = self.rollup

        rollup_function = self.rollup_function

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluation_delay is not UNSET:
            field_dict["evaluationDelay"] = evaluation_delay
        if expression is not UNSET:
            field_dict["expression"] = expression
        if rollup is not UNSET:
            field_dict["rollup"] = rollup
        if rollup_function is not UNSET:
            field_dict["rollupFunction"] = rollup_function

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        evaluation_delay = d.pop("evaluationDelay", UNSET)

        expression = d.pop("expression", UNSET)

        rollup = d.pop("rollup", UNSET)

        rollup_function = d.pop("rollupFunction", UNSET)

        query_is_the_whole_expression_in_the_language_monitor_spec_type_implies = cls(
            evaluation_delay=evaluation_delay,
            expression=expression,
            rollup=rollup,
            rollup_function=rollup_function,
        )

        query_is_the_whole_expression_in_the_language_monitor_spec_type_implies.additional_properties = d
        return query_is_the_whole_expression_in_the_language_monitor_spec_type_implies

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
