"""Client configuration for the groundcover SDK."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List, Optional

import httpx

from groundcover.exceptions import ConfigurationError

DEFAULT_BASE_URL = "https://api.groundcover.com"
DEFAULT_TIMEOUT = 30.0
DEFAULT_RETRY_COUNT = 3
DEFAULT_MIN_RETRY_WAIT = 1.0
DEFAULT_MAX_RETRY_WAIT = 30.0
DEFAULT_RETRY_STATUSES = [503, 429]


@dataclass
class ClientConfig:
    """Configuration for the groundcover SDK client.

    Reads from environment variables by default:
      - GC_API_KEY: API key for authentication (required)
      - GC_BACKEND_ID: Backend ID (required)
      - GC_BASE_URL: Base URL (optional, defaults to https://api.groundcover.com)
      - GC_TRACEPARENT: Default traceparent header (optional)

    Keyword arguments override environment variables.
    """

    api_key: Optional[str] = None
    backend_id: Optional[str] = None
    base_url: Optional[str] = None
    timeout: float = DEFAULT_TIMEOUT
    retry_count: int = DEFAULT_RETRY_COUNT
    min_retry_wait: float = DEFAULT_MIN_RETRY_WAIT
    max_retry_wait: float = DEFAULT_MAX_RETRY_WAIT
    retry_statuses: List[int] = field(default_factory=lambda: list(DEFAULT_RETRY_STATUSES))
    traceparent: Optional[str] = None
    http_transport: Optional[httpx.BaseTransport] = None
    async_http_transport: Optional[httpx.AsyncBaseTransport] = None

    def __post_init__(self) -> None:
        # Environment variable fallbacks
        if self.api_key is None:
            self.api_key = os.environ.get("GC_API_KEY")
        if self.backend_id is None:
            self.backend_id = os.environ.get("GC_BACKEND_ID")
        if self.base_url is None:
            self.base_url = os.environ.get("GC_BASE_URL", DEFAULT_BASE_URL)
        if self.traceparent is None:
            self.traceparent = os.environ.get("GC_TRACEPARENT")

    def validate(self) -> None:
        """Validate that all required configuration is present."""
        if not self.api_key:
            raise ConfigurationError("API key is required: set GC_API_KEY environment variable or pass api_key=")
        if not self.backend_id:
            raise ConfigurationError(
                "Backend ID is required: set GC_BACKEND_ID environment variable or pass backend_id="
            )

    @property
    def effective_base_url(self) -> str:
        """Return the normalized base URL."""
        url = self.base_url or DEFAULT_BASE_URL
        return _normalize_base_url(url)


def _normalize_base_url(base_url: str) -> str:
    """Normalize a base URL to ensure it has a valid scheme."""
    if not base_url:
        return ""

    # Handle protocol-relative URLs
    if base_url.startswith("//"):
        return "https:" + base_url

    # Handle relative paths starting with /
    if base_url.startswith("/") and not base_url.startswith("//"):
        return "https://" + base_url.lstrip("/")

    # Handle URLs without scheme
    if "://" not in base_url:
        return "https://" + base_url

    return base_url
