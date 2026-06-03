from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_thresholds import MonitorThresholds
    from ..models.monitor_variable import MonitorVariable


T = TypeVar("T", bound="MonitorOptions")


@_attrs_define
class MonitorOptions:
    """MonitorOptions represents options for a monitor

    Attributes:
        device_ids (list[str] | Unset):
        enable_logs_sample (bool | Unset):
        escalation_message (str | Unset):
        evaluation_delay (int | Unset):
        groupby_simple_monitor (bool | Unset):
        include_tags (bool | Unset):
        min_failure_duration (int | Unset):
        min_location_failed (int | Unset):
        new_group_delay (int | Unset):
        new_host_delay (int | Unset):
        no_data_timeframe (int | Unset):
        notification_preset_name (str | Unset):
        notify_audit (bool | Unset):
        notify_no_data (bool | Unset):
        on_missing_data (str | Unset):
        renotify_interval (int | Unset):
        renotify_occurrences (int | Unset):
        renotify_statuses (list[str] | Unset):
        require_full_window (bool | Unset):
        synthetics_check_id (str | Unset):
        thresholds (MonitorThresholds | Unset): MonitorThresholds represents thresholds for a monitor
        timeout_h (int | Unset):
        variables (list[MonitorVariable] | Unset):
    """

    device_ids: list[str] | Unset = UNSET
    enable_logs_sample: bool | Unset = UNSET
    escalation_message: str | Unset = UNSET
    evaluation_delay: int | Unset = UNSET
    groupby_simple_monitor: bool | Unset = UNSET
    include_tags: bool | Unset = UNSET
    min_failure_duration: int | Unset = UNSET
    min_location_failed: int | Unset = UNSET
    new_group_delay: int | Unset = UNSET
    new_host_delay: int | Unset = UNSET
    no_data_timeframe: int | Unset = UNSET
    notification_preset_name: str | Unset = UNSET
    notify_audit: bool | Unset = UNSET
    notify_no_data: bool | Unset = UNSET
    on_missing_data: str | Unset = UNSET
    renotify_interval: int | Unset = UNSET
    renotify_occurrences: int | Unset = UNSET
    renotify_statuses: list[str] | Unset = UNSET
    require_full_window: bool | Unset = UNSET
    synthetics_check_id: str | Unset = UNSET
    thresholds: MonitorThresholds | Unset = UNSET
    timeout_h: int | Unset = UNSET
    variables: list[MonitorVariable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_ids: list[str] | Unset = UNSET
        if not isinstance(self.device_ids, Unset):
            device_ids = self.device_ids

        enable_logs_sample = self.enable_logs_sample

        escalation_message = self.escalation_message

        evaluation_delay = self.evaluation_delay

        groupby_simple_monitor = self.groupby_simple_monitor

        include_tags = self.include_tags

        min_failure_duration = self.min_failure_duration

        min_location_failed = self.min_location_failed

        new_group_delay = self.new_group_delay

        new_host_delay = self.new_host_delay

        no_data_timeframe = self.no_data_timeframe

        notification_preset_name = self.notification_preset_name

        notify_audit = self.notify_audit

        notify_no_data = self.notify_no_data

        on_missing_data = self.on_missing_data

        renotify_interval = self.renotify_interval

        renotify_occurrences = self.renotify_occurrences

        renotify_statuses: list[str] | Unset = UNSET
        if not isinstance(self.renotify_statuses, Unset):
            renotify_statuses = self.renotify_statuses

        require_full_window = self.require_full_window

        synthetics_check_id = self.synthetics_check_id

        thresholds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = self.thresholds.to_dict()

        timeout_h = self.timeout_h

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_ids is not UNSET:
            field_dict["device_ids"] = device_ids
        if enable_logs_sample is not UNSET:
            field_dict["enable_logs_sample"] = enable_logs_sample
        if escalation_message is not UNSET:
            field_dict["escalation_message"] = escalation_message
        if evaluation_delay is not UNSET:
            field_dict["evaluation_delay"] = evaluation_delay
        if groupby_simple_monitor is not UNSET:
            field_dict["groupby_simple_monitor"] = groupby_simple_monitor
        if include_tags is not UNSET:
            field_dict["include_tags"] = include_tags
        if min_failure_duration is not UNSET:
            field_dict["min_failure_duration"] = min_failure_duration
        if min_location_failed is not UNSET:
            field_dict["min_location_failed"] = min_location_failed
        if new_group_delay is not UNSET:
            field_dict["new_group_delay"] = new_group_delay
        if new_host_delay is not UNSET:
            field_dict["new_host_delay"] = new_host_delay
        if no_data_timeframe is not UNSET:
            field_dict["no_data_timeframe"] = no_data_timeframe
        if notification_preset_name is not UNSET:
            field_dict["notification_preset_name"] = notification_preset_name
        if notify_audit is not UNSET:
            field_dict["notify_audit"] = notify_audit
        if notify_no_data is not UNSET:
            field_dict["notify_no_data"] = notify_no_data
        if on_missing_data is not UNSET:
            field_dict["on_missing_data"] = on_missing_data
        if renotify_interval is not UNSET:
            field_dict["renotify_interval"] = renotify_interval
        if renotify_occurrences is not UNSET:
            field_dict["renotify_occurrences"] = renotify_occurrences
        if renotify_statuses is not UNSET:
            field_dict["renotify_statuses"] = renotify_statuses
        if require_full_window is not UNSET:
            field_dict["require_full_window"] = require_full_window
        if synthetics_check_id is not UNSET:
            field_dict["synthetics_check_id"] = synthetics_check_id
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds
        if timeout_h is not UNSET:
            field_dict["timeout_h"] = timeout_h
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_thresholds import MonitorThresholds
        from ..models.monitor_variable import MonitorVariable

        d = dict(src_dict)
        device_ids = cast(list[str], d.pop("device_ids", UNSET))

        enable_logs_sample = d.pop("enable_logs_sample", UNSET)

        escalation_message = d.pop("escalation_message", UNSET)

        evaluation_delay = d.pop("evaluation_delay", UNSET)

        groupby_simple_monitor = d.pop("groupby_simple_monitor", UNSET)

        include_tags = d.pop("include_tags", UNSET)

        min_failure_duration = d.pop("min_failure_duration", UNSET)

        min_location_failed = d.pop("min_location_failed", UNSET)

        new_group_delay = d.pop("new_group_delay", UNSET)

        new_host_delay = d.pop("new_host_delay", UNSET)

        no_data_timeframe = d.pop("no_data_timeframe", UNSET)

        notification_preset_name = d.pop("notification_preset_name", UNSET)

        notify_audit = d.pop("notify_audit", UNSET)

        notify_no_data = d.pop("notify_no_data", UNSET)

        on_missing_data = d.pop("on_missing_data", UNSET)

        renotify_interval = d.pop("renotify_interval", UNSET)

        renotify_occurrences = d.pop("renotify_occurrences", UNSET)

        renotify_statuses = cast(list[str], d.pop("renotify_statuses", UNSET))

        require_full_window = d.pop("require_full_window", UNSET)

        synthetics_check_id = d.pop("synthetics_check_id", UNSET)

        _thresholds = d.pop("thresholds", UNSET)
        thresholds: MonitorThresholds | Unset
        if isinstance(_thresholds, Unset) or _thresholds is None:
            thresholds = UNSET
        else:
            thresholds = MonitorThresholds.from_dict(_thresholds)

        timeout_h = d.pop("timeout_h", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: list[MonitorVariable] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = MonitorVariable.from_dict(variables_item_data)

                variables.append(variables_item)

        monitor_options = cls(
            device_ids=device_ids,
            enable_logs_sample=enable_logs_sample,
            escalation_message=escalation_message,
            evaluation_delay=evaluation_delay,
            groupby_simple_monitor=groupby_simple_monitor,
            include_tags=include_tags,
            min_failure_duration=min_failure_duration,
            min_location_failed=min_location_failed,
            new_group_delay=new_group_delay,
            new_host_delay=new_host_delay,
            no_data_timeframe=no_data_timeframe,
            notification_preset_name=notification_preset_name,
            notify_audit=notify_audit,
            notify_no_data=notify_no_data,
            on_missing_data=on_missing_data,
            renotify_interval=renotify_interval,
            renotify_occurrences=renotify_occurrences,
            renotify_statuses=renotify_statuses,
            require_full_window=require_full_window,
            synthetics_check_id=synthetics_check_id,
            thresholds=thresholds,
            timeout_h=timeout_h,
            variables=variables,
        )

        monitor_options.additional_properties = d
        return monitor_options

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
