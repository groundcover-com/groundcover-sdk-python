from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_data_integration_config_request_tags import UpdateDataIntegrationConfigRequestTags


T = TypeVar("T", bound="UpdateDataIntegrationConfigRequest")


@_attrs_define
class UpdateDataIntegrationConfigRequest:
    """
    Attributes:
        cluster (str | Unset):
        config (str | Unset):
        is_paused (bool | Unset):
        name (str | Unset):
        tags (UpdateDataIntegrationConfigRequestTags | Unset):
    """

    cluster: str | Unset = UNSET
    config: str | Unset = UNSET
    is_paused: bool | Unset = UNSET
    name: str | Unset = UNSET
    tags: UpdateDataIntegrationConfigRequestTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        config = self.config

        is_paused = self.is_paused

        name = self.name

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if config is not UNSET:
            field_dict["config"] = config
        if is_paused is not UNSET:
            field_dict["is_paused"] = is_paused
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_data_integration_config_request_tags import UpdateDataIntegrationConfigRequestTags

        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        config = d.pop("config", UNSET)

        is_paused = d.pop("is_paused", UNSET)

        name = d.pop("name", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: UpdateDataIntegrationConfigRequestTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = UpdateDataIntegrationConfigRequestTags.from_dict(_tags)

        update_data_integration_config_request = cls(
            cluster=cluster,
            config=config,
            is_paused=is_paused,
            name=name,
            tags=tags,
        )

        update_data_integration_config_request.additional_properties = d
        return update_data_integration_config_request

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
