from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="WriteAPIs")


@_attrs_define
class WriteAPIs:
    """
    Attributes:
        created_at (str):
        id (str):
        instructions (str):
        is_organizational (bool):
        is_provisioned (bool):
        name (str):
        owner_user_id (str):
        revision (int):
        updated_at (str):
        when_to_use (str):
        created_by (None | str | Unset): Audit identity that created the Skill.
            Nullable: true
        description (None | str | Unset): Optional human-readable Skill description.
            Nullable: true
        identifier (None | str | Unset): Optional stable Skill identifier.
            Nullable: true
        owner_email (None | str | Unset): Owner email used for user-facing attribution when available.
            Nullable: true
        updated_by (None | str | Unset): Audit identity that most recently updated the Skill.
            Nullable: true
    """

    created_at: str
    id: str
    instructions: str
    is_organizational: bool
    is_provisioned: bool
    name: str
    owner_user_id: str
    revision: int
    updated_at: str
    when_to_use: str
    created_by: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    identifier: None | str | Unset = UNSET
    owner_email: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        instructions = self.instructions

        is_organizational = self.is_organizational

        is_provisioned = self.is_provisioned

        name = self.name

        owner_user_id = self.owner_user_id

        revision = self.revision

        updated_at = self.updated_at

        when_to_use = self.when_to_use

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        owner_email: None | str | Unset
        if isinstance(self.owner_email, Unset):
            owner_email = UNSET
        else:
            owner_email = self.owner_email

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "instructions": instructions,
                "is_organizational": is_organizational,
                "is_provisioned": is_provisioned,
                "name": name,
                "owner_user_id": owner_user_id,
                "revision": revision,
                "updated_at": updated_at,
                "when_to_use": when_to_use,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if owner_email is not UNSET:
            field_dict["owner_email"] = owner_email
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

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
        created_at = d.pop("created_at")

        id = d.pop("id")

        instructions = d.pop("instructions")

        is_organizational = d.pop("is_organizational")

        is_provisioned = d.pop("is_provisioned")

        name = d.pop("name")

        owner_user_id = d.pop("owner_user_id")

        revision = d.pop("revision")

        updated_at = d.pop("updated_at")

        when_to_use = d.pop("when_to_use")

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        def _parse_owner_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_email = _parse_owner_email(d.pop("owner_email", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        write_ap_is = cls(
            created_at=created_at,
            id=id,
            instructions=instructions,
            is_organizational=is_organizational,
            is_provisioned=is_provisioned,
            name=name,
            owner_user_id=owner_user_id,
            revision=revision,
            updated_at=updated_at,
            when_to_use=when_to_use,
            created_by=created_by,
            description=description,
            identifier=identifier,
            owner_email=owner_email,
            updated_by=updated_by,
        )

        write_ap_is.additional_properties = d
        return write_ap_is

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
