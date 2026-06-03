from __future__ import annotations

from enum import Enum


class NotificationSettingsDefinesTheNotificationSettingsForTheMonitorMethod(str, Enum):
    CONNECTEDAPPS = "connectedApps"
    NONOTIFICATIONS = "noNotifications"
    NOTIFICATIONROUTES = "notificationRoutes"

    def __str__(self) -> str:
        return str(self.value)
