from __future__ import annotations

from enum import Enum


class GoalEvalResultState(str, Enum):
    COMPLETE = "complete"
    DISABLED = "disabled"
    EXHAUSTED = "exhausted"
    FAILED = "failed"
    OUTDATED = "outdated"
    PENDING = "pending"
    SKIPPED = "skipped"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
