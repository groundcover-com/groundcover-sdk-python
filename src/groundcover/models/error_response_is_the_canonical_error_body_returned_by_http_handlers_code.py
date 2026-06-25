from __future__ import annotations

from enum import Enum


class ErrorResponseIsTheCanonicalErrorBodyReturnedByHTTPHandlersCode(str, Enum):
    EXCEEDED_MAX_ROWS_TO_GROUP_BY = "EXCEEDED_MAX_ROWS_TO_GROUP_BY"

    def __str__(self) -> str:
        return str(self.value)
