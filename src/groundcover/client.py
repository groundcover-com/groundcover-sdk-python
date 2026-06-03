"""Synchronous groundcover SDK client.

Wraps the generated AuthenticatedClient so that our Client can be passed
directly to generated API functions (duck-typing) while also providing
convenience helpers for endpoints that use non-JSON content types.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Union

import httpx
import yaml

from groundcover._generated_client import AuthenticatedClient
from groundcover.config import ClientConfig
from groundcover.exceptions import error_response_hook
from groundcover.transport import GroundcoverTransport


class Client:
    """Synchronous groundcover API client.

    Can be used directly with generated typed API functions::

        from groundcover.api.metrics import metrics_query
        from groundcover.models.query_request import QueryRequest

        with groundcover.Client() as client:
            result = metrics_query.sync_detailed(client=client, body=QueryRequest(...))

    Or with raw HTTP methods for advanced/unsupported endpoints::

        with groundcover.Client() as client:
            response = client.post("/api/metrics/query", json={...})
    """

    def __init__(self, **kwargs: Any) -> None:
        self._config = ClientConfig(**kwargs)
        self._config.validate()

        self._transport = GroundcoverTransport(self._config)
        self._auth_client = AuthenticatedClient(
            base_url=self._config.effective_base_url,
            token=self._config.api_key or "",
            httpx_args={
                "transport": self._transport,
                "event_hooks": {"response": [error_response_hook]},
            },
            timeout=httpx.Timeout(self._config.timeout),
        )

    # -- Duck-typing interface for generated API functions --

    @property
    def raise_on_unexpected_status(self) -> bool:
        return self._auth_client.raise_on_unexpected_status

    @raise_on_unexpected_status.setter
    def raise_on_unexpected_status(self, value: bool) -> None:
        self._auth_client.raise_on_unexpected_status = value

    def get_httpx_client(self) -> httpx.Client:
        """Return the underlying httpx.Client (creates one on first call)."""
        return self._auth_client.get_httpx_client()

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Return the underlying async httpx.Client (creates one on first call)."""
        return self._auth_client.get_async_httpx_client()

    # -- Raw HTTP convenience methods --

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        content: Optional[Union[str, bytes]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        traceparent: Optional[str] = None,
    ) -> httpx.Response:
        """Send an HTTP request to the groundcover API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            path: API path (e.g., "/api/dashboards")
            json: JSON body to send
            content: Raw body content (str or bytes)
            params: Query parameters
            headers: Additional headers
            traceparent: Per-request traceparent override

        Returns:
            httpx.Response

        Raises:
            AuthenticationError: On 401
            ForbiddenError: On 403
            NotFoundError: On 404
            ConflictError: On 409
            RateLimitError: On 429
            APIError: On other 4xx/5xx
        """
        extensions: Dict[str, Any] = {}
        if traceparent is not None:
            extensions["traceparent"] = traceparent

        return self.get_httpx_client().request(
            method,
            path,
            json=json,
            content=content,
            params=params,
            headers=headers,
            extensions=extensions,
        )

    def get(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a GET request."""
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a POST request."""
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a PUT request."""
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a DELETE request."""
        return self.request("DELETE", path, **kwargs)

    # -- Service-specific helpers for special content-type endpoints --

    def get_monitor(self, monitor_id: str, **kwargs: Any) -> Dict[str, Any]:
        """Get a monitor by ID. Returns parsed YAML as dict.

        The transport automatically fixes the response Content-Type to application/x-yaml.
        """
        response = self.get(f"/api/monitors/{monitor_id}", **kwargs)
        return yaml.safe_load(response.content)

    def create_monitor(self, monitor_yaml: Union[str, Dict[str, Any]], **kwargs: Any) -> httpx.Response:
        """Create a monitor from YAML content.

        Args:
            monitor_yaml: YAML string or dict (will be serialized to YAML)
        """
        if isinstance(monitor_yaml, dict):
            body = yaml.dump(monitor_yaml, default_flow_style=False)
        else:
            body = monitor_yaml
        return self.post(
            "/api/monitors",
            content=body,
            headers={"Content-Type": "application/x-yaml"},
            **kwargs,
        )

    def update_monitor(
        self, monitor_id: str, monitor_yaml: Union[str, Dict[str, Any]], **kwargs: Any
    ) -> httpx.Response:
        """Update a monitor from YAML content.

        Args:
            monitor_id: The monitor ID
            monitor_yaml: YAML string or dict (will be serialized to YAML)
        """
        if isinstance(monitor_yaml, dict):
            body = yaml.dump(monitor_yaml, default_flow_style=False)
        else:
            body = monitor_yaml
        return self.put(
            f"/api/monitors/{monitor_id}",
            content=body,
            headers={"Content-Type": "application/x-yaml"},
            **kwargs,
        )

    def create_workflow(self, workflow_text: str, **kwargs: Any) -> httpx.Response:
        """Create a workflow. The transport automatically sets Content-Type to text/plain."""
        return self.post("/api/workflows/create", content=workflow_text, **kwargs)

    # -- Context manager --

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._auth_client.__exit__(None, None, None)

    def __enter__(self) -> Client:
        self._auth_client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._auth_client.__exit__(*args)
