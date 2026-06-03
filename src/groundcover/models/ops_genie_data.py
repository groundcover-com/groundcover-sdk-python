from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ops_genie_data_severity_mapping import OpsGenieDataSeverityMapping


T = TypeVar("T", bound="OpsGenieData")


@_attrs_define
class OpsGenieData:
    """
    Attributes:
        api_key (str):
        region (str | Unset):  Example: us.
        severity_mapping (OpsGenieDataSeverityMapping | Unset):  Example: {'critical': 'P1', 'error': 'P2'}.
    """

    api_key: str
    region: str | Unset = UNSET
    severity_mapping: OpsGenieDataSeverityMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        region = self.region

        severity_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity_mapping, Unset):
            severity_mapping = self.severity_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if severity_mapping is not UNSET:
            field_dict["severity_mapping"] = severity_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ops_genie_data_severity_mapping import OpsGenieDataSeverityMapping

        d = dict(src_dict)
        api_key = d.pop("api_key")

        region = d.pop("region", UNSET)

        _severity_mapping = d.pop("severity_mapping", UNSET)
        severity_mapping: OpsGenieDataSeverityMapping | Unset
        if isinstance(_severity_mapping, Unset) or _severity_mapping is None:
            severity_mapping = UNSET
        else:
            severity_mapping = OpsGenieDataSeverityMapping.from_dict(_severity_mapping)

        ops_genie_data = cls(
            api_key=api_key,
            region=region,
            severity_mapping=severity_mapping,
        )

        ops_genie_data.additional_properties = d
        return ops_genie_data

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
