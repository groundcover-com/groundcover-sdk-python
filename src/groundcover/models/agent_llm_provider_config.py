from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_llm_provider_entry import AgentLLMProviderEntry


T = TypeVar("T", bound="AgentLLMProviderConfig")


@_attrs_define
class AgentLLMProviderConfig:
    """AgentLLMProviderConfig is the status payload returned by the LLM provider config
    endpoints. It never exposes the secret ref or the key.

        Attributes:
            base_url (str | Unset): Provider-compatible endpoint base URL, if configured.
            default_provider (None | str | Unset): Static provider configured by LLM_PROVIDER. Null when dummy_provider
                marks
                a deployment without a managed default. This is response-only metadata and
                is not part of AgentLLMProviderConfigRequest.
                Nullable: true
            is_secret_ref_set (bool | Unset): Whether an API key secret ref is configured.
            model_id (str | Unset):
            primary_provider_id (str | Unset):
            provider (str | Unset): The configured provider ("" when unset).
            providers (list[AgentLLMProviderEntry] | Unset):
            updated_at (str | Unset): When the config was last updated (ISO-8601), if set.
            updated_by (str | Unset): Identifier of whoever last updated the config, if known.
            version (int | Unset): Monotonic version, bumped on every write.
    """

    base_url: str | Unset = UNSET
    default_provider: None | str | Unset = UNSET
    is_secret_ref_set: bool | Unset = UNSET
    model_id: str | Unset = UNSET
    primary_provider_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    providers: list[AgentLLMProviderEntry] | Unset = UNSET
    updated_at: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        default_provider: None | str | Unset
        if isinstance(self.default_provider, Unset):
            default_provider = UNSET
        else:
            default_provider = self.default_provider

        is_secret_ref_set = self.is_secret_ref_set

        model_id = self.model_id

        primary_provider_id = self.primary_provider_id

        provider = self.provider

        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        updated_at = self.updated_at

        updated_by = self.updated_by

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if default_provider is not UNSET:
            field_dict["defaultProvider"] = default_provider
        if is_secret_ref_set is not UNSET:
            field_dict["isSecretRefSet"] = is_secret_ref_set
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if primary_provider_id is not UNSET:
            field_dict["primaryProviderId"] = primary_provider_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if providers is not UNSET:
            field_dict["providers"] = providers
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_llm_provider_entry import AgentLLMProviderEntry

        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        def _parse_default_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_provider = _parse_default_provider(d.pop("defaultProvider", UNSET))

        is_secret_ref_set = d.pop("isSecretRefSet", UNSET)

        model_id = d.pop("modelId", UNSET)

        primary_provider_id = d.pop("primaryProviderId", UNSET)

        provider = d.pop("provider", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[AgentLLMProviderEntry] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = AgentLLMProviderEntry.from_dict(providers_item_data)

                providers.append(providers_item)

        updated_at = d.pop("updatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        version = d.pop("version", UNSET)

        agent_llm_provider_config = cls(
            base_url=base_url,
            default_provider=default_provider,
            is_secret_ref_set=is_secret_ref_set,
            model_id=model_id,
            primary_provider_id=primary_provider_id,
            provider=provider,
            providers=providers,
            updated_at=updated_at,
            updated_by=updated_by,
            version=version,
        )

        agent_llm_provider_config.additional_properties = d
        return agent_llm_provider_config

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
