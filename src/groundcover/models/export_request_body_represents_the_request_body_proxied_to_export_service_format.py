from __future__ import annotations

from enum import Enum


class ExportRequestBodyRepresentsTheRequestBodyProxiedToExportServiceFormat(str, Enum):
    PDF = "pdf"
    PNG = "png"

    def __str__(self) -> str:
        return str(self.value)
