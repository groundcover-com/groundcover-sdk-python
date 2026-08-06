from __future__ import annotations

from enum import Enum


class ExportServiceDrainingResponseBodyError(str, Enum):
    EXPORT_SERVICE_DRAINING = "EXPORT_SERVICE_DRAINING"

    def __str__(self) -> str:
        return str(self.value)
