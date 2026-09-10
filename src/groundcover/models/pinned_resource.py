from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="PinnedResource")


@_attrs_define
class PinnedResource:
    """PinnedResource is one entry of a member's ordered pin list. PinOrder is
    exposed so a client that only reads this endpoint can still compute the next
    pin's number without also fetching the dashboards list.

        Attributes:
            name (str | Unset):
            pin_order (int | Unset):
            resource_type (str | Unset):
            resource_uuid (str | Unset):
    """

    name: str | Unset = UNSET
    pin_order: int | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        pin_order = self.pin_order

        resource_type = self.resource_type

        resource_uuid = self.resource_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if pin_order is not UNSET:
            field_dict["pinOrder"] = pin_order
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if resource_uuid is not UNSET:
            field_dict["resourceUuid"] = resource_uuid

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
        name = d.pop("name", UNSET)

        pin_order = d.pop("pinOrder", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        resource_uuid = d.pop("resourceUuid", UNSET)

        pinned_resource = cls(
            name=name,
            pin_order=pin_order,
            resource_type=resource_type,
            resource_uuid=resource_uuid,
        )

        pinned_resource.additional_properties = d
        return pinned_resource

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
