from __future__ import annotations

from enum import Enum


class GoalsSearchRequestIsOnePageOfTheGoalsTabSort(str, Enum):
    TIMESTAMP_DESC = "timestamp_desc"

    def __str__(self) -> str:
        return str(self.value)
