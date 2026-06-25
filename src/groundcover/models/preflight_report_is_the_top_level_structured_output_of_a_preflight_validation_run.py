from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_plan_provides_a_prioritized_path_to_improve_query_success_rate import (
        CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate,
    )
    from ..models.finding_represents_a_single_preflight_validation_finding import (
        FindingRepresentsASinglePreflightValidationFinding,
    )
    from ..models.integration_count_holds_an_integration_name_and_its_count_for_sorted_output import (
        IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput,
    )
    from ..models.unified_summary_is_the_single_hierarchical_summary_included_in_json_output import (
        UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput,
    )
    from ..models.wet_report_holds_the_complete_wet_mode_results_for_inclusion_in_preflight_report import (
        WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport,
    )


T = TypeVar("T", bound="PreflightReportIsTheTopLevelStructuredOutputOfAPreflightValidationRun")


@_attrs_define
class PreflightReportIsTheTopLevelStructuredOutputOfAPreflightValidationRun:
    """
    Attributes:
        coverage_plan (CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate | Unset):
        integrations_summary (list[IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput] | Unset):
        raw_findings (list[FindingRepresentsASinglePreflightValidationFinding] | Unset):
        summary (UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput | Unset):
        wet_results (WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport | Unset):
    """

    coverage_plan: CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate | Unset = UNSET
    integrations_summary: list[IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput] | Unset = UNSET
    raw_findings: list[FindingRepresentsASinglePreflightValidationFinding] | Unset = UNSET
    summary: UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput | Unset = UNSET
    wet_results: WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coverage_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coverage_plan, Unset):
            coverage_plan = self.coverage_plan.to_dict()

        integrations_summary: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.integrations_summary, Unset):
            integrations_summary = []
            for integrations_summary_item_data in self.integrations_summary:
                integrations_summary_item = integrations_summary_item_data.to_dict()
                integrations_summary.append(integrations_summary_item)

        raw_findings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.raw_findings, Unset):
            raw_findings = []
            for raw_findings_item_data in self.raw_findings:
                raw_findings_item = raw_findings_item_data.to_dict()
                raw_findings.append(raw_findings_item)

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        wet_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wet_results, Unset):
            wet_results = self.wet_results.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coverage_plan is not UNSET:
            field_dict["coverage_plan"] = coverage_plan
        if integrations_summary is not UNSET:
            field_dict["integrations_summary"] = integrations_summary
        if raw_findings is not UNSET:
            field_dict["raw_findings"] = raw_findings
        if summary is not UNSET:
            field_dict["summary"] = summary
        if wet_results is not UNSET:
            field_dict["wet_results"] = wet_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_plan_provides_a_prioritized_path_to_improve_query_success_rate import (
            CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate,
        )
        from ..models.finding_represents_a_single_preflight_validation_finding import (
            FindingRepresentsASinglePreflightValidationFinding,
        )
        from ..models.integration_count_holds_an_integration_name_and_its_count_for_sorted_output import (
            IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput,
        )
        from ..models.unified_summary_is_the_single_hierarchical_summary_included_in_json_output import (
            UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput,
        )
        from ..models.wet_report_holds_the_complete_wet_mode_results_for_inclusion_in_preflight_report import (
            WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport,
        )

        d = dict(src_dict)
        _coverage_plan = d.pop("coverage_plan", UNSET)
        coverage_plan: CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate | Unset
        if isinstance(_coverage_plan, Unset) or _coverage_plan is None:
            coverage_plan = UNSET
        else:
            coverage_plan = CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate.from_dict(_coverage_plan)

        _integrations_summary = d.pop("integrations_summary", UNSET)
        integrations_summary: list[IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput] | Unset = UNSET
        if _integrations_summary is not UNSET:
            integrations_summary = []
            for integrations_summary_item_data in _integrations_summary:
                integrations_summary_item = IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput.from_dict(
                    integrations_summary_item_data
                )

                integrations_summary.append(integrations_summary_item)

        _raw_findings = d.pop("raw_findings", UNSET)
        raw_findings: list[FindingRepresentsASinglePreflightValidationFinding] | Unset = UNSET
        if _raw_findings is not UNSET:
            raw_findings = []
            for raw_findings_item_data in _raw_findings:
                raw_findings_item = FindingRepresentsASinglePreflightValidationFinding.from_dict(raw_findings_item_data)

                raw_findings.append(raw_findings_item)

        _summary = d.pop("summary", UNSET)
        summary: UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput | Unset
        if isinstance(_summary, Unset) or _summary is None:
            summary = UNSET
        else:
            summary = UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput.from_dict(_summary)

        _wet_results = d.pop("wet_results", UNSET)
        wet_results: WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport | Unset
        if isinstance(_wet_results, Unset) or _wet_results is None:
            wet_results = UNSET
        else:
            wet_results = WetReportHoldsTheCompleteWetModeResultsForInclusionInPreflightReport.from_dict(_wet_results)

        preflight_report_is_the_top_level_structured_output_of_a_preflight_validation_run = cls(
            coverage_plan=coverage_plan,
            integrations_summary=integrations_summary,
            raw_findings=raw_findings,
            summary=summary,
            wet_results=wet_results,
        )

        preflight_report_is_the_top_level_structured_output_of_a_preflight_validation_run.additional_properties = d
        return preflight_report_is_the_top_level_structured_output_of_a_preflight_validation_run

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
