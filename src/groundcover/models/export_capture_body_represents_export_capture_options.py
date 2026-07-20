from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ExportCaptureBodyRepresentsExportCaptureOptions")


@_attrs_define
class ExportCaptureBodyRepresentsExportCaptureOptions:
    """
    Attributes:
        fullscreen (bool | Unset): Whether to capture the full page instead of the resolved element bounds.
    """

    fullscreen: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fullscreen = self.fullscreen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fullscreen is not UNSET:
            field_dict["fullscreen"] = fullscreen

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
        fullscreen = d.pop("fullscreen", UNSET)

        export_capture_body_represents_export_capture_options = cls(
            fullscreen=fullscreen,
        )

        export_capture_body_represents_export_capture_options.additional_properties = d
        return export_capture_body_represents_export_capture_options

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
