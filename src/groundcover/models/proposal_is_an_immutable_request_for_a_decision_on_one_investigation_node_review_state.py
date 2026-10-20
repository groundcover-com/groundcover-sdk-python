from __future__ import annotations

from enum import Enum


class ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeReviewState(str, Enum):
    DEFERRED = "deferred"
    QUEUED = "queued"
    REVIEWING = "reviewing"

    def __str__(self) -> str:
        return str(self.value)
