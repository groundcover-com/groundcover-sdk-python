from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_model_capabilities import AgentModelCapabilities


T = TypeVar("T", bound="AgentChatModel")


@_attrs_define
class AgentChatModel:
    """
    Attributes:
        capabilities (AgentModelCapabilities):
        display_name (str):
        is_default (bool):
        model_id (str):
        provider (str):
        provider_id (str):
    """

    capabilities: AgentModelCapabilities
    display_name: str
    is_default: bool
    model_id: str
    provider: str
    provider_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capabilities = self.capabilities.to_dict()

        display_name = self.display_name

        is_default = self.is_default

        model_id = self.model_id

        provider = self.provider

        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capabilities": capabilities,
                "displayName": display_name,
                "isDefault": is_default,
                "modelId": model_id,
                "provider": provider,
                "providerId": provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_model_capabilities import AgentModelCapabilities

        d = dict(src_dict)
        capabilities = AgentModelCapabilities.from_dict(d.pop("capabilities"))

        display_name = d.pop("displayName")

        is_default = d.pop("isDefault")

        model_id = d.pop("modelId")

        provider = d.pop("provider")

        provider_id = d.pop("providerId")

        agent_chat_model = cls(
            capabilities=capabilities,
            display_name=display_name,
            is_default=is_default,
            model_id=model_id,
            provider=provider,
            provider_id=provider_id,
        )

        agent_chat_model.additional_properties = d
        return agent_chat_model

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
