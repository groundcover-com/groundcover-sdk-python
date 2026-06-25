from __future__ import annotations

from enum import Enum


class SearchRequestExtendsTheMonitorModelWithOptionalAbsoluteTimeBoundsExecutionErrorState(str, Enum):
    ALERTING = "Alerting"
    ERROR = "Error"
    OK = "OK"

    def __str__(self) -> str:
        return str(self.value)
