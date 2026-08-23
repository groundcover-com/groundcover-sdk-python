from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt")


@_attrs_define
class TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt:
    """
    Attributes:
        metric (str | Unset):
        tags (list[str] | Unset):
    """

    metric: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if tags is not UNSET:
            field_dict["tags"] = tags

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
        metric = d.pop("metric", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        tagged_metric_names_a_metric_plus_every_classification_that_applies_to_it = cls(
            metric=metric,
            tags=tags,
        )

        tagged_metric_names_a_metric_plus_every_classification_that_applies_to_it.additional_properties = d
        return tagged_metric_names_a_metric_plus_every_classification_that_applies_to_it

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
