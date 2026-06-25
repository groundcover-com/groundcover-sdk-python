from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unsupported_breakdown_is_the_level_4_summary_why_are_things_unsupported import (
        UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupported,
    )


T = TypeVar("T", bound="UnsupportedCountsForTheUnifiedSummary")


@_attrs_define
class UnsupportedCountsForTheUnifiedSummary:
    """
    Attributes:
        supported (int | Unset):
        unsupported (int | Unset):
        unsupported_breakdown (UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupported | Unset): Grouped first by
            asset type, then by the specific reason (conversion error message).
    """

    supported: int | Unset = UNSET
    unsupported: int | Unset = UNSET
    unsupported_breakdown: UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupported | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supported = self.supported

        unsupported = self.unsupported

        unsupported_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unsupported_breakdown, Unset):
            unsupported_breakdown = self.unsupported_breakdown.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supported is not UNSET:
            field_dict["supported"] = supported
        if unsupported is not UNSET:
            field_dict["unsupported"] = unsupported
        if unsupported_breakdown is not UNSET:
            field_dict["unsupported_breakdown"] = unsupported_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unsupported_breakdown_is_the_level_4_summary_why_are_things_unsupported import (
            UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupported,
        )

        d = dict(src_dict)
        supported = d.pop("supported", UNSET)

        unsupported = d.pop("unsupported", UNSET)

        _unsupported_breakdown = d.pop("unsupported_breakdown", UNSET)
        unsupported_breakdown: UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupported | Unset
        if isinstance(_unsupported_breakdown, Unset) or _unsupported_breakdown is None:
            unsupported_breakdown = UNSET
        else:
            unsupported_breakdown = UnsupportedBreakdownIsTheLevel4SummaryWhyAreThingsUnsupported.from_dict(
                _unsupported_breakdown
            )

        unsupported_counts_for_the_unified_summary = cls(
            supported=supported,
            unsupported=unsupported,
            unsupported_breakdown=unsupported_breakdown,
        )

        unsupported_counts_for_the_unified_summary.additional_properties = d
        return unsupported_counts_for_the_unified_summary

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
