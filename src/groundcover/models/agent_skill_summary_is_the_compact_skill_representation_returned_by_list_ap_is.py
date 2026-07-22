from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs")


@_attrs_define
class AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs:
    """
    Attributes:
        created_at (str):
        id (str):
        is_organizational (bool):
        is_provisioned (bool):
        name (str):
        revision (int):
        updated_at (str):
        when_to_use (str):
        description (None | str | Unset): Optional human-readable Skill description.
            Nullable: true
        identifier (None | str | Unset): Optional stable Skill identifier.
            Nullable: true
    """

    created_at: str
    id: str
    is_organizational: bool
    is_provisioned: bool
    name: str
    revision: int
    updated_at: str
    when_to_use: str
    description: None | str | Unset = UNSET
    identifier: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        is_organizational = self.is_organizational

        is_provisioned = self.is_provisioned

        name = self.name

        revision = self.revision

        updated_at = self.updated_at

        when_to_use = self.when_to_use

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "is_organizational": is_organizational,
                "is_provisioned": is_provisioned,
                "name": name,
                "revision": revision,
                "updated_at": updated_at,
                "when_to_use": when_to_use,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

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
        created_at = d.pop("created_at")

        id = d.pop("id")

        is_organizational = d.pop("is_organizational")

        is_provisioned = d.pop("is_provisioned")

        name = d.pop("name")

        revision = d.pop("revision")

        updated_at = d.pop("updated_at")

        when_to_use = d.pop("when_to_use")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        agent_skill_summary_is_the_compact_skill_representation_returned_by_list_ap_is = cls(
            created_at=created_at,
            id=id,
            is_organizational=is_organizational,
            is_provisioned=is_provisioned,
            name=name,
            revision=revision,
            updated_at=updated_at,
            when_to_use=when_to_use,
            description=description,
            identifier=identifier,
        )

        agent_skill_summary_is_the_compact_skill_representation_returned_by_list_ap_is.additional_properties = d
        return agent_skill_summary_is_the_compact_skill_representation_returned_by_list_ap_is

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
