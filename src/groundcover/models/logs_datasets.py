from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LogsDatasets")


@_attrs_define
class LogsDatasets:
    """
    Attributes:
        events (int | Unset):
        rum (int | Unset):
        traces (int | Unset):
    """

    events: int | Unset = UNSET
    rum: int | Unset = UNSET
    traces: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        rum = self.rum

        traces = self.traces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if rum is not UNSET:
            field_dict["rum"] = rum
        if traces is not UNSET:
            field_dict["traces"] = traces

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
        events = d.pop("events", UNSET)

        rum = d.pop("rum", UNSET)

        traces = d.pop("traces", UNSET)

        logs_datasets = cls(
            events=events,
            rum=rum,
            traces=traces,
        )

        logs_datasets.additional_properties = d
        return logs_datasets

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
