from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ops_genie_data_response_severity_mapping import OpsGenieDataResponseSeverityMapping


T = TypeVar("T", bound="OpsGenieDataResponse")


@_attrs_define
class OpsGenieDataResponse:
    """
    Attributes:
        region (str | Unset): The OpsGenie region (us or eu) Example: us.
        severity_mapping (OpsGenieDataResponseSeverityMapping | Unset): Custom severity mapping (if configured) Example:
            {'critical': 'P1', 'error': 'P2'}.
    """

    region: str | Unset = UNSET
    severity_mapping: OpsGenieDataResponseSeverityMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        severity_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity_mapping, Unset):
            severity_mapping = self.severity_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if severity_mapping is not UNSET:
            field_dict["severity_mapping"] = severity_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ops_genie_data_response_severity_mapping import OpsGenieDataResponseSeverityMapping

        d = dict(src_dict)
        region = d.pop("region", UNSET)

        _severity_mapping = d.pop("severity_mapping", UNSET)
        severity_mapping: OpsGenieDataResponseSeverityMapping | Unset
        if isinstance(_severity_mapping, Unset) or _severity_mapping is None:
            severity_mapping = UNSET
        else:
            severity_mapping = OpsGenieDataResponseSeverityMapping.from_dict(_severity_mapping)

        ops_genie_data_response = cls(
            region=region,
            severity_mapping=severity_mapping,
        )

        ops_genie_data_response.additional_properties = d
        return ops_genie_data_response

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
