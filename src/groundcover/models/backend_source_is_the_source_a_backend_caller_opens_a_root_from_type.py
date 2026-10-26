from __future__ import annotations

from enum import Enum


class BackendSourceIsTheSourceABackendCallerOpensARootFromType(str, Enum):
    AUTOMATION = "automation"

    def __str__(self) -> str:
        return str(self.value)
