from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goals_search_request_is_one_page_of_the_goals_tab_sort import GoalsSearchRequestIsOnePageOfTheGoalsTabSort
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )


T = TypeVar("T", bound="GoalsSearchRequestIsOnePageOfTheGoalsTab")


@_attrs_define
class GoalsSearchRequestIsOnePageOfTheGoalsTab:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        start (datetime.datetime): Start time of the request range
        cursor (str | Unset): Cursor is the previous page's cursor. It expires after 15 minutes and is
            valid only with the same sources, query, time range, sort, evalFields, data scope and
            Eval catalog; any Eval edit makes it cursor_invalid.
        eval_fields (list[str] | Unset): EvalFields are Eval field references, <evalKey>.<fieldKey> from the catalog's
            evalKey and key,
            as in the query; at most 100.
        limit (int | Unset): Limit is the page size: 50 when 0, at most 200.
        query (str | Unset): Query is a gcQL filter; pipes are not supported yet. Free text searches the goal title as
            the other search routes do: each word matches a whole word of the title and a quoted phrase must also appear in
            it, ignoring case; title is also a filter field, where title:"..." is an exact match and title:*word* a case-
            insensitive LIKE. Each other term names a known field (a goal field, a short judgment field such as outcome, or
            <evalKey>.<fieldKey>).
            A value of an enum or boolean Eval field must be one of its options.
            The goal time field is timestamp; _time is not accepted.
            The request window is [start, end): end is exclusive.
        sort (GoalsSearchRequestIsOnePageOfTheGoalsTabSort | Unset): Sort is timestamp_desc when empty; no other order
            exists.
            timestamp_desc goalSortTimestampDesc
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Page-level conditions, ANDed
            with query; same fields and rules as query.
    """

    end: datetime.datetime
    start: datetime.datetime
    cursor: str | Unset = UNSET
    eval_fields: list[str] | Unset = UNSET
    limit: int | Unset = UNSET
    query: str | Unset = UNSET
    sort: GoalsSearchRequestIsOnePageOfTheGoalsTabSort | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        cursor = self.cursor

        eval_fields: list[str] | Unset = UNSET
        if not isinstance(self.eval_fields, Unset):
            eval_fields = self.eval_fields

        limit = self.limit

        query = self.query

        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

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
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if eval_fields is not UNSET:
            field_dict["evalFields"] = eval_fields
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if sort is not UNSET:
            field_dict["sort"] = sort
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

        start = parse_datetime(d.pop("start"))

        cursor = d.pop("cursor", UNSET)

        eval_fields = cast(list[str], d.pop("evalFields", UNSET))

        limit = d.pop("limit", UNSET)

        query = d.pop("query", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: GoalsSearchRequestIsOnePageOfTheGoalsTabSort | Unset
        if isinstance(_sort, Unset) or _sort is None:
            sort = UNSET
        else:
            sort = GoalsSearchRequestIsOnePageOfTheGoalsTabSort(_sort)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        goals_search_request_is_one_page_of_the_goals_tab = cls(
            end=end,
            start=start,
            cursor=cursor,
            eval_fields=eval_fields,
            limit=limit,
            query=query,
            sort=sort,
            sources=sources,
        )

        goals_search_request_is_one_page_of_the_goals_tab.additional_properties = d
        return goals_search_request_is_one_page_of_the_goals_tab

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
