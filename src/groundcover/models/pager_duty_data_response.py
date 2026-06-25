from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager_duty_data_response_severity_mapping import PagerDutyDataResponseSeverityMapping


T = TypeVar("T", bound="PagerDutyDataResponse")


@_attrs_define
class PagerDutyDataResponse:
    """
    Attributes:
        severity_mapping (PagerDutyDataResponseSeverityMapping | Unset): Custom severity mapping (if configured)
            Example: {'S1': 'critical', 'S2': 'error', 'S3': 'warning', 'S4': 'info'}.
    """

    severity_mapping: PagerDutyDataResponseSeverityMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity_mapping, Unset):
            severity_mapping = self.severity_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if severity_mapping is not UNSET:
            field_dict["severity_mapping"] = severity_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pager_duty_data_response_severity_mapping import PagerDutyDataResponseSeverityMapping

        d = dict(src_dict)
        _severity_mapping = d.pop("severity_mapping", UNSET)
        severity_mapping: PagerDutyDataResponseSeverityMapping | Unset
        if isinstance(_severity_mapping, Unset) or _severity_mapping is None:
            severity_mapping = UNSET
        else:
            severity_mapping = PagerDutyDataResponseSeverityMapping.from_dict(_severity_mapping)

        pager_duty_data_response = cls(
            severity_mapping=severity_mapping,
        )

        pager_duty_data_response.additional_properties = d
        return pager_duty_data_response

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
