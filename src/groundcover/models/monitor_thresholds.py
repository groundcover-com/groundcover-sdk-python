from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MonitorThresholds")


@_attrs_define
class MonitorThresholds:
    """MonitorThresholds represents thresholds for a monitor

    Attributes:
        critical (float | Unset):
        critical_recovery (float | Unset):
        ok (float | Unset):
        unknown (float | Unset):
        warning (float | Unset):
        warning_recovery (float | Unset):
    """

    critical: float | Unset = UNSET
    critical_recovery: float | Unset = UNSET
    ok: float | Unset = UNSET
    unknown: float | Unset = UNSET
    warning: float | Unset = UNSET
    warning_recovery: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        critical = self.critical

        critical_recovery = self.critical_recovery

        ok = self.ok

        unknown = self.unknown

        warning = self.warning

        warning_recovery = self.warning_recovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if critical_recovery is not UNSET:
            field_dict["critical_recovery"] = critical_recovery
        if ok is not UNSET:
            field_dict["ok"] = ok
        if unknown is not UNSET:
            field_dict["unknown"] = unknown
        if warning is not UNSET:
            field_dict["warning"] = warning
        if warning_recovery is not UNSET:
            field_dict["warning_recovery"] = warning_recovery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        critical = d.pop("critical", UNSET)

        critical_recovery = d.pop("critical_recovery", UNSET)

        ok = d.pop("ok", UNSET)

        unknown = d.pop("unknown", UNSET)

        warning = d.pop("warning", UNSET)

        warning_recovery = d.pop("warning_recovery", UNSET)

        monitor_thresholds = cls(
            critical=critical,
            critical_recovery=critical_recovery,
            ok=ok,
            unknown=unknown,
            warning=warning,
            warning_recovery=warning_recovery,
        )

        monitor_thresholds.additional_properties = d
        return monitor_thresholds

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
