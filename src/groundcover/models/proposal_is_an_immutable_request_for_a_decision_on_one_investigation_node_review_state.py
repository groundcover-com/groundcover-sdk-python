from __future__ import annotations

from enum import Enum


class ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState(str, Enum):
    DEFERRED = "deferred"
    NEEDS_PERSON = "needs_person"
    QUEUED = "queued"
    REVIEWING = "reviewing"

    def __str__(self) -> str:
        return str(self.value)
