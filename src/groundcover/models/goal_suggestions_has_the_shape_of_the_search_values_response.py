from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.goal_suggestion import GoalSuggestion


T = TypeVar("T", bound="GoalSuggestionsHasTheShapeOfTheSearchValuesResponse")


@_attrs_define
class GoalSuggestionsHasTheShapeOfTheSearchValuesResponse:
    """
    Attributes:
        is_limit_reached (bool): IsLimitReached is true when more values exist than Limit.
        results (list[GoalSuggestion]):
    """

    is_limit_reached: bool
    results: list[GoalSuggestion]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_limit_reached = self.is_limit_reached

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isLimitReached": is_limit_reached,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.goal_suggestion import GoalSuggestion

        d = dict(src_dict)
        is_limit_reached = d.pop("isLimitReached")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = GoalSuggestion.from_dict(results_item_data)

            results.append(results_item)

        goal_suggestions_has_the_shape_of_the_search_values_response = cls(
            is_limit_reached=is_limit_reached,
            results=results,
        )

        goal_suggestions_has_the_shape_of_the_search_values_response.additional_properties = d
        return goal_suggestions_has_the_shape_of_the_search_values_response

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
