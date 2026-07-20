from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_auth_body_represents_the_auth_mode_sent_to_export_service_type import (
    ExportAuthBodyRepresentsTheAuthModeSentToExportServiceType,
)

T = TypeVar("T", bound="ExportAuthBodyRepresentsTheAuthModeSentToExportService")


@_attrs_define
class ExportAuthBodyRepresentsTheAuthModeSentToExportService:
    """
    Attributes:
        type_ (ExportAuthBodyRepresentsTheAuthModeSentToExportServiceType): Auth type.
    """

    type_: ExportAuthBodyRepresentsTheAuthModeSentToExportServiceType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
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
        type_ = ExportAuthBodyRepresentsTheAuthModeSentToExportServiceType(d.pop("type"))

        export_auth_body_represents_the_auth_mode_sent_to_export_service = cls(
            type_=type_,
        )

        export_auth_body_represents_the_auth_mode_sent_to_export_service.additional_properties = d
        return export_auth_body_represents_the_auth_mode_sent_to_export_service

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
