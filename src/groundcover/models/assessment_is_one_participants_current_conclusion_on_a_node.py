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
    from ..models.missing_groundcover_integration import MissingGroundcoverIntegration


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
        missing_groundcover_integrations (list[MissingGroundcoverIntegration] | Unset): Groundcover integrations
            recommended by this assessment.
        verdict_approved_by (InvestigationAuthor | Unset):
        verdict_proposal_id (UUID | Unset): The approved conclusion whose verdict set Verdict.
        verdict_reason (str | Unset):
        verdict_set_at (datetime.datetime | Unset): When that conclusion was approved.
        verdict_set_by (InvestigationAuthor | Unset):
    """

    author: InvestigationAuthor
    details: str
    evidence: list[InvestigationEvidence]
    id: UUID
    investigation_id: UUID
    revision: int
    updated_at: datetime.datetime
    verdict: AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict
    missing_groundcover_integrations: list[MissingGroundcoverIntegration] | Unset = UNSET
    verdict_approved_by: InvestigationAuthor | Unset = UNSET
    verdict_proposal_id: UUID | Unset = UNSET
    verdict_reason: str | Unset = UNSET
    verdict_set_at: datetime.datetime | Unset = UNSET
    verdict_set_by: InvestigationAuthor | Unset = UNSET
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

        missing_groundcover_integrations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing_groundcover_integrations, Unset):
            missing_groundcover_integrations = []
            for missing_groundcover_integrations_item_data in self.missing_groundcover_integrations:
                missing_groundcover_integrations_item = missing_groundcover_integrations_item_data.to_dict()
                missing_groundcover_integrations.append(missing_groundcover_integrations_item)

        verdict_approved_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verdict_approved_by, Unset):
            verdict_approved_by = self.verdict_approved_by.to_dict()

        verdict_proposal_id: str | Unset = UNSET
        if not isinstance(self.verdict_proposal_id, Unset):
            verdict_proposal_id = str(self.verdict_proposal_id)

        verdict_reason = self.verdict_reason

        verdict_set_at: str | Unset = UNSET
        if not isinstance(self.verdict_set_at, Unset):
            verdict_set_at = self.verdict_set_at.isoformat()

        verdict_set_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verdict_set_by, Unset):
            verdict_set_by = self.verdict_set_by.to_dict()

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
        if missing_groundcover_integrations is not UNSET:
            field_dict["missingGroundcoverIntegrations"] = missing_groundcover_integrations
        if verdict_approved_by is not UNSET:
            field_dict["verdictApprovedBy"] = verdict_approved_by
        if verdict_proposal_id is not UNSET:
            field_dict["verdictProposalId"] = verdict_proposal_id
        if verdict_reason is not UNSET:
            field_dict["verdictReason"] = verdict_reason
        if verdict_set_at is not UNSET:
            field_dict["verdictSetAt"] = verdict_set_at
        if verdict_set_by is not UNSET:
            field_dict["verdictSetBy"] = verdict_set_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor
        from ..models.investigation_evidence import InvestigationEvidence
        from ..models.missing_groundcover_integration import MissingGroundcoverIntegration

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

        _missing_groundcover_integrations = d.pop("missingGroundcoverIntegrations", UNSET)
        missing_groundcover_integrations: list[MissingGroundcoverIntegration] | Unset = UNSET
        if _missing_groundcover_integrations is not UNSET:
            missing_groundcover_integrations = []
            for missing_groundcover_integrations_item_data in _missing_groundcover_integrations:
                missing_groundcover_integrations_item = MissingGroundcoverIntegration.from_dict(
                    missing_groundcover_integrations_item_data
                )

                missing_groundcover_integrations.append(missing_groundcover_integrations_item)

        _verdict_approved_by = d.pop("verdictApprovedBy", UNSET)
        verdict_approved_by: InvestigationAuthor | Unset
        if isinstance(_verdict_approved_by, Unset) or _verdict_approved_by is None:
            verdict_approved_by = UNSET
        else:
            verdict_approved_by = InvestigationAuthor.from_dict(_verdict_approved_by)

        _verdict_proposal_id = d.pop("verdictProposalId", UNSET)
        verdict_proposal_id: UUID | Unset
        if isinstance(_verdict_proposal_id, Unset) or _verdict_proposal_id is None:
            verdict_proposal_id = UNSET
        else:
            verdict_proposal_id = UUID(_verdict_proposal_id)

        verdict_reason = d.pop("verdictReason", UNSET)

        _verdict_set_at = d.pop("verdictSetAt", UNSET)
        verdict_set_at: datetime.datetime | Unset
        if isinstance(_verdict_set_at, Unset) or _verdict_set_at is None:
            verdict_set_at = UNSET
        else:
            verdict_set_at = parse_datetime(_verdict_set_at)

        _verdict_set_by = d.pop("verdictSetBy", UNSET)
        verdict_set_by: InvestigationAuthor | Unset
        if isinstance(_verdict_set_by, Unset) or _verdict_set_by is None:
            verdict_set_by = UNSET
        else:
            verdict_set_by = InvestigationAuthor.from_dict(_verdict_set_by)

        assessment_is_one_participants_current_conclusion_on_a_node = cls(
            author=author,
            details=details,
            evidence=evidence,
            id=id,
            investigation_id=investigation_id,
            revision=revision,
            updated_at=updated_at,
            verdict=verdict,
            missing_groundcover_integrations=missing_groundcover_integrations,
            verdict_approved_by=verdict_approved_by,
            verdict_proposal_id=verdict_proposal_id,
            verdict_reason=verdict_reason,
            verdict_set_at=verdict_set_at,
            verdict_set_by=verdict_set_by,
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
