from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subject_step_is_one_node_on_the_current_root_to_assigned_path import (
        SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath,
    )


T = TypeVar("T", bound="GoalSuggestion")


@_attrs_define
class GoalSuggestion:
    """GoalSuggestion is one value the caller may insert. Subject suggestions
    carry the current path so two children with the same label stay distinct,
    and so a parent filters its subtree. Count covers the full filtered window.

        Attributes:
            count (int): Count is the number of matching goals with this value.
            value (str):
            subject_id (str | Unset): SubjectID and SubjectPath, ordered root to subject, are set on subject suggestions
                only.
            subject_path (list[SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath] | Unset):
    """

    count: int
    value: str
    subject_id: str | Unset = UNSET
    subject_path: list[SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value = self.value

        subject_id = self.subject_id

        subject_path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_path, Unset):
            subject_path = []
            for subject_path_item_data in self.subject_path:
                subject_path_item = subject_path_item_data.to_dict()
                subject_path.append(subject_path_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "value": value,
            }
        )
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if subject_path is not UNSET:
            field_dict["subjectPath"] = subject_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subject_step_is_one_node_on_the_current_root_to_assigned_path import (
            SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath,
        )

        d = dict(src_dict)
        count = d.pop("count")

        value = d.pop("value")

        subject_id = d.pop("subjectId", UNSET)

        _subject_path = d.pop("subjectPath", UNSET)
        subject_path: list[SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath] | Unset = UNSET
        if _subject_path is not UNSET:
            subject_path = []
            for subject_path_item_data in _subject_path:
                subject_path_item = SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath.from_dict(subject_path_item_data)

                subject_path.append(subject_path_item)

        goal_suggestion = cls(
            count=count,
            value=value,
            subject_id=subject_id,
            subject_path=subject_path,
        )

        goal_suggestion.additional_properties = d
        return goal_suggestion

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
