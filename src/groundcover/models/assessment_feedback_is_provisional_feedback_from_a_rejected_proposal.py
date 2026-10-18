from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assessment_feedback_is_provisional_feedback_from_a_rejected_proposal_verdict import (
    AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposalVerdict,
)

T = TypeVar("T", bound="AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposal")


@_attrs_define
class AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposal:
    """
    Attributes:
        proposal_id (UUID):
        reason (str):
        verdict (AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposalVerdict): open VerdictOpen
            correct VerdictCorrect
            incorrect VerdictIncorrect
    """

    proposal_id: UUID
    reason: str
    verdict: AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposalVerdict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = str(self.proposal_id)

        reason = self.reason

        verdict = self.verdict.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposalId": proposal_id,
                "reason": reason,
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
        proposal_id = UUID(d.pop("proposalId"))

        reason = d.pop("reason")

        verdict = AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposalVerdict(d.pop("verdict"))

        assessment_feedback_is_provisional_feedback_from_a_rejected_proposal = cls(
            proposal_id=proposal_id,
            reason=reason,
            verdict=verdict,
        )

        assessment_feedback_is_provisional_feedback_from_a_rejected_proposal.additional_properties = d
        return assessment_feedback_is_provisional_feedback_from_a_rejected_proposal

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
