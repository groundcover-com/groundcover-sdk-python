from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary_by_datasource import (
        WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByDatasource,
    )
    from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary_by_type import (
        WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByType,
    )
    from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary_not_tested_reasons import (
        WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryNotTestedReasons,
    )


T = TypeVar("T", bound="WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary")


@_attrs_define
class WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary:
    """Two "with data" rates provide different perspectives:
    WithDataPct: of tested queries only (denominator = wet-tested, including dedup fan-out)
    WithDataOfTotalPct: of all extractable queries from supported assets (broadest available
    denominator; note this undercounts because queries inside unsupported widgets and
    unsupported asset types are not included)

        Attributes:
            by_datasource (WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByDatasource | Unset):
            by_type (WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByType | Unset):
            errors (int | Unset):
            not_tested (int | Unset):
            not_tested_reasons (WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryNotTestedReasons |
                Unset):
            returned_data (int | Unset):
            returned_data_pct_of_tested (float | Unset):
            returned_data_pct_of_total (float | Unset):
            returned_empty (int | Unset):
            tested (int | Unset):
            total_queries (int | Unset):
    """

    by_datasource: WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByDatasource | Unset = UNSET
    by_type: WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByType | Unset = UNSET
    errors: int | Unset = UNSET
    not_tested: int | Unset = UNSET
    not_tested_reasons: (
        WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryNotTestedReasons | Unset
    ) = UNSET
    returned_data: int | Unset = UNSET
    returned_data_pct_of_tested: float | Unset = UNSET
    returned_data_pct_of_total: float | Unset = UNSET
    returned_empty: int | Unset = UNSET
    tested: int | Unset = UNSET
    total_queries: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_datasource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_datasource, Unset):
            by_datasource = self.by_datasource.to_dict()

        by_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = self.by_type.to_dict()

        errors = self.errors

        not_tested = self.not_tested

        not_tested_reasons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.not_tested_reasons, Unset):
            not_tested_reasons = self.not_tested_reasons.to_dict()

        returned_data = self.returned_data

        returned_data_pct_of_tested = self.returned_data_pct_of_tested

        returned_data_pct_of_total = self.returned_data_pct_of_total

        returned_empty = self.returned_empty

        tested = self.tested

        total_queries = self.total_queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_datasource is not UNSET:
            field_dict["by_datasource"] = by_datasource
        if by_type is not UNSET:
            field_dict["by_type"] = by_type
        if errors is not UNSET:
            field_dict["errors"] = errors
        if not_tested is not UNSET:
            field_dict["not_tested"] = not_tested
        if not_tested_reasons is not UNSET:
            field_dict["not_tested_reasons"] = not_tested_reasons
        if returned_data is not UNSET:
            field_dict["returned_data"] = returned_data
        if returned_data_pct_of_tested is not UNSET:
            field_dict["returned_data_pct_of_tested"] = returned_data_pct_of_tested
        if returned_data_pct_of_total is not UNSET:
            field_dict["returned_data_pct_of_total"] = returned_data_pct_of_total
        if returned_empty is not UNSET:
            field_dict["returned_empty"] = returned_empty
        if tested is not UNSET:
            field_dict["tested"] = tested
        if total_queries is not UNSET:
            field_dict["total_queries"] = total_queries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary_by_datasource import (
            WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByDatasource,
        )
        from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary_by_type import (
            WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByType,
        )
        from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary_not_tested_reasons import (
            WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryNotTestedReasons,
        )

        d = dict(src_dict)
        _by_datasource = d.pop("by_datasource", UNSET)
        by_datasource: WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByDatasource | Unset
        if isinstance(_by_datasource, Unset) or _by_datasource is None:
            by_datasource = UNSET
        else:
            by_datasource = WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByDatasource.from_dict(
                _by_datasource
            )

        _by_type = d.pop("by_type", UNSET)
        by_type: WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByType | Unset
        if isinstance(_by_type, Unset) or _by_type is None:
            by_type = UNSET
        else:
            by_type = WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryByType.from_dict(_by_type)

        errors = d.pop("errors", UNSET)

        not_tested = d.pop("not_tested", UNSET)

        _not_tested_reasons = d.pop("not_tested_reasons", UNSET)
        not_tested_reasons: (
            WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryNotTestedReasons | Unset
        )
        if isinstance(_not_tested_reasons, Unset) or _not_tested_reasons is None:
            not_tested_reasons = UNSET
        else:
            not_tested_reasons = (
                WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummaryNotTestedReasons.from_dict(
                    _not_tested_reasons
                )
            )

        returned_data = d.pop("returned_data", UNSET)

        returned_data_pct_of_tested = d.pop("returned_data_pct_of_tested", UNSET)

        returned_data_pct_of_total = d.pop("returned_data_pct_of_total", UNSET)

        returned_empty = d.pop("returned_empty", UNSET)

        tested = d.pop("tested", UNSET)

        total_queries = d.pop("total_queries", UNSET)

        wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary = cls(
            by_datasource=by_datasource,
            by_type=by_type,
            errors=errors,
            not_tested=not_tested,
            not_tested_reasons=not_tested_reasons,
            returned_data=returned_data,
            returned_data_pct_of_tested=returned_data_pct_of_tested,
            returned_data_pct_of_total=returned_data_pct_of_total,
            returned_empty=returned_empty,
            tested=tested,
            total_queries=total_queries,
        )

        wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary.additional_properties = d
        return wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary

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
