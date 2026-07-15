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
    from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import SqlPipelineDefinesAPipelineForSearchQueries


T = TypeVar("T", bound="AwsCurSearchRequest")


@_attrs_define
class AwsCurSearchRequest:
    """AwsCurSearchRequest is the shared request body of the aws_cur search
    endpoints. Exactly one of Query or Pipeline must be provided. Unlike the
    apm/ingestion domains there are no mandatory top-level filters — every
    aws_cost_reports_v1 row is a cost line item.

        Attributes:
            end (datetime.datetime): End time of the request range
            start (datetime.datetime): Start time of the request range
            filters (str | Unset): Extra filters to apply on the cost report rows.
            pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
                container for the join operation ONLY.
                When Union is set, the pipeline acts as a container for the union operation ONLY.
                In these cases, no other fields should be used.
            query (str | Unset): GCQL query to filter cost report rows. Either `query` or `pipeline`
                must be provided.
            sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources to filter cost
                report rows.
    """

    end: datetime.datetime
    start: datetime.datetime
    filters: str | Unset = UNSET
    pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    query: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        filters = self.filters

        pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline, Unset):
            pipeline = self.pipeline.to_dict()

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
        if filters is not UNSET:
            field_dict["filters"] = filters
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
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
        from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import (
            SqlPipelineDefinesAPipelineForSearchQueries,
        )

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        start = parse_datetime(d.pop("start"))

        filters = d.pop("filters", UNSET)

        _pipeline = d.pop("pipeline", UNSET)
        pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset
        if isinstance(_pipeline, Unset) or _pipeline is None:
            pipeline = UNSET
        else:
            pipeline = SqlPipelineDefinesAPipelineForSearchQueries.from_dict(_pipeline)

        query = d.pop("query", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        aws_cur_search_request = cls(
            end=end,
            start=start,
            filters=filters,
            pipeline=pipeline,
            query=query,
            sources=sources,
        )

        aws_cur_search_request.additional_properties = d
        return aws_cur_search_request

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
