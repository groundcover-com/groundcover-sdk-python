from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_trigger import (
    TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointTrigger,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_monitor_display_controls_how_the_test_notification_is_presented import (
        TestMonitorDisplayControlsHowTheTestNotificationIsPresented,
    )
    from ..models.test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered import (
        TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered,
    )
    from ..models.test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_labels import (
        TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointLabels,
    )
    from ..models.test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_query import (
        TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery,
    )


T = TypeVar("T", bound="TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpoint")


@_attrs_define
class TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpoint:
    """
    Attributes:
        monitor_name (str): The name of the monitor being tested Example: High CPU Usage.
        trigger (TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointTrigger): The trigger state to simulate
            Example: Alerting.
        display (TestMonitorDisplayControlsHowTheTestNotificationIsPresented | Unset): Mirrors the monitor DisplayModel
            structure.
        labels (TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointLabels | Unset): Labels to match against
            notification routes Example: {'cluster': 'prod', 'namespace': 'api'}.
        notification_settings (TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered | Unset):
            Mirrors the monitor NotificationSettings structure.
        query (TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery | Unset): Query metadata from the
            monitor definition.
            Keys match template variables: expression, data_type, instant_rollup. Example: {'data_type': 'logs',
            'expression': '* | stats count()', 'instant_rollup': '5m'}.
        send_notifications (bool | Unset): Whether to actually send test notifications to providers.
            When false, only returns matched routes without side effects. Example: True.
        severity (str | Unset): Severity for the test notification Example: critical.
        threshold (str | Unset): Threshold value from the monitor definition.
            Used to populate the {{threshold}} template variable in test notifications. Example: 2500.
        username (str | Unset): The username (email) of the user who initiated the test.
            Populated automatically from the authenticated user context. Example: user@example.com.
    """

    monitor_name: str
    trigger: TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointTrigger
    display: TestMonitorDisplayControlsHowTheTestNotificationIsPresented | Unset = UNSET
    labels: TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointLabels | Unset = UNSET
    notification_settings: TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered | Unset = (
        UNSET
    )
    query: TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery | Unset = UNSET
    send_notifications: bool | Unset = UNSET
    severity: str | Unset = UNSET
    threshold: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_name = self.monitor_name

        trigger = self.trigger.value

        display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        send_notifications = self.send_notifications

        severity = self.severity

        threshold = self.threshold

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitor_name": monitor_name,
                "trigger": trigger,
            }
        )
        if display is not UNSET:
            field_dict["display"] = display
        if labels is not UNSET:
            field_dict["labels"] = labels
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if query is not UNSET:
            field_dict["query"] = query
        if send_notifications is not UNSET:
            field_dict["send_notifications"] = send_notifications
        if severity is not UNSET:
            field_dict["severity"] = severity
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_monitor_display_controls_how_the_test_notification_is_presented import (
            TestMonitorDisplayControlsHowTheTestNotificationIsPresented,
        )
        from ..models.test_monitor_notification_settings_specifies_how_the_test_notification_should_be_delivered import (
            TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered,
        )
        from ..models.test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_labels import (
            TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointLabels,
        )
        from ..models.test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_query import (
            TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery,
        )

        d = dict(src_dict)
        monitor_name = d.pop("monitor_name")

        trigger = TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointTrigger(d.pop("trigger"))

        _display = d.pop("display", UNSET)
        display: TestMonitorDisplayControlsHowTheTestNotificationIsPresented | Unset
        if isinstance(_display, Unset) or _display is None:
            display = UNSET
        else:
            display = TestMonitorDisplayControlsHowTheTestNotificationIsPresented.from_dict(_display)

        _labels = d.pop("labels", UNSET)
        labels: TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointLabels | Unset
        if isinstance(_labels, Unset) or _labels is None:
            labels = UNSET
        else:
            labels = TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointLabels.from_dict(_labels)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered | Unset
        if isinstance(_notification_settings, Unset) or _notification_settings is None:
            notification_settings = UNSET
        else:
            notification_settings = (
                TestMonitorNotificationSettingsSpecifiesHowTheTestNotificationShouldBeDelivered.from_dict(
                    _notification_settings
                )
            )

        _query = d.pop("query", UNSET)
        query: TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery | Unset
        if isinstance(_query, Unset) or _query is None:
            query = UNSET
        else:
            query = TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery.from_dict(_query)

        send_notifications = d.pop("send_notifications", UNSET)

        severity = d.pop("severity", UNSET)

        threshold = d.pop("threshold", UNSET)

        username = d.pop("username", UNSET)

        test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint = cls(
            monitor_name=monitor_name,
            trigger=trigger,
            display=display,
            labels=labels,
            notification_settings=notification_settings,
            query=query,
            send_notifications=send_notifications,
            severity=severity,
            threshold=threshold,
            username=username,
        )

        test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint.additional_properties = d
        return test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
