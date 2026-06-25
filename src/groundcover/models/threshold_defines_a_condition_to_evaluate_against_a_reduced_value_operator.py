from __future__ import annotations

from enum import Enum


class ThresholdDefinesAConditionToEvaluateAgainstAReducedValueOperator(str, Enum):
    GT = "gt"
    VALUE_1 = " lt"
    VALUE_2 = " gte"
    VALUE_3 = " lte"
    VALUE_4 = " eq"
    VALUE_5 = " neq"
    VALUE_6 = " within_range"
    VALUE_7 = " outside_range"
    VALUE_8 = " within_range_included"
    VALUE_9 = " outside_range_included"

    def __str__(self) -> str:
        return str(self.value)
