from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_attributes_response_attributes import TraceAttributesResponseAttributes
    from ..models.trace_attributes_response_tags import TraceAttributesResponseTags


T = TypeVar("T", bound="TraceAttributesResponse")


@_attrs_define
class TraceAttributesResponse:
    """
    Attributes:
        attributes (TraceAttributesResponseAttributes | Unset):
        span_id (str | Unset):
        tags (TraceAttributesResponseTags | Unset):
    """

    attributes: TraceAttributesResponseAttributes | Unset = UNSET
    span_id: str | Unset = UNSET
    tags: TraceAttributesResponseTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        span_id = self.span_id

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_attributes_response_attributes import TraceAttributesResponseAttributes
        from ..models.trace_attributes_response_tags import TraceAttributesResponseTags

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: TraceAttributesResponseAttributes | Unset
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = TraceAttributesResponseAttributes.from_dict(_attributes)

        span_id = d.pop("spanId", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: TraceAttributesResponseTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = TraceAttributesResponseTags.from_dict(_tags)

        trace_attributes_response = cls(
            attributes=attributes,
            span_id=span_id,
            tags=tags,
        )

        trace_attributes_response.additional_properties = d
        return trace_attributes_response

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
