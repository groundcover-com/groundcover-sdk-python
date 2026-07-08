from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentLLMProviderConfig")


@_attrs_define
class AgentLLMProviderConfig:
    """AgentLLMProviderConfig is the status payload returned by the LLM provider config
    endpoints. It never exposes the secret ref or the key.

        Attributes:
            is_secret_ref_set (bool | Unset): Whether an API key secret ref is configured.
            provider (str | Unset): The configured provider ("" when unset).
            updated_at (str | Unset): When the config was last updated (ISO-8601), if set.
            updated_by (str | Unset): Identifier of whoever last updated the config, if known.
            version (int | Unset): Monotonic version, bumped on every write.
    """

    is_secret_ref_set: bool | Unset = UNSET
    provider: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_secret_ref_set = self.is_secret_ref_set

        provider = self.provider

        updated_at = self.updated_at

        updated_by = self.updated_by

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_secret_ref_set is not UNSET:
            field_dict["isSecretRefSet"] = is_secret_ref_set
        if provider is not UNSET:
            field_dict["provider"] = provider
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if version is not UNSET:
            field_dict["version"] = version

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
        is_secret_ref_set = d.pop("isSecretRefSet", UNSET)

        provider = d.pop("provider", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        version = d.pop("version", UNSET)

        agent_llm_provider_config = cls(
            is_secret_ref_set=is_secret_ref_set,
            provider=provider,
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
