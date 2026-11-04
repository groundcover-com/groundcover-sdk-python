from __future__ import annotations

from enum import Enum


class InvestigationBackendSourceType(str, Enum):
    AUTOMATION = "automation"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
