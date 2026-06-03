from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_link_attributes import SpanLinkAttributes


T = TypeVar("T", bound="SpanLink")


@_attrs_define
class SpanLink:
    """
    Attributes:
        attributes (SpanLinkAttributes | Unset):
        span_id (str | Unset):
        trace_id (str | Unset):
        trace_state (str | Unset):
    """

    attributes: SpanLinkAttributes | Unset = UNSET
    span_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    trace_state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        span_id = self.span_id

        trace_id = self.trace_id

        trace_state = self.trace_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if trace_state is not UNSET:
            field_dict["traceState"] = trace_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_link_attributes import SpanLinkAttributes

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: SpanLinkAttributes | Unset
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = SpanLinkAttributes.from_dict(_attributes)

        span_id = d.pop("spanId", UNSET)

        trace_id = d.pop("traceId", UNSET)

        trace_state = d.pop("traceState", UNSET)

        span_link = cls(
            attributes=attributes,
            span_id=span_id,
            trace_id=trace_id,
            trace_state=trace_state,
        )

        span_link.additional_properties = d
        return span_link

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
