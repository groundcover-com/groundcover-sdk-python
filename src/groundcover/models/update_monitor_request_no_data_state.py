from __future__ import annotations

from enum import Enum


class UpdateMonitorRequestNoDataState(str, Enum):
    ALERTING = "Alerting"
    NODATA = "NoData"
    OK = "OK"

    def __str__(self) -> str:
        return str(self.value)
