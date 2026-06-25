from __future__ import annotations

from enum import Enum


class V2CreateSilenceRequestRecurrenceType(str, Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
