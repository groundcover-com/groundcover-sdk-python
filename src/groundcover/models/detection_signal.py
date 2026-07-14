from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DetectionSignal")


@_attrs_define
class DetectionSignal:
    """DetectionSignal is one signal a template's Detection checks to suggest
    whether the tenant's data would populate the dashboard. Inert in MVP.

        Attributes:
            datasource (str | Unset):
            expect (str | Unset):
            expr (str | Unset):
    """

    datasource: str | Unset = UNSET
    expect: str | Unset = UNSET
    expr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource = self.datasource

        expect = self.expect

        expr = self.expr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if expect is not UNSET:
            field_dict["expect"] = expect
        if expr is not UNSET:
            field_dict["expr"] = expr

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
        datasource = d.pop("datasource", UNSET)

        expect = d.pop("expect", UNSET)

        expr = d.pop("expr", UNSET)

        detection_signal = cls(
            datasource=datasource,
            expect=expect,
            expr=expr,
        )

        detection_signal.additional_properties = d
        return detection_signal

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
