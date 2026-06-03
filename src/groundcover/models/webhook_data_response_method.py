from __future__ import annotations

from enum import Enum


class WebhookDataResponseMethod(str, Enum):
    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
