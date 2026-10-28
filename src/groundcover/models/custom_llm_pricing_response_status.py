from __future__ import annotations

from enum import Enum


class CustomLLMPricingResponseStatus(str, Enum):
    ACTIVE = "active"
    APPLYING = "applying"

    def __str__(self) -> str:
        return str(self.value)
