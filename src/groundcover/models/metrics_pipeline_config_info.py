from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relabel_config import RelabelConfig


T = TypeVar("T", bound="MetricsPipelineConfigInfo")


@_attrs_define
class MetricsPipelineConfigInfo:
    """Represents a metrics pipeline relabeling configuration entry

    Attributes:
        created_by (str | Unset):
        created_timestamp (datetime.datetime | Unset):
        rules (RelabelConfig | Unset):
        uuid (str | Unset):
    """

    created_by: str | Unset = UNSET
    created_timestamp: datetime.datetime | Unset = UNSET
    rules: RelabelConfig | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        created_timestamp: str | Unset = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_timestamp is not UNSET:
            field_dict["created_timestamp"] = created_timestamp
        if rules is not UNSET:
            field_dict["rules"] = rules
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relabel_config import RelabelConfig

        d = dict(src_dict)
        created_by = d.pop("created_by", UNSET)

        _created_timestamp = d.pop("created_timestamp", UNSET)
        created_timestamp: datetime.datetime | Unset
        if isinstance(_created_timestamp, Unset) or _created_timestamp is None:
            created_timestamp = UNSET
        else:
            created_timestamp = parse_datetime(_created_timestamp)

        _rules = d.pop("rules", UNSET)
        rules: RelabelConfig | Unset
        if isinstance(_rules, Unset) or _rules is None:
            rules = UNSET
        else:
            rules = RelabelConfig.from_dict(_rules)

        uuid = d.pop("uuid", UNSET)

        metrics_pipeline_config_info = cls(
            created_by=created_by,
            created_timestamp=created_timestamp,
            rules=rules,
            uuid=uuid,
        )

        metrics_pipeline_config_info.additional_properties = d
        return metrics_pipeline_config_info

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
