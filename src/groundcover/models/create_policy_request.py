from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_scope_contains_either_simple_or_advanced_scope_definitions import (
        DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions,
    )
    from ..models.role_map_defines_the_mapping_of_roles_to_permissions import (
        RoleMapDefinesTheMappingOfRolesToPermissions,
    )


T = TypeVar("T", bound="CreatePolicyRequest")


@_attrs_define
class CreatePolicyRequest:
    """
    Attributes:
        name (str): Name of the policy.
        claim_role (str | Unset): Optional claim role for the policy.
        data_scope (DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions | Unset):
        description (str | Unset): Optional description for the policy.
        role (RoleMapDefinesTheMappingOfRolesToPermissions | Unset): It is used within a Policy.
    """

    name: str
    claim_role: str | Unset = UNSET
    data_scope: DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions | Unset = UNSET
    description: str | Unset = UNSET
    role: RoleMapDefinesTheMappingOfRolesToPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        claim_role = self.claim_role

        data_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_scope, Unset):
            data_scope = self.data_scope.to_dict()

        description = self.description

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if claim_role is not UNSET:
            field_dict["claimRole"] = claim_role
        if data_scope is not UNSET:
            field_dict["dataScope"] = data_scope
        if description is not UNSET:
            field_dict["description"] = description
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_scope_contains_either_simple_or_advanced_scope_definitions import (
            DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions,
        )
        from ..models.role_map_defines_the_mapping_of_roles_to_permissions import (
            RoleMapDefinesTheMappingOfRolesToPermissions,
        )

        d = dict(src_dict)
        name = d.pop("name")

        claim_role = d.pop("claimRole", UNSET)

        _data_scope = d.pop("dataScope", UNSET)
        data_scope: DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions | Unset
        if isinstance(_data_scope, Unset) or _data_scope is None:
            data_scope = UNSET
        else:
            data_scope = DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions.from_dict(_data_scope)

        description = d.pop("description", UNSET)

        _role = d.pop("role", UNSET)
        role: RoleMapDefinesTheMappingOfRolesToPermissions | Unset
        if isinstance(_role, Unset) or _role is None:
            role = UNSET
        else:
            role = RoleMapDefinesTheMappingOfRolesToPermissions.from_dict(_role)

        create_policy_request = cls(
            name=name,
            claim_role=claim_role,
            data_scope=data_scope,
            description=description,
            role=role,
        )

        create_policy_request.additional_properties = d
        return create_policy_request

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
