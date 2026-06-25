from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="WetResultHoldsTheOutcomeOfExecutingASingleWetQuery")


@_attrs_define
class WetResultHoldsTheOutcomeOfExecutingASingleWetQuery:
    """
    Attributes:
        asset_id (str | Unset):
        asset_name (str | Unset):
        asset_type (str | Unset):
        datasource (str | Unset):
        error (str | Unset):
        latency (int | Unset): Duration wraps time.Duration. It is used to parse the custom duration format
            from YAML.
            This type should not propagate beyond the scope of input/output processing.
        original_dd (str | Unset):
        query (str | Unset):
        query_id (str | Unset):
        query_type (str | Unset):
        resolved_query (str | Unset):
        status (str | Unset):
        widget_title (str | Unset):
        window (str | Unset):
    """

    asset_id: str | Unset = UNSET
    asset_name: str | Unset = UNSET
    asset_type: str | Unset = UNSET
    datasource: str | Unset = UNSET
    error: str | Unset = UNSET
    latency: int | Unset = UNSET
    original_dd: str | Unset = UNSET
    query: str | Unset = UNSET
    query_id: str | Unset = UNSET
    query_type: str | Unset = UNSET
    resolved_query: str | Unset = UNSET
    status: str | Unset = UNSET
    widget_title: str | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type = self.asset_type

        datasource = self.datasource

        error = self.error

        latency = self.latency

        original_dd = self.original_dd

        query = self.query

        query_id = self.query_id

        query_type = self.query_type

        resolved_query = self.resolved_query

        status = self.status

        widget_title = self.widget_title

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if error is not UNSET:
            field_dict["error"] = error
        if latency is not UNSET:
            field_dict["latency"] = latency
        if original_dd is not UNSET:
            field_dict["original_dd"] = original_dd
        if query is not UNSET:
            field_dict["query"] = query
        if query_id is not UNSET:
            field_dict["query_id"] = query_id
        if query_type is not UNSET:
            field_dict["query_type"] = query_type
        if resolved_query is not UNSET:
            field_dict["resolved_query"] = resolved_query
        if status is not UNSET:
            field_dict["status"] = status
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title
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
        asset_id = d.pop("asset_id", UNSET)

        asset_name = d.pop("asset_name", UNSET)

        asset_type = d.pop("asset_type", UNSET)

        datasource = d.pop("datasource", UNSET)

        error = d.pop("error", UNSET)

        latency = d.pop("latency", UNSET)

        original_dd = d.pop("original_dd", UNSET)

        query = d.pop("query", UNSET)

        query_id = d.pop("query_id", UNSET)

        query_type = d.pop("query_type", UNSET)

        resolved_query = d.pop("resolved_query", UNSET)

        status = d.pop("status", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        window = d.pop("window", UNSET)

        wet_result_holds_the_outcome_of_executing_a_single_wet_query = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
            datasource=datasource,
            error=error,
            latency=latency,
            original_dd=original_dd,
            query=query,
            query_id=query_id,
            query_type=query_type,
            resolved_query=resolved_query,
            status=status,
            widget_title=widget_title,
            window=window,
        )

        wet_result_holds_the_outcome_of_executing_a_single_wet_query.additional_properties = d
        return wet_result_holds_the_outcome_of_executing_a_single_wet_query

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
