from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates")


@_attrs_define
class AgentSkillRequestIsForwardedToAgentServiceForSkillCreationAndUpdates:
    """
    Attributes:
        instructions (str):
        name (str):
        when_to_use (str):
        description (None | str | Unset):
        is_organizational (bool | None | Unset): Whether the Skill is available to the whole organization. Defaults to
            false. Admin only.
            Nullable: true
    """

    instructions: str
    name: str
    when_to_use: str
    description: None | str | Unset = UNSET
    is_organizational: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instructions = self.instructions

        name = self.name

        when_to_use = self.when_to_use

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_organizational: bool | None | Unset
        if isinstance(self.is_organizational, Unset):
            is_organizational = UNSET
        else:
            is_organizational = self.is_organizational

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instructions": instructions,
                "name": name,
                "when_to_use": when_to_use,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_organizational is not UNSET:
            field_dict["is_organizational"] = is_organizational

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
        instructions = d.pop("instructions")

        name = d.pop("name")

        when_to_use = d.pop("when_to_use")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_organizational(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_organizational = _parse_is_organizational(d.pop("is_organizational", UNSET))

        agent_skill_request_is_forwarded_to_agent_service_for_skill_creation_and_updates = cls(
            instructions=instructions,
            name=name,
            when_to_use=when_to_use,
            description=description,
            is_organizational=is_organizational,
        )

        agent_skill_request_is_forwarded_to_agent_service_for_skill_creation_and_updates.additional_properties = d
        return agent_skill_request_is_forwarded_to_agent_service_for_skill_creation_and_updates

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
