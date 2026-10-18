from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assessment_verdict_request import AssessmentVerdictRequest


T = TypeVar("T", bound="DecideProposalRequestApprovesOrRejectsAPendingProposal")


@_attrs_define
class DecideProposalRequestApprovesOrRejectsAPendingProposal:
    """
    Attributes:
        reason (str):
        assessment_verdicts (list[AssessmentVerdictRequest] | Unset): Each assessment may appear once. Approvals judge
            assessments only for resolve/refute.
    """

    reason: str
    assessment_verdicts: list[AssessmentVerdictRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        assessment_verdicts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assessment_verdicts, Unset):
            assessment_verdicts = []
            for assessment_verdicts_item_data in self.assessment_verdicts:
                assessment_verdicts_item = assessment_verdicts_item_data.to_dict()
                assessment_verdicts.append(assessment_verdicts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if assessment_verdicts is not UNSET:
            field_dict["assessmentVerdicts"] = assessment_verdicts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assessment_verdict_request import AssessmentVerdictRequest

        d = dict(src_dict)
        reason = d.pop("reason")

        _assessment_verdicts = d.pop("assessmentVerdicts", UNSET)
        assessment_verdicts: list[AssessmentVerdictRequest] | Unset = UNSET
        if _assessment_verdicts is not UNSET:
            assessment_verdicts = []
            for assessment_verdicts_item_data in _assessment_verdicts:
                assessment_verdicts_item = AssessmentVerdictRequest.from_dict(assessment_verdicts_item_data)

                assessment_verdicts.append(assessment_verdicts_item)

        decide_proposal_request_approves_or_rejects_a_pending_proposal = cls(
            reason=reason,
            assessment_verdicts=assessment_verdicts,
        )

        decide_proposal_request_approves_or_rejects_a_pending_proposal.additional_properties = d
        return decide_proposal_request_approves_or_rejects_a_pending_proposal

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
