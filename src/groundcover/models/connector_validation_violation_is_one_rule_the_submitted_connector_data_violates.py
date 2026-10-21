from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectorValidationViolationIsOneRuleTheSubmittedConnectorDataViolates")


@_attrs_define
class ConnectorValidationViolationIsOneRuleTheSubmittedConnectorDataViolates:
    """
    Attributes:
        message (str): Human-readable explanation.
        path (str): Field path in the submitted data. Example: oauth_config.scopes.bot.
        rule (str): Stable, machine-readable rule code. Example: required_scope.
        value (str | Unset): The offending scope, event or URL, when there is one. Example: chat:write.
    """

    message: str
    path: str
    rule: str
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        path = self.path

        rule = self.rule

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "path": path,
                "rule": rule,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

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
        message = d.pop("message")

        path = d.pop("path")

        rule = d.pop("rule")

        value = d.pop("value", UNSET)

        connector_validation_violation_is_one_rule_the_submitted_connector_data_violates = cls(
            message=message,
            path=path,
            rule=rule,
            value=value,
        )

        connector_validation_violation_is_one_rule_the_submitted_connector_data_violates.additional_properties = d
        return connector_validation_violation_is_one_rule_the_submitted_connector_data_violates

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
