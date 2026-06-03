from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_mappings_request_provider import UpdateMappingsRequestProvider

if TYPE_CHECKING:
    from ..models.mapping_config import MappingConfig


T = TypeVar("T", bound="UpdateMappingsRequest")


@_attrs_define
class UpdateMappingsRequest:
    """
    Attributes:
        config (MappingConfig):
        provider (UpdateMappingsRequestProvider): The provider type for this mappings configuration.
        version (int): The current version of the mappings configuration (for optimistic concurrency control).
    """

    config: MappingConfig
    provider: UpdateMappingsRequestProvider
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        provider = self.provider.value

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "provider": provider,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mapping_config import MappingConfig

        d = dict(src_dict)
        config = MappingConfig.from_dict(d.pop("config"))

        provider = UpdateMappingsRequestProvider(d.pop("provider"))

        version = d.pop("version")

        update_mappings_request = cls(
            config=config,
            provider=provider,
            version=version,
        )

        update_mappings_request.additional_properties = d
        return update_mappings_request

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
