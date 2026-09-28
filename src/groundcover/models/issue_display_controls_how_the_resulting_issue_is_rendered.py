from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="IssueDisplayControlsHowTheResultingIssueIsRendered")


@_attrs_define
class IssueDisplayControlsHowTheResultingIssueIsRendered:
    """
    Attributes:
        context_labels (list[str] | Unset):
        description (str | Unset):
        template_language (str | Unset):
        title (str | Unset):
    """

    context_labels: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    template_language: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_labels: list[str] | Unset = UNSET
        if not isinstance(self.context_labels, Unset):
            context_labels = self.context_labels

        description = self.description

        template_language = self.template_language

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_labels is not UNSET:
            field_dict["contextLabels"] = context_labels
        if description is not UNSET:
            field_dict["description"] = description
        if template_language is not UNSET:
            field_dict["templateLanguage"] = template_language
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        context_labels = cast(list[str], d.pop("contextLabels", UNSET))

        description = d.pop("description", UNSET)

        template_language = d.pop("templateLanguage", UNSET)

        title = d.pop("title", UNSET)

        issue_display_controls_how_the_resulting_issue_is_rendered = cls(
            context_labels=context_labels,
            description=description,
            template_language=template_language,
            title=title,
        )

        issue_display_controls_how_the_resulting_issue_is_rendered.additional_properties = d
        return issue_display_controls_how_the_resulting_issue_is_rendered

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
