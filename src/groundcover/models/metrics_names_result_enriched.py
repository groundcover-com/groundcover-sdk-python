from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MetricsNamesResultEnriched")


@_attrs_define
class MetricsNamesResultEnriched:
    """
    Attributes:
        description (str | Unset): Description is the metric description.
        highlights (list[str] | Unset): Highlights contains the matching parts of the metric name based on the filter.
        name (str | Unset): Name is the metric name.
        type_ (str | Unset): Type is the metric type (e.g., "gauge", "counter").
        unit (str | Unset): Unit is the metric unit (e.g., "bytes", "seconds").
    """

    description: str | Unset = UNSET
    highlights: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        highlights: list[str] | Unset = UNSET
        if not isinstance(self.highlights, Unset):
            highlights = self.highlights

        name = self.name

        type_ = self.type_

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if highlights is not UNSET:
            field_dict["highlights"] = highlights
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unit is not UNSET:
            field_dict["unit"] = unit

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
        description = d.pop("description", UNSET)

        highlights = cast(list[str], d.pop("highlights", UNSET))

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        unit = d.pop("unit", UNSET)

        metrics_names_result_enriched = cls(
            description=description,
            highlights=highlights,
            name=name,
            type_=type_,
            unit=unit,
        )

        metrics_names_result_enriched.additional_properties = d
        return metrics_names_result_enriched

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
