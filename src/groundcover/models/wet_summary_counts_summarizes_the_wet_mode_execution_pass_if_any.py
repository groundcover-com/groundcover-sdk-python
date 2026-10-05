from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny")


@_attrs_define
class WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny:
    """
    Attributes:
        errors (int | Unset):
        no_data (int | Unset):
        ok (int | Unset):
        queries_total (int | Unset):
        skipped (int | Unset):
        tested (int | Unset):
        unique_executed (int | Unset):
    """

    errors: int | Unset = UNSET
    no_data: int | Unset = UNSET
    ok: int | Unset = UNSET
    queries_total: int | Unset = UNSET
    skipped: int | Unset = UNSET
    tested: int | Unset = UNSET
    unique_executed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        no_data = self.no_data

        ok = self.ok

        queries_total = self.queries_total

        skipped = self.skipped

        tested = self.tested

        unique_executed = self.unique_executed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if no_data is not UNSET:
            field_dict["no_data"] = no_data
        if ok is not UNSET:
            field_dict["ok"] = ok
        if queries_total is not UNSET:
            field_dict["queries_total"] = queries_total
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if tested is not UNSET:
            field_dict["tested"] = tested
        if unique_executed is not UNSET:
            field_dict["unique_executed"] = unique_executed

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

        no_data = d.pop("no_data", UNSET)

        ok = d.pop("ok", UNSET)

        queries_total = d.pop("queries_total", UNSET)

        skipped = d.pop("skipped", UNSET)

        tested = d.pop("tested", UNSET)

        unique_executed = d.pop("unique_executed", UNSET)

        wet_summary_counts_summarizes_the_wet_mode_execution_pass_if_any = cls(
            errors=errors,
            no_data=no_data,
            ok=ok,
            queries_total=queries_total,
            skipped=skipped,
            tested=tested,
            unique_executed=unique_executed,
        )

        wet_summary_counts_summarizes_the_wet_mode_execution_pass_if_any.additional_properties = d
        return wet_summary_counts_summarizes_the_wet_mode_execution_pass_if_any

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
