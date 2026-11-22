from __future__ import annotations

from enum import Enum


class ListMigrationIssuesAssetType(str, Enum):
    DASHBOARDS = "dashboards"
    MONITORS = "monitors"

    def __str__(self) -> str:
        return str(self.value)
