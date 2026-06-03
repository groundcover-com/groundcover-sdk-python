from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group


T = TypeVar("T", bound="AdvancedDataScopeDefinesFineGrainedDataScopingRules")


@_attrs_define
class AdvancedDataScopeDefinesFineGrainedDataScopingRules:
    """
    Attributes:
        events (Group | Unset):
        logs (Group | Unset):
        metrics (Group | Unset):
        traces (Group | Unset):
        workloads (Group | Unset):
    """

    events: Group | Unset = UNSET
    logs: Group | Unset = UNSET
    metrics: Group | Unset = UNSET
    traces: Group | Unset = UNSET
    workloads: Group | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        logs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = self.logs.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        traces: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traces, Unset):
            traces = self.traces.to_dict()

        workloads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = self.workloads.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if logs is not UNSET:
            field_dict["logs"] = logs
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if traces is not UNSET:
            field_dict["traces"] = traces
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group import Group

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: Group | Unset
        if isinstance(_events, Unset) or _events is None:
            events = UNSET
        else:
            events = Group.from_dict(_events)

        _logs = d.pop("logs", UNSET)
        logs: Group | Unset
        if isinstance(_logs, Unset) or _logs is None:
            logs = UNSET
        else:
            logs = Group.from_dict(_logs)

        _metrics = d.pop("metrics", UNSET)
        metrics: Group | Unset
        if isinstance(_metrics, Unset) or _metrics is None:
            metrics = UNSET
        else:
            metrics = Group.from_dict(_metrics)

        _traces = d.pop("traces", UNSET)
        traces: Group | Unset
        if isinstance(_traces, Unset) or _traces is None:
            traces = UNSET
        else:
            traces = Group.from_dict(_traces)

        _workloads = d.pop("workloads", UNSET)
        workloads: Group | Unset
        if isinstance(_workloads, Unset) or _workloads is None:
            workloads = UNSET
        else:
            workloads = Group.from_dict(_workloads)

        advanced_data_scope_defines_fine_grained_data_scoping_rules = cls(
            events=events,
            logs=logs,
            metrics=metrics,
            traces=traces,
            workloads=workloads,
        )

        advanced_data_scope_defines_fine_grained_data_scoping_rules.additional_properties = d
        return advanced_data_scope_defines_fine_grained_data_scoping_rules

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
