from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_feature_permissions_contains_role_defaults_with_consolidated_policy_overrides_applied_additional_property import (
    EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesAppliedAdditionalProperty,
)

T = TypeVar("T", bound="EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesApplied")


@_attrs_define
class EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesApplied:
    """ """

    additional_properties: dict[
        str, EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesAppliedAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

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
        effective_feature_permissions_contains_role_defaults_with_consolidated_policy_overrides_applied = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesAppliedAdditionalProperty(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        effective_feature_permissions_contains_role_defaults_with_consolidated_policy_overrides_applied.additional_properties = additional_properties
        return effective_feature_permissions_contains_role_defaults_with_consolidated_policy_overrides_applied

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesAppliedAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: EffectiveFeaturePermissionsContainsRoleDefaultsWithConsolidatedPolicyOverridesAppliedAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
