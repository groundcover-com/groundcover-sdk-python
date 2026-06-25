from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="UpdateViewRequest")


@_attrs_define
class UpdateViewRequest:
    """
    Attributes:
        current_revision (int | Unset):
        description (str | Unset):
        name (str | Unset):
        override (bool | Unset):
        preset (str | Unset):
        team (str | Unset):
        view_type (str | Unset):
    """

    current_revision: int | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    override: bool | Unset = UNSET
    preset: str | Unset = UNSET
    team: str | Unset = UNSET
    view_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_revision = self.current_revision

        description = self.description

        name = self.name

        override = self.override

        preset = self.preset

        team = self.team

        view_type = self.view_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_revision is not UNSET:
            field_dict["currentRevision"] = current_revision
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if override is not UNSET:
            field_dict["override"] = override
        if preset is not UNSET:
            field_dict["preset"] = preset
        if team is not UNSET:
            field_dict["team"] = team
        if view_type is not UNSET:
            field_dict["viewType"] = view_type

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
        current_revision = d.pop("currentRevision", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        override = d.pop("override", UNSET)

        preset = d.pop("preset", UNSET)

        team = d.pop("team", UNSET)

        view_type = d.pop("viewType", UNSET)

        update_view_request = cls(
            current_revision=current_revision,
            description=description,
            name=name,
            override=override,
            preset=preset,
            team=team,
            view_type=view_type,
        )

        update_view_request.additional_properties = d
        return update_view_request

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
