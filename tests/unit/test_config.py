"""Tests for groundcover.config."""

from __future__ import annotations

import pytest

from groundcover.config import ClientConfig, _normalize_base_url
from groundcover.exceptions import ConfigurationError


class TestClientConfig:
    def test_defaults(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.setenv("GC_BACKEND_ID", "test-backend")
        monkeypatch.delenv("GC_BASE_URL", raising=False)
        monkeypatch.delenv("GC_TRACEPARENT", raising=False)

        config = ClientConfig()
        assert config.api_key == "test-key"
        assert config.backend_id == "test-backend"
        assert config.base_url == "https://api.groundcover.com"
        assert config.timeout == 30.0
        assert config.retry_count == 3
        assert config.min_retry_wait == 1.0
        assert config.max_retry_wait == 30.0
        assert config.retry_statuses == [503, 429]
        assert config.traceparent is None

    def test_env_vars(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "env-key")
        monkeypatch.setenv("GC_BACKEND_ID", "env-backend")
        monkeypatch.setenv("GC_BASE_URL", "https://custom.api.com")
        monkeypatch.setenv("GC_TRACEPARENT", "00-trace-span-01")

        config = ClientConfig()
        assert config.api_key == "env-key"
        assert config.backend_id == "env-backend"
        assert config.base_url == "https://custom.api.com"
        assert config.traceparent == "00-trace-span-01"

    def test_kwargs_override_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "env-key")
        monkeypatch.setenv("GC_BACKEND_ID", "env-backend")

        config = ClientConfig(api_key="override-key", backend_id="override-backend")
        assert config.api_key == "override-key"
        assert config.backend_id == "override-backend"

    def test_validate_missing_api_key(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("GC_API_KEY", raising=False)
        monkeypatch.setenv("GC_BACKEND_ID", "test-backend")

        config = ClientConfig()
        with pytest.raises(ConfigurationError, match="API key is required"):
            config.validate()

    def test_validate_missing_backend_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.delenv("GC_BACKEND_ID", raising=False)

        config = ClientConfig()
        with pytest.raises(ConfigurationError, match="Backend ID is required"):
            config.validate()

    def test_validate_success(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GC_API_KEY", "test-key")
        monkeypatch.setenv("GC_BACKEND_ID", "test-backend")

        config = ClientConfig()
        config.validate()  # Should not raise

    def test_effective_base_url(self) -> None:
        config = ClientConfig(api_key="k", backend_id="b", base_url="example.com")
        assert config.effective_base_url == "https://example.com"

    def test_retry_statuses_independent_across_instances(self) -> None:
        c1 = ClientConfig(api_key="k", backend_id="b")
        c2 = ClientConfig(api_key="k", backend_id="b")
        c1.retry_statuses.append(500)
        assert 500 not in c2.retry_statuses


class TestNormalizeBaseURL:
    def test_empty(self) -> None:
        assert _normalize_base_url("") == ""

    def test_protocol_relative(self) -> None:
        assert _normalize_base_url("//example.com") == "https://example.com"

    def test_relative_path(self) -> None:
        assert _normalize_base_url("/example.com") == "https://example.com"

    def test_no_scheme(self) -> None:
        assert _normalize_base_url("example.com") == "https://example.com"

    def test_with_scheme(self) -> None:
        assert _normalize_base_url("https://example.com") == "https://example.com"

    def test_http_scheme(self) -> None:
        assert _normalize_base_url("http://localhost:8080") == "http://localhost:8080"
