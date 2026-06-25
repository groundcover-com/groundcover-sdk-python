from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssertionDefinesModelForAssertion")


@_attrs_define
class AssertionDefinesModelForAssertion:
    """
    Attributes:
        operator (str | Unset):
        property_ (str | Unset):
        severity (str | Unset):
        source (str | Unset):
        target (str | Unset):
    """

    operator: str | Unset = UNSET
    property_: str | Unset = UNSET
    severity: str | Unset = UNSET
    source: str | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

        property_ = self.property_

        severity = self.severity

        source = self.source

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operator is not UNSET:
            field_dict["operator"] = operator
        if property_ is not UNSET:
            field_dict["property"] = property_
        if severity is not UNSET:
            field_dict["severity"] = severity
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target

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
        operator = d.pop("operator", UNSET)

        property_ = d.pop("property", UNSET)

        severity = d.pop("severity", UNSET)

        source = d.pop("source", UNSET)

        target = d.pop("target", UNSET)

        assertion_defines_model_for_assertion = cls(
            operator=operator,
            property_=property_,
            severity=severity,
            source=source,
            target=target,
        )

        assertion_defines_model_for_assertion.additional_properties = d
        return assertion_defines_model_for_assertion

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
