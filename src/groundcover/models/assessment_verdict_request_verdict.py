from __future__ import annotations

from enum import Enum


class AssessmentVerdictRequestVerdict(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"

    def __str__(self) -> str:
        return str(self.value)
