from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CreateDashboardRequest")


@_attrs_define
class CreateDashboardRequest:
    """
    Attributes:
        description (str | Unset):
        is_provisioned (bool | Unset):
        name (str | Unset):
        preset (str | Unset):
        tags (list[str] | Unset): Tags to attach to the dashboard (array of free-text strings; whitespace-trimmed,
            original casing preserved)
        team (str | Unset):
    """

    description: str | Unset = UNSET
    is_provisioned: bool | Unset = UNSET
    name: str | Unset = UNSET
    preset: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    team: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        is_provisioned = self.is_provisioned

        name = self.name

        preset = self.preset

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        team = self.team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if is_provisioned is not UNSET:
            field_dict["isProvisioned"] = is_provisioned
        if name is not UNSET:
            field_dict["name"] = name
        if preset is not UNSET:
            field_dict["preset"] = preset
        if tags is not UNSET:
            field_dict["tags"] = tags
        if team is not UNSET:
            field_dict["team"] = team

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

        is_provisioned = d.pop("isProvisioned", UNSET)

        name = d.pop("name", UNSET)

        preset = d.pop("preset", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        team = d.pop("team", UNSET)

        create_dashboard_request = cls(
            description=description,
            is_provisioned=is_provisioned,
            name=name,
            preset=preset,
            tags=tags,
            team=team,
        )

        create_dashboard_request.additional_properties = d
        return create_dashboard_request

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
