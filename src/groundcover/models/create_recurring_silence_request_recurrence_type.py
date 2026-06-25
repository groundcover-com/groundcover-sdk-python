from __future__ import annotations

from enum import Enum


class CreateRecurringSilenceRequestRecurrenceType(str, Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
