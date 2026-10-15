from __future__ import annotations

from enum import Enum


class ProposalChildDescribesANodeToCreateIfTheProposalIsApprovedKind(str, Enum):
    HYPOTHESIS = "hypothesis"
    QUESTION = "question"

    def __str__(self) -> str:
        return str(self.value)
