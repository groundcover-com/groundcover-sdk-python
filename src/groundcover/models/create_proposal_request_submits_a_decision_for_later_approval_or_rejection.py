from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_proposal_request_submits_a_decision_for_later_approval_or_rejection_type import (
    CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejectionType,
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


T = TypeVar("T", bound="CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejection")


@_attrs_define
class CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejection:
    """
    Attributes:
        details (str):
        type_ (CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejectionType): create_child ProposalCreateChild
            resolve ProposalResolve
            refute ProposalRefute
            stop ProposalStop
        assessment_verdicts (list[AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead]
            | Unset): Required for resolve and refute: exactly one per open assessment on the node, at its current revision.
            Not allowed for create_child and stop.
        child (ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset):
        evidence (list[EvidenceRequest] | Unset): Findings from the same tree; omitted means none. Each finding may
            appear once.
    """

    details: str
    type_: CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejectionType
    assessment_verdicts: (
        list[AssessmentVerdictRequestGradesOneOpenAssessmentOnTheNodeAtTheRevisionTheProposerRead] | Unset
    ) = UNSET
    child: ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset = UNSET
    evidence: list[EvidenceRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

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
                "details": details,
                "type": type_,
            }
        )
        if assessment_verdicts is not UNSET:
            field_dict["assessmentVerdicts"] = assessment_verdicts
        if child is not UNSET:
            field_dict["child"] = child
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
        details = d.pop("details")

        type_ = CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejectionType(d.pop("type"))

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

        _evidence = d.pop("evidence", UNSET)
        evidence: list[EvidenceRequest] | Unset = UNSET
        if _evidence is not UNSET:
            evidence = []
            for evidence_item_data in _evidence:
                evidence_item = EvidenceRequest.from_dict(evidence_item_data)

                evidence.append(evidence_item)

        create_proposal_request_submits_a_decision_for_later_approval_or_rejection = cls(
            details=details,
            type_=type_,
            assessment_verdicts=assessment_verdicts,
            child=child,
            evidence=evidence,
        )

        create_proposal_request_submits_a_decision_for_later_approval_or_rejection.additional_properties = d
        return create_proposal_request_submits_a_decision_for_later_approval_or_rejection

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
