from __future__ import annotations

from enum import Enum


class CustomResolveThresholdDefinesAHysteresisRecoveryConditionForAThresholdOperator(str, Enum):
    GT = "gt"
    LT = "lt"
    OUTSIDE_RANGE = "outside_range"
    WITHIN_RANGE = "within_range"

    def __str__(self) -> str:
        return str(self.value)
