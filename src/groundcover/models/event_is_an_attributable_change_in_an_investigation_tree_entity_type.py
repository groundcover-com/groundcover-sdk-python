from __future__ import annotations

from enum import Enum


class EventIsAnAttributableChangeInAnInvestigationTreeEntityType(str, Enum):
    ASSESSMENT = "assessment"
    FINDING = "finding"
    INVESTIGATION = "investigation"
    PARTICIPANT = "participant"
    PROPOSAL = "proposal"
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
