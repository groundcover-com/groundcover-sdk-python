from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.synthetic_test_monitor import SyntheticTestMonitor


T = TypeVar("T", bound="SyntheticTestListItem")


@_attrs_define
class SyntheticTestListItem:
    """
    Attributes:
        creator (str | Unset):
        id (str | Unset):
        interval (str | Unset):
        last_check_latency (str | Unset):
        last_check_time (str | Unset):
        modified_at (str | Unset):
        monitor (SyntheticTestMonitor | Unset):
        name (str | Unset):
        status (str | Unset):
        synthetic_type (str | Unset):
        target (str | Unset):
    """

    creator: str | Unset = UNSET
    id: str | Unset = UNSET
    interval: str | Unset = UNSET
    last_check_latency: str | Unset = UNSET
    last_check_time: str | Unset = UNSET
    modified_at: str | Unset = UNSET
    monitor: SyntheticTestMonitor | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    synthetic_type: str | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator = self.creator

        id = self.id

        interval = self.interval

        last_check_latency = self.last_check_latency

        last_check_time = self.last_check_time

        modified_at = self.modified_at

        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        name = self.name

        status = self.status

        synthetic_type = self.synthetic_type

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if interval is not UNSET:
            field_dict["interval"] = interval
        if last_check_latency is not UNSET:
            field_dict["lastCheckLatency"] = last_check_latency
        if last_check_time is not UNSET:
            field_dict["lastCheckTime"] = last_check_time
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if synthetic_type is not UNSET:
            field_dict["syntheticType"] = synthetic_type
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.synthetic_test_monitor import SyntheticTestMonitor

        d = dict(src_dict)
        creator = d.pop("creator", UNSET)

        id = d.pop("id", UNSET)

        interval = d.pop("interval", UNSET)

        last_check_latency = d.pop("lastCheckLatency", UNSET)

        last_check_time = d.pop("lastCheckTime", UNSET)

        modified_at = d.pop("modifiedAt", UNSET)

        _monitor = d.pop("monitor", UNSET)
        monitor: SyntheticTestMonitor | Unset
        if isinstance(_monitor, Unset) or _monitor is None:
            monitor = UNSET
        else:
            monitor = SyntheticTestMonitor.from_dict(_monitor)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        synthetic_type = d.pop("syntheticType", UNSET)

        target = d.pop("target", UNSET)

        synthetic_test_list_item = cls(
            creator=creator,
            id=id,
            interval=interval,
            last_check_latency=last_check_latency,
            last_check_time=last_check_time,
            modified_at=modified_at,
            monitor=monitor,
            name=name,
            status=status,
            synthetic_type=synthetic_type,
            target=target,
        )

        synthetic_test_list_item.additional_properties = d
        return synthetic_test_list_item

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
