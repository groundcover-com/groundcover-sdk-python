from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager_duty_data_severity_mapping import PagerDutyDataSeverityMapping


T = TypeVar("T", bound="PagerDutyData")


@_attrs_define
class PagerDutyData:
    """
    Attributes:
        routing_key (str):
        severity_mapping (PagerDutyDataSeverityMapping | Unset):  Example: {'S1': 'critical', 'error': 'warning'}.
    """

    routing_key: str
    severity_mapping: PagerDutyDataSeverityMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routing_key = self.routing_key

        severity_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity_mapping, Unset):
            severity_mapping = self.severity_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "routing_key": routing_key,
            }
        )
        if severity_mapping is not UNSET:
            field_dict["severity_mapping"] = severity_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pager_duty_data_severity_mapping import PagerDutyDataSeverityMapping

        d = dict(src_dict)
        routing_key = d.pop("routing_key")

        _severity_mapping = d.pop("severity_mapping", UNSET)
        severity_mapping: PagerDutyDataSeverityMapping | Unset
        if isinstance(_severity_mapping, Unset) or _severity_mapping is None:
            severity_mapping = UNSET
        else:
            severity_mapping = PagerDutyDataSeverityMapping.from_dict(_severity_mapping)

        pager_duty_data = cls(
            routing_key=routing_key,
            severity_mapping=severity_mapping,
        )

        pager_duty_data.additional_properties = d
        return pager_duty_data

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
