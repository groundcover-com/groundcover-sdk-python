from __future__ import annotations

from enum import Enum


class AssetInstallResultStatus(str, Enum):
    ALREADY_INSTALLED = "already_installed"
    FAILED = "failed"
    INSTALLED = "installed"
    NOT_CONVERTIBLE = "not_convertible"
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)
