from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan")


@_attrs_define
class ExecutedQueryIsTheEvidenceForAUnitsWetOutcomeTheQueryThatRan:
    """the window it ran over, and what came back.

    Attributes:
        datasource (str | Unset):
        error (str | Unset):
        language (str | Unset):
        metric (str | Unset): Metric names the query's underlying metric, for datasource == "metrics"
            only. Without it a metrics query that returned no data cannot be traced
            back to which metric was empty without parsing the query text.
        original_dd (str | Unset):
        query (str | Unset):
        query_id (str | Unset):
        resolved_query (str | Unset):
        status (str | Unset):
        window (str | Unset):
    """

    datasource: str | Unset = UNSET
    error: str | Unset = UNSET
    language: str | Unset = UNSET
    metric: str | Unset = UNSET
    original_dd: str | Unset = UNSET
    query: str | Unset = UNSET
    query_id: str | Unset = UNSET
    resolved_query: str | Unset = UNSET
    status: str | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource = self.datasource

        error = self.error

        language = self.language

        metric = self.metric

        original_dd = self.original_dd

        query = self.query

        query_id = self.query_id

        resolved_query = self.resolved_query

        status = self.status

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if error is not UNSET:
            field_dict["error"] = error
        if language is not UNSET:
            field_dict["language"] = language
        if metric is not UNSET:
            field_dict["metric"] = metric
        if original_dd is not UNSET:
            field_dict["original_dd"] = original_dd
        if query is not UNSET:
            field_dict["query"] = query
        if query_id is not UNSET:
            field_dict["query_id"] = query_id
        if resolved_query is not UNSET:
            field_dict["resolved_query"] = resolved_query
        if status is not UNSET:
            field_dict["status"] = status
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        datasource = d.pop("datasource", UNSET)

        error = d.pop("error", UNSET)

        language = d.pop("language", UNSET)

        metric = d.pop("metric", UNSET)

        original_dd = d.pop("original_dd", UNSET)

        query = d.pop("query", UNSET)

        query_id = d.pop("query_id", UNSET)

        resolved_query = d.pop("resolved_query", UNSET)

        status = d.pop("status", UNSET)

        window = d.pop("window", UNSET)

        executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran = cls(
            datasource=datasource,
            error=error,
            language=language,
            metric=metric,
            original_dd=original_dd,
            query=query,
            query_id=query_id,
            resolved_query=resolved_query,
            status=status,
            window=window,
        )

        executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran.additional_properties = d
        return executed_query_is_the_evidence_for_a_units_wet_outcome_the_query_that_ran

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
