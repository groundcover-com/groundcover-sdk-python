from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MemberView")


@_attrs_define
class MemberView:
    """
    Attributes:
        archived_timestamp (datetime.datetime | Unset):
        created_timestamp (datetime.datetime | Unset):
        description (str | Unset):
        is_default (bool | Unset):
        is_favorite (bool | Unset):
        is_provisioned (bool | Unset):
        name (str | Unset):
        origin_id (str | Unset):
        origin_type (str | Unset):
        owner (str | Unset):
        preset (str | Unset):
        revision_number (int | Unset):
        status (str | Unset):
        team (str | Unset):
        tenant_uuid (str | Unset):
        updated_by (str | Unset):
        updated_timestamp (datetime.datetime | Unset):
        uuid (str | Unset):
        view_type (str | Unset):
    """

    archived_timestamp: datetime.datetime | Unset = UNSET
    created_timestamp: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    is_provisioned: bool | Unset = UNSET
    name: str | Unset = UNSET
    origin_id: str | Unset = UNSET
    origin_type: str | Unset = UNSET
    owner: str | Unset = UNSET
    preset: str | Unset = UNSET
    revision_number: int | Unset = UNSET
    status: str | Unset = UNSET
    team: str | Unset = UNSET
    tenant_uuid: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    updated_timestamp: datetime.datetime | Unset = UNSET
    uuid: str | Unset = UNSET
    view_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived_timestamp: str | Unset = UNSET
        if not isinstance(self.archived_timestamp, Unset):
            archived_timestamp = self.archived_timestamp.isoformat()

        created_timestamp: str | Unset = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        description = self.description

        is_default = self.is_default

        is_favorite = self.is_favorite

        is_provisioned = self.is_provisioned

        name = self.name

        origin_id = self.origin_id

        origin_type = self.origin_type

        owner = self.owner

        preset = self.preset

        revision_number = self.revision_number

        status = self.status

        team = self.team

        tenant_uuid = self.tenant_uuid

        updated_by = self.updated_by

        updated_timestamp: str | Unset = UNSET
        if not isinstance(self.updated_timestamp, Unset):
            updated_timestamp = self.updated_timestamp.isoformat()

        uuid = self.uuid

        view_type = self.view_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_timestamp is not UNSET:
            field_dict["archivedTimestamp"] = archived_timestamp
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_provisioned is not UNSET:
            field_dict["isProvisioned"] = is_provisioned
        if name is not UNSET:
            field_dict["name"] = name
        if origin_id is not UNSET:
            field_dict["originId"] = origin_id
        if origin_type is not UNSET:
            field_dict["originType"] = origin_type
        if owner is not UNSET:
            field_dict["owner"] = owner
        if preset is not UNSET:
            field_dict["preset"] = preset
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if status is not UNSET:
            field_dict["status"] = status
        if team is not UNSET:
            field_dict["team"] = team
        if tenant_uuid is not UNSET:
            field_dict["tenantUuid"] = tenant_uuid
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if updated_timestamp is not UNSET:
            field_dict["updatedTimestamp"] = updated_timestamp
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if view_type is not UNSET:
            field_dict["viewType"] = view_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        _archived_timestamp = d.pop("archivedTimestamp", UNSET)
        archived_timestamp: datetime.datetime | Unset
        if isinstance(_archived_timestamp, Unset) or _archived_timestamp is None:
            archived_timestamp = UNSET
        else:
            archived_timestamp = parse_datetime(_archived_timestamp)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: datetime.datetime | Unset
        if isinstance(_created_timestamp, Unset) or _created_timestamp is None:
            created_timestamp = UNSET
        else:
            created_timestamp = parse_datetime(_created_timestamp)

        description = d.pop("description", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        is_provisioned = d.pop("isProvisioned", UNSET)

        name = d.pop("name", UNSET)

        origin_id = d.pop("originId", UNSET)

        origin_type = d.pop("originType", UNSET)

        owner = d.pop("owner", UNSET)

        preset = d.pop("preset", UNSET)

        revision_number = d.pop("revisionNumber", UNSET)

        status = d.pop("status", UNSET)

        team = d.pop("team", UNSET)

        tenant_uuid = d.pop("tenantUuid", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        _updated_timestamp = d.pop("updatedTimestamp", UNSET)
        updated_timestamp: datetime.datetime | Unset
        if isinstance(_updated_timestamp, Unset) or _updated_timestamp is None:
            updated_timestamp = UNSET
        else:
            updated_timestamp = parse_datetime(_updated_timestamp)

        uuid = d.pop("uuid", UNSET)

        view_type = d.pop("viewType", UNSET)

        member_view = cls(
            archived_timestamp=archived_timestamp,
            created_timestamp=created_timestamp,
            description=description,
            is_default=is_default,
            is_favorite=is_favorite,
            is_provisioned=is_provisioned,
            name=name,
            origin_id=origin_id,
            origin_type=origin_type,
            owner=owner,
            preset=preset,
            revision_number=revision_number,
            status=status,
            team=team,
            tenant_uuid=tenant_uuid,
            updated_by=updated_by,
            updated_timestamp=updated_timestamp,
            uuid=uuid,
            view_type=view_type,
        )

        member_view.additional_properties = d
        return member_view

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
