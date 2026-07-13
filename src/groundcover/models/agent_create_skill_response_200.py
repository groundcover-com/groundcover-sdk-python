from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.write_ap_is import WriteAPIs


T = TypeVar("T", bound="AgentCreateSkillResponse200")


@_attrs_define
class AgentCreateSkillResponse200:
    """
    Attributes:
        skill (WriteAPIs):
        status (str):
    """

    skill: WriteAPIs
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skill = self.skill.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "skill": skill,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.write_ap_is import WriteAPIs

        d = dict(src_dict)
        skill = WriteAPIs.from_dict(d.pop("skill"))

        status = d.pop("status")

        agent_create_skill_response_200 = cls(
            skill=skill,
            status=status,
        )

        agent_create_skill_response_200.additional_properties = d
        return agent_create_skill_response_200

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
