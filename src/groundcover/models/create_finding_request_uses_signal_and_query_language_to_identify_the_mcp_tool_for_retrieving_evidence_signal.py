from __future__ import annotations

from enum import Enum


class CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceSignal(str, Enum):
    DB_MEASUREMENTS = "db_measurements"
    ENTITIES = "entities"
    EVENTS = "events"
    ISSUES = "issues"
    K8S = "k8s"
    LINK = "link"
    LOGS = "logs"
    METRICS = "metrics"
    MONITORS = "monitors"
    OTHER = "other"
    PROFILING = "profiling"
    RUM = "rum"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)
