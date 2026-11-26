from __future__ import annotations

from enum import Enum


class EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogType(str, Enum):
    BOOLEAN = "boolean"
    ENUM = "enum"
    FLOAT = "float"
    INTEGER = "integer"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
