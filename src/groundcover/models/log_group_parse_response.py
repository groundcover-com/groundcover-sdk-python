from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LogGroupParseResponse")


@_attrs_define
class LogGroupParseResponse:
    """
    Attributes:
        condition_logic_operator (str | Unset):
        group_id (str | Unset):
        ottl_conditions (list[str] | Unset):
        ottl_statements (list[str] | Unset):
        rule_name (str | Unset):
        statements_error_mode (str | Unset):
    """

    condition_logic_operator: str | Unset = UNSET
    group_id: str | Unset = UNSET
    ottl_conditions: list[str] | Unset = UNSET
    ottl_statements: list[str] | Unset = UNSET
    rule_name: str | Unset = UNSET
    statements_error_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_logic_operator = self.condition_logic_operator

        group_id = self.group_id

        ottl_conditions: list[str] | Unset = UNSET
        if not isinstance(self.ottl_conditions, Unset):
            ottl_conditions = self.ottl_conditions

        ottl_statements: list[str] | Unset = UNSET
        if not isinstance(self.ottl_statements, Unset):
            ottl_statements = self.ottl_statements

        rule_name = self.rule_name

        statements_error_mode = self.statements_error_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition_logic_operator is not UNSET:
            field_dict["conditionLogicOperator"] = condition_logic_operator
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if ottl_conditions is not UNSET:
            field_dict["ottlConditions"] = ottl_conditions
        if ottl_statements is not UNSET:
            field_dict["ottlStatements"] = ottl_statements
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if statements_error_mode is not UNSET:
            field_dict["statementsErrorMode"] = statements_error_mode

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
        condition_logic_operator = d.pop("conditionLogicOperator", UNSET)

        group_id = d.pop("groupId", UNSET)

        ottl_conditions = cast(list[str], d.pop("ottlConditions", UNSET))

        ottl_statements = cast(list[str], d.pop("ottlStatements", UNSET))

        rule_name = d.pop("ruleName", UNSET)

        statements_error_mode = d.pop("statementsErrorMode", UNSET)

        log_group_parse_response = cls(
            condition_logic_operator=condition_logic_operator,
            group_id=group_id,
            ottl_conditions=ottl_conditions,
            ottl_statements=ottl_statements,
            rule_name=rule_name,
            statements_error_mode=statements_error_mode,
        )

        log_group_parse_response.additional_properties = d
        return log_group_parse_response

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
