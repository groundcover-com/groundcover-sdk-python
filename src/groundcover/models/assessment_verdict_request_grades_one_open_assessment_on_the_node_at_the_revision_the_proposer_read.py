from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assessment_verdict_request_grades_one_open_assessment_on_the_node_at_the_revision_the_proposer_read_verdict import (
    AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerReadVerdict,
)

T = TypeVar("T", bound="AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead")


@_attrs_define
class AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead:
    """
    Attributes:
        assessment_id (UUID):
        reason (str):
        revision (int): The assessment's revision the verdict grades.
        verdict (AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerReadVerdict):
    """

    assessment_id: UUID
    reason: str
    revision: int
    verdict: AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerReadVerdict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assessment_id = str(self.assessment_id)

        reason = self.reason

        revision = self.revision

        verdict = self.verdict.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessmentId": assessment_id,
                "reason": reason,
                "revision": revision,
                "verdict": verdict,
            }
        )

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
        assessment_id = UUID(d.pop("assessmentId"))

        reason = d.pop("reason")

        revision = d.pop("revision")

        verdict = AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerReadVerdict(
            d.pop("verdict")
        )

        assessment_verdict_request_grades_one_open_assessment_on_the_node_at_the_revision_the_proposer_read = cls(
            assessment_id=assessment_id,
            reason=reason,
            revision=revision,
            verdict=verdict,
        )

        assessment_verdict_request_grades_one_open_assessment_on_the_node_at_the_revision_the_proposer_read.additional_properties = d
        return assessment_verdict_request_grades_one_open_assessment_on_the_node_at_the_revision_the_proposer_read

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
