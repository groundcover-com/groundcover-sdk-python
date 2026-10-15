from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assessment_is_one_participants_current_conclusion_on_a_node import (
        AssessmentIsOneParticipantsCurrentConclusionOnANode,
    )
    from ..models.investigation_finding import InvestigationFinding
    from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
        InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
    )
    from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node import (
        ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode,
    )


T = TypeVar("T", bound="GetInvestigationResponse")


@_attrs_define
class GetInvestigationResponse:
    """
    Attributes:
        assessments (list[AssessmentIsOneParticipantsCurrentConclusionOnANode]): Each participant's assessment on this
            node, its evidence embedding the cited findings; an empty collection is [].
        children (list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]):
        events_after (int): Tree events after afterTimestamp, or all events when it is omitted.
        findings (list[InvestigationFinding]): Findings belonging to this node, included for all callers; an empty
            collection is [].
        investigation (InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion):
        proposals (list[ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode]): Pending and decided proposals
            on this node; an empty collection is [].
        next_after_timestamp (datetime.datetime | Unset): Timestamp of the latest tree event in this snapshot.
    """

    assessments: list[AssessmentIsOneParticipantsCurrentConclusionOnANode]
    children: list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]
    events_after: int
    findings: list[InvestigationFinding]
    investigation: InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion
    proposals: list[ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode]
    next_after_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assessments = []
        for assessments_item_data in self.assessments:
            assessments_item = assessments_item_data.to_dict()
            assessments.append(assessments_item)

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        events_after = self.events_after

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        investigation = self.investigation.to_dict()

        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        next_after_timestamp: str | Unset = UNSET
        if not isinstance(self.next_after_timestamp, Unset):
            next_after_timestamp = self.next_after_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessments": assessments,
                "children": children,
                "eventsAfter": events_after,
                "findings": findings,
                "investigation": investigation,
                "proposals": proposals,
            }
        )
        if next_after_timestamp is not UNSET:
            field_dict["nextAfterTimestamp"] = next_after_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assessment_is_one_participants_current_conclusion_on_a_node import (
            AssessmentIsOneParticipantsCurrentConclusionOnANode,
        )
        from ..models.investigation_finding import InvestigationFinding
        from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
            InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
        )
        from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node import (
            ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode,
        )

        d = dict(src_dict)
        assessments = []
        _assessments = d.pop("assessments")
        for assessments_item_data in _assessments:
            assessments_item = AssessmentIsOneParticipantsCurrentConclusionOnANode.from_dict(assessments_item_data)

            assessments.append(assessments_item)

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion.from_dict(
                children_item_data
            )

            children.append(children_item)

        events_after = d.pop("eventsAfter")

        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = InvestigationFinding.from_dict(findings_item_data)

            findings.append(findings_item)

        investigation = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion.from_dict(
            d.pop("investigation")
        )

        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode.from_dict(
                proposals_item_data
            )

            proposals.append(proposals_item)

        _next_after_timestamp = d.pop("nextAfterTimestamp", UNSET)
        next_after_timestamp: datetime.datetime | Unset
        if isinstance(_next_after_timestamp, Unset) or _next_after_timestamp is None:
            next_after_timestamp = UNSET
        else:
            next_after_timestamp = parse_datetime(_next_after_timestamp)

        get_investigation_response = cls(
            assessments=assessments,
            children=children,
            events_after=events_after,
            findings=findings,
            investigation=investigation,
            proposals=proposals,
            next_after_timestamp=next_after_timestamp,
        )

        get_investigation_response.additional_properties = d
        return get_investigation_response

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
