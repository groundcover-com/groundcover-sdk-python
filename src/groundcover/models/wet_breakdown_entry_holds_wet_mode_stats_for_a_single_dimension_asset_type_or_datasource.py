from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="WetBreakdownEntryHoldsWetModeStatsForASingleDimensionAssetTypeOrDatasource")


@_attrs_define
class WetBreakdownEntryHoldsWetModeStatsForASingleDimensionAssetTypeOrDatasource:
    """
    Attributes:
        errors (int | Unset):
        returned_data (int | Unset):
        returned_data_pct (float | Unset):
        returned_empty (int | Unset):
        tested (int | Unset):
    """

    errors: int | Unset = UNSET
    returned_data: int | Unset = UNSET
    returned_data_pct: float | Unset = UNSET
    returned_empty: int | Unset = UNSET
    tested: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        returned_data = self.returned_data

        returned_data_pct = self.returned_data_pct

        returned_empty = self.returned_empty

        tested = self.tested

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if returned_data is not UNSET:
            field_dict["returned_data"] = returned_data
        if returned_data_pct is not UNSET:
            field_dict["returned_data_pct"] = returned_data_pct
        if returned_empty is not UNSET:
            field_dict["returned_empty"] = returned_empty
        if tested is not UNSET:
            field_dict["tested"] = tested

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
        errors = d.pop("errors", UNSET)

        returned_data = d.pop("returned_data", UNSET)

        returned_data_pct = d.pop("returned_data_pct", UNSET)

        returned_empty = d.pop("returned_empty", UNSET)

        tested = d.pop("tested", UNSET)

        wet_breakdown_entry_holds_wet_mode_stats_for_a_single_dimension_asset_type_or_datasource = cls(
            errors=errors,
            returned_data=returned_data,
            returned_data_pct=returned_data_pct,
            returned_empty=returned_empty,
            tested=tested,
        )

        wet_breakdown_entry_holds_wet_mode_stats_for_a_single_dimension_asset_type_or_datasource.additional_properties = d
        return wet_breakdown_entry_holds_wet_mode_stats_for_a_single_dimension_asset_type_or_datasource

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
