from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DistributionValue")


@_attrs_define
class DistributionValue:
    """
    Attributes:
        count (int | Unset):
        item (str | Unset):
        percent (float | Unset):
    """

    count: int | Unset = UNSET
    item: str | Unset = UNSET
    percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        item = self.item

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if item is not UNSET:
            field_dict["item"] = item
        if percent is not UNSET:
            field_dict["percent"] = percent

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

        item = d.pop("item", UNSET)

        percent = d.pop("percent", UNSET)

        distribution_value = cls(
            count=count,
            item=item,
            percent=percent,
        )

        distribution_value.additional_properties = d
        return distribution_value

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
