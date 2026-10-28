from __future__ import annotations

from enum import Enum


class InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesItStatus(str, Enum):
    FAILED = "failed"
    PENDING = "pending"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
