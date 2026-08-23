from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suggestion_reason_is_one_scoring_signal_that_contributed_to_a_suggestion import (
        SuggestionReasonIsOneScoringSignalThatContributedToASuggestion,
    )


T = TypeVar("T", bound="SuggestionProposesAnAlternativeForAMissingResource")


@_attrs_define
class SuggestionProposesAnAlternativeForAMissingResource:
    """
    Attributes:
        confidence (float | Unset):
        reasons (list[SuggestionReasonIsOneScoringSignalThatContributedToASuggestion] | Unset):
        type_ (str | Unset):
        value (str | Unset):
    """

    confidence: float | Unset = UNSET
    reasons: list[SuggestionReasonIsOneScoringSignalThatContributedToASuggestion] | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item = reasons_item_data.to_dict()
                reasons.append(reasons_item)

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggestion_reason_is_one_scoring_signal_that_contributed_to_a_suggestion import (
            SuggestionReasonIsOneScoringSignalThatContributedToASuggestion,
        )

        d = dict(src_dict)
        confidence = d.pop("confidence", UNSET)

        _reasons = d.pop("reasons", UNSET)
        reasons: list[SuggestionReasonIsOneScoringSignalThatContributedToASuggestion] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = SuggestionReasonIsOneScoringSignalThatContributedToASuggestion.from_dict(
                    reasons_item_data
                )

                reasons.append(reasons_item)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        suggestion_proposes_an_alternative_for_a_missing_resource = cls(
            confidence=confidence,
            reasons=reasons,
            type_=type_,
            value=value,
        )

        suggestion_proposes_an_alternative_for_a_missing_resource.additional_properties = d
        return suggestion_proposes_an_alternative_for_a_missing_resource

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
