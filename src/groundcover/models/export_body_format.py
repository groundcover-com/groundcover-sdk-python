from __future__ import annotations

from enum import Enum


class ExportBodyFormat(str, Enum):
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
