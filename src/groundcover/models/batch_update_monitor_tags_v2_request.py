from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="BatchUpdateMonitorTagsV2Request")


@_attrs_define
class BatchUpdateMonitorTagsV2Request:
    """
    Attributes:
        monitor_uuids (list[UUID]):
        tags_to_add (list[str] | Unset): Tags to add to each monitor. Entries are trimmed and exact-case
            deduplicated. At least one of tagsToAdd or tagsToRemove must be non-empty
            after that, and the two lists must not share a tag (400 otherwise). A
            monitor may carry at most 20 tags afterwards (reported per monitor), so at
            most 20 distinct tags can be added.
        tags_to_remove (list[str] | Unset): Tags to remove from each monitor. Same rules as tagsToAdd; removing a tag
            a monitor does not carry is a no-op.
    """

    monitor_uuids: list[UUID]
    tags_to_add: list[str] | Unset = UNSET
    tags_to_remove: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_uuids = []
        for monitor_uuids_item_data in self.monitor_uuids:
            monitor_uuids_item = str(monitor_uuids_item_data)
            monitor_uuids.append(monitor_uuids_item)

        tags_to_add: list[str] | Unset = UNSET
        if not isinstance(self.tags_to_add, Unset):
            tags_to_add = self.tags_to_add

        tags_to_remove: list[str] | Unset = UNSET
        if not isinstance(self.tags_to_remove, Unset):
            tags_to_remove = self.tags_to_remove

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitorUuids": monitor_uuids,
            }
        )
        if tags_to_add is not UNSET:
            field_dict["tagsToAdd"] = tags_to_add
        if tags_to_remove is not UNSET:
            field_dict["tagsToRemove"] = tags_to_remove

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
        monitor_uuids = []
        _monitor_uuids = d.pop("monitorUuids")
        for monitor_uuids_item_data in _monitor_uuids:
            monitor_uuids_item = UUID(monitor_uuids_item_data)

            monitor_uuids.append(monitor_uuids_item)

        tags_to_add = cast(list[str], d.pop("tagsToAdd", UNSET))

        tags_to_remove = cast(list[str], d.pop("tagsToRemove", UNSET))

        batch_update_monitor_tags_v2_request = cls(
            monitor_uuids=monitor_uuids,
            tags_to_add=tags_to_add,
            tags_to_remove=tags_to_remove,
        )

        batch_update_monitor_tags_v2_request.additional_properties = d
        return batch_update_monitor_tags_v2_request

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
