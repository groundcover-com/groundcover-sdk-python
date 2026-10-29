from __future__ import annotations

from enum import Enum


class EventIsAnAttributableChangeInAnInvestigationTreeType(str, Enum):
    ASSESSMENT_JUDGED = "assessment.judged"
    ASSESSMENT_UPDATED = "assessment.updated"
    FINDING_CREATED = "finding.created"
    FINDING_RETRACTED = "finding.retracted"
    INVESTIGATION_CLOSED = "investigation.closed"
    INVESTIGATION_OPENED = "investigation.opened"
    INVESTIGATOR_RUN_REJECTED = "investigator.run_rejected"
    INVESTIGATOR_RUN_REQUESTED = "investigator.run_requested"
    MODERATOR_RUN_LIMIT_REACHED = "moderator.run_limit_reached"
    MODERATOR_RUN_REJECTED = "moderator.run_rejected"
    PARTICIPANT_JOINED = "participant.joined"
    PROPOSAL_APPROVED = "proposal.approved"
    PROPOSAL_CREATED = "proposal.created"
    PROPOSAL_DEFERRED = "proposal.deferred"
    PROPOSAL_REJECTED = "proposal.rejected"
    PROPOSAL_SUPERSEDED = "proposal.superseded"

    def __str__(self) -> str:
        return str(self.value)
