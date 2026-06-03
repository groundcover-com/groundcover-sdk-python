from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateTenantAISettingsRequest")


@_attrs_define
class UpdateTenantAISettingsRequest:
    """
    Attributes:
        customer_ai_features_opt_out (bool):
    """

    customer_ai_features_opt_out: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_ai_features_opt_out = self.customer_ai_features_opt_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerAIFeaturesOptOut": customer_ai_features_opt_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        customer_ai_features_opt_out = d.pop("customerAIFeaturesOptOut")

        update_tenant_ai_settings_request = cls(
            customer_ai_features_opt_out=customer_ai_features_opt_out,
        )

        update_tenant_ai_settings_request.additional_properties = d
        return update_tenant_ai_settings_request

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
