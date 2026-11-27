from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present import (
        InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent,
    )


T = TypeVar("T", bound="SubjectBucket")


@_attrs_define
class SubjectBucket:
    """SubjectBucket is one slice of the subject chart, bucketed by the goal's
    subject_id facet. At the root a bucket is a top-level subtree, and the
    bucket of the subject other (Direct), under its catalog label, also holds
    goals with no current subject. Under a parent, buckets are child subtrees plus the parent's
    direct assignments (Direct). Costs sum recorded values in USD, including
    pending goals; their known counts expose partial coverage. NonSuccessGoals
    and nonSuccessGenAiCostTotal count goals whose outcome is partial_success,
    failure, abandoned or blocked; they are not the charts' unresolved blocker state.

        Attributes:
            frustration (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could
                be evaluated, so there is no rate.
            gen_ai_cost_total (float | None): GenAiCostTotal is the bucket's total cost in USD.
            gen_ai_cost_total_known (int): GenAiCostTotalKnown counts the goals with a recorded cost.
            goals (int):
            label (str):
            non_success_gen_ai_cost_total (float | None): NonSuccessGenAiCostTotal is the total cost of the non-success
                goals in USD.
            non_success_gen_ai_cost_total_known (int): NonSuccessGenAiCostTotalKnown counts the non-success goals with a
                recorded cost.
            non_success_goals (int):
            share (float):
            subject_id (str):
            success (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            direct (bool | Unset):
            drilldown (str | Unset): Drilldown is the clause of this bucket. To open it, send the same sources and
                (<request query>) AND <clause>, or the clause alone when the request query
                is empty; that selects exactly this bucket's goals. A parent's Direct bucket
                has none: gcQL cannot select a subject without its children.
    """

    frustration: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    gen_ai_cost_total: float | None
    gen_ai_cost_total_known: int
    goals: int
    label: str
    non_success_gen_ai_cost_total: float | None
    non_success_gen_ai_cost_total_known: int
    non_success_goals: int
    share: float
    subject_id: str
    success: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    direct: bool | Unset = UNSET
    drilldown: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frustration = self.frustration.to_dict()

        gen_ai_cost_total: float | None
        gen_ai_cost_total = self.gen_ai_cost_total

        gen_ai_cost_total_known = self.gen_ai_cost_total_known

        goals = self.goals

        label = self.label

        non_success_gen_ai_cost_total: float | None
        non_success_gen_ai_cost_total = self.non_success_gen_ai_cost_total

        non_success_gen_ai_cost_total_known = self.non_success_gen_ai_cost_total_known

        non_success_goals = self.non_success_goals

        share = self.share

        subject_id = self.subject_id

        success = self.success.to_dict()

        direct = self.direct

        drilldown = self.drilldown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frustration": frustration,
                "genAiCostTotal": gen_ai_cost_total,
                "genAiCostTotalKnown": gen_ai_cost_total_known,
                "goals": goals,
                "label": label,
                "nonSuccessGenAiCostTotal": non_success_gen_ai_cost_total,
                "nonSuccessGenAiCostTotalKnown": non_success_gen_ai_cost_total_known,
                "nonSuccessGoals": non_success_goals,
                "share": share,
                "subjectId": subject_id,
                "success": success,
            }
        )
        if direct is not UNSET:
            field_dict["direct"] = direct
        if drilldown is not UNSET:
            field_dict["drilldown"] = drilldown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present import (
            InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent,
        )

        d = dict(src_dict)
        frustration = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("frustration"))

        def _parse_gen_ai_cost_total(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        gen_ai_cost_total = _parse_gen_ai_cost_total(d.pop("genAiCostTotal"))

        gen_ai_cost_total_known = d.pop("genAiCostTotalKnown")

        goals = d.pop("goals")

        label = d.pop("label")

        def _parse_non_success_gen_ai_cost_total(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        non_success_gen_ai_cost_total = _parse_non_success_gen_ai_cost_total(d.pop("nonSuccessGenAiCostTotal"))

        non_success_gen_ai_cost_total_known = d.pop("nonSuccessGenAiCostTotalKnown")

        non_success_goals = d.pop("nonSuccessGoals")

        share = d.pop("share")

        subject_id = d.pop("subjectId")

        success = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("success"))

        direct = d.pop("direct", UNSET)

        drilldown = d.pop("drilldown", UNSET)

        subject_bucket = cls(
            frustration=frustration,
            gen_ai_cost_total=gen_ai_cost_total,
            gen_ai_cost_total_known=gen_ai_cost_total_known,
            goals=goals,
            label=label,
            non_success_gen_ai_cost_total=non_success_gen_ai_cost_total,
            non_success_gen_ai_cost_total_known=non_success_gen_ai_cost_total_known,
            non_success_goals=non_success_goals,
            share=share,
            subject_id=subject_id,
            success=success,
            direct=direct,
            drilldown=drilldown,
        )

        subject_bucket.additional_properties = d
        return subject_bucket

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
