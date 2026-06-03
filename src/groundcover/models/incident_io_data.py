from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_io_data_severity_mapping import IncidentIODataSeverityMapping


T = TypeVar("T", bound="IncidentIOData")


@_attrs_define
class IncidentIOData:
    """
    Attributes:
        url (str):  Example: https://api.incident.io/v2/alert_events/http/XXXXXXXXXXXXXXXXXX?token=XXXXXXXXXXXXXXXXXXXXX
            XXXXXXXXXXXXXXXXXXXXXXX.
        severity_mapping (IncidentIODataSeverityMapping | Unset):  Example: {'S1': 'critical', 'critical': 'error'}.
    """

    url: str
    severity_mapping: IncidentIODataSeverityMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        severity_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity_mapping, Unset):
            severity_mapping = self.severity_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if severity_mapping is not UNSET:
            field_dict["severity_mapping"] = severity_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_io_data_severity_mapping import IncidentIODataSeverityMapping

        d = dict(src_dict)
        url = d.pop("url")

        _severity_mapping = d.pop("severity_mapping", UNSET)
        severity_mapping: IncidentIODataSeverityMapping | Unset
        if isinstance(_severity_mapping, Unset) or _severity_mapping is None:
            severity_mapping = UNSET
        else:
            severity_mapping = IncidentIODataSeverityMapping.from_dict(_severity_mapping)

        incident_io_data = cls(
            url=url,
            severity_mapping=severity_mapping,
        )

        incident_io_data.additional_properties = d
        return incident_io_data

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
