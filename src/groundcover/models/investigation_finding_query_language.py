from __future__ import annotations

from enum import Enum


class InvestigationFindingQueryLanguage(str, Enum):
    GCQL = "gcql"
    METRICSQL = "metricsql"

    def __str__(self) -> str:
        return str(self.value)
