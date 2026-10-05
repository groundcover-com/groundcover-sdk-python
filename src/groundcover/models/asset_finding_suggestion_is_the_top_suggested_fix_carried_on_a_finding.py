from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_finding_suggestion_is_the_top_suggested_fix_carried_on_a_finding_kind import (
    AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFindingKind,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding")


@_attrs_define
class AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding:
    """
    Attributes:
        applied_at (datetime.datetime | Unset): Set when the suggestion is already applied, automatically or by a user.
        confidence (float | Unset): How sure the suggestion is, from 0 to 1. A rule the tenant already has is 1.
        kind (AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFindingKind | Unset): Kind of rule the suggestion
            would create.
        reason (str | Unset): Top reason code behind the suggestion.
        value (str | Unset): The suggested groundcover-side value.
    """

    applied_at: datetime.datetime | Unset = UNSET
    confidence: float | Unset = UNSET
    kind: AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFindingKind | Unset = UNSET
    reason: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_at: str | Unset = UNSET
        if not isinstance(self.applied_at, Unset):
            applied_at = self.applied_at.isoformat()

        confidence = self.confidence

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        reason = self.reason

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_at is not UNSET:
            field_dict["applied_at"] = applied_at
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if kind is not UNSET:
            field_dict["kind"] = kind
        if reason is not UNSET:
            field_dict["reason"] = reason
        if value is not UNSET:
            field_dict["value"] = value

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
        _applied_at = d.pop("applied_at", UNSET)
        applied_at: datetime.datetime | Unset
        if isinstance(_applied_at, Unset) or _applied_at is None:
            applied_at = UNSET
        else:
            applied_at = parse_datetime(_applied_at)

        confidence = d.pop("confidence", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFindingKind | Unset
        if isinstance(_kind, Unset) or _kind is None:
            kind = UNSET
        else:
            kind = AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFindingKind(_kind)

        reason = d.pop("reason", UNSET)

        value = d.pop("value", UNSET)

        asset_finding_suggestion_is_the_top_suggested_fix_carried_on_a_finding = cls(
            applied_at=applied_at,
            confidence=confidence,
            kind=kind,
            reason=reason,
            value=value,
        )

        asset_finding_suggestion_is_the_top_suggested_fix_carried_on_a_finding.additional_properties = d
        return asset_finding_suggestion_is_the_top_suggested_fix_carried_on_a_finding

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
