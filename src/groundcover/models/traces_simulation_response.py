from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_record import SpanRecord


T = TypeVar("T", bound="TracesSimulationResponse")


@_attrs_define
class TracesSimulationResponse:
    """
    Attributes:
        error (str | Unset):
        rule_ran (bool | Unset):
        rule_valid (bool | Unset):
        span_dropped (bool | Unset):
        span_record (SpanRecord | Unset):
    """

    error: str | Unset = UNSET
    rule_ran: bool | Unset = UNSET
    rule_valid: bool | Unset = UNSET
    span_dropped: bool | Unset = UNSET
    span_record: SpanRecord | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        rule_ran = self.rule_ran

        rule_valid = self.rule_valid

        span_dropped = self.span_dropped

        span_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.span_record, Unset):
            span_record = self.span_record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if rule_ran is not UNSET:
            field_dict["ruleRan"] = rule_ran
        if rule_valid is not UNSET:
            field_dict["ruleValid"] = rule_valid
        if span_dropped is not UNSET:
            field_dict["spanDropped"] = span_dropped
        if span_record is not UNSET:
            field_dict["spanRecord"] = span_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_record import SpanRecord

        d = dict(src_dict)
        error = d.pop("error", UNSET)

        rule_ran = d.pop("ruleRan", UNSET)

        rule_valid = d.pop("ruleValid", UNSET)

        span_dropped = d.pop("spanDropped", UNSET)

        _span_record = d.pop("spanRecord", UNSET)
        span_record: SpanRecord | Unset
        if isinstance(_span_record, Unset) or _span_record is None:
            span_record = UNSET
        else:
            span_record = SpanRecord.from_dict(_span_record)

        traces_simulation_response = cls(
            error=error,
            rule_ran=rule_ran,
            rule_valid=rule_valid,
            span_dropped=span_dropped,
            span_record=span_record,
        )

        traces_simulation_response.additional_properties = d
        return traces_simulation_response

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
