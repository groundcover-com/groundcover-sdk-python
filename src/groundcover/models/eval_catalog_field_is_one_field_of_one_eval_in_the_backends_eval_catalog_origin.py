from __future__ import annotations

from enum import Enum


class EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogOrigin(str, Enum):
    BUILT_IN = "built_in"
    USER_CREATED = "user_created"

    def __str__(self) -> str:
        return str(self.value)
