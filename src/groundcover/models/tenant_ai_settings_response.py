from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TenantAISettingsResponse")


@_attrs_define
class TenantAISettingsResponse:
    """
    Attributes:
        allow_ai_features (bool | Unset):
        backend_name (str | Unset):
        customer_ai_features_opt_out (bool | Unset):
        effective_ai_features_enabled (bool | Unset):
    """

    allow_ai_features: bool | Unset = UNSET
    backend_name: str | Unset = UNSET
    customer_ai_features_opt_out: bool | Unset = UNSET
    effective_ai_features_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_ai_features = self.allow_ai_features

        backend_name = self.backend_name

        customer_ai_features_opt_out = self.customer_ai_features_opt_out

        effective_ai_features_enabled = self.effective_ai_features_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_ai_features is not UNSET:
            field_dict["allowAIFeatures"] = allow_ai_features
        if backend_name is not UNSET:
            field_dict["backendName"] = backend_name
        if customer_ai_features_opt_out is not UNSET:
            field_dict["customerAIFeaturesOptOut"] = customer_ai_features_opt_out
        if effective_ai_features_enabled is not UNSET:
            field_dict["effectiveAIFeaturesEnabled"] = effective_ai_features_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        allow_ai_features = d.pop("allowAIFeatures", UNSET)

        backend_name = d.pop("backendName", UNSET)

        customer_ai_features_opt_out = d.pop("customerAIFeaturesOptOut", UNSET)

        effective_ai_features_enabled = d.pop("effectiveAIFeaturesEnabled", UNSET)

        tenant_ai_settings_response = cls(
            allow_ai_features=allow_ai_features,
            backend_name=backend_name,
            customer_ai_features_opt_out=customer_ai_features_opt_out,
            effective_ai_features_enabled=effective_ai_features_enabled,
        )

        tenant_ai_settings_response.additional_properties = d
        return tenant_ai_settings_response

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
