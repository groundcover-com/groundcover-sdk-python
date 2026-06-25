from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentCustomInstructions")


@_attrs_define
class AgentCustomInstructions:
    """AgentCustomInstructions is the custom instructions payload returned by
    agent-service for reads and upserts.

        Attributes:
            instructions (str | Unset): The custom instructions text ("" when none are configured).
            updated_at (str | Unset): When the instructions were last updated (ISO-8601), if set.
            updated_by (str | Unset): Identifier of whoever last updated the instructions, if known.
    """

    instructions: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instructions = self.instructions

        updated_at = self.updated_at

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

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
        instructions = d.pop("instructions", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        agent_custom_instructions = cls(
            instructions=instructions,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        agent_custom_instructions.additional_properties = d
        return agent_custom_instructions

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
