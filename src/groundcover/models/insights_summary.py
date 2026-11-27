from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present import (
        InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent,
    )
    from ..models.insights_totals_are_the_published_goals_the_filters_selected import (
        InsightsTotalsAreThePublishedGoalsTheFiltersSelected,
    )
    from ..models.subject_bucket import SubjectBucket


T = TypeVar("T", bound="InsightsSummary")


@_attrs_define
class InsightsSummary:
    """InsightsSummary is the overview payload. A ratio with denominator 0 has no
    rate. Totals, PendingGoals and UnclassifiedGoals cover the whole filtered
    population, also under parentSubjectId. UnclassifiedGoals counts the goals of
    the root bucket of the subject other (subject_id:"other"); under a parent no
    such bucket is returned.

        Attributes:
            frustration (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could
                be evaluated, so there is no rate.
            latest_reported_at (datetime.datetime | None):
            pending_goals (int):
            satisfaction (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could
                be evaluated, so there is no rate.
            subjects (list[SubjectBucket]):
            success (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            totals (InsightsTotalsAreThePublishedGoalsTheFiltersSelected):
            unclassified_goals (int):
    """

    frustration: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    latest_reported_at: datetime.datetime | None
    pending_goals: int
    satisfaction: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    subjects: list[SubjectBucket]
    success: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    totals: InsightsTotalsAreThePublishedGoalsTheFiltersSelected
    unclassified_goals: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frustration = self.frustration.to_dict()

        latest_reported_at: None | str
        if isinstance(self.latest_reported_at, datetime.datetime):
            latest_reported_at = self.latest_reported_at.isoformat()
        else:
            latest_reported_at = self.latest_reported_at

        pending_goals = self.pending_goals

        satisfaction = self.satisfaction.to_dict()

        subjects = []
        for subjects_item_data in self.subjects:
            subjects_item = subjects_item_data.to_dict()
            subjects.append(subjects_item)

        success = self.success.to_dict()

        totals = self.totals.to_dict()

        unclassified_goals = self.unclassified_goals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frustration": frustration,
                "latestReportedAt": latest_reported_at,
                "pendingGoals": pending_goals,
                "satisfaction": satisfaction,
                "subjects": subjects,
                "success": success,
                "totals": totals,
                "unclassifiedGoals": unclassified_goals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present import (
            InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent,
        )
        from ..models.insights_totals_are_the_published_goals_the_filters_selected import (
            InsightsTotalsAreThePublishedGoalsTheFiltersSelected,
        )
        from ..models.subject_bucket import SubjectBucket

        d = dict(src_dict)
        frustration = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("frustration"))

        def _parse_latest_reported_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_reported_at_type_0 = datetime.datetime.fromisoformat(data)

                return latest_reported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        latest_reported_at = _parse_latest_reported_at(d.pop("latestReportedAt"))

        pending_goals = d.pop("pendingGoals")

        satisfaction = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("satisfaction"))

        subjects = []
        _subjects = d.pop("subjects")
        for subjects_item_data in _subjects:
            subjects_item = SubjectBucket.from_dict(subjects_item_data)

            subjects.append(subjects_item)

        success = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("success"))

        totals = InsightsTotalsAreThePublishedGoalsTheFiltersSelected.from_dict(d.pop("totals"))

        unclassified_goals = d.pop("unclassifiedGoals")

        insights_summary = cls(
            frustration=frustration,
            latest_reported_at=latest_reported_at,
            pending_goals=pending_goals,
            satisfaction=satisfaction,
            subjects=subjects,
            success=success,
            totals=totals,
            unclassified_goals=unclassified_goals,
        )

        insights_summary.additional_properties = d
        return insights_summary

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
