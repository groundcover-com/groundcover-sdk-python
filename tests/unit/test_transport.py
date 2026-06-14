"""Tests for groundcover.transport.

HIGH PRIORITY: These tests verify the most critical integration points:
- Auth header injection
- Monitor YAML content-type fix
- Workflow text/plain content-type fix
- Retry behavior
"""

from __future__ import annotations

import httpx
import pytest
import respx

from groundcover.config import ClientConfig
from groundcover.transport import (
    HEADER_AUTHORIZATION,
    HEADER_BACKEND_ID,
    HEADER_TRACEPARENT,
    HEADER_USER_AGENT,
    USER_AGENT,
    YAML_CONTENT_TYPE,
    GroundcoverTransport,
    _is_monitor_get_path,
)


@pytest.fixture
def config() -> ClientConfig:
    return ClientConfig(
        api_key="test-api-key",
        backend_id="test-backend",
        base_url="https://api.test.com",
        retry_count=0,  # Disable retries for most tests
    )


@pytest.fixture
def config_with_traceparent() -> ClientConfig:
    return ClientConfig(
        api_key="test-api-key",
        backend_id="test-backend",
        base_url="https://api.test.com",
        traceparent="00-defaulttrace-defaultspan-01",
        retry_count=0,
    )


class TestIsMonitorGetPath:
    def test_monitor_id_path(self) -> None:
        assert _is_monitor_get_path("/api/monitors/abc123") is True

    def test_monitor_id_path_trailing_slash(self) -> None:
        assert _is_monitor_get_path("/api/monitors/abc123/") is True

    def test_monitor_silences_path(self) -> None:
        assert _is_monitor_get_path("/api/monitors/silences") is False

    def test_monitor_list_path(self) -> None:
        assert _is_monitor_get_path("/api/monitors/list") is False

    def test_monitor_recurring_silences_path(self) -> None:
        assert _is_monitor_get_path("/api/monitors/recurring-silences") is False

    def test_monitors_root(self) -> None:
        # /api/monitors doesn't match the regex (no id segment)
        assert _is_monitor_get_path("/api/monitors") is False

    def test_monitor_subresource(self) -> None:
        # /api/monitors/abc123/something has too many segments
        assert _is_monitor_get_path("/api/monitors/abc123/something") is False


