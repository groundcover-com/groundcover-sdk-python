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
    from ..models.cursor_source_specifies_the_source_repository_for_the_agent import (
        CursorSourceSpecifiesTheSourceRepositoryForTheAgent,
    )
    from ..models.cursor_target_specifies_target_branch_and_pr_behavior import (
        CursorTargetSpecifiesTargetBranchAndPRBehavior,
    )


T = TypeVar("T", bound="CursorLaunchAgentRequestIsTheRequestBodyForLaunchingACursorCloudAgent")


@_attrs_define
class CursorLaunchAgentRequestIsTheRequestBodyForLaunchingACursorCloudAgent:
    """
    Attributes:
        model (str | Unset):
        prompt (CursorPromptRepresentsAPromptWithTextAndOptionalImages | Unset):
        source (CursorSourceSpecifiesTheSourceRepositoryForTheAgent | Unset):
        target (CursorTargetSpecifiesTargetBranchAndPRBehavior | Unset):
    """

    model: str | Unset = UNSET
    prompt: CursorPromptRepresentsAPromptWithTextAndOptionalImages | Unset = UNSET
    source: CursorSourceSpecifiesTheSourceRepositoryForTheAgent | Unset = UNSET
    target: CursorTargetSpecifiesTargetBranchAndPRBehavior | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_prompt_represents_a_prompt_with_text_and_optional_images import (
            CursorPromptRepresentsAPromptWithTextAndOptionalImages,
        )
        from ..models.cursor_source_specifies_the_source_repository_for_the_agent import (
            CursorSourceSpecifiesTheSourceRepositoryForTheAgent,
        )
        from ..models.cursor_target_specifies_target_branch_and_pr_behavior import (
            CursorTargetSpecifiesTargetBranchAndPRBehavior,
        )

        d = dict(src_dict)
        model = d.pop("model", UNSET)

        _prompt = d.pop("prompt", UNSET)
        prompt: CursorPromptRepresentsAPromptWithTextAndOptionalImages | Unset
        if isinstance(_prompt, Unset) or _prompt is None:
            prompt = UNSET
        else:
            prompt = CursorPromptRepresentsAPromptWithTextAndOptionalImages.from_dict(_prompt)

        _source = d.pop("source", UNSET)
        source: CursorSourceSpecifiesTheSourceRepositoryForTheAgent | Unset
        if isinstance(_source, Unset) or _source is None:
            source = UNSET
        else:
            source = CursorSourceSpecifiesTheSourceRepositoryForTheAgent.from_dict(_source)

        _target = d.pop("target", UNSET)
        target: CursorTargetSpecifiesTargetBranchAndPRBehavior | Unset
        if isinstance(_target, Unset) or _target is None:
            target = UNSET
        else:
            target = CursorTargetSpecifiesTargetBranchAndPRBehavior.from_dict(_target)

        cursor_launch_agent_request_is_the_request_body_for_launching_a_cursor_cloud_agent = cls(
            model=model,
            prompt=prompt,
            source=source,
            target=target,
        )

        cursor_launch_agent_request_is_the_request_body_for_launching_a_cursor_cloud_agent.additional_properties = d
        return cursor_launch_agent_request_is_the_request_body_for_launching_a_cursor_cloud_agent

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
