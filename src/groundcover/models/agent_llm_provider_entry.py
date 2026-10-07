from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentLLMProviderEntry")


@_attrs_define
class AgentLLMProviderEntry:
    """
    Attributes:
        base_url (str | Unset):
        enabled_models (list[str] | Unset):
        id (str | Unset):
        is_secret_ref_set (bool | Unset):
        model_id (str | Unset):
        provider (str | Unset):
        unpriced_models (list[str] | Unset): Enabled models for which the cost calculator has no model-specific pricing.
    """

    base_url: str | Unset = UNSET
    enabled_models: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    is_secret_ref_set: bool | Unset = UNSET
    model_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    unpriced_models: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        enabled_models: list[str] | Unset = UNSET
        if not isinstance(self.enabled_models, Unset):
            enabled_models = self.enabled_models

        id = self.id

        is_secret_ref_set = self.is_secret_ref_set

        model_id = self.model_id

        provider = self.provider

        unpriced_models: list[str] | Unset = UNSET
        if not isinstance(self.unpriced_models, Unset):
            unpriced_models = self.unpriced_models

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if enabled_models is not UNSET:
            field_dict["enabledModels"] = enabled_models
        if id is not UNSET:
            field_dict["id"] = id
        if is_secret_ref_set is not UNSET:
            field_dict["isSecretRefSet"] = is_secret_ref_set
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if unpriced_models is not UNSET:
            field_dict["unpricedModels"] = unpriced_models

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
        base_url = d.pop("baseUrl", UNSET)

        enabled_models = cast(list[str], d.pop("enabledModels", UNSET))

        id = d.pop("id", UNSET)

        is_secret_ref_set = d.pop("isSecretRefSet", UNSET)

        model_id = d.pop("modelId", UNSET)

        provider = d.pop("provider", UNSET)

        unpriced_models = cast(list[str], d.pop("unpricedModels", UNSET))

        agent_llm_provider_entry = cls(
            base_url=base_url,
            enabled_models=enabled_models,
            id=id,
            is_secret_ref_set=is_secret_ref_set,
            model_id=model_id,
            provider=provider,
            unpriced_models=unpriced_models,
        )

        agent_llm_provider_entry.additional_properties = d
        return agent_llm_provider_entry

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
