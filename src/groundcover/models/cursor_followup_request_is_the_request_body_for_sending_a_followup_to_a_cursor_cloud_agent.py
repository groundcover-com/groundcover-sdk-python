from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_prompt_represents_a_prompt_with_text_and_optional_images import (
        CursorPromptRepresentsAPromptWithTextAndOptionalImages,
    )


T = TypeVar("T", bound="CursorFollowupRequestIsTheRequestBodyForSendingAFollowupToACursorCloudAgent")


@_attrs_define
class CursorFollowupRequestIsTheRequestBodyForSendingAFollowupToACursorCloudAgent:
    """
    Attributes:
        prompt (CursorPromptRepresentsAPromptWithTextAndOptionalImages | Unset):
    """

    prompt: CursorPromptRepresentsAPromptWithTextAndOptionalImages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prompt is not UNSET:
            field_dict["prompt"] = prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_prompt_represents_a_prompt_with_text_and_optional_images import (
            CursorPromptRepresentsAPromptWithTextAndOptionalImages,
        )

        d = dict(src_dict)
        _prompt = d.pop("prompt", UNSET)
        prompt: CursorPromptRepresentsAPromptWithTextAndOptionalImages | Unset
        if isinstance(_prompt, Unset) or _prompt is None:
            prompt = UNSET
        else:
            prompt = CursorPromptRepresentsAPromptWithTextAndOptionalImages.from_dict(_prompt)

        cursor_followup_request_is_the_request_body_for_sending_a_followup_to_a_cursor_cloud_agent = cls(
            prompt=prompt,
        )

        cursor_followup_request_is_the_request_body_for_sending_a_followup_to_a_cursor_cloud_agent.additional_properties = d
        return cursor_followup_request_is_the_request_body_for_sending_a_followup_to_a_cursor_cloud_agent

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
