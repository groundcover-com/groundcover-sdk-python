from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentDiscoverModelsRequest")


@_attrs_define
class AgentDiscoverModelsRequest:
    """
    Attributes:
        provider (str):
        api_key (str | Unset): Sensitive credential used only for discovery; never persisted.
        base_url (str | Unset):
        provider_id (str | Unset):
    """

    provider: str
    api_key: str | Unset = UNSET
    base_url: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        api_key = self.api_key

        base_url = self.base_url

        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id

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

        api_key = d.pop("apiKey", UNSET)

        base_url = d.pop("baseUrl", UNSET)

        provider_id = d.pop("providerId", UNSET)

        agent_discover_models_request = cls(
            provider=provider,
            api_key=api_key,
            base_url=base_url,
            provider_id=provider_id,
        )

        agent_discover_models_request.additional_properties = d
        return agent_discover_models_request

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
