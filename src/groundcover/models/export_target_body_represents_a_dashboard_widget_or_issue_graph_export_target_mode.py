from __future__ import annotations

from enum import Enum


class ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetMode(str, Enum):
    DEFAULT = "default"
    WORKLOAD = "workload"

    def __str__(self) -> str:
        return str(self.value)
