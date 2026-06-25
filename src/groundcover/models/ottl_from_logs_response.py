from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="OttlFromLogsResponse")


@_attrs_define
class OttlFromLogsResponse:
    """
    Attributes:
        condition_logic_operator (str | Unset):
        ottl (list[str] | Unset):
        ottl_conditions (list[str] | Unset):
        rule_name (str | Unset):
        statements_error_mode (str | Unset):
    """

    condition_logic_operator: str | Unset = UNSET
    ottl: list[str] | Unset = UNSET
    ottl_conditions: list[str] | Unset = UNSET
    rule_name: str | Unset = UNSET
    statements_error_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_logic_operator = self.condition_logic_operator

        ottl: list[str] | Unset = UNSET
        if not isinstance(self.ottl, Unset):
            ottl = self.ottl

        ottl_conditions: list[str] | Unset = UNSET
        if not isinstance(self.ottl_conditions, Unset):
            ottl_conditions = self.ottl_conditions

        rule_name = self.rule_name

        statements_error_mode = self.statements_error_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition_logic_operator is not UNSET:
            field_dict["condition_logic_operator"] = condition_logic_operator
        if ottl is not UNSET:
            field_dict["ottl"] = ottl
        if ottl_conditions is not UNSET:
            field_dict["ottl_conditions"] = ottl_conditions
        if rule_name is not UNSET:
            field_dict["rule_name"] = rule_name
        if statements_error_mode is not UNSET:
            field_dict["statements_error_mode"] = statements_error_mode

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
        condition_logic_operator = d.pop("condition_logic_operator", UNSET)

        ottl = cast(list[str], d.pop("ottl", UNSET))

        ottl_conditions = cast(list[str], d.pop("ottl_conditions", UNSET))

        rule_name = d.pop("rule_name", UNSET)

        statements_error_mode = d.pop("statements_error_mode", UNSET)

        ottl_from_logs_response = cls(
            condition_logic_operator=condition_logic_operator,
            ottl=ottl,
            ottl_conditions=ottl_conditions,
            rule_name=rule_name,
            statements_error_mode=statements_error_mode,
        )

        ottl_from_logs_response.additional_properties = d
        return ottl_from_logs_response

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
