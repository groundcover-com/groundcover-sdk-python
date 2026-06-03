from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pattern_data import PatternData


T = TypeVar("T", bound="LogsPatternsResponse")


@_attrs_define
class LogsPatternsResponse:
    """
    Attributes:
        limit_reached (bool | Unset):
        patterns (list[PatternData] | Unset):
    """

    limit_reached: bool | Unset = UNSET
    patterns: list[PatternData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_reached = self.limit_reached

        patterns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.patterns, Unset):
            patterns = []
            for patterns_item_data in self.patterns:
                patterns_item = patterns_item_data.to_dict()
                patterns.append(patterns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_reached is not UNSET:
            field_dict["limitReached"] = limit_reached
        if patterns is not UNSET:
            field_dict["patterns"] = patterns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pattern_data import PatternData

        d = dict(src_dict)
        limit_reached = d.pop("limitReached", UNSET)

        _patterns = d.pop("patterns", UNSET)
        patterns: list[PatternData] | Unset = UNSET
        if _patterns is not UNSET:
            patterns = []
            for patterns_item_data in _patterns:
                patterns_item = PatternData.from_dict(patterns_item_data)

                patterns.append(patterns_item)

        logs_patterns_response = cls(
            limit_reached=limit_reached,
            patterns=patterns,
        )

        logs_patterns_response.additional_properties = d
        return logs_patterns_response

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
