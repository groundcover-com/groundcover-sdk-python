from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.goal_row_is_one_published_goal_on_the_list import GoalRowIsOnePublishedGoalOnTheList


T = TypeVar("T", bound="GoalListPageIsOnePageAndTheCursorForThePageAfterIt")


@_attrs_define
class GoalListPageIsOnePageAndTheCursorForThePageAfterIt:
    """
    Attributes:
        goals (list[GoalRowIsOnePublishedGoalOnTheList]):
        cursor (str | Unset): Cursor is absent on the last page.
    """

    goals: list[GoalRowIsOnePublishedGoalOnTheList]
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goals = []
        for goals_item_data in self.goals:
            goals_item = goals_item_data.to_dict()
            goals.append(goals_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goals": goals,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.goal_row_is_one_published_goal_on_the_list import GoalRowIsOnePublishedGoalOnTheList

        d = dict(src_dict)
        goals = []
        _goals = d.pop("goals")
        for goals_item_data in _goals:
            goals_item = GoalRowIsOnePublishedGoalOnTheList.from_dict(goals_item_data)

            goals.append(goals_item)

        cursor = d.pop("cursor", UNSET)

        goal_list_page_is_one_page_and_the_cursor_for_the_page_after_it = cls(
            goals=goals,
            cursor=cursor,
        )

        goal_list_page_is_one_page_and_the_cursor_for_the_page_after_it.additional_properties = d
        return goal_list_page_is_one_page_and_the_cursor_for_the_page_after_it

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
