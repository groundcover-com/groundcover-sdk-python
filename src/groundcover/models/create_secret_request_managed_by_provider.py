from __future__ import annotations

from enum import Enum


class CreateSecretRequestManagedByProvider(str, Enum):
    NONE = "none"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
