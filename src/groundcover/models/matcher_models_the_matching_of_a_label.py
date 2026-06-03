from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MatcherModelsTheMatchingOfALabel")


@_attrs_define
class MatcherModelsTheMatchingOfALabel:
    """
    Attributes:
        name (str | Unset):
        type_ (int | Unset):
        value (str | Unset):
    """

    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        type_ = d.pop("Type", UNSET)

        value = d.pop("Value", UNSET)

        matcher_models_the_matching_of_a_label = cls(
            name=name,
            type_=type_,
            value=value,
        )

        matcher_models_the_matching_of_a_label.additional_properties = d
        return matcher_models_the_matching_of_a_label

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
