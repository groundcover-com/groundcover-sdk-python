from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ValueMapping")


@_attrs_define
class ValueMapping:
    """
    Attributes:
        groundcover_value (str): GroundcoverValue is the replacement value in the converted query.
        source_key (str): SourceKey is the exact Datadog key whose value should be mapped.
        source_value (str): SourceValue is the exact Datadog value to replace.
        groundcover_key (str | Unset): GroundcoverKey is derived from SourceKey and the applicable key mapping.
            It is returned for display but is never applied as a separate key-mapping rule.
        metric_pattern (str | Unset): MetricPattern optionally scopes this mapping to groundcover metric names (not
            source metric names).
            It is not supported for logs, traces, or events.
    """

    groundcover_value: str
    source_key: str
    source_value: str
    groundcover_key: str | Unset = UNSET
    metric_pattern: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groundcover_value = self.groundcover_value

        source_key = self.source_key

        source_value = self.source_value

        groundcover_key = self.groundcover_key

        metric_pattern = self.metric_pattern

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groundcover_value": groundcover_value,
                "source_key": source_key,
                "source_value": source_value,
            }
        )
        if groundcover_key is not UNSET:
            field_dict["groundcover_key"] = groundcover_key
        if metric_pattern is not UNSET:
            field_dict["metric_pattern"] = metric_pattern

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
        groundcover_value = d.pop("groundcover_value")

        source_key = d.pop("source_key")

        source_value = d.pop("source_value")

        groundcover_key = d.pop("groundcover_key", UNSET)

        metric_pattern = d.pop("metric_pattern", UNSET)

        value_mapping = cls(
            groundcover_value=groundcover_value,
            source_key=source_key,
            source_value=source_value,
            groundcover_key=groundcover_key,
            metric_pattern=metric_pattern,
        )

        value_mapping.additional_properties = d
        return value_mapping

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
