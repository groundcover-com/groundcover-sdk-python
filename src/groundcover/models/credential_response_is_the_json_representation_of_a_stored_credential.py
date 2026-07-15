from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_capabilities_contains_optional_provider_owned_feature_metadata import (
        ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata,
    )
    from ..models.credential_response_is_the_json_representation_of_a_stored_credential_data import (
        CredentialResponseIsTheJSONRepresentationOfAStoredCredentialData,
    )


T = TypeVar("T", bound="CredentialResponseIsTheJSONRepresentationOfAStoredCredential")


@_attrs_define
class CredentialResponseIsTheJSONRepresentationOfAStoredCredential:
    """
    Attributes:
        auth_type (str | Unset): The authentication type Example: api_key.
        capabilities (ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata | Unset):
        created_at (str | Unset): Creation timestamp Example: 2026-03-15 12:20:55+00:00.
        data (CredentialResponseIsTheJSONRepresentationOfAStoredCredentialData | Unset): Provider-specific metadata
        description (str | Unset): Optional description for this credential
        enabled (bool | Unset): Whether this credential is administratively enabled
        id (str | Unset): The credential ID Example: 550e8400-e29b-41d4-a716-446655440000.
        is_org_level (bool | Unset): Whether this is an org-level credential
        name (str | Unset): Human-readable name for this credential Example: My Cursor Key.
        org_credential_id (str | Unset): Linked org connector ID for user-level credentials, when applicable Example:
            550e8400-e29b-41d4-a716-446655440001.
        provider (str | Unset): The provider name Example: cursor.
        status (str | Unset): The credential status Example: active.
        updated_at (str | Unset): Last update timestamp Example: 2026-03-15 12:20:55+00:00.
        usable (bool | Unset): Whether this credential can currently be resolved by comm-hub
        user (str | Unset): The user who owns this credential (email or user ID)
    """

    auth_type: str | Unset = UNSET
    capabilities: ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata | Unset = UNSET
    created_at: str | Unset = UNSET
    data: CredentialResponseIsTheJSONRepresentationOfAStoredCredentialData | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_org_level: bool | Unset = UNSET
    name: str | Unset = UNSET
    org_credential_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    usable: bool | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        created_at = self.created_at

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        description = self.description

        enabled = self.enabled

        id = self.id

        is_org_level = self.is_org_level

        name = self.name

        org_credential_id = self.org_credential_id

        provider = self.provider

        status = self.status

        updated_at = self.updated_at

        usable = self.usable

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if is_org_level is not UNSET:
            field_dict["is_org_level"] = is_org_level
        if name is not UNSET:
            field_dict["name"] = name
        if org_credential_id is not UNSET:
            field_dict["org_credential_id"] = org_credential_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if usable is not UNSET:
            field_dict["usable"] = usable
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_capabilities_contains_optional_provider_owned_feature_metadata import (
            ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata,
        )
        from ..models.credential_response_is_the_json_representation_of_a_stored_credential_data import (
            CredentialResponseIsTheJSONRepresentationOfAStoredCredentialData,
        )

        d = dict(src_dict)
        auth_type = d.pop("auth_type", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata | Unset
        if isinstance(_capabilities, Unset) or _capabilities is None:
            capabilities = UNSET
        else:
            capabilities = ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata.from_dict(_capabilities)

        created_at = d.pop("created_at", UNSET)

        _data = d.pop("data", UNSET)
        data: CredentialResponseIsTheJSONRepresentationOfAStoredCredentialData | Unset
        if isinstance(_data, Unset) or _data is None:
            data = UNSET
        else:
            data = CredentialResponseIsTheJSONRepresentationOfAStoredCredentialData.from_dict(_data)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        is_org_level = d.pop("is_org_level", UNSET)

        name = d.pop("name", UNSET)

        org_credential_id = d.pop("org_credential_id", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        usable = d.pop("usable", UNSET)

        user = d.pop("user", UNSET)

        credential_response_is_the_json_representation_of_a_stored_credential = cls(
            auth_type=auth_type,
            capabilities=capabilities,
            created_at=created_at,
            data=data,
            description=description,
            enabled=enabled,
            id=id,
            is_org_level=is_org_level,
            name=name,
            org_credential_id=org_credential_id,
            provider=provider,
            status=status,
            updated_at=updated_at,
            usable=usable,
            user=user,
        )

        credential_response_is_the_json_representation_of_a_stored_credential.additional_properties = d
        return credential_response_is_the_json_representation_of_a_stored_credential

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
