"""Demonstrate custom client configuration."""

import groundcover
from groundcover.api.dashboards import get_dashboards


def main() -> None:
    # Override all settings explicitly
    client = groundcover.Client(
        api_key="your-api-key",
        backend_id="your-backend-id",
        base_url="https://api.groundcover.com",
        timeout=60.0,
        retry_count=5,
        min_retry_wait=2.0,
        max_retry_wait=60.0,
        retry_statuses=[500, 502, 503, 504, 429],
    )

    try:
        result = get_dashboards.sync_detailed(client=client)
        print(f"Status: {result.status_code}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
