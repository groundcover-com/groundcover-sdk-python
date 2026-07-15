from __future__ import annotations

from enum import Enum


class SearchValuesRequestType(str, Enum):
    APM = "apm"
    AWS_CUR = "aws_cur"
    ENTITIES = "entities"
    EVENTS = "events"
    INGESTION_MEASUREMENTS = "ingestion_measurements"
    ISSUES = "issues"
    LOGS = "logs"
    MONITORS = "monitors"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)
