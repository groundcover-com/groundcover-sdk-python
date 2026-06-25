from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DashboardSummary")


@_attrs_define
class DashboardSummary:
    """
    Attributes:
        description (str | Unset):
        name (str | Unset):
        origin_id (str | Unset):
        origin_type (str | Unset):
        uuid (str | Unset):
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    origin_id: str | Unset = UNSET
    origin_type: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        origin_id = self.origin_id

        origin_type = self.origin_type

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if origin_id is not UNSET:
            field_dict["originId"] = origin_id
        if origin_type is not UNSET:
            field_dict["originType"] = origin_type
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
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        origin_id = d.pop("originId", UNSET)

        origin_type = d.pop("originType", UNSET)

        uuid = d.pop("uuid", UNSET)

        dashboard_summary = cls(
            description=description,
            name=name,
            origin_id=origin_id,
            origin_type=origin_type,
            uuid=uuid,
        )

        dashboard_summary.additional_properties = d
        return dashboard_summary

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
