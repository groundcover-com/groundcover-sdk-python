from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="BatchGetMonitorsRequest")


@_attrs_define
class BatchGetMonitorsRequest:
    """
    Attributes:
        monitor_uui_ds (list[UUID] | Unset):
    """

    monitor_uui_ds: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_uui_ds: list[str] | Unset = UNSET
        if not isinstance(self.monitor_uui_ds, Unset):
            monitor_uui_ds = []
            for monitor_uui_ds_item_data in self.monitor_uui_ds:
                monitor_uui_ds_item = str(monitor_uui_ds_item_data)
                monitor_uui_ds.append(monitor_uui_ds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor_uui_ds is not UNSET:
            field_dict["monitorUUIDs"] = monitor_uui_ds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        _monitor_uui_ds = d.pop("monitorUUIDs", UNSET)
        monitor_uui_ds: list[UUID] | Unset = UNSET
        if _monitor_uui_ds is not UNSET:
            monitor_uui_ds = []
            for monitor_uui_ds_item_data in _monitor_uui_ds:
                monitor_uui_ds_item = UUID(monitor_uui_ds_item_data)

                monitor_uui_ds.append(monitor_uui_ds_item)

        batch_get_monitors_request = cls(
            monitor_uui_ds=monitor_uui_ds,
        )

        batch_get_monitors_request.additional_properties = d
        return batch_get_monitors_request

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
