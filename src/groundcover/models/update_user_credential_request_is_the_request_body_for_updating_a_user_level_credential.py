from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_user_credential_request_is_the_request_body_for_updating_a_user_level_credential_data import (
        UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredentialData,
    )


T = TypeVar("T", bound="UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredential")


@_attrs_define
class UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredential:
    """
    Attributes:
        data (UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredentialData): Provider-specific
            credential data
        description (str | Unset): Optional description for this credential Example: Used for the main project.
        name (str | Unset): Human-readable name for this credential Example: My Cursor Key.
    """

    data: UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredentialData
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_user_credential_request_is_the_request_body_for_updating_a_user_level_credential_data import (
            UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredentialData,
        )

        d = dict(src_dict)
        data = UpdateUserCredentialRequestIsTheRequestBodyForUpdatingAUserLevelCredentialData.from_dict(d.pop("data"))

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        update_user_credential_request_is_the_request_body_for_updating_a_user_level_credential = cls(
            data=data,
            description=description,
            name=name,
        )

        update_user_credential_request_is_the_request_body_for_updating_a_user_level_credential.additional_properties = d
        return update_user_credential_request_is_the_request_body_for_updating_a_user_level_credential

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
