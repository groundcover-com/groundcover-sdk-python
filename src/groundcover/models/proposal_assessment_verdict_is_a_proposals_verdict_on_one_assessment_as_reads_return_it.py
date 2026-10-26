from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proposal_assessment_verdict_is_a_proposals_verdict_on_one_assessment_as_reads_return_it_verdict import (
    ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnItVerdict,
)

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor


T = TypeVar("T", bound="ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt")


@_attrs_define
class ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt:
    """
    Attributes:
        assessment_author (InvestigationAuthor):
        assessment_id (UUID):
        assessment_revision (int): The assessment's current revision; the verdict applies only while it equals Revision.
        reason (str):
        revision (int):
        verdict (ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnItVerdict):
    """

    assessment_author: InvestigationAuthor
    assessment_id: UUID
    assessment_revision: int
    reason: str
    revision: int
    verdict: ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnItVerdict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assessment_author = self.assessment_author.to_dict()

        assessment_id = str(self.assessment_id)

        assessment_revision = self.assessment_revision

        reason = self.reason

        revision = self.revision

        verdict = self.verdict.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessmentAuthor": assessment_author,
                "assessmentId": assessment_id,
                "assessmentRevision": assessment_revision,
                "reason": reason,
                "revision": revision,
                "verdict": verdict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor

        d = dict(src_dict)
        assessment_author = InvestigationAuthor.from_dict(d.pop("assessmentAuthor"))

        assessment_id = UUID(d.pop("assessmentId"))

        assessment_revision = d.pop("assessmentRevision")

        reason = d.pop("reason")

        revision = d.pop("revision")

        verdict = ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnItVerdict(d.pop("verdict"))

        proposal_assessment_verdict_is_a_proposals_verdict_on_one_assessment_as_reads_return_it = cls(
            assessment_author=assessment_author,
            assessment_id=assessment_id,
            assessment_revision=assessment_revision,
            reason=reason,
            revision=revision,
            verdict=verdict,
        )

        proposal_assessment_verdict_is_a_proposals_verdict_on_one_assessment_as_reads_return_it.additional_properties = d
        return proposal_assessment_verdict_is_a_proposals_verdict_on_one_assessment_as_reads_return_it

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
