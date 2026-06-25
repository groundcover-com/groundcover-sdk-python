from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TraceDetailsRequestInfo")


@_attrs_define
class TraceDetailsRequestInfo:
    """
    Attributes:
        body (str | Unset):
        body_size_bytes (int | Unset):
        headers (str | Unset):
        is_truncated (bool | Unset):
        query_params (str | Unset):
    """

    body: str | Unset = UNSET
    body_size_bytes: int | Unset = UNSET
    headers: str | Unset = UNSET
    is_truncated: bool | Unset = UNSET
    query_params: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        body_size_bytes = self.body_size_bytes

        headers = self.headers

        is_truncated = self.is_truncated

        query_params = self.query_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if body_size_bytes is not UNSET:
            field_dict["bodySizeBytes"] = body_size_bytes
        if headers is not UNSET:
            field_dict["headers"] = headers
        if is_truncated is not UNSET:
            field_dict["isTruncated"] = is_truncated
        if query_params is not UNSET:
            field_dict["queryParams"] = query_params

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
        body = d.pop("body", UNSET)

        body_size_bytes = d.pop("bodySizeBytes", UNSET)

        headers = d.pop("headers", UNSET)

        is_truncated = d.pop("isTruncated", UNSET)

        query_params = d.pop("queryParams", UNSET)

        trace_details_request_info = cls(
            body=body,
            body_size_bytes=body_size_bytes,
            headers=headers,
            is_truncated=is_truncated,
            query_params=query_params,
        )

        trace_details_request_info.additional_properties = d
        return trace_details_request_info

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
