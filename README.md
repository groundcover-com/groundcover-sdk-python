# groundcover Python SDK

Official Python SDK for the [groundcover](https://groundcover.com) API.

## Installation

### 1. Install uv (skip if you already have it)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install the SDK

```bash
uv init   # skip if you already have a pyproject.toml
uv add "git+https://github.com/groundcover-com/groundcover-sdk-python.git"
```

## Requirements

- Python 3.9+
- A groundcover API key and Backend ID

## Quick Start

```python
import groundcover
from groundcover.api.metrics import metrics_query
from groundcover.models.query_request import QueryRequest
from groundcover.models.query_request_query_type import QueryRequestQueryType
from datetime import datetime, timedelta, timezone

with groundcover.Client() as client:
    now = datetime.now(timezone.utc)
    result = metrics_query.sync_detailed(
        client=client,
        body=QueryRequest(
            promql="up",
            query_type=QueryRequestQueryType.INSTANT,
            start=now - timedelta(hours=1),
            end=now,
        ),
    )
    print(result.parsed)
```

The SDK provides **typed API functions** as the primary interface.
Import the operation module and call `sync_detailed()` (or `asyncio_detailed()` for async):

```python
from groundcover.api.logs import search_logs
from groundcover.models.logs_search_request import LogsSearchRequest

result = search_logs.sync_detailed(
    client=client,
    body=LogsSearchRequest(start=start, end=end, query="* | stats count(*)"),
)
```

Raw HTTP methods (`client.get()`, `client.post()`, etc.) remain available for
advanced use cases or endpoints not yet available as typed functions.

## Configuration

The SDK reads from environment variables by default:

| Variable | Description | Required |
|---|---|---|
| `GC_API_KEY` | Your groundcover API key | Yes |
| `GC_BACKEND_ID` | Your groundcover Backend ID | Yes |
| `GC_BASE_URL` | API base URL (default: `https://api.groundcover.com`) | No |
| `GC_TRACEPARENT` | Default traceparent header for tracing | No |

You can also pass configuration explicitly:

```python
client = groundcover.Client(
    api_key="your-api-key",
    backend_id="your-backend-id",
    base_url="https://api.groundcover.com",
    timeout=60.0,
    retry_count=5,
)
```

## Async Support

```python
import groundcover
from groundcover.api.dashboards import get_dashboards

async with groundcover.AsyncClient() as client:
    result = await get_dashboards.asyncio_detailed(client=client)
```

## Monitors (YAML)

Monitor endpoints use YAML content-type, so they have dedicated client helper methods:

```python
with groundcover.Client() as client:
    # Create from YAML string
    client.create_monitor(yaml_string)

    # Get returns parsed YAML as dict
    monitor = client.get_monitor("monitor-id")

    # Update
    client.update_monitor("monitor-id", updated_yaml)

    # Delete uses the typed API
    from groundcover.api.monitors import delete_monitor
    delete_monitor.sync_detailed("monitor-id", client=client)
```

## Workflow SDK removal

> **Breaking change (AI-461):** The public Python SDK no longer exposes workflow
> create, list, or delete operations for `POST /api/workflows/create`,
> `POST /api/workflows/list`, and `DELETE /api/workflows/{id}`. This removes
> `Client.create_workflow()`, `AsyncClient.create_workflow()`, and the generated
> workflow list/delete operations. For temporary compatibility, the unchanged
> endpoints can be called directly through REST. Workflows are deprecated;
> migrate notification automation to [Destinations](https://docs.groundcover.com/integrations/connected-apps)
> and [Notification Routes](https://docs.groundcover.com/use-groundcover/monitors/notification-routes) using
> the [workflow migration guide](https://docs.groundcover.com/use-groundcover/workflows#migration-steps).

## Condition Builder

```python
from groundcover.utils import ConditionSet

conditions = (
    ConditionSet()
    .add("namespace", "production")
    .add("workload", "api-server")
    .add_oom_event_conditions()
    .build()
)

response = client.post("/api/logs/v2/search", json={
    "query": "* | stats count(*)",
    "conditions": conditions,
    ...
})
```

## Error Handling

All requests — both typed API calls and raw HTTP methods — raise the
same typed exceptions:

```python
import groundcover

try:
    result = get_dashboard.sync_detailed("nonexistent", client=client)
except groundcover.NotFoundError:
    print("Dashboard not found")
except groundcover.AuthenticationError:
    print("Invalid API key")
except groundcover.RateLimitError:
    print("Rate limited, SDK retries automatically on 429/503")
except groundcover.APIError as e:
    print(f"API error {e.status_code}: {e.body}")
```

## Retry Behavior

By default, the SDK retries on HTTP 503 and 429 with exponential backoff and jitter:

- **Default retries**: 3
- **Default retry statuses**: 503 (Service Unavailable), 429 (Too Many Requests)
- **Backoff**: Exponential with jitter, 1s min, 30s max

## Development

```bash
cd sdk-python
uv sync --extra dev

# Run unit tests
make test-unit

# Run linting
make lint

# Format code
make format
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
