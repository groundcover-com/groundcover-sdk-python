from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_integration_config_tags import DataIntegrationConfigTags


T = TypeVar("T", bound="DataIntegrationConfig")


@_attrs_define
class DataIntegrationConfig:
    """
    Attributes:
        cluster (str | Unset):
        config (str | Unset):
        id (str | Unset):
        is_archived (bool | Unset):
        is_paused (bool | Unset):
        name (str | Unset):
        tags (DataIntegrationConfigTags | Unset):
        type_ (str | Unset):
        update_timestamp (datetime.datetime | Unset):
        updated_by (str | Unset):
    """

    cluster: str | Unset = UNSET
    config: str | Unset = UNSET
    id: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_paused: bool | Unset = UNSET
    name: str | Unset = UNSET
    tags: DataIntegrationConfigTags | Unset = UNSET
    type_: str | Unset = UNSET
    update_timestamp: datetime.datetime | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        config = self.config

        id = self.id

        is_archived = self.is_archived

        is_paused = self.is_paused

        name = self.name

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        type_ = self.type_

        update_timestamp: str | Unset = UNSET
        if not isinstance(self.update_timestamp, Unset):
            update_timestamp = self.update_timestamp.isoformat()

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if config is not UNSET:
            field_dict["config"] = config
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived
        if is_paused is not UNSET:
            field_dict["is_paused"] = is_paused
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if update_timestamp is not UNSET:
            field_dict["update_timestamp"] = update_timestamp
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_integration_config_tags import DataIntegrationConfigTags

        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        config = d.pop("config", UNSET)

        id = d.pop("id", UNSET)

        is_archived = d.pop("is_archived", UNSET)

        is_paused = d.pop("is_paused", UNSET)

        name = d.pop("name", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: DataIntegrationConfigTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = DataIntegrationConfigTags.from_dict(_tags)

        type_ = d.pop("type", UNSET)

        _update_timestamp = d.pop("update_timestamp", UNSET)
        update_timestamp: datetime.datetime | Unset
        if isinstance(_update_timestamp, Unset) or _update_timestamp is None:
            update_timestamp = UNSET
        else:
            update_timestamp = parse_datetime(_update_timestamp)

        updated_by = d.pop("updated_by", UNSET)

        data_integration_config = cls(
            cluster=cluster,
            config=config,
            id=id,
            is_archived=is_archived,
            is_paused=is_paused,
            name=name,
            tags=tags,
            type_=type_,
            update_timestamp=update_timestamp,
            updated_by=updated_by,
        )

        data_integration_config.additional_properties = d
        return data_integration_config

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
