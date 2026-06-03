from __future__ import annotations

from enum import Enum


class SearchRequestExtendsTheMonitorModelWithOptionalAbsoluteTimeBoundsMeasurementType(str, Enum):
    EVENT = "event"
    STATE = "state"

    def __str__(self) -> str:
        return str(self.value)
