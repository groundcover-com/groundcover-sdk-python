from __future__ import annotations

from enum import Enum


class SearchValuesRequestType(str, Enum):
    APM = "apm"
    ENTITIES = "entities"
    EVENTS = "events"
    ISSUES = "issues"
    LOGS = "logs"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)
