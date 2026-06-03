from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.values_response_item import ValuesResponseItem


T = TypeVar("T", bound="MetricValuesResponseV2")


@_attrs_define
class MetricValuesResponseV2:
    """
    Attributes:
        is_limit_reached (bool | Unset):
        values (list[ValuesResponseItem] | Unset):
    """

    is_limit_reached: bool | Unset = UNSET
    values: list[ValuesResponseItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_limit_reached = self.is_limit_reached

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.values_response_item import ValuesResponseItem

        d = dict(src_dict)
        is_limit_reached = d.pop("isLimitReached", UNSET)

        _values = d.pop("values", UNSET)
        values: list[ValuesResponseItem] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ValuesResponseItem.from_dict(values_item_data)

                values.append(values_item)

        metric_values_response_v2 = cls(
            is_limit_reached=is_limit_reached,
            values=values,
        )

        metric_values_response_v2.additional_properties = d
        return metric_values_response_v2

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
