from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wet_result_holds_the_outcome_of_executing_a_single_wet_query import (
        WetResultHoldsTheOutcomeOfExecutingASingleWetQuery,
    )


T = TypeVar("T", bound="WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport")


@_attrs_define
class WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport:
    """
    Attributes:
        errors (list[WetResultHoldsTheOutcomeOfExecutingASingleWetQuery] | Unset):
        no_data (list[WetResultHoldsTheOutcomeOfExecutingASingleWetQuery] | Unset):
    """

    errors: list[WetResultHoldsTheOutcomeOfExecutingASingleWetQuery] | Unset = UNSET
    no_data: list[WetResultHoldsTheOutcomeOfExecutingASingleWetQuery] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        no_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.no_data, Unset):
            no_data = []
            for no_data_item_data in self.no_data:
                no_data_item = no_data_item_data.to_dict()
                no_data.append(no_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if no_data is not UNSET:
            field_dict["no_data"] = no_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wet_result_holds_the_outcome_of_executing_a_single_wet_query import (
            WetResultHoldsTheOutcomeOfExecutingASingleWetQuery,
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[WetResultHoldsTheOutcomeOfExecutingASingleWetQuery] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = WetResultHoldsTheOutcomeOfExecutingASingleWetQuery.from_dict(errors_item_data)

                errors.append(errors_item)

        _no_data = d.pop("no_data", UNSET)
        no_data: list[WetResultHoldsTheOutcomeOfExecutingASingleWetQuery] | Unset = UNSET
        if _no_data is not UNSET:
            no_data = []
            for no_data_item_data in _no_data:
                no_data_item = WetResultHoldsTheOutcomeOfExecutingASingleWetQuery.from_dict(no_data_item_data)

                no_data.append(no_data_item)

        wet_report_holds_the_complete_wet_mode_results_for_inclusion_in_preflight_report = cls(
            errors=errors,
            no_data=no_data,
        )

        wet_report_holds_the_complete_wet_mode_results_for_inclusion_in_preflight_report.additional_properties = d
        return wet_report_holds_the_complete_wet_mode_results_for_inclusion_in_preflight_report

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
