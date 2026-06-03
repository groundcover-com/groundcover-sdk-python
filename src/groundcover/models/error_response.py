from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        details (Any | Unset):
        docs_url (str | Unset):
        message (str | Unset):
        trace_id (str | Unset):
        type_ (str | Unset):
    """

    details: Any | Unset = UNSET
    docs_url: str | Unset = UNSET
    message: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        docs_url = self.docs_url

        message = self.message

        trace_id = self.trace_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if docs_url is not UNSET:
            field_dict["docs_url"] = docs_url
        if message is not UNSET:
            field_dict["message"] = message
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        details = d.pop("details", UNSET)

        docs_url = d.pop("docs_url", UNSET)

        message = d.pop("message", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        type_ = d.pop("type", UNSET)

        error_response = cls(
            details=details,
            docs_url=docs_url,
            message=message,
            trace_id=trace_id,
            type_=type_,
        )

        error_response.additional_properties = d
        return error_response

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
