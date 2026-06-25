from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linear_project_is_a_linear_project_for_a_team import LinearProjectIsALinearProjectForATeam


T = TypeVar("T", bound="LinearProjectListResponseContainsLinearProjectPickerResults")


@_attrs_define
class LinearProjectListResponseContainsLinearProjectPickerResults:
    """
    Attributes:
        projects (list[LinearProjectIsALinearProjectForATeam] | Unset):
        truncated (bool | Unset):
    """

    projects: list[LinearProjectIsALinearProjectForATeam] | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linear_project_is_a_linear_project_for_a_team import LinearProjectIsALinearProjectForATeam

        d = dict(src_dict)
        _projects = d.pop("projects", UNSET)
        projects: list[LinearProjectIsALinearProjectForATeam] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = LinearProjectIsALinearProjectForATeam.from_dict(projects_item_data)

                projects.append(projects_item)

        truncated = d.pop("truncated", UNSET)

        linear_project_list_response_contains_linear_project_picker_results = cls(
            projects=projects,
            truncated=truncated,
        )

        linear_project_list_response_contains_linear_project_picker_results.additional_properties = d
        return linear_project_list_response_contains_linear_project_picker_results

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
