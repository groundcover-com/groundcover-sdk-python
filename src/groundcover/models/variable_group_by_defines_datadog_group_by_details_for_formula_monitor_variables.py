from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables")


@_attrs_define
class VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables:
    """
    Attributes:
        facet (str | Unset):
    """

    facet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facet = self.facet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facet is not UNSET:
            field_dict["facet"] = facet

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
        facet = d.pop("facet", UNSET)

        variable_group_by_defines_datadog_group_by_details_for_formula_monitor_variables = cls(
            facet=facet,
        )

        variable_group_by_defines_datadog_group_by_details_for_formula_monitor_variables.additional_properties = d
        return variable_group_by_defines_datadog_group_by_details_for_formula_monitor_variables

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
