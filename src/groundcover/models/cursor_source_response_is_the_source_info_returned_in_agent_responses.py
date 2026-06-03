from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses")


@_attrs_define
class CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses:
    """
    Attributes:
        ref (str | Unset):
        repository (str | Unset):
    """

    ref: str | Unset = UNSET
    repository: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        repository = self.repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["ref"] = ref
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        ref = d.pop("ref", UNSET)

        repository = d.pop("repository", UNSET)

        cursor_source_response_is_the_source_info_returned_in_agent_responses = cls(
            ref=ref,
            repository=repository,
        )

        cursor_source_response_is_the_source_info_returned_in_agent_responses.additional_properties = d
        return cursor_source_response_is_the_source_info_returned_in_agent_responses

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
