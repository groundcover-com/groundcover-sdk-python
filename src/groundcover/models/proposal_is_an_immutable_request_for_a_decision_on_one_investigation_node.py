from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node_review_state import (
    ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState,
)
from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node_status import (
    ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeStatus,
)
from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node_type import (
    ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeType,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor
    from ..models.investigation_evidence import InvestigationEvidence
    from ..models.proposal_assessment_verdict_is_a_proposals_verdict_on_one_assessment_as_reads_return_it import (
        ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt,
    )
    from ..models.proposal_child_describes_a_node_to_create_if_the_proposal_is_approved import (
        ProposalChildDescribesANodeToCreateIfTheProposalIsApproved,
    )
    from ..models.proposal_decision_records_who_decided_a_proposal_and_why import (
        ProposalDecisionRecordsWhoDecidedAProposalAndWhy,
    )


T = TypeVar("T", bound="ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode")


@_attrs_define
class ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (InvestigationAuthor):
        details (str):
        evidence (list[InvestigationEvidence]):
        id (UUID):
        investigation_id (UUID):
        status (ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeStatus):
        type_ (ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeType): create_child ProposalCreateChild
            resolve ProposalResolve
            refute ProposalRefute
            stop ProposalStop
        assessment_verdicts (list[ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt] | Unset):
            A resolve or refute's verdicts on the node's assessments, each at the revision it graded.
        blocked_by (list[UUID] | Unset): Open descendants blocking a pending resolve or refute, computed at read time.
        child (ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset):
        child_id (UUID | Unset):
        decision (ProposalDecisionRecordsWhoDecidedAProposalAndWhy | Unset):
        review_state (ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState | Unset): Where a
            pending proposal stands in moderation; set only by the tree-wide proposals list.
            deferred: blockedBy is non-empty; reviewing: a review of its decision group is starting or running;
            needs_person: its group's cycle used up its reviews, so a person decides; queued: none of these.
            queued ReviewStateQueued
            reviewing ReviewStateReviewing
            deferred ReviewStateDeferred
            needs_person ReviewStateNeedsPerson
    """

    created_at: datetime.datetime
    created_by: InvestigationAuthor
    details: str
    evidence: list[InvestigationEvidence]
    id: UUID
    investigation_id: UUID
    status: ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeStatus
    type_: ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeType
    assessment_verdicts: list[ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt] | Unset = (
        UNSET
    )
    blocked_by: list[UUID] | Unset = UNSET
    child: ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset = UNSET
    child_id: UUID | Unset = UNSET
    decision: ProposalDecisionRecordsWhoDecidedAProposalAndWhy | Unset = UNSET
    review_state: ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by.to_dict()

        details = self.details

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        id = str(self.id)

        investigation_id = str(self.investigation_id)

        status = self.status.value

        type_ = self.type_.value

        assessment_verdicts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assessment_verdicts, Unset):
            assessment_verdicts = []
            for assessment_verdicts_item_data in self.assessment_verdicts:
                assessment_verdicts_item = assessment_verdicts_item_data.to_dict()
                assessment_verdicts.append(assessment_verdicts_item)

        blocked_by: list[str] | Unset = UNSET
        if not isinstance(self.blocked_by, Unset):
            blocked_by = []
            for blocked_by_item_data in self.blocked_by:
                blocked_by_item = str(blocked_by_item_data)
                blocked_by.append(blocked_by_item)

        child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child, Unset):
            child = self.child.to_dict()

        child_id: str | Unset = UNSET
        if not isinstance(self.child_id, Unset):
            child_id = str(self.child_id)

        decision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.to_dict()

        review_state: str | Unset = UNSET
        if not isinstance(self.review_state, Unset):
            review_state = self.review_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "createdBy": created_by,
                "details": details,
                "evidence": evidence,
                "id": id,
                "investigationId": investigation_id,
                "status": status,
                "type": type_,
            }
        )
        if assessment_verdicts is not UNSET:
            field_dict["assessmentVerdicts"] = assessment_verdicts
        if blocked_by is not UNSET:
            field_dict["blockedBy"] = blocked_by
        if child is not UNSET:
            field_dict["child"] = child
        if child_id is not UNSET:
            field_dict["childId"] = child_id
        if decision is not UNSET:
            field_dict["decision"] = decision
        if review_state is not UNSET:
            field_dict["reviewState"] = review_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor
        from ..models.investigation_evidence import InvestigationEvidence
        from ..models.proposal_assessment_verdict_is_a_proposals_verdict_on_one_assessment_as_reads_return_it import (
            ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt,
        )
        from ..models.proposal_child_describes_a_node_to_create_if_the_proposal_is_approved import (
            ProposalChildDescribesANodeToCreateIfTheProposalIsApproved,
        )
        from ..models.proposal_decision_records_who_decided_a_proposal_and_why import (
            ProposalDecisionRecordsWhoDecidedAProposalAndWhy,
        )

        d = dict(src_dict)
        created_at = parse_datetime(d.pop("createdAt"))

        created_by = InvestigationAuthor.from_dict(d.pop("createdBy"))

        details = d.pop("details")

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = InvestigationEvidence.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        id = UUID(d.pop("id"))

        investigation_id = UUID(d.pop("investigationId"))

        status = ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeStatus(d.pop("status"))

        type_ = ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeType(d.pop("type"))

        _assessment_verdicts = d.pop("assessmentVerdicts", UNSET)
        assessment_verdicts: (
            list[ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt] | Unset
        ) = UNSET
        if _assessment_verdicts is not UNSET:
            assessment_verdicts = []
            for assessment_verdicts_item_data in _assessment_verdicts:
                assessment_verdicts_item = (
                    ProposalAssessmentVerdictIsAProposalsVerdictOnOneAssessmentAsReadsReturnIt.from_dict(
                        assessment_verdicts_item_data
                    )
                )

                assessment_verdicts.append(assessment_verdicts_item)

        _blocked_by = d.pop("blockedBy", UNSET)
        blocked_by: list[UUID] | Unset = UNSET
        if _blocked_by is not UNSET:
            blocked_by = []
            for blocked_by_item_data in _blocked_by:
                blocked_by_item = UUID(blocked_by_item_data)

                blocked_by.append(blocked_by_item)

        _child = d.pop("child", UNSET)
        child: ProposalChildDescribesANodeToCreateIfTheProposalIsApproved | Unset
        if isinstance(_child, Unset) or _child is None:
            child = UNSET
        else:
            child = ProposalChildDescribesANodeToCreateIfTheProposalIsApproved.from_dict(_child)

        _child_id = d.pop("childId", UNSET)
        child_id: UUID | Unset
        if isinstance(_child_id, Unset) or _child_id is None:
            child_id = UNSET
        else:
            child_id = UUID(_child_id)

        _decision = d.pop("decision", UNSET)
        decision: ProposalDecisionRecordsWhoDecidedAProposalAndWhy | Unset
        if isinstance(_decision, Unset) or _decision is None:
            decision = UNSET
        else:
            decision = ProposalDecisionRecordsWhoDecidedAProposalAndWhy.from_dict(_decision)

        _review_state = d.pop("reviewState", UNSET)
        review_state: ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState | Unset
        if isinstance(_review_state, Unset) or _review_state is None:
            review_state = UNSET
        else:
            review_state = ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState(_review_state)

        proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node = cls(
            created_at=created_at,
            created_by=created_by,
            details=details,
            evidence=evidence,
            id=id,
            investigation_id=investigation_id,
            status=status,
            type_=type_,
            assessment_verdicts=assessment_verdicts,
            blocked_by=blocked_by,
            child=child,
            child_id=child_id,
            decision=decision,
            review_state=review_state,
        )

        proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node.additional_properties = d
        return proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node

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
