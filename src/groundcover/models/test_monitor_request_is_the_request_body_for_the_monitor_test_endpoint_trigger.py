from __future__ import annotations

from enum import Enum


class TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointTrigger(str, Enum):
    ALERTING = "Alerting"
    NORMAL = "Normal"

    def __str__(self) -> str:
        return str(self.value)
