from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SuggestionProposesAnAlternativeForAMissingResource")


@_attrs_define
class SuggestionProposesAnAlternativeForAMissingResource:
    """
    Attributes:
        confidence (float | Unset):
        reason (str | Unset):
        type_ (str | Unset):
        value (str | Unset):
    """

    confidence: float | Unset = UNSET
    reason: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        reason = self.reason

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if reason is not UNSET:
            field_dict["reason"] = reason
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        confidence = d.pop("confidence", UNSET)

        reason = d.pop("reason", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        suggestion_proposes_an_alternative_for_a_missing_resource = cls(
            confidence=confidence,
            reason=reason,
            type_=type_,
            value=value,
        )

        suggestion_proposes_an_alternative_for_a_missing_resource.additional_properties = d
        return suggestion_proposes_an_alternative_for_a_missing_resource

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
