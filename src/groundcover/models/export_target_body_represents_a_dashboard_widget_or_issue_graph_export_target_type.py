from __future__ import annotations

from enum import Enum


class ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetType(str, Enum):
    DASHBOARD = "dashboard"
    ISSUEGRAPH = "issueGraph"
    WIDGET = "widget"

    def __str__(self) -> str:
        return str(self.value)
