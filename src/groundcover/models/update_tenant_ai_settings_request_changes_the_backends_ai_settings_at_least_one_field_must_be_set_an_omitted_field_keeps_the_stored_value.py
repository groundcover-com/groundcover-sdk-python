from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar(
    "T",
    bound="UpdateTenantAISettingsRequestChangesTheBackendsAISettingsAtLeastOneFieldMustBeSetAnOmittedFieldKeepsTheStoredValue",
)


@_attrs_define
class UpdateTenantAISettingsRequestChangesTheBackendsAISettingsAtLeastOneFieldMustBeSetAnOmittedFieldKeepsTheStoredValue:
    """
    Attributes:
        customer_ai_features_opt_out (bool | None | Unset): Opts the backend out of AI features; omitted keeps the
            stored value.
        semantic_intelligence_enabled (bool | None | Unset): Turns background analysis of AI conversations on or off;
            omitted keeps the stored value.
    """

    customer_ai_features_opt_out: bool | None | Unset = UNSET
    semantic_intelligence_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_ai_features_opt_out: bool | None | Unset
        if isinstance(self.customer_ai_features_opt_out, Unset):
            customer_ai_features_opt_out = UNSET
        else:
            customer_ai_features_opt_out = self.customer_ai_features_opt_out

        semantic_intelligence_enabled: bool | None | Unset
        if isinstance(self.semantic_intelligence_enabled, Unset):
            semantic_intelligence_enabled = UNSET
        else:
            semantic_intelligence_enabled = self.semantic_intelligence_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_ai_features_opt_out is not UNSET:
            field_dict["customerAIFeaturesOptOut"] = customer_ai_features_opt_out
        if semantic_intelligence_enabled is not UNSET:
            field_dict["semanticIntelligenceEnabled"] = semantic_intelligence_enabled

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

        def _parse_customer_ai_features_opt_out(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        customer_ai_features_opt_out = _parse_customer_ai_features_opt_out(d.pop("customerAIFeaturesOptOut", UNSET))

        def _parse_semantic_intelligence_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        semantic_intelligence_enabled = _parse_semantic_intelligence_enabled(
            d.pop("semanticIntelligenceEnabled", UNSET)
        )

        update_tenant_ai_settings_request_changes_the_backends_ai_settings_at_least_one_field_must_be_set_an_omitted_field_keeps_the_stored_value = cls(
            customer_ai_features_opt_out=customer_ai_features_opt_out,
            semantic_intelligence_enabled=semantic_intelligence_enabled,
        )

        update_tenant_ai_settings_request_changes_the_backends_ai_settings_at_least_one_field_must_be_set_an_omitted_field_keeps_the_stored_value.additional_properties = d
        return update_tenant_ai_settings_request_changes_the_backends_ai_settings_at_least_one_field_must_be_set_an_omitted_field_keeps_the_stored_value

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
