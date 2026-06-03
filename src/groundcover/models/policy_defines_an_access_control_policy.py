from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
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


T = TypeVar("T", bound="PolicyDefinesAnAccessControlPolicy")


@_attrs_define
class PolicyDefinesAnAccessControlPolicy:
    """
    Attributes:
        name (str): Name of the policy.
        claim_role (str | Unset): Optional claim role for the policy.
        created_by (str | Unset): Email of the user who created the policy.
        created_timestamp (datetime.datetime | Unset): Timestamp when the policy was created.
        data_scope (DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions | Unset):
        description (str | Unset): Optional description of the policy.
        read_only (bool | Unset): Indicates if the policy is read-only (system managed).
        revision_number (int | Unset): Revision number for optimistic locking.
        role (RoleMapDefinesTheMappingOfRolesToPermissions | Unset): It is used within a Policy.
        tenant_uuid (str | Unset): Tenant associated with the policy.
        updated_by (str | Unset): Email of the user who last updated the policy.
        updated_timestamp (datetime.datetime | Unset): Timestamp when the policy was last updated.
        uuid (str | Unset): Unique identifier for the policy.
    """

    name: str
    claim_role: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_timestamp: datetime.datetime | Unset = UNSET
    data_scope: DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions | Unset = UNSET
    description: str | Unset = UNSET
    read_only: bool | Unset = UNSET
    revision_number: int | Unset = UNSET
    role: RoleMapDefinesTheMappingOfRolesToPermissions | Unset = UNSET
    tenant_uuid: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    updated_timestamp: datetime.datetime | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        claim_role = self.claim_role

        created_by = self.created_by

        created_timestamp: str | Unset = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        data_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_scope, Unset):
            data_scope = self.data_scope.to_dict()

        description = self.description

        read_only = self.read_only

        revision_number = self.revision_number

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        tenant_uuid = self.tenant_uuid

        updated_by = self.updated_by

        updated_timestamp: str | Unset = UNSET
        if not isinstance(self.updated_timestamp, Unset):
            updated_timestamp = self.updated_timestamp.isoformat()

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if claim_role is not UNSET:
            field_dict["claimRole"] = claim_role
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if data_scope is not UNSET:
            field_dict["dataScope"] = data_scope
        if description is not UNSET:
            field_dict["description"] = description
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if role is not UNSET:
            field_dict["role"] = role
        if tenant_uuid is not UNSET:
            field_dict["tenantUuid"] = tenant_uuid
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if updated_timestamp is not UNSET:
            field_dict["updatedTimestamp"] = updated_timestamp
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

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

        created_by = d.pop("createdBy", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: datetime.datetime | Unset
        if isinstance(_created_timestamp, Unset) or _created_timestamp is None:
            created_timestamp = UNSET
        else:
            created_timestamp = parse_datetime(_created_timestamp)

        _data_scope = d.pop("dataScope", UNSET)
        data_scope: DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions | Unset
        if isinstance(_data_scope, Unset) or _data_scope is None:
            data_scope = UNSET
        else:
            data_scope = DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions.from_dict(_data_scope)

        description = d.pop("description", UNSET)

        read_only = d.pop("readOnly", UNSET)

        revision_number = d.pop("revisionNumber", UNSET)

        _role = d.pop("role", UNSET)
        role: RoleMapDefinesTheMappingOfRolesToPermissions | Unset
        if isinstance(_role, Unset) or _role is None:
            role = UNSET
        else:
            role = RoleMapDefinesTheMappingOfRolesToPermissions.from_dict(_role)

        tenant_uuid = d.pop("tenantUuid", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        _updated_timestamp = d.pop("updatedTimestamp", UNSET)
        updated_timestamp: datetime.datetime | Unset
        if isinstance(_updated_timestamp, Unset) or _updated_timestamp is None:
            updated_timestamp = UNSET
        else:
            updated_timestamp = parse_datetime(_updated_timestamp)

        uuid = d.pop("uuid", UNSET)

        policy_defines_an_access_control_policy = cls(
            name=name,
            claim_role=claim_role,
            created_by=created_by,
            created_timestamp=created_timestamp,
            data_scope=data_scope,
            description=description,
            read_only=read_only,
            revision_number=revision_number,
            role=role,
            tenant_uuid=tenant_uuid,
            updated_by=updated_by,
            updated_timestamp=updated_timestamp,
            uuid=uuid,
        )

        policy_defines_an_access_control_policy.additional_properties = d
        return policy_defines_an_access_control_policy

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
