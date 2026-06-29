from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_defines_a_searchable_column_and_its_properties import (
        ColumnDefinesASearchableColumnAndItsProperties,
    )
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.group import Group


T = TypeVar("T", bound="LogsFiltersRequestParams")


@_attrs_define
class LogsFiltersRequestParams:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        start (datetime.datetime): Start time of the request range
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        enable_estimate (bool | Unset):
        enable_stream (bool | Unset):
        group (Group | Unset):
        limit_per_category (int | Unset):
        query (str | Unset):
        required (list[ColumnDefinesASearchableColumnAndItsProperties] | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
    """

    end: datetime.datetime
    start: datetime.datetime
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    enable_estimate: bool | Unset = UNSET
    enable_stream: bool | Unset = UNSET
    group: Group | Unset = UNSET
    limit_per_category: int | Unset = UNSET
    query: str | Unset = UNSET
    required: list[ColumnDefinesASearchableColumnAndItsProperties] | Unset = UNSET
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

        enable_estimate = self.enable_estimate

        enable_stream = self.enable_stream

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        limit_per_category = self.limit_per_category

        query = self.query

        required: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = []
            for required_item_data in self.required:
                required_item = required_item_data.to_dict()
                required.append(required_item)

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
        if enable_estimate is not UNSET:
            field_dict["enableEstimate"] = enable_estimate
        if enable_stream is not UNSET:
            field_dict["enableStream"] = enable_stream
        if group is not UNSET:
            field_dict["group"] = group
        if limit_per_category is not UNSET:
            field_dict["limitPerCategory"] = limit_per_category
        if query is not UNSET:
            field_dict["query"] = query
        if required is not UNSET:
            field_dict["required"] = required
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_defines_a_searchable_column_and_its_properties import (
            ColumnDefinesASearchableColumnAndItsProperties,
        )
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

        enable_estimate = d.pop("enableEstimate", UNSET)

        enable_stream = d.pop("enableStream", UNSET)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        limit_per_category = d.pop("limitPerCategory", UNSET)

        query = d.pop("query", UNSET)

        _required = d.pop("required", UNSET)
        required: list[ColumnDefinesASearchableColumnAndItsProperties] | Unset = UNSET
        if _required is not UNSET:
            required = []
            for required_item_data in _required:
                required_item = ColumnDefinesASearchableColumnAndItsProperties.from_dict(required_item_data)

                required.append(required_item)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        logs_filters_request_params = cls(
            end=end,
            start=start,
            conditions=conditions,
            enable_estimate=enable_estimate,
            enable_stream=enable_stream,
            group=group,
            limit_per_category=limit_per_category,
            query=query,
            required=required,
            sources=sources,
        )

        logs_filters_request_params.additional_properties = d
        return logs_filters_request_params

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
