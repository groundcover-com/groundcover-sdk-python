"""E2E tests for data integrations endpoints. Mirrors sdk/tests/e2e/dataintegrations_test.go."""

from __future__ import annotations

import json
import time

import groundcover
from groundcover.api.integrations import (
    create_data_integration_config,
    delete_data_integration_config,
    describe_data_integration,
    get_data_integration_config,
    get_data_integration_configs,
    update_data_integration_config,
)
from groundcover.exceptions import APIError
from groundcover.models.create_data_integration_config_request import (
    CreateDataIntegrationConfigRequest,
)

CLOUDWATCH_CONFIG = """{
  "version": 1,
  "name": "test-cloudwatch",
  "scrapeInterval": "5m",
  "stsRegion": "us-east-1",
  "exporters": ["prometheus"],
  "regions": ["us-east-1"],
  "roleArn": "arn:aws:iam::123456789012:role/test-role",
  "awsMetrics": [
    {
      "namespace": "AWS/EC2",
      "metrics": [
        {
          "name": "CPUUtilization",
          "statistics": ["Average"],
          "period": 300,
          "length": 300,
          "nullAsZero": false
        }
      ]
    }
  ],
  "apiConcurrencyLimits": {
    "listMetrics": 3,
    "getMetricData": 5,
    "getMetricStatistics": 5,
    "listInventory": 10
  },
  "withContextTagsOnInfoMetrics": false,
  "withInventoryDiscovery": true
}"""

CLOUDWATCH_CONFIG_UPDATED = """{
  "version": 1,
  "name": "test-cloudwatch",
  "scrapeInterval": "5m",
  "stsRegion": "us-east-2",
  "exporters": ["prometheus"],
  "regions": ["us-east-2"],
  "roleArn": "arn:aws:iam::123456789012:role/test-role",
  "awsMetrics": [
    {
      "namespace": "AWS/EC2",
      "metrics": [
        {
          "name": "CPUUtilization",
          "statistics": ["Average"],
          "period": 300,
          "length": 300,
          "nullAsZero": false
        }
      ]
    }
  ],
  "apiConcurrencyLimits": {
    "listMetrics": 1,
    "getMetricData": 5,
    "getMetricStatistics": 5,
    "listInventory": 10
  },
  "withContextTagsOnInfoMetrics": false,
  "withInventoryDiscovery": true
}"""


def test_list_data_integration_configs(gc_client: groundcover.Client) -> None:
    """List data integration configurations."""
    result = get_data_integration_configs.sync_detailed(client=gc_client)
    assert result.status_code == 200


def test_describe_data_integration_type(gc_client: groundcover.Client) -> None:
    """Describe a data integration type."""
    result = describe_data_integration.sync_detailed("cloudwatch", client=gc_client)
    assert result.status_code == 200


class TestCloudwatchLifecycle:
    """Full CRUD lifecycle for CloudWatch data integration."""

    def test_cloudwatch_crud(self, gc_client: groundcover.Client) -> None:
        unique_name = f"sdk-e2e-test-cloudwatch-{time.time_ns()}"
        config_id = None

        try:
            # Create
            create_result = create_data_integration_config.sync_detailed(
                "cloudwatch",
                client=gc_client,
                body=CreateDataIntegrationConfigRequest(
                    config=CLOUDWATCH_CONFIG,
                    name=unique_name,
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            assert create_data["config"] == CLOUDWATCH_CONFIG
            assert create_data["id"]
            assert create_data["update_timestamp"]
            assert create_data.get("is_archived") is not True
            config_id = create_data["id"]
            original_timestamp = create_data["update_timestamp"]

            # Get - verify config
            get_result = get_data_integration_config.sync_detailed("cloudwatch", config_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["config"] == CLOUDWATCH_CONFIG
            assert get_data.get("is_archived") is not True

            # Update - change region and concurrency
            update_result = update_data_integration_config.sync_detailed(
                "cloudwatch",
                config_id,
                client=gc_client,
                body=CreateDataIntegrationConfigRequest(
                    config=CLOUDWATCH_CONFIG_UPDATED,
                    name=unique_name,
                ),
            )
            assert update_result.status_code == 200
            update_data = json.loads(update_result.content)
            assert update_data["config"] == CLOUDWATCH_CONFIG_UPDATED
            assert update_data["update_timestamp"]
            assert update_data["update_timestamp"] > original_timestamp

            # Get - verify updated config
            get_result = get_data_integration_config.sync_detailed("cloudwatch", config_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["config"] == CLOUDWATCH_CONFIG_UPDATED
            assert get_data.get("is_archived") is not True

            # Delete
            delete_data_integration_config.sync_detailed("cloudwatch", config_id, client=gc_client)

            # Verify deletion - should return error
            try:
                get_result = get_data_integration_config.sync_detailed("cloudwatch", config_id, client=gc_client)
                # If no exception, check for error status
                assert get_result.status_code in (404, 400), (
                    f"Expected 404 after deletion, got {get_result.status_code}"
                )
            except APIError:
                pass  # Expected

            config_id = None

        finally:
            if config_id:
                try:
                    delete_data_integration_config.sync_detailed("cloudwatch", config_id, client=gc_client)
                except Exception:
                    pass
