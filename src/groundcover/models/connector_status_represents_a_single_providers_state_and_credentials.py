from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_response_is_the_json_representation_of_a_stored_credential import (
        CredentialResponseIsTheJSONRepresentationOfAStoredCredential,
    )


T = TypeVar("T", bound="ConnectorStatusRepresentsASingleProvidersStateAndCredentials")


@_attrs_define
class ConnectorStatusRepresentsASingleProvidersStateAndCredentials:
    """
    Attributes:
        credentials (list[CredentialResponseIsTheJSONRepresentationOfAStoredCredential] | Unset): Credentials for this
            connector
        enabled (bool | Unset): Whether the connector is enabled (org-level credential exists)
    """

    credentials: list[CredentialResponseIsTheJSONRepresentationOfAStoredCredential] | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_response_is_the_json_representation_of_a_stored_credential import (
            CredentialResponseIsTheJSONRepresentationOfAStoredCredential,
        )

        d = dict(src_dict)
        _credentials = d.pop("credentials", UNSET)
        credentials: list[CredentialResponseIsTheJSONRepresentationOfAStoredCredential] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = CredentialResponseIsTheJSONRepresentationOfAStoredCredential.from_dict(
                    credentials_item_data
                )

                credentials.append(credentials_item)

        enabled = d.pop("enabled", UNSET)

        connector_status_represents_a_single_providers_state_and_credentials = cls(
            credentials=credentials,
            enabled=enabled,
        )

        connector_status_represents_a_single_providers_state_and_credentials.additional_properties = d
        return connector_status_represents_a_single_providers_state_and_credentials

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
