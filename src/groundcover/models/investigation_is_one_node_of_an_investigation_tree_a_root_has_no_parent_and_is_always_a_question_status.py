from __future__ import annotations

from enum import Enum


class InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus(str, Enum):
    OPEN = "open"
    REFUTED = "refuted"
    RESOLVED = "resolved"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
