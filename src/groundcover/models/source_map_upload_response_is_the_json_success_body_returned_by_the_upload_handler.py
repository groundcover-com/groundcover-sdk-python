from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler")


@_attrs_define
class SourceMapUploadResponseIsTheJSONSuccessBodyReturnedByTheUploadHandler:
    """
    Attributes:
        app_id (str | Unset):
        filename (str | Unset):
        release_id (str | Unset):
        size_bytes (int | Unset):
        status (str | Unset):
    """

    app_id: str | Unset = UNSET
    filename: str | Unset = UNSET
    release_id: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        filename = self.filename

        release_id = self.release_id

        size_bytes = self.size_bytes

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if release_id is not UNSET:
            field_dict["release_id"] = release_id
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if status is not UNSET:
            field_dict["status"] = status

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
        app_id = d.pop("app_id", UNSET)

        filename = d.pop("filename", UNSET)

        release_id = d.pop("release_id", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        status = d.pop("status", UNSET)

        source_map_upload_response_is_the_json_success_body_returned_by_the_upload_handler = cls(
            app_id=app_id,
            filename=filename,
            release_id=release_id,
            size_bytes=size_bytes,
            status=status,
        )

        source_map_upload_response_is_the_json_success_body_returned_by_the_upload_handler.additional_properties = d
        return source_map_upload_response_is_the_json_success_body_returned_by_the_upload_handler

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
