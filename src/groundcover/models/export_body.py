from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_body_format import ExportBodyFormat

T = TypeVar("T", bound="ExportBody")


@_attrs_define
class ExportBody:
    """
    Attributes:
        format_ (ExportBodyFormat): Format names the emitted resource.
        uuids (list[UUID]): UUIDs of the monitors to export, rendered in this order.
    """

    format_: ExportBodyFormat
    uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        uuids = []
        for uuids_item_data in self.uuids:
            uuids_item = str(uuids_item_data)
            uuids.append(uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "uuids": uuids,
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
        format_ = ExportBodyFormat(d.pop("format"))

        uuids = []
        _uuids = d.pop("uuids")
        for uuids_item_data in _uuids:
            uuids_item = UUID(uuids_item_data)

            uuids.append(uuids_item)

        export_body = cls(
            format_=format_,
            uuids=uuids,
        )

        export_body.additional_properties = d
        return export_body

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
