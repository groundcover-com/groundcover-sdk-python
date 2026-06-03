from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_list_item import MonitorListItem


T = TypeVar("T", bound="MonitorListResponse")


@_attrs_define
class MonitorListResponse:
    """
    Attributes:
        done (bool | Unset): Whether all matching results have been returned (no more pages).
        monitors (list[MonitorListItem] | Unset): List of monitors matching the criteria.
    """

    done: bool | Unset = UNSET
    monitors: list[MonitorListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        monitors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = []
            for monitors_item_data in self.monitors:
                monitors_item = monitors_item_data.to_dict()
                monitors.append(monitors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done is not UNSET:
            field_dict["done"] = done
        if monitors is not UNSET:
            field_dict["monitors"] = monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_list_item import MonitorListItem

        d = dict(src_dict)
        done = d.pop("done", UNSET)

        _monitors = d.pop("monitors", UNSET)
        monitors: list[MonitorListItem] | Unset = UNSET
        if _monitors is not UNSET:
            monitors = []
            for monitors_item_data in _monitors:
                monitors_item = MonitorListItem.from_dict(monitors_item_data)

                monitors.append(monitors_item)

        monitor_list_response = cls(
            done=done,
            monitors=monitors,
        )

        monitor_list_response.additional_properties = d
        return monitor_list_response

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
