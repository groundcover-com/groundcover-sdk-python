from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorTargetSpecifiesTargetBranchAndPRBehavior")


@_attrs_define
class CursorTargetSpecifiesTargetBranchAndPRBehavior:
    """
    Attributes:
        auto_branch (bool | Unset):
        auto_create_pr (bool | Unset):
        branch_name (str | Unset):
        open_as_cursor_github_app (bool | Unset):
        skip_reviewer_request (bool | Unset):
    """

    auto_branch: bool | Unset = UNSET
    auto_create_pr: bool | Unset = UNSET
    branch_name: str | Unset = UNSET
    open_as_cursor_github_app: bool | Unset = UNSET
    skip_reviewer_request: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_branch = self.auto_branch

        auto_create_pr = self.auto_create_pr

        branch_name = self.branch_name

        open_as_cursor_github_app = self.open_as_cursor_github_app

        skip_reviewer_request = self.skip_reviewer_request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_branch is not UNSET:
            field_dict["autoBranch"] = auto_branch
        if auto_create_pr is not UNSET:
            field_dict["autoCreatePr"] = auto_create_pr
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if open_as_cursor_github_app is not UNSET:
            field_dict["openAsCursorGithubApp"] = open_as_cursor_github_app
        if skip_reviewer_request is not UNSET:
            field_dict["skipReviewerRequest"] = skip_reviewer_request

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
        auto_branch = d.pop("autoBranch", UNSET)

        auto_create_pr = d.pop("autoCreatePr", UNSET)

        branch_name = d.pop("branchName", UNSET)

        open_as_cursor_github_app = d.pop("openAsCursorGithubApp", UNSET)

        skip_reviewer_request = d.pop("skipReviewerRequest", UNSET)

        cursor_target_specifies_target_branch_and_pr_behavior = cls(
            auto_branch=auto_branch,
            auto_create_pr=auto_create_pr,
            branch_name=branch_name,
            open_as_cursor_github_app=open_as_cursor_github_app,
            skip_reviewer_request=skip_reviewer_request,
        )

        cursor_target_specifies_target_branch_and_pr_behavior.additional_properties = d
        return cursor_target_specifies_target_branch_and_pr_behavior

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
