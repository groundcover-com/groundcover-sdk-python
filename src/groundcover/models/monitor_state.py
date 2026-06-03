from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_state_groups import MonitorStateGroups


T = TypeVar("T", bound="MonitorState")


@_attrs_define
class MonitorState:
    """MonitorState represents the state of a monitor

    Attributes:
        groups (MonitorStateGroups | Unset):
    """

    groups: MonitorStateGroups | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_state_groups import MonitorStateGroups

        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: MonitorStateGroups | Unset
        if isinstance(_groups, Unset) or _groups is None:
            groups = UNSET
        else:
            groups = MonitorStateGroups.from_dict(_groups)

        monitor_state = cls(
            groups=groups,
        )

        monitor_state.additional_properties = d
        return monitor_state

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
