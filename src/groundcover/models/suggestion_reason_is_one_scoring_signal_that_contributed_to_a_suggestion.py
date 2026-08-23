from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SuggestionReasonIsOneScoringSignalThatContributedToASuggestion")


@_attrs_define
class SuggestionReasonIsOneScoringSignalThatContributedToASuggestion:
    """Weight is the signal's additive contribution within the scorer that produced
    it. Name-similarity signals and value-overlap signals are scored
    independently, so when both back the same candidate the suggestion carries
    reasons from each and Confidence is the higher of the two estimates rather
    than their sum — weights add up within a scorer, not across them.

    Detail carries the evidence behind the signal. For value-overlap signals that
    means the matched values themselves, which is what makes the difference
    between a suggestion worth acting on and one worth eyeballing.

        Attributes:
            code (str | Unset):
            detail (str | Unset):
            weight (float | Unset):
    """

    code: str | Unset = UNSET
    detail: str | Unset = UNSET
    weight: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        detail = self.detail

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail
        if weight is not UNSET:
            field_dict["weight"] = weight

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
        code = d.pop("code", UNSET)

        detail = d.pop("detail", UNSET)

        weight = d.pop("weight", UNSET)

        suggestion_reason_is_one_scoring_signal_that_contributed_to_a_suggestion = cls(
            code=code,
            detail=detail,
            weight=weight,
        )

        suggestion_reason_is_one_scoring_signal_that_contributed_to_a_suggestion.additional_properties = d
        return suggestion_reason_is_one_scoring_signal_that_contributed_to_a_suggestion

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
