from __future__ import annotations

from enum import Enum


class InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus(str, Enum):
    ANSWERED = "answered"
    OPEN = "open"
    REFUTED = "refuted"
    STOPPED = "stopped"
    SUPPORTED = "supported"

    def __str__(self) -> str:
        return str(self.value)
