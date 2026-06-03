from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorImageIsABase64EncodedImageAttachedToAPrompt")


@_attrs_define
class CursorImageIsABase64EncodedImageAttachedToAPrompt:
    """
    Attributes:
        data (str): Base64-encoded image data
        height (int | Unset): Image height in pixels
        width (int | Unset): Image width in pixels
    """

    data: str
    height: int | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        data = d.pop("data")

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        cursor_image_is_a_base_64_encoded_image_attached_to_a_prompt = cls(
            data=data,
            height=height,
            width=width,
        )

        cursor_image_is_a_base_64_encoded_image_attached_to_a_prompt.additional_properties = d
        return cursor_image_is_a_base_64_encoded_image_attached_to_a_prompt

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
