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


T = TypeVar("T", bound="GoalsAutocompleteRequest")


@_attrs_define
class GoalsAutocompleteRequest:
    """goalsAutocompleteRequest suggests values of Field that occur on visible
    goals matching Sources and Query. Prefix is the text still being typed; a
    condition of Query on Field with that value is the draft and is ignored,
    whatever its operator. Sources are never the draft.

        Attributes:
            end (datetime.datetime): End time of the request range
            field (str): Field is a string or string-array goal column other than title, or an Eval text, enum or boolean
                field.
            start (datetime.datetime): Start time of the request range
            limit (int | Unset): Limit is the number of suggestions: 20 when 0, at most 50.
            prefix (str | Unset): Prefix is the text still being typed; values start with it.
            query (str | Unset): Query is the gcQL filter being edited; pipes are not supported yet. Free text searches the
                goal title as the other search routes do: each word matches a whole word of the title and a quoted phrase must
                also appear in it, ignoring case; title is also a filter field, where title:"..." is an exact match and
                title:*word* a case-insensitive LIKE. Each other term names a known field (a goal field, a short judgment field
                such as outcome, or <evalKey>.<fieldKey>).
                A value of an enum or boolean Eval field must be one of its options.
                The goal time field is timestamp; _time is not accepted.
                The request window is [start, end): end is exclusive.
            sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Page-level conditions, ANDed
                with query; same fields and rules as query.
    """

    end: datetime.datetime
    field: str
    start: datetime.datetime
    limit: int | Unset = UNSET
    prefix: str | Unset = UNSET
    query: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        field = self.field

        start = self.start.isoformat()

        limit = self.limit

        prefix = self.prefix

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
                "field": field,
                "start": start,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
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

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        field = d.pop("field")

        start = parse_datetime(d.pop("start"))

        limit = d.pop("limit", UNSET)

        prefix = d.pop("prefix", UNSET)

        query = d.pop("query", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        goals_autocomplete_request = cls(
            end=end,
            field=field,
            start=start,
            limit=limit,
            prefix=prefix,
            query=query,
            sources=sources,
        )

        goals_autocomplete_request.additional_properties = d
        return goals_autocomplete_request

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
