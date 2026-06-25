from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="PatternParamDistributionValue")


@_attrs_define
class PatternParamDistributionValue:
    """
    Attributes:
        pattern_param_value (str | Unset):
        pattern_param_value_count (int | Unset):
        pattern_param_value_percentage (float | Unset):
    """

    pattern_param_value: str | Unset = UNSET
    pattern_param_value_count: int | Unset = UNSET
    pattern_param_value_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern_param_value = self.pattern_param_value

        pattern_param_value_count = self.pattern_param_value_count

        pattern_param_value_percentage = self.pattern_param_value_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pattern_param_value is not UNSET:
            field_dict["patternParamValue"] = pattern_param_value
        if pattern_param_value_count is not UNSET:
            field_dict["patternParamValueCount"] = pattern_param_value_count
        if pattern_param_value_percentage is not UNSET:
            field_dict["patternParamValuePercentage"] = pattern_param_value_percentage

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
        pattern_param_value = d.pop("patternParamValue", UNSET)

        pattern_param_value_count = d.pop("patternParamValueCount", UNSET)

        pattern_param_value_percentage = d.pop("patternParamValuePercentage", UNSET)

        pattern_param_distribution_value = cls(
            pattern_param_value=pattern_param_value,
            pattern_param_value_count=pattern_param_value_count,
            pattern_param_value_percentage=pattern_param_value_percentage,
        )

        pattern_param_distribution_value.additional_properties = d
        return pattern_param_distribution_value

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
