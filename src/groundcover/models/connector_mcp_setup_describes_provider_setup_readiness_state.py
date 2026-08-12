from __future__ import annotations

from enum import Enum


class ConnectorMCPSetupDescribesProviderSetupReadinessState(str, Enum):
    READY = "ready"
    UPDATE_REQUIRED = "update_required"

    def __str__(self) -> str:
        return str(self.value)
