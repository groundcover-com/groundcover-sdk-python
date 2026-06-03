from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.display_model_controls_how_the_monitor_is_presented_template_language import (
    DisplayModelControlsHowTheMonitorIsPresentedTemplateLanguage,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DisplayModelControlsHowTheMonitorIsPresented")


@_attrs_define
class DisplayModelControlsHowTheMonitorIsPresented:
    """
    Attributes:
        context_header_labels (list[str] | Unset):
        description (str | Unset):
        header (str | Unset):
        resource_header_labels (list[str] | Unset):
        template_language (DisplayModelControlsHowTheMonitorIsPresentedTemplateLanguage | Unset): Template language for
            header and description fields. If omitted or empty, legacy Go template syntax is used.
    """

    context_header_labels: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    header: str | Unset = UNSET
    resource_header_labels: list[str] | Unset = UNSET
    template_language: DisplayModelControlsHowTheMonitorIsPresentedTemplateLanguage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_header_labels: list[str] | Unset = UNSET
        if not isinstance(self.context_header_labels, Unset):
            context_header_labels = self.context_header_labels

        description = self.description

        header = self.header

        resource_header_labels: list[str] | Unset = UNSET
        if not isinstance(self.resource_header_labels, Unset):
            resource_header_labels = self.resource_header_labels

        template_language: str | Unset = UNSET
        if not isinstance(self.template_language, Unset):
            template_language = self.template_language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_header_labels is not UNSET:
            field_dict["contextHeaderLabels"] = context_header_labels
        if description is not UNSET:
            field_dict["description"] = description
        if header is not UNSET:
            field_dict["header"] = header
        if resource_header_labels is not UNSET:
            field_dict["resourceHeaderLabels"] = resource_header_labels
        if template_language is not UNSET:
            field_dict["templateLanguage"] = template_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        context_header_labels = cast(list[str], d.pop("contextHeaderLabels", UNSET))

        description = d.pop("description", UNSET)

        header = d.pop("header", UNSET)

        resource_header_labels = cast(list[str], d.pop("resourceHeaderLabels", UNSET))

        _template_language = d.pop("templateLanguage", UNSET)
        template_language: DisplayModelControlsHowTheMonitorIsPresentedTemplateLanguage | Unset
        if isinstance(_template_language, Unset) or _template_language is None:
            template_language = UNSET
        else:
            template_language = DisplayModelControlsHowTheMonitorIsPresentedTemplateLanguage(_template_language)

        display_model_controls_how_the_monitor_is_presented = cls(
            context_header_labels=context_header_labels,
            description=description,
            header=header,
            resource_header_labels=resource_header_labels,
            template_language=template_language,
        )

        display_model_controls_how_the_monitor_is_presented.additional_properties = d
        return display_model_controls_how_the_monitor_is_presented

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
