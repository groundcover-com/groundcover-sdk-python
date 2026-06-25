from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.group import Group


T = TypeVar("T", bound="LogsPatternsParamDistributionRequestParams")


@_attrs_define
class LogsPatternsParamDistributionRequestParams:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        start (datetime.datetime): Start time of the request range
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        group (Group | Unset):
        limit (int | Unset):
        param_index (int | Unset):
        pattern (str | Unset):
        pattern_id (int | Unset):
        query (str | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
    """

    end: datetime.datetime
    start: datetime.datetime
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    group: Group | Unset = UNSET
    limit: int | Unset = UNSET
    param_index: int | Unset = UNSET
    pattern: str | Unset = UNSET
    pattern_id: int | Unset = UNSET
    query: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        limit = self.limit

        param_index = self.param_index

        pattern = self.pattern

        pattern_id = self.pattern_id

        query = self.query

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if group is not UNSET:
            field_dict["group"] = group
        if limit is not UNSET:
            field_dict["limit"] = limit
        if param_index is not UNSET:
            field_dict["paramIndex"] = param_index
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if pattern_id is not UNSET:
            field_dict["patternId"] = pattern_id
        if query is not UNSET:
            field_dict["query"] = query
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.group import Group

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        start = parse_datetime(d.pop("start"))

        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        limit = d.pop("limit", UNSET)

        param_index = d.pop("paramIndex", UNSET)

        pattern = d.pop("pattern", UNSET)

        pattern_id = d.pop("patternId", UNSET)

        query = d.pop("query", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        logs_patterns_param_distribution_request_params = cls(
            end=end,
            start=start,
            conditions=conditions,
            group=group,
            limit=limit,
            param_index=param_index,
            pattern=pattern,
            pattern_id=pattern_id,
            query=query,
            sources=sources,
        )

        logs_patterns_param_distribution_request_params.additional_properties = d
        return logs_patterns_param_distribution_request_params

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
