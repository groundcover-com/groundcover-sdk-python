from __future__ import annotations

from enum import Enum


class ExportAuthBodyRepresentsTheAuthModeSentToExportServiceType(str, Enum):
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
