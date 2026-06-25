from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_repository_item_represents_a_single_git_hub_repository import (
        CursorRepositoryItemRepresentsASingleGitHubRepository,
    )


T = TypeVar("T", bound="CursorListRepositoriesResponseIsTheResponseForTheListRepositoriesEndpoint")


@_attrs_define
class CursorListRepositoriesResponseIsTheResponseForTheListRepositoriesEndpoint:
    """
    Attributes:
        repositories (list[CursorRepositoryItemRepresentsASingleGitHubRepository] | Unset):
    """

    repositories: list[CursorRepositoryItemRepresentsASingleGitHubRepository] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repositories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = []
            for repositories_item_data in self.repositories:
                repositories_item = repositories_item_data.to_dict()
                repositories.append(repositories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repositories is not UNSET:
            field_dict["repositories"] = repositories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_repository_item_represents_a_single_git_hub_repository import (
            CursorRepositoryItemRepresentsASingleGitHubRepository,
        )

        d = dict(src_dict)
        _repositories = d.pop("repositories", UNSET)
        repositories: list[CursorRepositoryItemRepresentsASingleGitHubRepository] | Unset = UNSET
        if _repositories is not UNSET:
            repositories = []
            for repositories_item_data in _repositories:
                repositories_item = CursorRepositoryItemRepresentsASingleGitHubRepository.from_dict(
                    repositories_item_data
                )

                repositories.append(repositories_item)

        cursor_list_repositories_response_is_the_response_for_the_list_repositories_endpoint = cls(
            repositories=repositories,
        )

        cursor_list_repositories_response_is_the_response_for_the_list_repositories_endpoint.additional_properties = d
        return cursor_list_repositories_response_is_the_response_for_the_list_repositories_endpoint

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
