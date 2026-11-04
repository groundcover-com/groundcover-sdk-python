from __future__ import annotations

from enum import Enum


class EventIsAnAttributableChangeInAnInvestigationTreeEntityType(str, Enum):
    ASSESSMENT = "assessment"
    FINDING = "finding"
    INVESTIGATION = "investigation"
    INVESTIGATOR = "investigator"
    MODERATOR = "moderator"
    PARTICIPANT = "participant"
    PROPOSAL = "proposal"
    SYNC_TARGET = "sync_target"

    def __str__(self) -> str:
        return str(self.value)
