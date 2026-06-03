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


T = TypeVar("T", bound="SessionsFiltersRequestParams")


@_attrs_define
class SessionsFiltersRequestParams:
    """
    Attributes:
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        end (datetime.datetime | Unset):
        required (list[ColumnDefinesASearchableColumnAndItsProperties] | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        start (datetime.datetime | Unset):
    """

    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    required: list[ColumnDefinesASearchableColumnAndItsProperties] | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

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

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if end is not UNSET:
            field_dict["end"] = end
        if required is not UNSET:
            field_dict["required"] = required
        if sources is not UNSET:
            field_dict["sources"] = sources
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_defines_a_searchable_column_and_its_properties import (
            ColumnDefinesASearchableColumnAndItsProperties,
        )
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

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

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset) or _start is None:
            start = UNSET
        else:
            start = parse_datetime(_start)

        sessions_filters_request_params = cls(
            conditions=conditions,
            end=end,
            required=required,
            sources=sources,
            start=start,
        )

        sessions_filters_request_params.additional_properties = d
        return sessions_filters_request_params

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
