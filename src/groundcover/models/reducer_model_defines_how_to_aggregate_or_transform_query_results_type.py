from __future__ import annotations

from enum import Enum


class ReducerModelDefinesHowToAggregateOrTransformQueryResultsType(str, Enum):
    COUNT = "count"
    LAST = "last"
    MATH = "math"
    MAX = "max"
    MEAN = "mean"
    MIN = "min"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
