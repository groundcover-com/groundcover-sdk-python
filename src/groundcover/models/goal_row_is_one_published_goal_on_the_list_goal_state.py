from __future__ import annotations

from enum import Enum


class GoalRowIsOnePublishedGoalOnTheListGoalState(str, Enum):
    COMPLETE = "complete"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
