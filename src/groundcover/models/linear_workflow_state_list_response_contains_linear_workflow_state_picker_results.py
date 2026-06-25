from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linear_workflow_state_is_a_linear_workflow_state_for_a_team import (
        LinearWorkflowStateIsALinearWorkflowStateForATeam,
    )


T = TypeVar("T", bound="LinearWorkflowStateListResponseContainsLinearWorkflowStatePickerResults")


@_attrs_define
class LinearWorkflowStateListResponseContainsLinearWorkflowStatePickerResults:
    """
    Attributes:
        states (list[LinearWorkflowStateIsALinearWorkflowStateForATeam] | Unset):
        truncated (bool | Unset):
    """

    states: list[LinearWorkflowStateIsALinearWorkflowStateForATeam] | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if states is not UNSET:
            field_dict["states"] = states
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linear_workflow_state_is_a_linear_workflow_state_for_a_team import (
            LinearWorkflowStateIsALinearWorkflowStateForATeam,
        )

        d = dict(src_dict)
        _states = d.pop("states", UNSET)
        states: list[LinearWorkflowStateIsALinearWorkflowStateForATeam] | Unset = UNSET
        if _states is not UNSET:
            states = []
            for states_item_data in _states:
                states_item = LinearWorkflowStateIsALinearWorkflowStateForATeam.from_dict(states_item_data)

                states.append(states_item)

        truncated = d.pop("truncated", UNSET)

        linear_workflow_state_list_response_contains_linear_workflow_state_picker_results = cls(
            states=states,
            truncated=truncated,
        )

        linear_workflow_state_list_response_contains_linear_workflow_state_picker_results.additional_properties = d
        return linear_workflow_state_list_response_contains_linear_workflow_state_picker_results

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
