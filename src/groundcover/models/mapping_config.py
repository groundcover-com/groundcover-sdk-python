from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_mapping import KeyMapping
    from ..models.mapping_config_metric_name_char_replace import MappingConfigMetricNameCharReplace
    from ..models.metric_mapping import MetricMapping


T = TypeVar("T", bound="MappingConfig")


@_attrs_define
class MappingConfig:
    """
    Attributes:
        default_rate_window (str | Unset):
        key_mappings (list[KeyMapping] | Unset):
        metric_mappings (list[MetricMapping] | Unset):
        metric_name_char_replace (MappingConfigMetricNameCharReplace | Unset):
    """

    default_rate_window: str | Unset = UNSET
    key_mappings: list[KeyMapping] | Unset = UNSET
    metric_mappings: list[MetricMapping] | Unset = UNSET
    metric_name_char_replace: MappingConfigMetricNameCharReplace | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_rate_window = self.default_rate_window

        key_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_mappings, Unset):
            key_mappings = []
            for key_mappings_item_data in self.key_mappings:
                key_mappings_item = key_mappings_item_data.to_dict()
                key_mappings.append(key_mappings_item)

        metric_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metric_mappings, Unset):
            metric_mappings = []
            for metric_mappings_item_data in self.metric_mappings:
                metric_mappings_item = metric_mappings_item_data.to_dict()
                metric_mappings.append(metric_mappings_item)

        metric_name_char_replace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric_name_char_replace, Unset):
            metric_name_char_replace = self.metric_name_char_replace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_rate_window is not UNSET:
            field_dict["default_rate_window"] = default_rate_window
        if key_mappings is not UNSET:
            field_dict["key_mappings"] = key_mappings
        if metric_mappings is not UNSET:
            field_dict["metric_mappings"] = metric_mappings
        if metric_name_char_replace is not UNSET:
            field_dict["metric_name_char_replace"] = metric_name_char_replace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_mapping import KeyMapping
        from ..models.mapping_config_metric_name_char_replace import MappingConfigMetricNameCharReplace
        from ..models.metric_mapping import MetricMapping

        d = dict(src_dict)
        default_rate_window = d.pop("default_rate_window", UNSET)

        _key_mappings = d.pop("key_mappings", UNSET)
        key_mappings: list[KeyMapping] | Unset = UNSET
        if _key_mappings is not UNSET:
            key_mappings = []
            for key_mappings_item_data in _key_mappings:
                key_mappings_item = KeyMapping.from_dict(key_mappings_item_data)

                key_mappings.append(key_mappings_item)

        _metric_mappings = d.pop("metric_mappings", UNSET)
        metric_mappings: list[MetricMapping] | Unset = UNSET
        if _metric_mappings is not UNSET:
            metric_mappings = []
            for metric_mappings_item_data in _metric_mappings:
                metric_mappings_item = MetricMapping.from_dict(metric_mappings_item_data)

                metric_mappings.append(metric_mappings_item)

        _metric_name_char_replace = d.pop("metric_name_char_replace", UNSET)
        metric_name_char_replace: MappingConfigMetricNameCharReplace | Unset
        if isinstance(_metric_name_char_replace, Unset) or _metric_name_char_replace is None:
            metric_name_char_replace = UNSET
        else:
            metric_name_char_replace = MappingConfigMetricNameCharReplace.from_dict(_metric_name_char_replace)

        mapping_config = cls(
            default_rate_window=default_rate_window,
            key_mappings=key_mappings,
            metric_mappings=metric_mappings,
            metric_name_char_replace=metric_name_char_replace,
        )

        mapping_config.additional_properties = d
        return mapping_config

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
