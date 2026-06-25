from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_credential_request_is_the_request_body_for_creating_a_user_level_credential_data import (
        CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredentialData,
    )


T = TypeVar("T", bound="CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredential")


@_attrs_define
class CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredential:
    """The provider is taken from the :provider path parameter.

    Attributes:
        data (CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredentialData): Provider-specific
            credential data (e.g. {"api_key": "...", "auto_create_pr": true})
        name (str): Human-readable name for this credential Example: My Cursor Key.
        description (str | Unset): Optional description for this credential Example: Used for the main project.
    """

    data: CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredentialData
    name: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_user_credential_request_is_the_request_body_for_creating_a_user_level_credential_data import (
            CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredentialData,
        )

        d = dict(src_dict)
        data = CreateUserCredentialRequestIsTheRequestBodyForCreatingAUserLevelCredentialData.from_dict(d.pop("data"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        create_user_credential_request_is_the_request_body_for_creating_a_user_level_credential = cls(
            data=data,
            name=name,
            description=description,
        )

        create_user_credential_request_is_the_request_body_for_creating_a_user_level_credential.additional_properties = d
        return create_user_credential_request_is_the_request_body_for_creating_a_user_level_credential

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
