from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_account_policy_ref import ServiceAccountPolicyRef


T = TypeVar("T", bound="ServiceAccountsWithPolicy")


@_attrs_define
class ServiceAccountsWithPolicy:
    """
    Attributes:
        deleted (bool | Unset): Indicates if the service account has been marked for deletion.
        email (str | Unset): The email address of the service account.
        last_active (datetime.datetime | Unset): Timestamp of the last activity detected for this service account.
        name (str | Unset): The name of the service account.
        policies (list[ServiceAccountPolicyRef] | Unset): Policies assigned to the service account.
        service_account_id (str | Unset): The UUID of the service account.
    """

    deleted: bool | Unset = UNSET
    email: str | Unset = UNSET
    last_active: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    policies: list[ServiceAccountPolicyRef] | Unset = UNSET
    service_account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        email = self.email

        last_active: str | Unset = UNSET
        if not isinstance(self.last_active, Unset):
            last_active = self.last_active.isoformat()

        name = self.name

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        service_account_id = self.service_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if email is not UNSET:
            field_dict["email"] = email
        if last_active is not UNSET:
            field_dict["lastActive"] = last_active
        if name is not UNSET:
            field_dict["name"] = name
        if policies is not UNSET:
            field_dict["policies"] = policies
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_account_policy_ref import ServiceAccountPolicyRef

        d = dict(src_dict)
        deleted = d.pop("deleted", UNSET)

        email = d.pop("email", UNSET)

        _last_active = d.pop("lastActive", UNSET)
        last_active: datetime.datetime | Unset
        if isinstance(_last_active, Unset) or _last_active is None:
            last_active = UNSET
        else:
            last_active = parse_datetime(_last_active)

        name = d.pop("name", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[ServiceAccountPolicyRef] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = ServiceAccountPolicyRef.from_dict(policies_item_data)

                policies.append(policies_item)

        service_account_id = d.pop("serviceAccountId", UNSET)

        service_accounts_with_policy = cls(
            deleted=deleted,
            email=email,
            last_active=last_active,
            name=name,
            policies=policies,
            service_account_id=service_account_id,
        )

        service_accounts_with_policy.additional_properties = d
        return service_accounts_with_policy

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
