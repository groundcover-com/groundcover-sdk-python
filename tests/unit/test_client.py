"""Tests for groundcover.client."""

from __future__ import annotations

import asyncio

import httpx
import pytest

import groundcover
from groundcover.async_client import AsyncClient
from groundcover.client import Client
from groundcover.exceptions import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
)


class TestClientInit:
    def test_missing_api_key(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("GC_API_KEY", raising=False)
        monkeypatch.delenv("GC_BACKEND_ID", raising=False)
        with pytest.raises(ConfigurationError, match="API key"):
            Client()

    def test_missing_backend_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.delenv("GC_BACKEND_ID", raising=False)
        with pytest.raises(ConfigurationError, match="Backend ID"):
            Client()

    def test_context_manager(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.setenv("GC_BACKEND_ID", "test-backend")
        with Client() as client:
            assert client is not None

    def test_explicit_config(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("GC_API_KEY", raising=False)
        monkeypatch.delenv("GC_BACKEND_ID", raising=False)
        client = Client(api_key="explicit-key", backend_id="explicit-backend")
        assert client._config.api_key == "explicit-key"
        assert client._config.backend_id == "explicit-backend"
        client.close()


class TestClientErrorHandling:
    """Test that HTTP error responses raise the correct exceptions."""

    @pytest.fixture(autouse=True)
    def setup_client(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.setenv("GC_BACKEND_ID", "test-backend")

    def _make_client_with_mock(self, status_code: int, body: str = "") -> Client:
        """Create a client with a mock transport that returns a fixed response."""

        class MockTransport(httpx.BaseTransport):
            def handle_request(self, request: httpx.Request) -> httpx.Response:
                return httpx.Response(status_code, text=body)

        return Client(
            api_key="test-key",
            backend_id="test-backend",
            http_transport=MockTransport(),
            retry_count=0,  # Disable retries for error-handling tests
        )

    def test_401_raises_authentication_error(self) -> None:
        client = self._make_client_with_mock(401, "unauthorized")
        with pytest.raises(AuthenticationError):
            client.get("/api/dashboards")
        client.close()

    def test_403_raises_forbidden_error(self) -> None:
        client = self._make_client_with_mock(403, "forbidden")
        with pytest.raises(ForbiddenError):
            client.get("/api/dashboards")
        client.close()

    def test_404_raises_not_found_error(self) -> None:
        client = self._make_client_with_mock(404, "not found")
        with pytest.raises(NotFoundError):
            client.get("/api/dashboards/nonexistent")
        client.close()

    def test_429_raises_rate_limit_error(self) -> None:
        client = self._make_client_with_mock(429, "rate limited")
        with pytest.raises(RateLimitError):
            client.get("/api/dashboards")
        client.close()

    def test_500_raises_api_error(self) -> None:
        client = self._make_client_with_mock(500, "internal error")
        with pytest.raises(APIError) as exc_info:
            client.get("/api/dashboards")
        assert exc_info.value.status_code == 500
        client.close()

    def test_200_no_error(self) -> None:
        client = self._make_client_with_mock(200, '{"ok": true}')
        response = client.get("/api/dashboards")
        assert response.status_code == 200
        client.close()


class TestDuckTyping:
    """Test that Client/AsyncClient duck-type as AuthenticatedClient."""

    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.setenv("GC_BACKEND_ID", "test-backend")

    def test_get_httpx_client_returns_httpx_client(self) -> None:
        client = Client(api_key="test-key", backend_id="test-backend")
        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)
        client.close()

    def test_raise_on_unexpected_status_property(self) -> None:
        client = Client(api_key="test-key", backend_id="test-backend")
        assert client.raise_on_unexpected_status is False
        client.raise_on_unexpected_status = True
        assert client.raise_on_unexpected_status is True
        client.close()

    def test_async_get_async_httpx_client(self) -> None:
        client = AsyncClient(api_key="test-key", backend_id="test-backend")
        httpx_client = client.get_async_httpx_client()
        assert isinstance(httpx_client, httpx.AsyncClient)
        asyncio.run(client.aclose())

    def test_async_raise_on_unexpected_status_property(self) -> None:
        client = AsyncClient(api_key="test-key", backend_id="test-backend")
        assert client.raise_on_unexpected_status is False
        client.raise_on_unexpected_status = True
        assert client.raise_on_unexpected_status is True
        asyncio.run(client.aclose())

    def test_client_works_with_generated_api_function(self) -> None:
        """Verify Client can be passed to a generated API function."""

        class MockTransport(httpx.BaseTransport):
            def handle_request(self, request: httpx.Request) -> httpx.Response:
                return httpx.Response(200, json={"status": "success", "data": None})

        client = Client(
            api_key="test-key",
            backend_id="test-backend",
            http_transport=MockTransport(),
            retry_count=0,
        )

        from groundcover.api.metrics import metrics_query
        from groundcover.models.query_request import QueryRequest

        result = metrics_query.sync_detailed(
            client=client,
            body=QueryRequest(promql="up"),
        )
        assert result.status_code == 200
        assert result.parsed is not None
        assert result.parsed["status"] == "success"
        client.close()


class TestModuleExports:
    def test_client_exported(self) -> None:
        assert hasattr(groundcover, "Client")

    def test_async_client_exported(self) -> None:
        assert hasattr(groundcover, "AsyncClient")

    def test_version_exported(self) -> None:
        assert hasattr(groundcover, "__version__")

    def test_exceptions_exported(self) -> None:
        assert hasattr(groundcover, "GroundcoverError")
        assert hasattr(groundcover, "ConfigurationError")
        assert hasattr(groundcover, "APIError")
        assert hasattr(groundcover, "AuthenticationError")
        assert hasattr(groundcover, "ForbiddenError")
        assert hasattr(groundcover, "NotFoundError")
        assert hasattr(groundcover, "ConflictError")
        assert hasattr(groundcover, "RateLimitError")
