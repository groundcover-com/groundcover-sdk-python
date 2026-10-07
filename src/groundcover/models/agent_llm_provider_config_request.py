from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_llm_provider_entry_request import AgentLLMProviderEntryRequest


T = TypeVar("T", bound="AgentLLMProviderConfigRequest")


@_attrs_define
class AgentLLMProviderConfigRequest:
    """AgentLLMProviderConfigRequest is forwarded to agent-service to set the org-level
    LLM provider config. The raw key is never sent here — only the Fleet Manager ref.

        Attributes:
            base_url (str | Unset): Provider-compatible endpoint base URL. Conditionally required when provider is
                anthropic_compatible_endpoint; enforced by agent-service validation.
            model_id (str | Unset):
            primary_provider_id (str | Unset):
            provider (str | Unset): Legacy single-provider selection. Use providers and primaryProviderId for multiple
                configurations.
            providers (list[AgentLLMProviderEntryRequest] | Unset):
            secret_ref (str | Unset): Fleet Manager secret ref (secretRef::store::<id>) for the provider's API key.
                Omit for providers that authenticate via ambient identity.
    """

    base_url: str | Unset = UNSET
    model_id: str | Unset = UNSET
    primary_provider_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    providers: list[AgentLLMProviderEntryRequest] | Unset = UNSET
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        model_id = self.model_id

        primary_provider_id = self.primary_provider_id

        provider = self.provider

        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        secret_ref = self.secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if primary_provider_id is not UNSET:
            field_dict["primaryProviderId"] = primary_provider_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if providers is not UNSET:
            field_dict["providers"] = providers
        if secret_ref is not UNSET:
            field_dict["secretRef"] = secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_llm_provider_entry_request import AgentLLMProviderEntryRequest

        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        model_id = d.pop("modelId", UNSET)

        primary_provider_id = d.pop("primaryProviderId", UNSET)

        provider = d.pop("provider", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[AgentLLMProviderEntryRequest] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = AgentLLMProviderEntryRequest.from_dict(providers_item_data)

                providers.append(providers_item)

        secret_ref = d.pop("secretRef", UNSET)

        agent_llm_provider_config_request = cls(
            base_url=base_url,
            model_id=model_id,
            primary_provider_id=primary_provider_id,
            provider=provider,
            providers=providers,
            secret_ref=secret_ref,
        )

        agent_llm_provider_config_request.additional_properties = d
        return agent_llm_provider_config_request

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
