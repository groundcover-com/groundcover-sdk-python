from __future__ import annotations

from enum import Enum


class CreateMonitorRequestMeasurementType(str, Enum):
    EVENT = "event"
    STATE = "state"

    def __str__(self) -> str:
        return str(self.value)
