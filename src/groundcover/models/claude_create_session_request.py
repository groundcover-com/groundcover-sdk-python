from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ClaudeCreateSessionRequest")


@_attrs_define
class ClaudeCreateSessionRequest:
    """ClaudeCreateSessionRequest is the facade request body for creating a Claude
    Managed Agents session. The caller supplies only title/prompt; the router
    forwards it to comm-hub, which resolves the stored credential server-side.

        Attributes:
            prompt (str): The initial prompt sent to the agent. Example: Summarize the open issues in this repository.
            title (str | Unset): Optional session title.
    """

    prompt: str
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

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
        prompt = d.pop("prompt")

        title = d.pop("title", UNSET)

        claude_create_session_request = cls(
            prompt=prompt,
            title=title,
        )

        claude_create_session_request.additional_properties = d
        return claude_create_session_request

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
