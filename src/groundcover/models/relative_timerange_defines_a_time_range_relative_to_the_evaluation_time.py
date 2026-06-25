from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime")


@_attrs_define
class RelativeTimerangeDefinesATimeRangeRelativeToTheEvaluationTime:
    """
    Attributes:
        from_ (str | Unset): Start of the range relative to now (e.g., "-5m", "-1h").
        to (str | Unset): End of the range relative to now (e.g., "-1m", "now").
    """

    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

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
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        relative_timerange_defines_a_time_range_relative_to_the_evaluation_time = cls(
            from_=from_,
            to=to,
        )

        relative_timerange_defines_a_time_range_relative_to_the_evaluation_time.additional_properties = d
        return relative_timerange_defines_a_time_range_relative_to_the_evaluation_time

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
