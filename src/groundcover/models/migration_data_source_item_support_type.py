from __future__ import annotations

from enum import Enum


class MigrationDataSourceItemSupportType(str, Enum):
    NOT_SUPPORTED = "not_supported"
    SUPPORTED = "supported"

    def __str__(self) -> str:
        return str(self.value)
