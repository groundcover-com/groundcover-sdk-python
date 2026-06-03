from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.synthetic_monitor_eval_interval_represents_the_evaluation_interval_for_a_synthetic_monitor import (
        SyntheticMonitorEvalIntervalRepresentsTheEvaluationIntervalForASyntheticMonitor,
    )


T = TypeVar("T", bound="SyntheticMonitorConfigRepresentsOptionalMonitorConfigurationOverridesForASyntheticTest")


@_attrs_define
class SyntheticMonitorConfigRepresentsOptionalMonitorConfigurationOverridesForASyntheticTest:
    """Fields left empty use the default values when creating the monitor.

    Attributes:
        connected_apps (list[str] | Unset): ConnectedApps lists connected app IDs for direct notification delivery
            (requires method "connectedApps").
        disable_renotification (bool | Unset): DisableRenotification disables repeated notifications for the same issue.
        enabled_workflows (list[str] | Unset):
        evaluation_interval (SyntheticMonitorEvalIntervalRepresentsTheEvaluationIntervalForASyntheticMonitor | Unset):
        execution_error_state (str | Unset):
        issue_description (str | Unset):
        issue_summary (str | Unset):
        lookbehind_window (str | Unset):
        monitor_name (str | Unset):
        no_data_state (str | Unset):
        notification_method (str | Unset): NotificationMethod determines how the synthetic monitor delivers alert
            notifications.
            Valid values: "notificationRoutes" (default), "connectedApps", "noNotifications".
        query (str | Unset): Query is read-only: auto-generated from the synthetic test ID.
        renotification_interval (str | Unset):
        severity (str | Unset):
        status_filters (list[str] | Unset): StatusFilters restricts which issue statuses trigger notifications (requires
            method "connectedApps").
    """

    connected_apps: list[str] | Unset = UNSET
    disable_renotification: bool | Unset = UNSET
    enabled_workflows: list[str] | Unset = UNSET
    evaluation_interval: SyntheticMonitorEvalIntervalRepresentsTheEvaluationIntervalForASyntheticMonitor | Unset = UNSET
    execution_error_state: str | Unset = UNSET
    issue_description: str | Unset = UNSET
    issue_summary: str | Unset = UNSET
    lookbehind_window: str | Unset = UNSET
    monitor_name: str | Unset = UNSET
    no_data_state: str | Unset = UNSET
    notification_method: str | Unset = UNSET
    query: str | Unset = UNSET
    renotification_interval: str | Unset = UNSET
    severity: str | Unset = UNSET
    status_filters: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_apps: list[str] | Unset = UNSET
        if not isinstance(self.connected_apps, Unset):
            connected_apps = self.connected_apps

        disable_renotification = self.disable_renotification

        enabled_workflows: list[str] | Unset = UNSET
        if not isinstance(self.enabled_workflows, Unset):
            enabled_workflows = self.enabled_workflows

        evaluation_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evaluation_interval, Unset):
            evaluation_interval = self.evaluation_interval.to_dict()

        execution_error_state = self.execution_error_state

        issue_description = self.issue_description

        issue_summary = self.issue_summary

        lookbehind_window = self.lookbehind_window

        monitor_name = self.monitor_name

        no_data_state = self.no_data_state

        notification_method = self.notification_method

        query = self.query

        renotification_interval = self.renotification_interval

        severity = self.severity

        status_filters: list[str] | Unset = UNSET
        if not isinstance(self.status_filters, Unset):
            status_filters = self.status_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_apps is not UNSET:
            field_dict["connectedApps"] = connected_apps
        if disable_renotification is not UNSET:
            field_dict["disableRenotification"] = disable_renotification
        if enabled_workflows is not UNSET:
            field_dict["enabledWorkflows"] = enabled_workflows
        if evaluation_interval is not UNSET:
            field_dict["evaluationInterval"] = evaluation_interval
        if execution_error_state is not UNSET:
            field_dict["executionErrorState"] = execution_error_state
        if issue_description is not UNSET:
            field_dict["issue_description"] = issue_description
        if issue_summary is not UNSET:
            field_dict["issue_summary"] = issue_summary
        if lookbehind_window is not UNSET:
            field_dict["lookbehind_window"] = lookbehind_window
        if monitor_name is not UNSET:
            field_dict["monitor_name"] = monitor_name
        if no_data_state is not UNSET:
            field_dict["noDataState"] = no_data_state
        if notification_method is not UNSET:
            field_dict["notificationMethod"] = notification_method
        if query is not UNSET:
            field_dict["query"] = query
        if renotification_interval is not UNSET:
            field_dict["renotificationInterval"] = renotification_interval
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status_filters is not UNSET:
            field_dict["statusFilters"] = status_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.synthetic_monitor_eval_interval_represents_the_evaluation_interval_for_a_synthetic_monitor import (
            SyntheticMonitorEvalIntervalRepresentsTheEvaluationIntervalForASyntheticMonitor,
        )

        d = dict(src_dict)
        connected_apps = cast(list[str], d.pop("connectedApps", UNSET))

        disable_renotification = d.pop("disableRenotification", UNSET)

        enabled_workflows = cast(list[str], d.pop("enabledWorkflows", UNSET))

        _evaluation_interval = d.pop("evaluationInterval", UNSET)
        evaluation_interval: SyntheticMonitorEvalIntervalRepresentsTheEvaluationIntervalForASyntheticMonitor | Unset
        if isinstance(_evaluation_interval, Unset) or _evaluation_interval is None:
            evaluation_interval = UNSET
        else:
            evaluation_interval = (
                SyntheticMonitorEvalIntervalRepresentsTheEvaluationIntervalForASyntheticMonitor.from_dict(
                    _evaluation_interval
                )
            )

        execution_error_state = d.pop("executionErrorState", UNSET)

        issue_description = d.pop("issue_description", UNSET)

        issue_summary = d.pop("issue_summary", UNSET)

        lookbehind_window = d.pop("lookbehind_window", UNSET)

        monitor_name = d.pop("monitor_name", UNSET)

        no_data_state = d.pop("noDataState", UNSET)

        notification_method = d.pop("notificationMethod", UNSET)

        query = d.pop("query", UNSET)

        renotification_interval = d.pop("renotificationInterval", UNSET)

        severity = d.pop("severity", UNSET)

        status_filters = cast(list[str], d.pop("statusFilters", UNSET))

        synthetic_monitor_config_represents_optional_monitor_configuration_overrides_for_a_synthetic_test = cls(
            connected_apps=connected_apps,
            disable_renotification=disable_renotification,
            enabled_workflows=enabled_workflows,
            evaluation_interval=evaluation_interval,
            execution_error_state=execution_error_state,
            issue_description=issue_description,
            issue_summary=issue_summary,
            lookbehind_window=lookbehind_window,
            monitor_name=monitor_name,
            no_data_state=no_data_state,
            notification_method=notification_method,
            query=query,
            renotification_interval=renotification_interval,
            severity=severity,
            status_filters=status_filters,
        )

        synthetic_monitor_config_represents_optional_monitor_configuration_overrides_for_a_synthetic_test.additional_properties = d
        return synthetic_monitor_config_represents_optional_monitor_configuration_overrides_for_a_synthetic_test

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
