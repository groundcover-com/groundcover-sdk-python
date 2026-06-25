from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MonitorListItem")


@_attrs_define
class MonitorListItem:
    """
    Attributes:
        title (str | Unset): Title of the monitor.
        type_ (str | Unset): Type of the monitor.
        uuid (UUID | Unset): Unique identifier for the monitor.
            Format: uuid
    """

    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

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
        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset) or _uuid is None:
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        monitor_list_item = cls(
            title=title,
            type_=type_,
            uuid=uuid,
        )

        monitor_list_item.additional_properties = d
        return monitor_list_item

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
