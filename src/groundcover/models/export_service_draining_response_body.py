from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_service_draining_response_body_error import ExportServiceDrainingResponseBodyError
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ExportServiceDrainingResponseBody")


@_attrs_define
class ExportServiceDrainingResponseBody:
    """ExportServiceDrainingResponseBody is the structured error payload returned
    when export-service is draining during shutdown.

        Attributes:
            error (ExportServiceDrainingResponseBodyError): Stable machine-readable error code.
            message (str): Human-readable explanation of the error. Example: Export service is shutting down.
            request_id (str | Unset): Export request identifier for log correlation.
    """

    error: ExportServiceDrainingResponseBodyError
    message: str
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        message = self.message

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
            }
        )
        if request_id is not UNSET:
            field_dict["requestId"] = request_id

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
        error = ExportServiceDrainingResponseBodyError(d.pop("error"))

        message = d.pop("message")

        request_id = d.pop("requestId", UNSET)

        export_service_draining_response_body = cls(
            error=error,
            message=message,
            request_id=request_id,
        )

        export_service_draining_response_body.additional_properties = d
        return export_service_draining_response_body

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
