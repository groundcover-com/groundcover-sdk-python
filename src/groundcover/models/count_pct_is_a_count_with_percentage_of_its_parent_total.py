from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CountPctIsACountWithPercentageOfItsParentTotal")


@_attrs_define
class CountPctIsACountWithPercentageOfItsParentTotal:
    """
    Attributes:
        count (int | Unset):
        pct (float | Unset):
    """

    count: int | Unset = UNSET
    pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        pct = self.pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if pct is not UNSET:
            field_dict["pct"] = pct

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
        count = d.pop("count", UNSET)

        pct = d.pop("pct", UNSET)

        count_pct_is_a_count_with_percentage_of_its_parent_total = cls(
            count=count,
            pct=pct,
        )

        count_pct_is_a_count_with_percentage_of_its_parent_total.additional_properties = d
        return count_pct_is_a_count_with_percentage_of_its_parent_total

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
