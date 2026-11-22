from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence")


@_attrs_define
class IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence:
    """
    Attributes:
        asset_id (UUID):
        converted_query (None | str):
        finding_id (UUID):
        original_dd_query (None | str):
        widget_id (None | str):
    """

    asset_id: UUID
    converted_query: None | str
    finding_id: UUID
    original_dd_query: None | str
    widget_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        converted_query: None | str
        converted_query = self.converted_query

        finding_id = str(self.finding_id)

        original_dd_query: None | str
        original_dd_query = self.original_dd_query

        widget_id: None | str
        widget_id = self.widget_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "converted_query": converted_query,
                "finding_id": finding_id,
                "original_dd_query": original_dd_query,
                "widget_id": widget_id,
            }
        )

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
        asset_id = UUID(d.pop("asset_id"))

        def _parse_converted_query(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        converted_query = _parse_converted_query(d.pop("converted_query"))

        finding_id = UUID(d.pop("finding_id"))

        def _parse_original_dd_query(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_dd_query = _parse_original_dd_query(d.pop("original_dd_query"))

        def _parse_widget_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        widget_id = _parse_widget_id(d.pop("widget_id"))

        issue_context_finding_contains_the_stored_query_pair_for_one_issue_occurrence = cls(
            asset_id=asset_id,
            converted_query=converted_query,
            finding_id=finding_id,
            original_dd_query=original_dd_query,
            widget_id=widget_id,
        )

        issue_context_finding_contains_the_stored_query_pair_for_one_issue_occurrence.additional_properties = d
        return issue_context_finding_contains_the_stored_query_pair_for_one_issue_occurrence

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
