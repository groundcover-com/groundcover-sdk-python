from __future__ import annotations

from enum import Enum


class GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeType(str, Enum):
    CURSOR_EXPIRED = "cursor_expired"
    CURSOR_INVALID = "cursor_invalid"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
