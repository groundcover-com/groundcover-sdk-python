from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_widget_kind import TemplateWidgetKind
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TemplateWidget")


@_attrs_define
class TemplateWidget:
    """TemplateWidget is one entry of a template's authored topWidgets strip: a
    preset query widget's display name and visualization kind (the preset
    widget's visualizationConfig.type).

        Attributes:
            kind (TemplateWidgetKind | Unset): Kind drives the card glyph; the CI gate restricts it to the
                card-renderable set.
            name (str | Unset):
    """

    kind: TemplateWidgetKind | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name

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
        _kind = d.pop("kind", UNSET)
        kind: TemplateWidgetKind | Unset
        if isinstance(_kind, Unset) or _kind is None:
            kind = UNSET
        else:
            kind = TemplateWidgetKind(_kind)

        name = d.pop("name", UNSET)

        template_widget = cls(
            kind=kind,
            name=name,
        )

        template_widget.additional_properties = d
        return template_widget

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
