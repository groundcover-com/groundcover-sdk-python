from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_defines_a_searchable_column_and_its_properties import (
        ColumnDefinesASearchableColumnAndItsProperties,
    )


T = TypeVar("T", bound="FiltersRequestBody")


@_attrs_define
class FiltersRequestBody:
    """
    Attributes:
        query (str | Unset): Optional gcQL query narrowing the faceted set (e.g. free text, owner:x,
            tags:y, source:z, status:active).
            Empty means no query filter — including no status filter, so callers wanting
            only active dashboards must include status:active. Facets are disjunctive:
            a facet's own keyed conditions don't narrow that facet's value list, so a
            selected value's siblings stay listed and multi-select works (parity with
            monitors instances/filters).
        required (list[ColumnDefinesASearchableColumnAndItsProperties] | Unset): Optional list of facet keys (owner,
            tags, source) that must appear in the
            response even when the filtered set produces no values for them — each such
            key comes back as an empty list instead of being omitted from the map. This
            only guarantees presence: every facet is computed regardless of what is listed
            here. Keys outside the supported facet set are rejected with a 400 rather than
            ignored.
        source (str | Unset): Deprecated: accepted (any value, unvalidated) and ignored — same contract as
            req.Sources on the type=monitors search path. Filter by source with the gcQL
            `source:` key in query, which is disjunctive where this field was not.
    """

    query: str | Unset = UNSET
    required: list[ColumnDefinesASearchableColumnAndItsProperties] | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        required: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = []
            for required_item_data in self.required:
                required_item = required_item_data.to_dict()
                required.append(required_item)

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if required is not UNSET:
            field_dict["required"] = required
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_defines_a_searchable_column_and_its_properties import (
            ColumnDefinesASearchableColumnAndItsProperties,
        )

        d = dict(src_dict)
        query = d.pop("query", UNSET)

        _required = d.pop("required", UNSET)
        required: list[ColumnDefinesASearchableColumnAndItsProperties] | Unset = UNSET
        if _required is not UNSET:
            required = []
            for required_item_data in _required:
                required_item = ColumnDefinesASearchableColumnAndItsProperties.from_dict(required_item_data)

                required.append(required_item)

        source = d.pop("source", UNSET)

        filters_request_body = cls(
            query=query,
            required=required,
            source=source,
        )

        filters_request_body.additional_properties = d
        return filters_request_body

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
