from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent")


@_attrs_define
class InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent:
    """Denominator 0 means nothing could be evaluated, so there is no rate.

    Attributes:
        denominator (int):
        numerator (int):
    """

    denominator: int
    numerator: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denominator = self.denominator

        numerator = self.numerator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "denominator": denominator,
                "numerator": numerator,
            }
        )

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
        denominator = d.pop("denominator")

        numerator = d.pop("numerator")

        insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present = cls(
            denominator=denominator,
            numerator=numerator,
        )

        insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present.additional_properties = d
        return insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present

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
