from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detection import Detection
    from ..models.template_widget import TemplateWidget


T = TypeVar("T", bound="CatalogTemplateResponse")


@_attrs_define
class CatalogTemplateResponse:
    """CatalogTemplateResponse is the catalog template header — the same fields
    the list endpoint serves — plus the full preset, for live preview.

        Attributes:
            catalog_id (str | Unset):
            description (str | Unset):
            detection (Detection | Unset): Detection groups the signals used to suggest dashboard relevance for a
                tenant. Inert in MVP (not evaluated against live data).
            display_name (str | Unset):
            integration (None | str | Unset): Integration is the integration family (e.g. "aws"), or null for
                native/non-integration templates.
            is_recommended (bool | Unset): IsRecommended flags a "start here" template (decision 2026-07-13).
                Mandatory and present on every template file; served verbatim.
            last_updated (str | Unset):
            pack (str | Unset):
            preset (str | Unset): Preset is the template's dashboard preset as an escaped JSON string.
            service (str | Unset): Service is the owning sub-service (e.g. "rds"); omitted when unset.
            tags (list[str] | Unset):
            top_widgets (list[TemplateWidget] | Unset): TopWidgets is the authored card widget strip (decision 2026-07-12):
                exactly 3 entries, each naming a preset query widget verbatim with kind
                equal to that widget's visualizationConfig.type. Served verbatim — the
                runtime never parses the preset for card metadata; the CI content gate
                (BE-2351) is the only place the preset schema is inspected.
            version (int | Unset):
    """

    catalog_id: str | Unset = UNSET
    description: str | Unset = UNSET
    detection: Detection | Unset = UNSET
    display_name: str | Unset = UNSET
    integration: None | str | Unset = UNSET
    is_recommended: bool | Unset = UNSET
    last_updated: str | Unset = UNSET
    pack: str | Unset = UNSET
    preset: str | Unset = UNSET
    service: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    top_widgets: list[TemplateWidget] | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_id = self.catalog_id

        description = self.description

        detection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detection, Unset):
            detection = self.detection.to_dict()

        display_name = self.display_name

        integration: None | str | Unset
        if isinstance(self.integration, Unset):
            integration = UNSET
        else:
            integration = self.integration

        is_recommended = self.is_recommended

        last_updated = self.last_updated

        pack = self.pack

        preset = self.preset

        service = self.service

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        top_widgets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_widgets, Unset):
            top_widgets = []
            for top_widgets_item_data in self.top_widgets:
                top_widgets_item = top_widgets_item_data.to_dict()
                top_widgets.append(top_widgets_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_id is not UNSET:
            field_dict["catalogId"] = catalog_id
        if description is not UNSET:
            field_dict["description"] = description
        if detection is not UNSET:
            field_dict["detection"] = detection
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if integration is not UNSET:
            field_dict["integration"] = integration
        if is_recommended is not UNSET:
            field_dict["isRecommended"] = is_recommended
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if pack is not UNSET:
            field_dict["pack"] = pack
        if preset is not UNSET:
            field_dict["preset"] = preset
        if service is not UNSET:
            field_dict["service"] = service
        if tags is not UNSET:
            field_dict["tags"] = tags
        if top_widgets is not UNSET:
            field_dict["topWidgets"] = top_widgets
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detection import Detection
        from ..models.template_widget import TemplateWidget

        d = dict(src_dict)
        catalog_id = d.pop("catalogId", UNSET)

        description = d.pop("description", UNSET)

        _detection = d.pop("detection", UNSET)
        detection: Detection | Unset
        if isinstance(_detection, Unset) or _detection is None:
            detection = UNSET
        else:
            detection = Detection.from_dict(_detection)

        display_name = d.pop("displayName", UNSET)

        def _parse_integration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration = _parse_integration(d.pop("integration", UNSET))

        is_recommended = d.pop("isRecommended", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        pack = d.pop("pack", UNSET)

        preset = d.pop("preset", UNSET)

        service = d.pop("service", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _top_widgets = d.pop("topWidgets", UNSET)
        top_widgets: list[TemplateWidget] | Unset = UNSET
        if _top_widgets is not UNSET:
            top_widgets = []
            for top_widgets_item_data in _top_widgets:
                top_widgets_item = TemplateWidget.from_dict(top_widgets_item_data)

                top_widgets.append(top_widgets_item)

        version = d.pop("version", UNSET)

        catalog_template_response = cls(
            catalog_id=catalog_id,
            description=description,
            detection=detection,
            display_name=display_name,
            integration=integration,
            is_recommended=is_recommended,
            last_updated=last_updated,
            pack=pack,
            preset=preset,
            service=service,
            tags=tags,
            top_widgets=top_widgets,
            version=version,
        )

        catalog_template_response.additional_properties = d
        return catalog_template_response

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
