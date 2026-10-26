from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assessment_is_one_participants_current_conclusion_on_a_node_verdict import (
    AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor
    from ..models.investigation_evidence import InvestigationEvidence


T = TypeVar("T", bound="AssessmentIsOneParticipantsCurrentConclusionOnANode")


@_attrs_define
class AssessmentIsOneParticipantsCurrentConclusionOnANode:
    """
    Attributes:
        author (InvestigationAuthor):
        details (str):
        evidence (list[InvestigationEvidence]):
        id (UUID):
        investigation_id (UUID):
        revision (int): Starts at 1; every update adds one.
        updated_at (datetime.datetime):
        verdict (AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict): Set from the approved conclusion's verdict
            on this revision; an update resets it to open.
        verdict_proposal_id (UUID | Unset): The approved conclusion whose verdict set Verdict.
        verdict_reason (str | Unset):
    """

    author: InvestigationAuthor
    details: str
    evidence: list[InvestigationEvidence]
    id: UUID
    investigation_id: UUID
    revision: int
    updated_at: datetime.datetime
    verdict: AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict
    verdict_proposal_id: UUID | Unset = UNSET
    verdict_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author.to_dict()

        details = self.details

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        id = str(self.id)

        investigation_id = str(self.investigation_id)

        revision = self.revision

        updated_at = self.updated_at.isoformat()

        verdict = self.verdict.value

        verdict_proposal_id: str | Unset = UNSET
        if not isinstance(self.verdict_proposal_id, Unset):
            verdict_proposal_id = str(self.verdict_proposal_id)

        verdict_reason = self.verdict_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "details": details,
                "evidence": evidence,
                "id": id,
                "investigationId": investigation_id,
                "revision": revision,
                "updatedAt": updated_at,
                "verdict": verdict,
            }
        )
        if verdict_proposal_id is not UNSET:
            field_dict["verdictProposalId"] = verdict_proposal_id
        if verdict_reason is not UNSET:
            field_dict["verdictReason"] = verdict_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor
        from ..models.investigation_evidence import InvestigationEvidence

        d = dict(src_dict)
        author = InvestigationAuthor.from_dict(d.pop("author"))

        details = d.pop("details")

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = InvestigationEvidence.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        id = UUID(d.pop("id"))

        investigation_id = UUID(d.pop("investigationId"))

        revision = d.pop("revision")

        updated_at = parse_datetime(d.pop("updatedAt"))

        verdict = AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict(d.pop("verdict"))

        _verdict_proposal_id = d.pop("verdictProposalId", UNSET)
        verdict_proposal_id: UUID | Unset
        if isinstance(_verdict_proposal_id, Unset) or _verdict_proposal_id is None:
            verdict_proposal_id = UNSET
        else:
            verdict_proposal_id = UUID(_verdict_proposal_id)

        verdict_reason = d.pop("verdictReason", UNSET)

        assessment_is_one_participants_current_conclusion_on_a_node = cls(
            author=author,
            details=details,
            evidence=evidence,
            id=id,
            investigation_id=investigation_id,
            revision=revision,
            updated_at=updated_at,
            verdict=verdict,
            verdict_proposal_id=verdict_proposal_id,
            verdict_reason=verdict_reason,
        )

        assessment_is_one_participants_current_conclusion_on_a_node.additional_properties = d
        return assessment_is_one_participants_current_conclusion_on_a_node

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
