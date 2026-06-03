from __future__ import annotations

from enum import Enum


class GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortBy(str, Enum):
    CLUSTER = "cluster"
    COUNT = "count"
    FIRSTSEEN = "firstSeen"
    INSTANCE = "instance"
    LASTSEEN = "lastSeen"
    NAMESPACE = "namespace"
    OBJECT_KIND = "object_kind"
    REASON = "reason"
    TIMESTAMP = "timestamp"
    TYPE = "type"
    WORKLOAD = "workload"

    def __str__(self) -> str:
        return str(self.value)
