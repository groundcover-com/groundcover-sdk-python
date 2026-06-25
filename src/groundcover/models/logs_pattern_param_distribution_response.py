from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pattern_param_distribution_value import PatternParamDistributionValue


T = TypeVar("T", bound="LogsPatternParamDistributionResponse")


@_attrs_define
class LogsPatternParamDistributionResponse:
    """
    Attributes:
        values (list[PatternParamDistributionValue] | Unset):
    """

    values: list[PatternParamDistributionValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pattern_param_distribution_value import PatternParamDistributionValue

        d = dict(src_dict)
        _values = d.pop("values", UNSET)
        values: list[PatternParamDistributionValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = PatternParamDistributionValue.from_dict(values_item_data)

                values.append(values_item)

        logs_pattern_param_distribution_response = cls(
            values=values,
        )

        logs_pattern_param_distribution_response.additional_properties = d
        return logs_pattern_param_distribution_response

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