class TestGroundcoverTransport:
    @respx.mock
    def test_auth_headers_injected(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        config.http_transport = None  # Use respx mock

        respx.get("https://api.test.com/api/dashboards").respond(200, json={"ok": True})

        client = httpx.Client(base_url="https://api.test.com", transport=transport)
        try:
            # We need to use respx differently - mock at the transport level
            # For simplicity, test header injection by examining what the transport does
            request = httpx.Request("GET", "https://api.test.com/api/dashboards")
            transport._inject_headers(request)

            assert request.headers[HEADER_AUTHORIZATION] == "Bearer test-api-key"
            assert request.headers[HEADER_BACKEND_ID] == "test-backend"
            assert request.headers[HEADER_USER_AGENT] == USER_AGENT
        finally:
            client.close()

    def test_traceparent_from_config(self, config_with_traceparent: ClientConfig) -> None:
        transport = GroundcoverTransport(config_with_traceparent)
        request = httpx.Request("GET", "https://api.test.com/api/dashboards")
        transport._inject_headers(request)

        assert request.headers[HEADER_TRACEPARENT] == "00-defaulttrace-defaultspan-01"

    def test_traceparent_per_request_override(self, config_with_traceparent: ClientConfig) -> None:
        transport = GroundcoverTransport(config_with_traceparent)
        request = httpx.Request(
            "GET",
            "https://api.test.com/api/dashboards",
            extensions={"traceparent": "00-customtrace-customspan-01"},
        )
        transport._inject_headers(request)

        assert request.headers[HEADER_TRACEPARENT] == "00-customtrace-customspan-01"

    def test_no_traceparent_when_not_configured(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/dashboards")
        transport._inject_headers(request)

        assert HEADER_TRACEPARENT not in request.headers

    def test_workflow_content_type_fix(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request(
            "POST",
            "https://api.test.com/api/workflows/create",
            content=b"workflow body",
        )
        transport._fix_request_content_type(request)

        assert request.headers["Content-Type"] == "text/plain"

    def test_workflow_content_type_not_applied_to_other_paths(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request(
            "POST",
            "https://api.test.com/api/dashboards",
            json={"name": "test"},
        )
        original_ct = request.headers.get("Content-Type", "")
        transport._fix_request_content_type(request)

        # Content-Type should not be changed
        assert request.headers.get("Content-Type", "") == original_ct

    def test_monitor_response_content_type_fix(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/monitors/abc123")
        response = httpx.Response(200, headers={"content-type": "text/html"})

        transport._fix_response_content_type(request, response)
        assert response.headers["content-type"] == YAML_CONTENT_TYPE

    def test_monitor_response_content_type_preserves_yaml(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/monitors/abc123")
        response = httpx.Response(200, headers={"content-type": "application/x-yaml; charset=utf-8"})

        transport._fix_response_content_type(request, response)
        assert response.headers["content-type"] == "application/x-yaml; charset=utf-8"

    def test_monitor_response_content_type_not_applied_to_silences(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/monitors/silences")
        response = httpx.Response(200, headers={"content-type": "application/json"})

        transport._fix_response_content_type(request, response)
        assert response.headers["content-type"] == "application/json"

    def test_monitor_response_content_type_not_applied_to_non_200(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/monitors/abc123")
        response = httpx.Response(404, headers={"content-type": "application/json"})

        transport._fix_response_content_type(request, response)
        assert response.headers["content-type"] == "application/json"

    def test_monitor_response_content_type_not_applied_to_post(self, config: ClientConfig) -> None:
        transport = GroundcoverTransport(config)
        request = httpx.Request("POST", "https://api.test.com/api/monitors/abc123")
        response = httpx.Response(200, headers={"content-type": "application/json"})

        transport._fix_response_content_type(request, response)
        assert response.headers["content-type"] == "application/json"


class TestRetry:
    def test_retry_on_503(self) -> None:
        """Test that requests are retried on 503 status codes."""
        call_count = 0

        class CountingTransport(httpx.BaseTransport):
            def handle_request(self, request: httpx.Request) -> httpx.Response:
                nonlocal call_count
                call_count += 1
                if call_count < 3:
                    return httpx.Response(503, text="Service Unavailable")
                return httpx.Response(200, text="OK")

        config = ClientConfig(
            api_key="test-key",
            backend_id="test-backend",
            base_url="https://api.test.com",
            retry_count=3,
            min_retry_wait=0.01,
            max_retry_wait=0.02,
            http_transport=CountingTransport(),
        )
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/dashboards")
        response = transport.handle_request(request)

        assert response.status_code == 200
        assert call_count == 3

    def test_retry_on_429(self) -> None:
        """Test that requests are retried on 429 status codes."""
        call_count = 0

        class CountingTransport(httpx.BaseTransport):
            def handle_request(self, request: httpx.Request) -> httpx.Response:
                nonlocal call_count
                call_count += 1
                if call_count < 2:
                    return httpx.Response(429, text="Too Many Requests")
                return httpx.Response(200, text="OK")

        config = ClientConfig(
            api_key="test-key",
            backend_id="test-backend",
            base_url="https://api.test.com",
            retry_count=3,
            min_retry_wait=0.01,
            max_retry_wait=0.02,
            http_transport=CountingTransport(),
        )
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/dashboards")
        response = transport.handle_request(request)

        assert response.status_code == 200
        assert call_count == 2

    def test_no_retry_on_400(self) -> None:
        """Test that 400 errors are NOT retried."""
        call_count = 0

        class CountingTransport(httpx.BaseTransport):
            def handle_request(self, request: httpx.Request) -> httpx.Response:
                nonlocal call_count
                call_count += 1
                return httpx.Response(400, text="Bad Request")

        config = ClientConfig(
            api_key="test-key",
            backend_id="test-backend",
            base_url="https://api.test.com",
            retry_count=3,
            min_retry_wait=0.01,
            max_retry_wait=0.02,
            http_transport=CountingTransport(),
        )
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/dashboards")
        response = transport.handle_request(request)

        assert response.status_code == 400
        assert call_count == 1  # No retries

    def test_max_retries_exhausted(self) -> None:
        """Test that after exhausting retries, the last response is returned."""
        call_count = 0

        class CountingTransport(httpx.BaseTransport):
            def handle_request(self, request: httpx.Request) -> httpx.Response:
                nonlocal call_count
                call_count += 1
                return httpx.Response(503, text="Service Unavailable")

        config = ClientConfig(
            api_key="test-key",
            backend_id="test-backend",
            base_url="https://api.test.com",
            retry_count=2,
            min_retry_wait=0.01,
            max_retry_wait=0.02,
            http_transport=CountingTransport(),
        )
        transport = GroundcoverTransport(config)
        request = httpx.Request("GET", "https://api.test.com/api/dashboards")
        response = transport.handle_request(request)

        assert response.status_code == 503
        assert call_count == 3  # 1 initial + 2 retries
