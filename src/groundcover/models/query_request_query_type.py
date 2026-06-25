from __future__ import annotations

from enum import Enum


class QueryRequestQueryType(str, Enum):
    INSTANT = "instant"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
