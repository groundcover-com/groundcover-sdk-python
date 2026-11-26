from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="GoalEvalValue")


@_attrs_define
class GoalEvalValue:
    """GoalEvalValue is one Eval field value; exactly the member that matches the
    field type is set. A field without a value of its type is left out.

        Attributes:
            boolean (bool | Unset):
            number (float | Unset): Number is the value of an integer or float field.
            text (str | Unset): Text is the value of a text or enum field.
    """

    boolean: bool | Unset = UNSET
    number: float | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boolean = self.boolean

        number = self.number

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boolean is not UNSET:
            field_dict["boolean"] = boolean
        if number is not UNSET:
            field_dict["number"] = number
        if text is not UNSET:
            field_dict["text"] = text

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
        boolean = d.pop("boolean", UNSET)

        number = d.pop("number", UNSET)

        text = d.pop("text", UNSET)

        goal_eval_value = cls(
            boolean=boolean,
            number=number,
            text=text,
        )

        goal_eval_value.additional_properties = d
        return goal_eval_value

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
