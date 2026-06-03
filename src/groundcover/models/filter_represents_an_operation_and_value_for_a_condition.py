from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="FilterRepresentsAnOperationAndValueForACondition")


@_attrs_define
class FilterRepresentsAnOperationAndValueForACondition:
    """
    Attributes:
        op (str | Unset):
        value (Any | Unset):
    """

    op: str | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        op = d.pop("op", UNSET)

        value = d.pop("value", UNSET)

        filter_represents_an_operation_and_value_for_a_condition = cls(
            op=op,
            value=value,
        )

        filter_represents_an_operation_and_value_for_a_condition.additional_properties = d
        return filter_represents_an_operation_and_value_for_a_condition

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
