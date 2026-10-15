from __future__ import annotations

from enum import Enum


class EvidenceRequestRelation(str, Enum):
    CONTRADICTS = "contradicts"
    SUPPORTS = "supports"

    def __str__(self) -> str:
        return str(self.value)
