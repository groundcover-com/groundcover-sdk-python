from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversion_warning_context import ConversionWarningContext


T = TypeVar("T", bound="ConversionWarning")


@_attrs_define
class ConversionWarning:
    """ConversionWarning represents a structured warning that occurred during conversion
    This is used across all converters (dashboard, monitor, etc.)

        Attributes:
            context (ConversionWarningContext | Unset):
            details (str | Unset):
            message (str | Unset):
            original_data (Any | Unset):
            severity (str | Unset):
            suggestions (list[str] | Unset):
            type_ (str | Unset): ConversionWarningType represents the type of conversion warning
    """

    context: ConversionWarningContext | Unset = UNSET
    details: str | Unset = UNSET
    message: str | Unset = UNSET
    original_data: Any | Unset = UNSET
    severity: str | Unset = UNSET
    suggestions: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        details = self.details

        message = self.message

        original_data = self.original_data

        severity = self.severity

        suggestions: list[str] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = self.suggestions

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if details is not UNSET:
            field_dict["details"] = details
        if message is not UNSET:
            field_dict["message"] = message
        if original_data is not UNSET:
            field_dict["originalData"] = original_data
        if severity is not UNSET:
            field_dict["severity"] = severity
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_warning_context import ConversionWarningContext

        d = dict(src_dict)
        _context = d.pop("context", UNSET)
        context: ConversionWarningContext | Unset
        if isinstance(_context, Unset) or _context is None:
            context = UNSET
        else:
            context = ConversionWarningContext.from_dict(_context)

        details = d.pop("details", UNSET)

        message = d.pop("message", UNSET)

        original_data = d.pop("originalData", UNSET)

        severity = d.pop("severity", UNSET)

        suggestions = cast(list[str], d.pop("suggestions", UNSET))

        type_ = d.pop("type", UNSET)

        conversion_warning = cls(
            context=context,
            details=details,
            message=message,
            original_data=original_data,
            severity=severity,
            suggestions=suggestions,
            type_=type_,
        )

        conversion_warning.additional_properties = d
        return conversion_warning

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
