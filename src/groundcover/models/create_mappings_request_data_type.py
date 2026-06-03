from __future__ import annotations

from enum import Enum


class CreateMappingsRequestDataType(str, Enum):
    EVENTS = "events"
    LOGS = "logs"
    METRICS = "metrics"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)
