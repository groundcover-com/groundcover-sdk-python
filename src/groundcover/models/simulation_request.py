from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_record import LogRecord


T = TypeVar("T", bound="SimulationRequest")


@_attrs_define
class SimulationRequest:
    """
    Attributes:
        log_record (LogRecord | Unset):
        rule_yaml (str | Unset):
    """

    log_record: LogRecord | Unset = UNSET
    rule_yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_record, Unset):
            log_record = self.log_record.to_dict()

        rule_yaml = self.rule_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log_record is not UNSET:
            field_dict["logRecord"] = log_record
        if rule_yaml is not UNSET:
            field_dict["ruleYaml"] = rule_yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_record import LogRecord

        d = dict(src_dict)
        _log_record = d.pop("logRecord", UNSET)
        log_record: LogRecord | Unset
        if isinstance(_log_record, Unset) or _log_record is None:
            log_record = UNSET
        else:
            log_record = LogRecord.from_dict(_log_record)

        rule_yaml = d.pop("ruleYaml", UNSET)

        simulation_request = cls(
            log_record=log_record,
            rule_yaml=rule_yaml,
        )

        simulation_request.additional_properties = d
        return simulation_request

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
