from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )


T = TypeVar("T", bound="LogParseGroupsRequest")


@_attrs_define
class LogParseGroupsRequest:
    """
    Attributes:
        max_pattern_groups (int | Unset): Maximum number of distinct pattern groups to generate
        query (str | Unset): GCQL Query to filter logs
        sample_min_top_pattern_percent (float | Unset): Minimum top pattern percent to include in the sample
        sample_time_interval (int | Unset): Duration wraps time.Duration. It is used to parse the custom duration format
            from YAML.
            This type should not propagate beyond the scope of input/output processing.
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources to filter logs
    """

    max_pattern_groups: int | Unset = UNSET
    query: str | Unset = UNSET
    sample_min_top_pattern_percent: float | Unset = UNSET
    sample_time_interval: int | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_pattern_groups = self.max_pattern_groups

        query = self.query

        sample_min_top_pattern_percent = self.sample_min_top_pattern_percent

        sample_time_interval = self.sample_time_interval

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_pattern_groups is not UNSET:
            field_dict["maxPatternGroups"] = max_pattern_groups
        if query is not UNSET:
            field_dict["query"] = query
        if sample_min_top_pattern_percent is not UNSET:
            field_dict["sampleMinTopPatternPercent"] = sample_min_top_pattern_percent
        if sample_time_interval is not UNSET:
            field_dict["sampleTimeInterval"] = sample_time_interval
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        max_pattern_groups = d.pop("maxPatternGroups", UNSET)

        query = d.pop("query", UNSET)

        sample_min_top_pattern_percent = d.pop("sampleMinTopPatternPercent", UNSET)

        sample_time_interval = d.pop("sampleTimeInterval", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        log_parse_groups_request = cls(
            max_pattern_groups=max_pattern_groups,
            query=query,
            sample_min_top_pattern_percent=sample_min_top_pattern_percent,
            sample_time_interval=sample_time_interval,
            sources=sources,
        )

        log_parse_groups_request.additional_properties = d
        return log_parse_groups_request

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
