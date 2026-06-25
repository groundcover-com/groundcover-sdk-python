from __future__ import annotations

from enum import Enum


class TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedAppConnectedAppType(str, Enum):
    INCIDENTIO = "incidentio"
    MS_TEAMS = "ms-teams"
    OPSGENIE = "opsgenie"
    PAGERDUTY = "pagerduty"
    SLACK_WEBHOOK = "slack-webhook"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
