from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentLLMProviderConfigRequest")


@_attrs_define
class AgentLLMProviderConfigRequest:
    """AgentLLMProviderConfigRequest is forwarded to agent-service to set the org-level
    LLM provider config. The raw key is never sent here — only the Fleet Manager ref.

        Attributes:
            provider (str): The LLM provider to use (anthropic, azure, vertex, bedrock).
            secret_ref (str | Unset): Fleet Manager secret ref (secretRef::store::<id>) for the provider's API key.
                Omit for providers that authenticate via ambient identity.
    """

    provider: str
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        secret_ref = self.secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
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
        provider = d.pop("provider")

        secret_ref = d.pop("secretRef", UNSET)

        agent_llm_provider_config_request = cls(
            provider=provider,
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
