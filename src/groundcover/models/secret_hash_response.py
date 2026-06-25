from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SecretHashResponse")


@_attrs_define
class SecretHashResponse:
    """
    Attributes:
        content_hash (str | Unset): FNV1a hash of the secret content (hex encoded) Example: a1b2c3d4e5f67890.
        id (str | Unset): The unique identifier for the secret Example: secretRef::store::a1b2c3d4e5f6.
        managed_by_provider (str | Unset): Indicates if this secret is managed by an external provider (e.g., terraform)
            Example: terraform.
        name (str | Unset): The name of the secret Example: my-api-key.
        type_ (str | Unset): The type of the secret Example: password.
    """

    content_hash: str | Unset = UNSET
    id: str | Unset = UNSET
    managed_by_provider: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_hash = self.content_hash

        id = self.id

        managed_by_provider = self.managed_by_provider

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash
        if id is not UNSET:
            field_dict["id"] = id
        if managed_by_provider is not UNSET:
            field_dict["managedByProvider"] = managed_by_provider
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        content_hash = d.pop("contentHash", UNSET)

        id = d.pop("id", UNSET)

        managed_by_provider = d.pop("managedByProvider", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        secret_hash_response = cls(
            content_hash=content_hash,
            id=id,
            managed_by_provider=managed_by_provider,
            name=name,
            type_=type_,
        )

        secret_hash_response.additional_properties = d
        return secret_hash_response

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
