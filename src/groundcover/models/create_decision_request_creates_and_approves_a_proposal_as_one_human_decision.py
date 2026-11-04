from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_decision_request_creates_and_approves_a_proposal_as_one_human_decision_type import (
    CreateDecisionRequestCreatesAndApprovesAProposalAsOneHumanDecisionType,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assessment_verdict_request_grades_one_open_assessment_on_the_node_at_the_revision_the_proposer_read import (
        AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead,
    )
    from ..models.evidence_request import EvidenceRequest
    from ..models.proposal_child_describes_a_node_to_create_if_the_proposal_is_approved import (
        ProposalChildDescribesANodeToCreateIfTheProposalIsApproved,
    )


T = TypeVar("T", bound="CreateDecisionRequestCreatesAndApprovesAProposalAsOneHumanDecision")


@_attrs_define
class CreateDecisionRequestCreatesAndApprovesAProposalAsOneHumanDecision:
    """
    Attributes:
        type_ (CreateDecisionRequestCreatesAndApprovesAProposalAsOneHumanDecisionType): create_child ProposalCreateChild
            resolve ProposalResolve
            refute ProposalRefute
            stop ProposalStop
        assessment_verdicts (list[AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead]
            | Unset): Optional verdicts for resolve and refute, at each assessment's current revision.
            Omitted open assessments remain unjudged. Not allowed for create_child and stop.
        child (ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset):
        details (str | Unset): Defaults to "Decided by user." when omitted or blank.
        evidence (list[EvidenceRequest] | Unset): Optional findings from the same tree. Each finding may appear once.
    """

    type_: CreateDecisionRequestCreatesAndApprovesAProposalAsOneHumanDecisionType
    assessment_verdicts: (
        list[AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead] | Unset
    ) = UNSET
    child: ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset = UNSET
    details: str | Unset = UNSET
    evidence: list[EvidenceRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        assessment_verdicts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assessment_verdicts, Unset):
            assessment_verdicts = []
            for assessment_verdicts_item_data in self.assessment_verdicts:
                assessment_verdicts_item = assessment_verdicts_item_data.to_dict()
                assessment_verdicts.append(assessment_verdicts_item)

        child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child, Unset):
            child = self.child.to_dict()

        details = self.details

        evidence: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = []
            for evidence_item_data in self.evidence:
                evidence_item = evidence_item_data.to_dict()
                evidence.append(evidence_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if assessment_verdicts is not UNSET:
            field_dict["assessmentVerdicts"] = assessment_verdicts
        if child is not UNSET:
            field_dict["child"] = child
        if details is not UNSET:
            field_dict["details"] = details
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assessment_verdict_request_grades_one_open_assessment_on_the_node_at_the_revision_the_proposer_read import (
            AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead,
        )
        from ..models.evidence_request import EvidenceRequest
        from ..models.proposal_child_describes_a_node_to_create_if_the_proposal_is_approved import (
            ProposalChildDescribesANodeToCreateIfTheProposalIsApproved,
        )

        d = dict(src_dict)
        type_ = CreateDecisionRequestCreatesAndApprovesAProposalAsOneHumanDecisionType(d.pop("type"))

        _assessment_verdicts = d.pop("assessmentVerdicts", UNSET)
        assessment_verdicts: (
            list[AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead] | Unset
        ) = UNSET
        if _assessment_verdicts is not UNSET:
            assessment_verdicts = []
            for assessment_verdicts_item_data in _assessment_verdicts:
                assessment_verdicts_item = (
                    AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead.from_dict(
                        assessment_verdicts_item_data
                    )
                )

                assessment_verdicts.append(assessment_verdicts_item)

        _child = d.pop("child", UNSET)
        child: ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset
        if isinstance(_child, Unset) or _child is None:
            child = UNSET
        else:
            child = ProposalChildDescribesANodeToCreateIfTheProposalIsApproved.from_dict(_child)

        details = d.pop("details", UNSET)

        _evidence = d.pop("evidence", UNSET)
        evidence: list[EvidenceRequest] | Unset = UNSET
        if _evidence is not UNSET:
            evidence = []
            for evidence_item_data in _evidence:
                evidence_item = EvidenceRequest.from_dict(evidence_item_data)

                evidence.append(evidence_item)

        create_decision_request_creates_and_approves_a_proposal_as_one_human_decision = cls(
            type_=type_,
            assessment_verdicts=assessment_verdicts,
            child=child,
            details=details,
            evidence=evidence,
        )

        create_decision_request_creates_and_approves_a_proposal_as_one_human_decision.additional_properties = d
        return create_decision_request_creates_and_approves_a_proposal_as_one_human_decision

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
