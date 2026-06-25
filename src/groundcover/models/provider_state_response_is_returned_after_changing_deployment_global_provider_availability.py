from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ProviderStateResponseIsReturnedAfterChangingDeploymentGlobalProviderAvailability")


@_attrs_define
class ProviderStateResponseIsReturnedAfterChangingDeploymentGlobalProviderAvailability:
    """
    Attributes:
        enabled (bool | Unset): Whether the provider is globally enabled
        provider (str | Unset): The provider name Example: cursor.
    """

    enabled: bool | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if provider is not UNSET:
            field_dict["provider"] = provider

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
        enabled = d.pop("enabled", UNSET)

        provider = d.pop("provider", UNSET)

        provider_state_response_is_returned_after_changing_deployment_global_provider_availability = cls(
            enabled=enabled,
            provider=provider,
        )

        provider_state_response_is_returned_after_changing_deployment_global_provider_availability.additional_properties = d
        return provider_state_response_is_returned_after_changing_deployment_global_provider_availability

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
