from __future__ import annotations

from enum import Enum


class AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict(str, Enum):
    ACCEPTED = "accepted"
    OPEN = "open"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
