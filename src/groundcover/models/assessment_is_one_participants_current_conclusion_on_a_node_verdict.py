from __future__ import annotations

from enum import Enum


class AssessmentIsOneParticipantsCurrentConclusionOnANodeVerdict(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
