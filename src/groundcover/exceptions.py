"""Exception hierarchy for the groundcover SDK."""

from __future__ import annotations

import httpx


class GroundcoverError(Exception):
    """Base exception for all groundcover SDK errors."""


class ConfigurationError(GroundcoverError):
    """Raised when required configuration is missing or invalid."""


class APIError(GroundcoverError):
    """Raised when the API returns an error response."""

    def __init__(self, status_code: int, body: str, message: str = "") -> None:
        self.status_code = status_code
        self.body = body
        msg = message or f"API error {status_code}"
        if body:
            msg = f"{msg}: {body}"
        super().__init__(msg)


class AuthenticationError(APIError):
    """Raised on 401 Unauthorized responses."""

    def __init__(self, body: str = "") -> None:
        super().__init__(401, body, "Authentication failed")


class ForbiddenError(APIError):
    """Raised on 403 Forbidden responses."""

    def __init__(self, body: str = "") -> None:
        super().__init__(403, body, "Forbidden")


class NotFoundError(APIError):
    """Raised on 404 Not Found responses."""

    def __init__(self, body: str = "") -> None:
        super().__init__(404, body, "Not found")


class ConflictError(APIError):
    """Raised on 409 Conflict responses."""

    def __init__(self, body: str = "") -> None:
        super().__init__(409, body, "Conflict")


class RateLimitError(APIError):
    """Raised on 429 Too Many Requests responses."""

    def __init__(self, body: str = "") -> None:
        super().__init__(429, body, "Rate limit exceeded")


_STATUS_TO_EXCEPTION: dict[int, type[APIError]] = {
    401: AuthenticationError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    429: RateLimitError,
}


def raise_for_status(status_code: int, body: str) -> None:
    """Raise an appropriate exception for an error HTTP status code."""
    if status_code < 400:
        return
    exc_class = _STATUS_TO_EXCEPTION.get(status_code, APIError)
    if exc_class is APIError:
        raise APIError(status_code, body)
    raise exc_class(body)


def error_response_hook(response: httpx.Response) -> None:
    """httpx response event hook that raises on error status codes.

    Safe to use with both sync and async httpx clients.
    ``response.read()`` is idempotent — the body is already buffered for
    non-streaming requests by the time event hooks fire.
    """
    response.read()
    raise_for_status(response.status_code, response.text)
