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


T = TypeVar("T", bound="IngestionMeasurementsSearchTimeSeriesRequest")


@_attrs_define
class IngestionMeasurementsSearchTimeSeriesRequest:
    """IngestionMeasurementsSearchTimeSeriesRequest extends the search request with time-series
    specific fields: BucketDuration (required), an optional ValueField to aggregate, and an
    optional FillValue for empty buckets.

        Attributes:
            end (datetime.datetime): End time of the request range
            start (datetime.datetime): Start time of the request range
            bucket_duration (str | Unset):
            fill_value (float | Unset): Value used to fill empty time buckets in the response. When omitted,
                empty buckets are filled with null.
            filters (str | Unset): Extra filters to apply on the ingestion measurements.
            pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
                container for the join operation ONLY.
                When Union is set, the pipeline acts as a container for the union operation ONLY.
                In these cases, no other fields should be used.
            query (str | Unset): GCQL query to filter ingestion measurements. Either `query` or
                `pipeline` must be provided. The query MUST include exactly one
                top-level `signal_type` filter and exactly one top-level
                `pipeline_stage` filter.
            sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources to filter ingestion
                measurements.
            value_field (str | Unset):
    """

    end: datetime.datetime
    start: datetime.datetime
    bucket_duration: str | Unset = UNSET
    fill_value: float | Unset = UNSET
    filters: str | Unset = UNSET
    pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    query: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    value_field: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        bucket_duration = self.bucket_duration

        fill_value = self.fill_value

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

        value_field = self.value_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if bucket_duration is not UNSET:
            field_dict["bucketDuration"] = bucket_duration
        if fill_value is not UNSET:
            field_dict["fillValue"] = fill_value
        if filters is not UNSET:
            field_dict["filters"] = filters
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if query is not UNSET:
            field_dict["query"] = query
        if sources is not UNSET:
            field_dict["sources"] = sources
        if value_field is not UNSET:
            field_dict["valueField"] = value_field

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

        bucket_duration = d.pop("bucketDuration", UNSET)

        fill_value = d.pop("fillValue", UNSET)

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

        value_field = d.pop("valueField", UNSET)

        ingestion_measurements_search_time_series_request = cls(
            end=end,
            start=start,
            bucket_duration=bucket_duration,
            fill_value=fill_value,
            filters=filters,
            pipeline=pipeline,
            query=query,
            sources=sources,
            value_field=value_field,
        )

        ingestion_measurements_search_time_series_request.additional_properties = d
        return ingestion_measurements_search_time_series_request

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
