"""Asynchronous groundcover SDK client.

Wraps the generated AuthenticatedClient so that our AsyncClient can be passed
directly to generated async API functions (duck-typing) while also providing
convenience helpers for endpoints that use non-JSON content types.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Union

import httpx
import yaml

from groundcover._generated_client import AuthenticatedClient
from groundcover.config import ClientConfig
from groundcover.exceptions import error_response_hook
from groundcover.transport import AsyncGroundcoverTransport


class AsyncClient:
    """Asynchronous groundcover API client.

    Can be used directly with generated typed async API functions::

        from groundcover.api.metrics import metrics_query
        from groundcover.models.query_request import QueryRequest

        async with groundcover.AsyncClient() as client:
            result = await metrics_query.asyncio_detailed(client=client, body=QueryRequest(...))

    Or with raw HTTP methods for advanced/unsupported endpoints::

        async with groundcover.AsyncClient() as client:
            response = await client.post("/api/metrics/query", json={...})
    """

    def __init__(self, **kwargs: Any) -> None:
        self._config = ClientConfig(**kwargs)
        self._config.validate()

        self._transport = AsyncGroundcoverTransport(self._config)
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
        """Return the underlying sync httpx.Client (creates one on first call)."""
        return self._auth_client.get_httpx_client()

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Return the underlying async httpx.Client (creates one on first call)."""
        return self._auth_client.get_async_httpx_client()

    # -- Raw HTTP convenience methods --

    async def request(
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
        """Send an async HTTP request to the groundcover API."""
        extensions: Dict[str, Any] = {}
        if traceparent is not None:
            extensions["traceparent"] = traceparent

        return await self.get_async_httpx_client().request(
            method,
            path,
            json=json,
            content=content,
            params=params,
            headers=headers,
            extensions=extensions,
        )

    async def get(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a GET request."""
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a POST request."""
        return await self.request("POST", path, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a PUT request."""
        return await self.request("PUT", path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send a DELETE request."""
        return await self.request("DELETE", path, **kwargs)

    # -- Service-specific helpers for special content-type endpoints --

    async def get_monitor(self, monitor_id: str, **kwargs: Any) -> Dict[str, Any]:
        """Get a monitor by ID. Returns parsed YAML as dict."""
        response = await self.get(f"/api/monitors/{monitor_id}", **kwargs)
        return yaml.safe_load(response.content)

    async def create_monitor(self, monitor_yaml: Union[str, Dict[str, Any]], **kwargs: Any) -> httpx.Response:
        """Create a monitor from YAML content."""
        if isinstance(monitor_yaml, dict):
            body = yaml.dump(monitor_yaml, default_flow_style=False)
        else:
            body = monitor_yaml
        return await self.post(
            "/api/monitors",
            content=body,
            headers={"Content-Type": "application/x-yaml"},
            **kwargs,
        )

    async def update_monitor(
        self, monitor_id: str, monitor_yaml: Union[str, Dict[str, Any]], **kwargs: Any
    ) -> httpx.Response:
        """Update a monitor from YAML content."""
        if isinstance(monitor_yaml, dict):
            body = yaml.dump(monitor_yaml, default_flow_style=False)
        else:
            body = monitor_yaml
        return await self.put(
            f"/api/monitors/{monitor_id}",
            content=body,
            headers={"Content-Type": "application/x-yaml"},
            **kwargs,
        )

    async def create_workflow(self, workflow_text: str, **kwargs: Any) -> httpx.Response:
        """Create a workflow. The transport automatically sets Content-Type to text/plain."""
        return await self.post("/api/workflows/create", content=workflow_text, **kwargs)

    # -- Context manager --

    async def aclose(self) -> None:
        """Close the underlying HTTP client."""
        await self._auth_client.__aexit__(None, None, None)

    async def __aenter__(self) -> AsyncClient:
        await self._auth_client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._auth_client.__aexit__(*args)
