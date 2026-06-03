from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_image_is_a_base_64_encoded_image_attached_to_a_prompt import (
        CursorImageIsABase64EncodedImageAttachedToAPrompt,
    )


T = TypeVar("T", bound="CursorPromptRepresentsAPromptWithTextAndOptionalImages")


@_attrs_define
class CursorPromptRepresentsAPromptWithTextAndOptionalImages:
    """
    Attributes:
        text (str): The prompt text Example: Fix the failing unit tests in auth_test.go.
        images (list[CursorImageIsABase64EncodedImageAttachedToAPrompt] | Unset): Optional images to include with the
            prompt
    """

    text: str
    images: list[CursorImageIsABase64EncodedImageAttachedToAPrompt] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_image_is_a_base_64_encoded_image_attached_to_a_prompt import (
            CursorImageIsABase64EncodedImageAttachedToAPrompt,
        )

        d = dict(src_dict)
        text = d.pop("text")

        _images = d.pop("images", UNSET)
        images: list[CursorImageIsABase64EncodedImageAttachedToAPrompt] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = CursorImageIsABase64EncodedImageAttachedToAPrompt.from_dict(images_item_data)

                images.append(images_item)

        cursor_prompt_represents_a_prompt_with_text_and_optional_images = cls(
            text=text,
            images=images,
        )

        cursor_prompt_represents_a_prompt_with_text_and_optional_images.additional_properties = d
        return cursor_prompt_represents_a_prompt_with_text_and_optional_images

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
