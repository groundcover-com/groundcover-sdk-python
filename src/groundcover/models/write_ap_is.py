from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

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
        revision (int):
        updated_at (str):
        when_to_use (str):
        created_by (str | Unset):
        description (str | Unset):
        identifier (str | Unset):
        updated_by (str | Unset):
    """

    created_at: str
    id: str
    instructions: str
    is_organizational: bool
    is_provisioned: bool
    name: str
    revision: int
    updated_at: str
    when_to_use: str
    created_by: str | Unset = UNSET
    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        instructions = self.instructions

        is_organizational = self.is_organizational

        is_provisioned = self.is_provisioned

        name = self.name

        revision = self.revision

        updated_at = self.updated_at

        when_to_use = self.when_to_use

        created_by = self.created_by

        description = self.description

        identifier = self.identifier

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

        revision = d.pop("revision")

        updated_at = d.pop("updated_at")

        when_to_use = d.pop("when_to_use")

        created_by = d.pop("created_by", UNSET)

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        write_ap_is = cls(
            created_at=created_at,
            id=id,
            instructions=instructions,
            is_organizational=is_organizational,
            is_provisioned=is_provisioned,
            name=name,
            revision=revision,
            updated_at=updated_at,
            when_to_use=when_to_use,
            created_by=created_by,
            description=description,
            identifier=identifier,
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
