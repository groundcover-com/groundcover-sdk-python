from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SubjectHoldsBothDatadogAndGCNamesForExplainability")


@_attrs_define
class SubjectHoldsBothDatadogAndGCNamesForExplainability:
    """
    Attributes:
        name_dd (str | Unset):
        name_gc (str | Unset):
    """

    name_dd: str | Unset = UNSET
    name_gc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_dd = self.name_dd

        name_gc = self.name_gc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_dd is not UNSET:
            field_dict["name_dd"] = name_dd
        if name_gc is not UNSET:
            field_dict["name_gc"] = name_gc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        name_dd = d.pop("name_dd", UNSET)

        name_gc = d.pop("name_gc", UNSET)

        subject_holds_both_datadog_and_gc_names_for_explainability = cls(
            name_dd=name_dd,
            name_gc=name_gc,
        )

        subject_holds_both_datadog_and_gc_names_for_explainability.additional_properties = d
        return subject_holds_both_datadog_and_gc_names_for_explainability

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
