from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_variable_compute import MonitorVariableCompute
    from ..models.variable_group_by_defines_datadog_group_by_details_for_formula_monitor_variables import (
        VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables,
    )
    from ..models.variable_search_holds_the_variable_search_query_for_formula_monitors import (
        VariableSearchHoldsTheVariableSearchQueryForFormulaMonitors,
    )


T = TypeVar("T", bound="MonitorVariable")


@_attrs_define
class MonitorVariable:
    """MonitorVariable represents a monitor variable

    Attributes:
        available_values (list[str] | Unset):
        compute (MonitorVariableCompute | Unset):
        data_source (str | Unset):
        default_value (str | Unset):
        group_by (list[VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables] | Unset):
        indexes (list[str] | Unset):
        name (str | Unset):
        prefix (str | Unset):
        search (VariableSearchHoldsTheVariableSearchQueryForFormulaMonitors | Unset):
        storage (str | Unset):
    """

    available_values: list[str] | Unset = UNSET
    compute: MonitorVariableCompute | Unset = UNSET
    data_source: str | Unset = UNSET
    default_value: str | Unset = UNSET
    group_by: list[VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables] | Unset = UNSET
    indexes: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    prefix: str | Unset = UNSET
    search: VariableSearchHoldsTheVariableSearchQueryForFormulaMonitors | Unset = UNSET
    storage: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_values: list[str] | Unset = UNSET
        if not isinstance(self.available_values, Unset):
            available_values = self.available_values

        compute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute, Unset):
            compute = self.compute.to_dict()

        data_source = self.data_source

        default_value = self.default_value

        group_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = []
            for group_by_item_data in self.group_by:
                group_by_item = group_by_item_data.to_dict()
                group_by.append(group_by_item)

        indexes: list[str] | Unset = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = self.indexes

        name = self.name

        prefix = self.prefix

        search: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        storage = self.storage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_values is not UNSET:
            field_dict["available_values"] = available_values
        if compute is not UNSET:
            field_dict["compute"] = compute
        if data_source is not UNSET:
            field_dict["data_source"] = data_source
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if name is not UNSET:
            field_dict["name"] = name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if search is not UNSET:
            field_dict["search"] = search
        if storage is not UNSET:
            field_dict["storage"] = storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_variable_compute import MonitorVariableCompute
        from ..models.variable_group_by_defines_datadog_group_by_details_for_formula_monitor_variables import (
            VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables,
        )
        from ..models.variable_search_holds_the_variable_search_query_for_formula_monitors import (
            VariableSearchHoldsTheVariableSearchQueryForFormulaMonitors,
        )

        d = dict(src_dict)
        available_values = cast(list[str], d.pop("available_values", UNSET))

        _compute = d.pop("compute", UNSET)
        compute: MonitorVariableCompute | Unset
        if isinstance(_compute, Unset) or _compute is None:
            compute = UNSET
        else:
            compute = MonitorVariableCompute.from_dict(_compute)

        data_source = d.pop("data_source", UNSET)

        default_value = d.pop("default_value", UNSET)

        _group_by = d.pop("group_by", UNSET)
        group_by: list[VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables] | Unset = UNSET
        if _group_by is not UNSET:
            group_by = []
            for group_by_item_data in _group_by:
                group_by_item = VariableGroupByDefinesDatadogGroupByDetailsForFormulaMonitorVariables.from_dict(
                    group_by_item_data
                )

                group_by.append(group_by_item)

        indexes = cast(list[str], d.pop("indexes", UNSET))

        name = d.pop("name", UNSET)

        prefix = d.pop("prefix", UNSET)

        _search = d.pop("search", UNSET)
        search: VariableSearchHoldsTheVariableSearchQueryForFormulaMonitors | Unset
        if isinstance(_search, Unset) or _search is None:
            search = UNSET
        else:
            search = VariableSearchHoldsTheVariableSearchQueryForFormulaMonitors.from_dict(_search)

        storage = d.pop("storage", UNSET)

        monitor_variable = cls(
            available_values=available_values,
            compute=compute,
            data_source=data_source,
            default_value=default_value,
            group_by=group_by,
            indexes=indexes,
            name=name,
            prefix=prefix,
            search=search,
            storage=storage,
        )

        monitor_variable.additional_properties = d
        return monitor_variable

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
