from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v2_monitor_entity import V2MonitorEntity


T = TypeVar("T", bound="BatchReadMonitorsV2ResponseMonitors")


@_attrs_define
class BatchReadMonitorsV2ResponseMonitors:
    """ """

    additional_properties: dict[str, V2MonitorEntity] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_monitor_entity import V2MonitorEntity

        d = dict(src_dict)
        batch_read_monitors_v2_response_monitors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = V2MonitorEntity.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        batch_read_monitors_v2_response_monitors.additional_properties = additional_properties
        return batch_read_monitors_v2_response_monitors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> V2MonitorEntity:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: V2MonitorEntity) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
