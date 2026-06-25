from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_span_result import RootSpanResult


T = TypeVar("T", bound="RootSpanDetails")


@_attrs_define
class RootSpanDetails:
    """
    Attributes:
        details (RootSpanResult | Unset): RootSpanResult is the scan target for GET_ROOT_SPAN_DETAILS and the item
            returned in the response. It contains only the fields consumed by the UI
            header panel; full payload data (bodies, headers) is fetched separately
            via /api/traces/v2/details when a span is selected.
    """

    details: RootSpanResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_span_result import RootSpanResult

        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: RootSpanResult | Unset
        if isinstance(_details, Unset) or _details is None:
            details = UNSET
        else:
            details = RootSpanResult.from_dict(_details)

        root_span_details = cls(
            details=details,
        )

        root_span_details.additional_properties = d
        return root_span_details

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
