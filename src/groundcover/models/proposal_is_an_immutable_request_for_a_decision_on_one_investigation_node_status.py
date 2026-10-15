from __future__ import annotations

from enum import Enum


class ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNodeStatus(str, Enum):
    APPROVED = "approved"
    PENDING = "pending"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"

    def __str__(self) -> str:
        return str(self.value)
