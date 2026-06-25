from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_policy_ref import ApiKeyPolicyRef


T = TypeVar("T", bound="ListApiKeysResponseItem")


@_attrs_define
class ListApiKeysResponseItem:
    """
    Attributes:
        created_by (str | Unset): Email of the user who created the key.
        creation_date (datetime.datetime | Unset): Timestamp when the key was created.
            Format: date-time
        description (str | Unset): Optional description for the API key.
        expired_at (datetime.datetime | Unset): Timestamp when the key expires/expired (null if no expiration).
            Format: date-time
        id (str | Unset): The UUID of the API key resource.
        last_active (datetime.datetime | Unset): Timestamp of the last activity detected for this key.
            Format: date-time
        name (str | Unset): User-defined name for the API key.
        policies (list[ApiKeyPolicyRef] | Unset): Policies associated with the service account owning this key.
        revoked_at (datetime.datetime | Unset): Timestamp when the key was revoked (null if active).
            Format: date-time
        service_account_id (str | Unset): The UUID of the service account this key belongs to.
        service_account_name (str | Unset): The name of the service account this key belongs to.
    """

    created_by: str | Unset = UNSET
    creation_date: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    expired_at: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    last_active: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    policies: list[ApiKeyPolicyRef] | Unset = UNSET
    revoked_at: datetime.datetime | Unset = UNSET
    service_account_id: str | Unset = UNSET
    service_account_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        creation_date: str | Unset = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        description = self.description

        expired_at: str | Unset = UNSET
        if not isinstance(self.expired_at, Unset):
            expired_at = self.expired_at.isoformat()

        id = self.id

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

        revoked_at: str | Unset = UNSET
        if not isinstance(self.revoked_at, Unset):
            revoked_at = self.revoked_at.isoformat()

        service_account_id = self.service_account_id

        service_account_name = self.service_account_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if description is not UNSET:
            field_dict["description"] = description
        if expired_at is not UNSET:
            field_dict["expiredAt"] = expired_at
        if id is not UNSET:
            field_dict["id"] = id
        if last_active is not UNSET:
            field_dict["lastActive"] = last_active
        if name is not UNSET:
            field_dict["name"] = name
        if policies is not UNSET:
            field_dict["policies"] = policies
        if revoked_at is not UNSET:
            field_dict["revokedAt"] = revoked_at
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if service_account_name is not UNSET:
            field_dict["serviceAccountName"] = service_account_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_policy_ref import ApiKeyPolicyRef

        d = dict(src_dict)
        created_by = d.pop("createdBy", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: datetime.datetime | Unset
        if isinstance(_creation_date, Unset) or _creation_date is None:
            creation_date = UNSET
        else:
            creation_date = parse_datetime(_creation_date)

        description = d.pop("description", UNSET)

        _expired_at = d.pop("expiredAt", UNSET)
        expired_at: datetime.datetime | Unset
        if isinstance(_expired_at, Unset) or _expired_at is None:
            expired_at = UNSET
        else:
            expired_at = parse_datetime(_expired_at)

        id = d.pop("id", UNSET)

        _last_active = d.pop("lastActive", UNSET)
        last_active: datetime.datetime | Unset
        if isinstance(_last_active, Unset) or _last_active is None:
            last_active = UNSET
        else:
            last_active = parse_datetime(_last_active)

        name = d.pop("name", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[ApiKeyPolicyRef] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = ApiKeyPolicyRef.from_dict(policies_item_data)

                policies.append(policies_item)

        _revoked_at = d.pop("revokedAt", UNSET)
        revoked_at: datetime.datetime | Unset
        if isinstance(_revoked_at, Unset) or _revoked_at is None:
            revoked_at = UNSET
        else:
            revoked_at = parse_datetime(_revoked_at)

        service_account_id = d.pop("serviceAccountId", UNSET)

        service_account_name = d.pop("serviceAccountName", UNSET)

        list_api_keys_response_item = cls(
            created_by=created_by,
            creation_date=creation_date,
            description=description,
            expired_at=expired_at,
            id=id,
            last_active=last_active,
            name=name,
            policies=policies,
            revoked_at=revoked_at,
            service_account_id=service_account_id,
            service_account_name=service_account_name,
        )

        list_api_keys_response_item.additional_properties = d
        return list_api_keys_response_item

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
