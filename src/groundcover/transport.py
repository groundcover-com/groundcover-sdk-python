"""Custom httpx transport for the groundcover SDK.

Handles auth headers, content-type fixes, and retry logic.
"""

from __future__ import annotations

import re
from typing import Optional

import httpx
from tenacity import (
    RetryError,
    retry,
    retry_if_result,
    stop_after_attempt,
    wait_exponential_jitter,
)

from groundcover.config import ClientConfig

HEADER_AUTHORIZATION = "Authorization"
HEADER_BACKEND_ID = "X-Backend-Id"
HEADER_USER_AGENT = "User-Agent"
HEADER_TRACEPARENT = "traceparent"
USER_AGENT = "groundcover-python-sdk"
YAML_CONTENT_TYPE = "application/x-yaml"

# Matches /api/monitors/{id} but not /api/monitors/silences or /api/monitors/list etc.
_GET_MONITOR_PATH_RE = re.compile(r"^/api/monitors/[^/]+/?$")
_MONITOR_NON_ID_SEGMENTS = {"silences", "list", "recurring-silences"}


def _is_monitor_get_path(path: str) -> bool:
    """Check if path is a single-monitor GET (not list/silences)."""
    if not _GET_MONITOR_PATH_RE.match(path):
        return False
    segment = path.rstrip("/").rsplit("/", 1)[-1]
    return segment not in _MONITOR_NON_ID_SEGMENTS


class GroundcoverTransport(httpx.BaseTransport):
    """Sync HTTP transport that injects auth headers, fixes content-types, and retries.

    Request lifecycle:
    1. Inject Authorization: Bearer {api_key}
    2. Inject X-Backend-Id: {backend_id}
    3. Inject User-Agent: groundcover-python-sdk
    4. Inject optional traceparent header
    5. Fix Content-Type to text/plain for POST /api/workflows/create
    6. Fix response Content-Type to application/x-yaml for GET /api/monitors/{id}
    7. Retry on configured status codes with exponential backoff + jitter
    """

    def __init__(self, config: ClientConfig) -> None:
        self._config = config
        self._inner = config.http_transport or httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self._inject_headers(request)
        self._fix_request_content_type(request)

        response = self._send_with_retry(request)

        self._fix_response_content_type(request, response)
        return response

    def close(self) -> None:
        self._inner.close()

    def _inject_headers(self, request: httpx.Request) -> None:
        request.headers[HEADER_AUTHORIZATION] = f"Bearer {self._config.api_key}"
        request.headers[HEADER_BACKEND_ID] = self._config.backend_id or ""
        request.headers[HEADER_USER_AGENT] = USER_AGENT

        # Per-request traceparent override via request extensions
        traceparent = request.extensions.get("traceparent")
        if isinstance(traceparent, str):
            request.headers[HEADER_TRACEPARENT] = traceparent
        elif self._config.traceparent:
            request.headers[HEADER_TRACEPARENT] = self._config.traceparent

    def _fix_request_content_type(self, request: httpx.Request) -> None:
        path = request.url.raw_path.decode("ascii", errors="ignore").rstrip("/")
        if request.method == "POST" and path == "/api/workflows/create":
            request.headers["Content-Type"] = "text/plain"

    def _fix_response_content_type(self, request: httpx.Request, response: httpx.Response) -> None:
        path = request.url.raw_path.decode("ascii", errors="ignore")
        if request.method == "GET" and response.status_code == 200 and _is_monitor_get_path(path):
            content_type = response.headers.get("content-type", "")
            if not content_type or not content_type.startswith(YAML_CONTENT_TYPE):
                response.headers["content-type"] = YAML_CONTENT_TYPE

    def _send_with_retry(self, request: httpx.Request) -> httpx.Response:
        retry_statuses = set(self._config.retry_statuses)

        @retry(
            stop=stop_after_attempt(1 + self._config.retry_count),
            wait=wait_exponential_jitter(
                initial=self._config.min_retry_wait,
                max=self._config.max_retry_wait,
            ),
            retry=retry_if_result(lambda resp: resp.status_code in retry_statuses),
            reraise=True,
        )
        def _do_send() -> httpx.Response:
            return self._inner.handle_request(request)

        try:
            return _do_send()
        except RetryError as e:
            # When all retries exhausted due to retry_if_result, return the last response
            if e.last_attempt.failed:
                raise e.last_attempt.result()
            return e.last_attempt.result()


class AsyncGroundcoverTransport(httpx.AsyncBaseTransport):
    """Async HTTP transport with the same behavior as GroundcoverTransport."""

    def __init__(self, config: ClientConfig) -> None:
        self._config = config
        self._inner = config.async_http_transport or httpx.AsyncHTTPTransport()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self._inject_headers(request)
        self._fix_request_content_type(request)

        response = await self._send_with_retry(request)

        self._fix_response_content_type(request, response)
        return response

    async def aclose(self) -> None:
        await self._inner.aclose()

    def _inject_headers(self, request: httpx.Request) -> None:
        request.headers[HEADER_AUTHORIZATION] = f"Bearer {self._config.api_key}"
        request.headers[HEADER_BACKEND_ID] = self._config.backend_id or ""
        request.headers[HEADER_USER_AGENT] = USER_AGENT

        traceparent = request.extensions.get("traceparent")
        if isinstance(traceparent, str):
            request.headers[HEADER_TRACEPARENT] = traceparent
        elif self._config.traceparent:
            request.headers[HEADER_TRACEPARENT] = self._config.traceparent

    def _fix_request_content_type(self, request: httpx.Request) -> None:
        path = request.url.raw_path.decode("ascii", errors="ignore").rstrip("/")
        if request.method == "POST" and path == "/api/workflows/create":
            request.headers["Content-Type"] = "text/plain"

    def _fix_response_content_type(self, request: httpx.Request, response: httpx.Response) -> None:
        path = request.url.raw_path.decode("ascii", errors="ignore")
        if request.method == "GET" and response.status_code == 200 and _is_monitor_get_path(path):
            content_type = response.headers.get("content-type", "")
            if not content_type or not content_type.startswith(YAML_CONTENT_TYPE):
                response.headers["content-type"] = YAML_CONTENT_TYPE

    async def _send_with_retry(self, request: httpx.Request) -> httpx.Response:
        retry_statuses = set(self._config.retry_statuses)
        max_attempts = 1 + self._config.retry_count
        last_response: Optional[httpx.Response] = None

        from tenacity import AsyncRetrying

        try:
            async for attempt in AsyncRetrying(
                stop=stop_after_attempt(max_attempts),
                wait=wait_exponential_jitter(
                    initial=self._config.min_retry_wait,
                    max=self._config.max_retry_wait,
                ),
                retry=retry_if_result(lambda resp: resp.status_code in retry_statuses),
                reraise=True,
            ):
                with attempt:
                    last_response = await self._inner.handle_async_request(request)
                attempt.retry_state.set_result(last_response)
        except RetryError as e:
            if e.last_attempt.failed:
                raise e.last_attempt.result()
            return e.last_attempt.result()

        assert last_response is not None
        return last_response
