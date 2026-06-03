from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distribution_value import DistributionValue


T = TypeVar("T", bound="ValuesDistributionResult")


@_attrs_define
class ValuesDistributionResult:
    """
    Attributes:
        key (str | Unset):
        key_count (int | Unset):
        presence_ratio (float | Unset):
        score (float | Unset):
        values (list[DistributionValue] | Unset):
    """

    key: str | Unset = UNSET
    key_count: int | Unset = UNSET
    presence_ratio: float | Unset = UNSET
    score: float | Unset = UNSET
    values: list[DistributionValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        key_count = self.key_count

        presence_ratio = self.presence_ratio

        score = self.score

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if key_count is not UNSET:
            field_dict["key_count"] = key_count
        if presence_ratio is not UNSET:
            field_dict["presence_ratio"] = presence_ratio
        if score is not UNSET:
            field_dict["score"] = score
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.distribution_value import DistributionValue

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        key_count = d.pop("key_count", UNSET)

        presence_ratio = d.pop("presence_ratio", UNSET)

        score = d.pop("score", UNSET)

        _values = d.pop("values", UNSET)
        values: list[DistributionValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = DistributionValue.from_dict(values_item_data)

                values.append(values_item)

        values_distribution_result = cls(
            key=key,
            key_count=key_count,
            presence_ratio=presence_ratio,
            score=score,
            values=values,
        )

        values_distribution_result.additional_properties = d
        return values_distribution_result

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
