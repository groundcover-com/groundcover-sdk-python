from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_author_type import InvestigationAuthorType
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="InvestigationAuthor")


@_attrs_define
class InvestigationAuthor:
    """
    Attributes:
        id (UUID):
        name (str):
        type_ (InvestigationAuthorType):
        agent_instance_id (str | Unset):
    """

    id: UUID
    name: str
    type_: InvestigationAuthorType
    agent_instance_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        agent_instance_id = self.agent_instance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
            }
        )
        if agent_instance_id is not UNSET:
            field_dict["agentInstanceId"] = agent_instance_id

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
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = InvestigationAuthorType(d.pop("type"))

        agent_instance_id = d.pop("agentInstanceId", UNSET)

        investigation_author = cls(
            id=id,
            name=name,
            type_=type_,
            agent_instance_id=agent_instance_id,
        )

        investigation_author.additional_properties = d
        return investigation_author

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
