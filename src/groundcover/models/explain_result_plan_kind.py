from __future__ import annotations

from enum import Enum


class ExplainResultPlanKind(str, Enum):
    CUSTOM = "custom"
    GENERIC = "generic"

    def __str__(self) -> str:
        return str(self.value)
