from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorRepositoryItemRepresentsASingleGitHubRepository")


@_attrs_define
class CursorRepositoryItemRepresentsASingleGitHubRepository:
    """
    Attributes:
        name (str | Unset):
        owner (str | Unset):
        repository (str | Unset):
    """

    name: str | Unset = UNSET
    owner: str | Unset = UNSET
    repository: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner = self.owner

        repository = self.repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        repository = d.pop("repository", UNSET)

        cursor_repository_item_represents_a_single_git_hub_repository = cls(
            name=name,
            owner=owner,
            repository=repository,
        )

        cursor_repository_item_represents_a_single_git_hub_repository.additional_properties = d
        return cursor_repository_item_represents_a_single_git_hub_repository

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
