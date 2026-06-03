from __future__ import annotations

from enum import Enum


class MigrationDataSourceItemStatus(str, Enum):
    ACTIVE = "active"
    PARTIAL = "partial"
    TODO = "todo"

    def __str__(self) -> str:
        return str(self.value)
