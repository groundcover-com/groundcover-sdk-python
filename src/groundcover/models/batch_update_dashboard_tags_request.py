from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="BatchUpdateDashboardTagsRequest")


@_attrs_define
class BatchUpdateDashboardTagsRequest:
    """
    Attributes:
        dashboard_uuids (list[UUID]):
        tags_to_add (list[str] | Unset): Tags to append to each dashboard. Entries are trimmed and exact-case
            deduplicated. At least one of tagsToAdd or tagsToRemove must be non-empty
            after normalization, and the two lists must not share a tag (400
            otherwise). 1000 is a resource-exhaustion bound, not a product tag limit:
            MAX_TAGS_PER_VIEW applies to each dashboard's resulting set
            (too_many_tags), not to the delta lists.
        tags_to_remove (list[str] | Unset): Tags to remove from each dashboard. Same normalization and disjointness
            rules as tagsToAdd; removing a tag a dashboard does not carry is a no-op.
    """

    dashboard_uuids: list[UUID]
    tags_to_add: list[str] | Unset = UNSET
    tags_to_remove: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboard_uuids = []
        for dashboard_uuids_item_data in self.dashboard_uuids:
            dashboard_uuids_item = str(dashboard_uuids_item_data)
            dashboard_uuids.append(dashboard_uuids_item)

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
                "dashboardUuids": dashboard_uuids,
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
        dashboard_uuids = []
        _dashboard_uuids = d.pop("dashboardUuids")
        for dashboard_uuids_item_data in _dashboard_uuids:
            dashboard_uuids_item = UUID(dashboard_uuids_item_data)

            dashboard_uuids.append(dashboard_uuids_item)

        tags_to_add = cast(list[str], d.pop("tagsToAdd", UNSET))

        tags_to_remove = cast(list[str], d.pop("tagsToRemove", UNSET))

        batch_update_dashboard_tags_request = cls(
            dashboard_uuids=dashboard_uuids,
            tags_to_add=tags_to_add,
            tags_to_remove=tags_to_remove,
        )

        batch_update_dashboard_tags_request.additional_properties = d
        return batch_update_dashboard_tags_request

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
