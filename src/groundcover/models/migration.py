from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Migration")


@_attrs_define
class Migration:
    """
    Attributes:
        created_at (datetime.datetime | Unset): The timestamp when the migration was created.
            Format: date-time
        created_by (str | Unset): The email of the user who created the migration.
        deleted_at (datetime.datetime | Unset): The timestamp when the migration was deleted.
            Format: date-time
        done_at (datetime.datetime | Unset): The timestamp when the migration was completed.
            Format: date-time
        migration_id (str | Unset): The unique identifier of the migration.
        name (str | Unset): The name of the migration.
        provider (str | Unset): The provider type for this migration.
        status (str | Unset): The current status of the migration.
        updated_at (datetime.datetime | Unset): The timestamp when the migration was last updated.
            Format: date-time
    """

    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    done_at: datetime.datetime | Unset = UNSET
    migration_id: str | Unset = UNSET
    name: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        done_at: str | Unset = UNSET
        if not isinstance(self.done_at, Unset):
            done_at = self.done_at.isoformat()

        migration_id = self.migration_id

        name = self.name

        provider = self.provider

        status = self.status

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if done_at is not UNSET:
            field_dict["doneAt"] = done_at
        if migration_id is not UNSET:
            field_dict["migrationId"] = migration_id
        if name is not UNSET:
            field_dict["name"] = name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        created_by = d.pop("createdBy", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset) or _deleted_at is None:
            deleted_at = UNSET
        else:
            deleted_at = parse_datetime(_deleted_at)

        _done_at = d.pop("doneAt", UNSET)
        done_at: datetime.datetime | Unset
        if isinstance(_done_at, Unset) or _done_at is None:
            done_at = UNSET
        else:
            done_at = parse_datetime(_done_at)

        migration_id = d.pop("migrationId", UNSET)

        name = d.pop("name", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        migration = cls(
            created_at=created_at,
            created_by=created_by,
            deleted_at=deleted_at,
            done_at=done_at,
            migration_id=migration_id,
            name=name,
            provider=provider,
            status=status,
            updated_at=updated_at,
        )

        migration.additional_properties = d
        return migration

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
