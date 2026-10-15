from __future__ import annotations

from enum import Enum


class InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsedCode(str, Enum):
    FINDING_RETRACTED = "FINDING_RETRACTED"
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
