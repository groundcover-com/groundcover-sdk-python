from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distribution_split_value import DistributionSplitValue


T = TypeVar("T", bound="ValuesSplitDistributionResult")


@_attrs_define
class ValuesSplitDistributionResult:
    """
    Attributes:
        baseline_key_count (int | Unset):
        baseline_presence_ratio (float | Unset):
        baseline_score (float | Unset):
        key (str | Unset):
        kl_score (float | Unset):
        score (float | Unset):
        selection_key_count (int | Unset):
        selection_presence_ratio (float | Unset):
        selection_score (float | Unset):
        values (list[DistributionSplitValue] | Unset):
    """

    baseline_key_count: int | Unset = UNSET
    baseline_presence_ratio: float | Unset = UNSET
    baseline_score: float | Unset = UNSET
    key: str | Unset = UNSET
    kl_score: float | Unset = UNSET
    score: float | Unset = UNSET
    selection_key_count: int | Unset = UNSET
    selection_presence_ratio: float | Unset = UNSET
    selection_score: float | Unset = UNSET
    values: list[DistributionSplitValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline_key_count = self.baseline_key_count

        baseline_presence_ratio = self.baseline_presence_ratio

        baseline_score = self.baseline_score

        key = self.key

        kl_score = self.kl_score

        score = self.score

        selection_key_count = self.selection_key_count

        selection_presence_ratio = self.selection_presence_ratio

        selection_score = self.selection_score

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baseline_key_count is not UNSET:
            field_dict["baseline_key_count"] = baseline_key_count
        if baseline_presence_ratio is not UNSET:
            field_dict["baseline_presence_ratio"] = baseline_presence_ratio
        if baseline_score is not UNSET:
            field_dict["baseline_score"] = baseline_score
        if key is not UNSET:
            field_dict["key"] = key
        if kl_score is not UNSET:
            field_dict["kl_score"] = kl_score
        if score is not UNSET:
            field_dict["score"] = score
        if selection_key_count is not UNSET:
            field_dict["selection_key_count"] = selection_key_count
        if selection_presence_ratio is not UNSET:
            field_dict["selection_presence_ratio"] = selection_presence_ratio
        if selection_score is not UNSET:
            field_dict["selection_score"] = selection_score
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.distribution_split_value import DistributionSplitValue

        d = dict(src_dict)
        baseline_key_count = d.pop("baseline_key_count", UNSET)

        baseline_presence_ratio = d.pop("baseline_presence_ratio", UNSET)

        baseline_score = d.pop("baseline_score", UNSET)

        key = d.pop("key", UNSET)

        kl_score = d.pop("kl_score", UNSET)

        score = d.pop("score", UNSET)

        selection_key_count = d.pop("selection_key_count", UNSET)

        selection_presence_ratio = d.pop("selection_presence_ratio", UNSET)

        selection_score = d.pop("selection_score", UNSET)

        _values = d.pop("values", UNSET)
        values: list[DistributionSplitValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = DistributionSplitValue.from_dict(values_item_data)

                values.append(values_item)

        values_split_distribution_result = cls(
            baseline_key_count=baseline_key_count,
            baseline_presence_ratio=baseline_presence_ratio,
            baseline_score=baseline_score,
            key=key,
            kl_score=kl_score,
            score=score,
            selection_key_count=selection_key_count,
            selection_presence_ratio=selection_presence_ratio,
            selection_score=selection_score,
            values=values,
        )

        values_split_distribution_result.additional_properties = d
        return values_split_distribution_result

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
