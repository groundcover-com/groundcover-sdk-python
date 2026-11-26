from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goal_eval_result_state import GoalEvalResultState
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.goal_eval_value import GoalEvalValue


T = TypeVar("T", bound="GoalEvalResult")


@_attrs_define
class GoalEvalResult:
    """GoalEvalResult is the current result of one requested Eval field on a goal
    row, judged against the catalog the request read.

        Attributes:
            state (GoalEvalResultState): State is the state of the field's Eval result.
                pending EvalResultPending
                complete EvalResultComplete
                failed EvalResultFailed
                exhausted EvalResultExhausted
                skipped EvalResultSkipped
                disabled EvalResultDisabled
                outdated EvalResultOutdated
                unavailable EvalResultUnavailable
            value (GoalEvalValue | Unset): GoalEvalValue is one Eval field value; exactly the member that matches the
                field type is set. A field without a value of its type is left out.
    """

    state: GoalEvalResultState
    value: GoalEvalValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.goal_eval_value import GoalEvalValue

        d = dict(src_dict)
        state = GoalEvalResultState(d.pop("state"))

        _value = d.pop("value", UNSET)
        value: GoalEvalValue | Unset
        if isinstance(_value, Unset) or _value is None:
            value = UNSET
        else:
            value = GoalEvalValue.from_dict(_value)

        goal_eval_result = cls(
            state=state,
            value=value,
        )

        goal_eval_result.additional_properties = d
        return goal_eval_result

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
