from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MetricsValuesResponse")


@_attrs_define
class MetricsValuesResponse:
    """
    Attributes:
        is_limit_reached (bool | Unset):
        key (str | Unset):
        name (str | Unset):
        values (list[str] | Unset):
    """

    is_limit_reached: bool | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_limit_reached = self.is_limit_reached

        key = self.key

        name = self.name

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        is_limit_reached = d.pop("isLimitReached", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        metrics_values_response = cls(
            is_limit_reached=is_limit_reached,
            key=key,
            name=name,
            values=values,
        )

        metrics_values_response.additional_properties = d
        return metrics_values_response

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
