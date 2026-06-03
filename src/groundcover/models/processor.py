from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Processor")


@_attrs_define
class Processor:
    """
    Attributes:
        alias_type (str | Unset):
        args (list[Any] | Unset):
        op (str | Unset):
    """

    alias_type: str | Unset = UNSET
    args: list[Any] | Unset = UNSET
    op: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias_type = self.alias_type

        args: list[Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        op = self.op

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias_type is not UNSET:
            field_dict["aliasType"] = alias_type
        if args is not UNSET:
            field_dict["args"] = args
        if op is not UNSET:
            field_dict["op"] = op

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        alias_type = d.pop("aliasType", UNSET)

        args = cast(list[Any], d.pop("args", UNSET))

        op = d.pop("op", UNSET)

        processor = cls(
            alias_type=alias_type,
            args=args,
            op=op,
        )

        processor.additional_properties = d
        return processor

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
