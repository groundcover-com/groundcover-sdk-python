from __future__ import annotations

from enum import Enum


class FetchAssetsRequestAssetTypesItem(str, Enum):
    AWS_INTEGRATIONS = "aws_integrations"
    AZURE_INTEGRATIONS = "azure_integrations"
    DASHBOARDS = "dashboards"
    GCP_INTEGRATIONS = "gcp_integrations"
    LOGS_PIPELINES = "logs_pipelines"
    METRICS = "metrics"
    MONITORS = "monitors"

    def __str__(self) -> str:
        return str(self.value)
