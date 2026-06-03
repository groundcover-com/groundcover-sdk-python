from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Description")


@_attrs_define
class Description:
    """
    Attributes:
        defaults (Any | Unset):
        options (Any | Unset):
        supported_actions (list[str] | Unset):
        version (int | Unset):
    """

    defaults: Any | Unset = UNSET
    options: Any | Unset = UNSET
    supported_actions: list[str] | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        defaults = self.defaults

        options = self.options

        supported_actions: list[str] | Unset = UNSET
        if not isinstance(self.supported_actions, Unset):
            supported_actions = self.supported_actions

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if options is not UNSET:
            field_dict["options"] = options
        if supported_actions is not UNSET:
            field_dict["supported_actions"] = supported_actions
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        defaults = d.pop("defaults", UNSET)

        options = d.pop("options", UNSET)

        supported_actions = cast(list[str], d.pop("supported_actions", UNSET))

        version = d.pop("version", UNSET)

        description = cls(
            defaults=defaults,
            options=options,
            supported_actions=supported_actions,
            version=version,
        )

        description.additional_properties = d
        return description

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
