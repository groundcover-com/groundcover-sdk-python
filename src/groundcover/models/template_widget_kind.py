from __future__ import annotations

from enum import Enum


class TemplateWidgetKind(str, Enum):
    BAR = "bar"
    PIE = "pie"
    STAT = "stat"
    TABLE = "table"
    TIME_SERIES = "time-series"
    TOP_LIST = "top-list"
    TREEMAP = "treemap"

    def __str__(self) -> str:
        return str(self.value)
