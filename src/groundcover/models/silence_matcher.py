from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SilenceMatcher")


@_attrs_define
class SilenceMatcher:
    """
    Attributes:
        is_equal (bool):
        is_regex (bool):
        name (str | Unset):
        value (str | Unset):
    """

    is_equal: bool
    is_regex: bool
    name: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_equal = self.is_equal

        is_regex = self.is_regex

        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEqual": is_equal,
                "isRegex": is_regex,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        is_equal = d.pop("isEqual")

        is_regex = d.pop("isRegex")

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        silence_matcher = cls(
            is_equal=is_equal,
            is_regex=is_regex,
            name=name,
            value=value,
        )

        silence_matcher.additional_properties = d
        return silence_matcher

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
