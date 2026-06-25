from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MonitorDetailsResponse")


@_attrs_define
class MonitorDetailsResponse:
    """
    Attributes:
        data (str | Unset): Monitor definition YAML.
        is_provisioned (bool | Unset): Whether the monitor is provisioned by IaC.
    """

    data: str | Unset = UNSET
    is_provisioned: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        is_provisioned = self.is_provisioned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if is_provisioned is not UNSET:
            field_dict["isProvisioned"] = is_provisioned

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
        data = d.pop("data", UNSET)

        is_provisioned = d.pop("isProvisioned", UNSET)

        monitor_details_response = cls(
            data=data,
            is_provisioned=is_provisioned,
        )

        monitor_details_response.additional_properties = d
        return monitor_details_response

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
