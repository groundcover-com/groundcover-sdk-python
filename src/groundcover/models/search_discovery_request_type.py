from __future__ import annotations

from enum import Enum


class SearchDiscoveryRequestType(str, Enum):
    APM = "apm"
    DASHBOARDS = "dashboards"
    ENTITIES = "entities"
    EVENTS = "events"
    ISSUES = "issues"
    LOGS = "logs"
    MONITORS = "monitors"
    RUM_EVENTS = "rum_events"
    RUM_SESSIONS = "rum_sessions"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)
