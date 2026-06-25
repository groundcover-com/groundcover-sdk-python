from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor import Monitor


T = TypeVar("T", bound="ConvertMonitorRequest")


@_attrs_define
class ConvertMonitorRequest:
    """
    Attributes:
        monitor (Monitor | Unset): Monitor represents a Datadog monitor
        vendor (str | Unset): Vendor represents a supported observability vendor
    """

    monitor: Monitor | Unset = UNSET
    vendor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor import Monitor

        d = dict(src_dict)
        _monitor = d.pop("monitor", UNSET)
        monitor: Monitor | Unset
        if isinstance(_monitor, Unset) or _monitor is None:
            monitor = UNSET
        else:
            monitor = Monitor.from_dict(_monitor)

        vendor = d.pop("vendor", UNSET)

        convert_monitor_request = cls(
            monitor=monitor,
            vendor=vendor,
        )

        convert_monitor_request.additional_properties = d
        return convert_monitor_request

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
