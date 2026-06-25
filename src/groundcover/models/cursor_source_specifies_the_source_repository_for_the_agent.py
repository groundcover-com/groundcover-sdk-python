from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorSourceSpecifiesTheSourceRepositoryForTheAgent")


@_attrs_define
class CursorSourceSpecifiesTheSourceRepositoryForTheAgent:
    """
    Attributes:
        pr_url (str | Unset): An existing pull request URL for context
        ref (str | Unset): The git ref (branch, tag, or commit) Example: main.
        repository (str | Unset): The repository URL Example: https://github.com/org/repo.
    """

    pr_url: str | Unset = UNSET
    ref: str | Unset = UNSET
    repository: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pr_url = self.pr_url

        ref = self.ref

        repository = self.repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pr_url is not UNSET:
            field_dict["prUrl"] = pr_url
        if ref is not UNSET:
            field_dict["ref"] = ref
        if repository is not UNSET:
            field_dict["repository"] = repository

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
        pr_url = d.pop("prUrl", UNSET)

        ref = d.pop("ref", UNSET)

        repository = d.pop("repository", UNSET)

        cursor_source_specifies_the_source_repository_for_the_agent = cls(
            pr_url=pr_url,
            ref=ref,
            repository=repository,
        )

        cursor_source_specifies_the_source_repository_for_the_agent.additional_properties = d
        return cursor_source_specifies_the_source_repository_for_the_agent

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
