from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="KeyItem")


@_attrs_define
class KeyItem:
    """
    Attributes:
        description (str | Unset):
        key (str | Unset):
        metric_names (list[str] | Unset):
        types (list[str] | Unset):
    """

    description: str | Unset = UNSET
    key: str | Unset = UNSET
    metric_names: list[str] | Unset = UNSET
    types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        key = self.key

        metric_names: list[str] | Unset = UNSET
        if not isinstance(self.metric_names, Unset):
            metric_names = self.metric_names

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = self.types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if metric_names is not UNSET:
            field_dict["metricNames"] = metric_names
        if types is not UNSET:
            field_dict["types"] = types

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
        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        metric_names = cast(list[str], d.pop("metricNames", UNSET))

        types = cast(list[str], d.pop("types", UNSET))

        key_item = cls(
            description=description,
            key=key,
            metric_names=metric_names,
            types=types,
        )

        key_item.additional_properties = d
        return key_item

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
