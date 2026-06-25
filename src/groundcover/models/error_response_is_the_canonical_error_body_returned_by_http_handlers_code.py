from __future__ import annotations

from enum import Enum


class ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlersCode(str, Enum):
    EXCEEDED_MAX_ROWS_TO_GROUP_BY = "EXCEEDED_MAX_ROWS_TO_GROUP_BY"
    MONITOR_DUPLICATE_TITLE = "MONITOR_DUPLICATE_TITLE"
    MONITOR_EVAL_FAILED = "MONITOR_EVAL_FAILED"
    MONITOR_VALIDATION_FAILED = "MONITOR_VALIDATION_FAILED"

    def __str__(self) -> str:
        return str(self.value)
