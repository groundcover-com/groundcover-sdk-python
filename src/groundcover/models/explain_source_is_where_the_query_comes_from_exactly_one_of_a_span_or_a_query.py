from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_source_is_a_query_the_caller_writes_it_need_not_have_run import (
        QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun,
    )
    from ..models.span_source import SpanSource


T = TypeVar("T", bound="ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery")


@_attrs_define
class ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery:
    """
    Attributes:
        query (QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun | Unset):
        span (SpanSource | Unset):
    """

    query: QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun | Unset = UNSET
    span: SpanSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        span: dict[str, Any] | Unset = UNSET
        if not isinstance(self.span, Unset):
            span = self.span.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if span is not UNSET:
            field_dict["span"] = span

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_source_is_a_query_the_caller_writes_it_need_not_have_run import (
            QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun,
        )
        from ..models.span_source import SpanSource

        d = dict(src_dict)
        _query = d.pop("query", UNSET)
        query: QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun | Unset
        if isinstance(_query, Unset) or _query is None:
            query = UNSET
        else:
            query = QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun.from_dict(_query)

        _span = d.pop("span", UNSET)
        span: SpanSource | Unset
        if isinstance(_span, Unset) or _span is None:
            span = UNSET
        else:
            span = SpanSource.from_dict(_span)

        explain_source_is_where_the_query_comes_from_exactly_one_of_a_span_or_a_query = cls(
            query=query,
            span=span,
        )

        explain_source_is_where_the_query_comes_from_exactly_one_of_a_span_or_a_query.additional_properties = d
        return explain_source_is_where_the_query_comes_from_exactly_one_of_a_span_or_a_query

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
