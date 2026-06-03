from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_secret_request_managed_by_provider import CreateSecretRequestManagedByProvider
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CreateSecretRequest")


@_attrs_define
class CreateSecretRequest:
    """
    Attributes:
        content (str):
        name (str): The name of the secret
        type_ (str): The type of the secret (e.g., api_key, password, basic_auth)
        managed_by_provider (CreateSecretRequestManagedByProvider | Unset): Indicates if this secret is managed by an
            external provider (e.g., terraform)
    """

    content: str
    name: str
    type_: str
    managed_by_provider: CreateSecretRequestManagedByProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        name = self.name

        type_ = self.type_

        managed_by_provider: str | Unset = UNSET
        if not isinstance(self.managed_by_provider, Unset):
            managed_by_provider = self.managed_by_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "name": name,
                "type": type_,
            }
        )
        if managed_by_provider is not UNSET:
            field_dict["managedByProvider"] = managed_by_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        content = d.pop("content")

        name = d.pop("name")

        type_ = d.pop("type")

        _managed_by_provider = d.pop("managedByProvider", UNSET)
        managed_by_provider: CreateSecretRequestManagedByProvider | Unset
        if isinstance(_managed_by_provider, Unset) or _managed_by_provider is None:
            managed_by_provider = UNSET
        else:
            managed_by_provider = CreateSecretRequestManagedByProvider(_managed_by_provider)

        create_secret_request = cls(
            content=content,
            name=name,
            type_=type_,
            managed_by_provider=managed_by_provider,
        )

        create_secret_request.additional_properties = d
        return create_secret_request

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
