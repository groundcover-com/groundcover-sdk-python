from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.queries_summary_holds_query_level_statistics_for_the_unified_summary_by_datasource import (
        QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummaryByDatasource,
    )


T = TypeVar("T", bound="QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary")


@_attrs_define
class QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary:
    """
    Attributes:
        by_datasource (QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummaryByDatasource | Unset):
        failed (int | Unset):
        passed (int | Unset):
        passed_pct (float | Unset):
        total (int | Unset):
    """

    by_datasource: QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummaryByDatasource | Unset = UNSET
    failed: int | Unset = UNSET
    passed: int | Unset = UNSET
    passed_pct: float | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_datasource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_datasource, Unset):
            by_datasource = self.by_datasource.to_dict()

        failed = self.failed

        passed = self.passed

        passed_pct = self.passed_pct

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_datasource is not UNSET:
            field_dict["by_datasource"] = by_datasource
        if failed is not UNSET:
            field_dict["failed"] = failed
        if passed is not UNSET:
            field_dict["passed"] = passed
        if passed_pct is not UNSET:
            field_dict["passed_pct"] = passed_pct
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queries_summary_holds_query_level_statistics_for_the_unified_summary_by_datasource import (
            QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummaryByDatasource,
        )

        d = dict(src_dict)
        _by_datasource = d.pop("by_datasource", UNSET)
        by_datasource: QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummaryByDatasource | Unset
        if isinstance(_by_datasource, Unset) or _by_datasource is None:
            by_datasource = UNSET
        else:
            by_datasource = QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummaryByDatasource.from_dict(
                _by_datasource
            )

        failed = d.pop("failed", UNSET)

        passed = d.pop("passed", UNSET)

        passed_pct = d.pop("passed_pct", UNSET)

        total = d.pop("total", UNSET)

        queries_summary_holds_query_level_statistics_for_the_unified_summary = cls(
            by_datasource=by_datasource,
            failed=failed,
            passed=passed,
            passed_pct=passed_pct,
            total=total,
        )

        queries_summary_holds_query_level_statistics_for_the_unified_summary.additional_properties = d
        return queries_summary_holds_query_level_statistics_for_the_unified_summary

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
