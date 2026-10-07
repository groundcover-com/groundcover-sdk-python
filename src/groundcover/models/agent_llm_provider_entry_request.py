from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentLLMProviderEntryRequest")


@_attrs_define
class AgentLLMProviderEntryRequest:
    """
    Attributes:
        id (str):
        model_id (str): Provider-specific model or deployment ID; custom IDs are validated by the provider.
        provider (str): Hosting service or compatible endpoint: anthropic, anthropic_compatible_endpoint, openai,
            openai_compatible_endpoint, bedrock, vertex, or azure.
        base_url (str | Unset):
        enabled_models (list[str] | Unset): Enabled model IDs for this provider. The primary modelId must be included.
            Omission preserves existing models and enables modelId for legacy clients.
        secret_ref (str | Unset):
    """

    id: str
    model_id: str
    provider: str
    base_url: str | Unset = UNSET
    enabled_models: list[str] | Unset = UNSET
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_id = self.model_id

        provider = self.provider

        base_url = self.base_url

        enabled_models: list[str] | Unset = UNSET
        if not isinstance(self.enabled_models, Unset):
            enabled_models = self.enabled_models

        secret_ref = self.secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "modelId": model_id,
                "provider": provider,
            }
        )
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if enabled_models is not UNSET:
            field_dict["enabledModels"] = enabled_models
        if secret_ref is not UNSET:
            field_dict["secretRef"] = secret_ref

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
        id = d.pop("id")

        model_id = d.pop("modelId")

        provider = d.pop("provider")

        base_url = d.pop("baseUrl", UNSET)

        enabled_models = cast(list[str], d.pop("enabledModels", UNSET))

        secret_ref = d.pop("secretRef", UNSET)

        agent_llm_provider_entry_request = cls(
            id=id,
            model_id=model_id,
            provider=provider,
            base_url=base_url,
            enabled_models=enabled_models,
            secret_ref=secret_ref,
        )

        agent_llm_provider_entry_request.additional_properties = d
        return agent_llm_provider_entry_request

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
