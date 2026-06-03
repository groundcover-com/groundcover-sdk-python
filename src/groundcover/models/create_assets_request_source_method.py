from __future__ import annotations

from enum import Enum


class CreateAssetsRequestSourceMethod(str, Enum):
    API = "api"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
