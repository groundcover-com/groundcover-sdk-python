from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mapping_response_provider import MappingResponseProvider
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mapping_config import MappingConfig


T = TypeVar("T", bound="MappingResponse")


@_attrs_define
class MappingResponse:
    """
    Attributes:
        config (MappingConfig | Unset):
        created_at (datetime.datetime | Unset): The timestamp when the mappings configuration was created.
            Format: date-time
        data_type (str | Unset): The data type for this mappings configuration.
        deleted_at (datetime.datetime | Unset): The timestamp when the mappings configuration was soft deleted.
            Format: date-time
        id (str | Unset): The unique identifier of the mappings configuration.
        provider (MappingResponseProvider | Unset): The provider type for this mappings configuration.
        updated_at (datetime.datetime | Unset): The timestamp when the mappings configuration was last updated.
            Format: date-time
        version (int | Unset): The version of this mappings configuration.
    """

    config: MappingConfig | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    data_type: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    provider: MappingResponseProvider | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        data_type = self.data_type

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        id = self.id

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if id is not UNSET:
            field_dict["id"] = id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mapping_config import MappingConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: MappingConfig | Unset
        if isinstance(_config, Unset) or _config is None:
            config = UNSET
        else:
            config = MappingConfig.from_dict(_config)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        data_type = d.pop("dataType", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset) or _deleted_at is None:
            deleted_at = UNSET
        else:
            deleted_at = parse_datetime(_deleted_at)

        id = d.pop("id", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: MappingResponseProvider | Unset
        if isinstance(_provider, Unset) or _provider is None:
            provider = UNSET
        else:
            provider = MappingResponseProvider(_provider)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        version = d.pop("version", UNSET)

        mapping_response = cls(
            config=config,
            created_at=created_at,
            data_type=data_type,
            deleted_at=deleted_at,
            id=id,
            provider=provider,
            updated_at=updated_at,
            version=version,
        )

        mapping_response.additional_properties = d
        return mapping_response

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
