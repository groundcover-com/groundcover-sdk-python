from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_skill_summary_is_the_compact_skill_representation_returned_by_list_ap_is import (
        AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs,
    )


T = TypeVar("T", bound="AgentListSkillsResponse200")


@_attrs_define
class AgentListSkillsResponse200:
    """
    Attributes:
        skills (list[AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs]):
        status (str):
    """

    skills: list[AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs]
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skills = []
        for skills_item_data in self.skills:
            skills_item = skills_item_data.to_dict()
            skills.append(skills_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "skills": skills,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_skill_summary_is_the_compact_skill_representation_returned_by_list_ap_is import (
            AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs,
        )

        d = dict(src_dict)
        skills = []
        _skills = d.pop("skills")
        for skills_item_data in _skills:
            skills_item = AgentSkillSummaryIsTheCompactSkillRepresentationReturnedByListAPIs.from_dict(skills_item_data)

            skills.append(skills_item)

        status = d.pop("status")

        agent_list_skills_response_200 = cls(
            skills=skills,
            status=status,
        )

        agent_list_skills_response_200.additional_properties = d
        return agent_list_skills_response_200

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
