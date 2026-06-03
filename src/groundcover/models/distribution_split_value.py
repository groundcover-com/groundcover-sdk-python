from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DistributionSplitValue")


@_attrs_define
class DistributionSplitValue:
    """
    Attributes:
        baseline_count (int | Unset):
        baseline_percent (float | Unset):
        item (str | Unset):
        selection_count (int | Unset):
        selection_percent (float | Unset):
        selection_to_baseline_ratio (float | Unset):
    """

    baseline_count: int | Unset = UNSET
    baseline_percent: float | Unset = UNSET
    item: str | Unset = UNSET
    selection_count: int | Unset = UNSET
    selection_percent: float | Unset = UNSET
    selection_to_baseline_ratio: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline_count = self.baseline_count

        baseline_percent = self.baseline_percent

        item = self.item

        selection_count = self.selection_count

        selection_percent = self.selection_percent

        selection_to_baseline_ratio = self.selection_to_baseline_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baseline_count is not UNSET:
            field_dict["baseline_count"] = baseline_count
        if baseline_percent is not UNSET:
            field_dict["baseline_percent"] = baseline_percent
        if item is not UNSET:
            field_dict["item"] = item
        if selection_count is not UNSET:
            field_dict["selection_count"] = selection_count
        if selection_percent is not UNSET:
            field_dict["selection_percent"] = selection_percent
        if selection_to_baseline_ratio is not UNSET:
            field_dict["selection_to_baseline_ratio"] = selection_to_baseline_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        baseline_count = d.pop("baseline_count", UNSET)

        baseline_percent = d.pop("baseline_percent", UNSET)

        item = d.pop("item", UNSET)

        selection_count = d.pop("selection_count", UNSET)

        selection_percent = d.pop("selection_percent", UNSET)

        selection_to_baseline_ratio = d.pop("selection_to_baseline_ratio", UNSET)

        distribution_split_value = cls(
            baseline_count=baseline_count,
            baseline_percent=baseline_percent,
            item=item,
            selection_count=selection_count,
            selection_percent=selection_percent,
            selection_to_baseline_ratio=selection_to_baseline_ratio,
        )

        distribution_split_value.additional_properties = d
        return distribution_split_value

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
