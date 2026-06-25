from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_record import LogRecord


T = TypeVar("T", bound="SimulationResponse")


@_attrs_define
class SimulationResponse:
    """
    Attributes:
        error (str | Unset):
        log_dropped (bool | Unset):
        log_record (LogRecord | Unset):
        rule_ran (bool | Unset):
        rule_valid (bool | Unset):
    """

    error: str | Unset = UNSET
    log_dropped: bool | Unset = UNSET
    log_record: LogRecord | Unset = UNSET
    rule_ran: bool | Unset = UNSET
    rule_valid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        log_dropped = self.log_dropped

        log_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_record, Unset):
            log_record = self.log_record.to_dict()

        rule_ran = self.rule_ran

        rule_valid = self.rule_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if log_dropped is not UNSET:
            field_dict["logDropped"] = log_dropped
        if log_record is not UNSET:
            field_dict["logRecord"] = log_record
        if rule_ran is not UNSET:
            field_dict["ruleRan"] = rule_ran
        if rule_valid is not UNSET:
            field_dict["ruleValid"] = rule_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_record import LogRecord

        d = dict(src_dict)
        error = d.pop("error", UNSET)

        log_dropped = d.pop("logDropped", UNSET)

        _log_record = d.pop("logRecord", UNSET)
        log_record: LogRecord | Unset
        if isinstance(_log_record, Unset) or _log_record is None:
            log_record = UNSET
        else:
            log_record = LogRecord.from_dict(_log_record)

        rule_ran = d.pop("ruleRan", UNSET)

        rule_valid = d.pop("ruleValid", UNSET)

        simulation_response = cls(
            error=error,
            log_dropped=log_dropped,
            log_record=log_record,
            rule_ran=rule_ran,
            rule_valid=rule_valid,
        )

        simulation_response.additional_properties = d
        return simulation_response

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
