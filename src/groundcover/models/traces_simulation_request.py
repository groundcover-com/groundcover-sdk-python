from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_record import SpanRecord


T = TypeVar("T", bound="TracesSimulationRequest")


@_attrs_define
class TracesSimulationRequest:
    """
    Attributes:
        rule_yaml (str | Unset):
        span (SpanRecord | Unset):
    """

    rule_yaml: str | Unset = UNSET
    span: SpanRecord | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_yaml = self.rule_yaml

        span: dict[str, Any] | Unset = UNSET
        if not isinstance(self.span, Unset):
            span = self.span.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_yaml is not UNSET:
            field_dict["ruleYaml"] = rule_yaml
        if span is not UNSET:
            field_dict["span"] = span

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_record import SpanRecord

        d = dict(src_dict)
        rule_yaml = d.pop("ruleYaml", UNSET)

        _span = d.pop("span", UNSET)
        span: SpanRecord | Unset
        if isinstance(_span, Unset) or _span is None:
            span = UNSET
        else:
            span = SpanRecord.from_dict(_span)

        traces_simulation_request = cls(
            rule_yaml=rule_yaml,
            span=span,
        )

        traces_simulation_request.additional_properties = d
        return traces_simulation_request

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
