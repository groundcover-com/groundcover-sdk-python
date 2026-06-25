from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LinearCommentIsACommentReturnedByTheTypedLinearConnectorAPI")


@_attrs_define
class LinearCommentIsACommentReturnedByTheTypedLinearConnectorAPI:
    """
    Attributes:
        body (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
    """

    body: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        created_at = self.created_at

        id = self.id

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

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
        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        linear_comment_is_a_comment_returned_by_the_typed_linear_connector_api = cls(
            body=body,
            created_at=created_at,
            id=id,
            updated_at=updated_at,
            url=url,
        )

        linear_comment_is_a_comment_returned_by_the_typed_linear_connector_api.additional_properties = d
        return linear_comment_is_a_comment_returned_by_the_typed_linear_connector_api

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
