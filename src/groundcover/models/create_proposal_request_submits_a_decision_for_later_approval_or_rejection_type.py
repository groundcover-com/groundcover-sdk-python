from __future__ import annotations

from enum import Enum


class CreateProposalRequestSubmitsADecisionForLaterApprovalOrRejectionType(str, Enum):
    CREATE_CHILD = "create_child"
    REFUTE = "refute"
    RESOLVE = "resolve"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
