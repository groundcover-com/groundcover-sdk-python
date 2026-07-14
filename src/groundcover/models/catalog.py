from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_template_list_item_is_a_thin_per_tenant_view_of_a_catalog_template import (
        CatalogTemplateListItemIsAThinPerTenantViewOfACatalogTemplate,
    )
    from ..models.pack_is_a_rail_grouping_for_the_catalog_browse_ui_authored_in_packs_json import (
        PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson,
    )


T = TypeVar("T", bound="Catalog")


@_attrs_define
class Catalog:
    """pack definitions plus thin templates, filtered by the request's gcQL filter.

    Attributes:
        packs (list[PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson] | Unset):
        templates (list[CatalogTemplateListItemIsAThinPerTenantViewOfACatalogTemplate] | Unset):
    """

    packs: list[PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson] | Unset = UNSET
    templates: list[CatalogTemplateListItemIsAThinPerTenantViewOfACatalogTemplate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packs, Unset):
            packs = []
            for packs_item_data in self.packs:
                packs_item = packs_item_data.to_dict()
                packs.append(packs_item)

        templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if packs is not UNSET:
            field_dict["packs"] = packs
        if templates is not UNSET:
            field_dict["templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_template_list_item_is_a_thin_per_tenant_view_of_a_catalog_template import (
            CatalogTemplateListItemIsAThinPerTenantViewOfACatalogTemplate,
        )
        from ..models.pack_is_a_rail_grouping_for_the_catalog_browse_ui_authored_in_packs_json import (
            PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson,
        )

        d = dict(src_dict)
        _packs = d.pop("packs", UNSET)
        packs: list[PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson] | Unset = UNSET
        if _packs is not UNSET:
            packs = []
            for packs_item_data in _packs:
                packs_item = PackIsARailGroupingForTheCatalogBrowseUIAuthoredInPacksJson.from_dict(packs_item_data)

                packs.append(packs_item)

        _templates = d.pop("templates", UNSET)
        templates: list[CatalogTemplateListItemIsAThinPerTenantViewOfACatalogTemplate] | Unset = UNSET
        if _templates is not UNSET:
            templates = []
            for templates_item_data in _templates:
                templates_item = CatalogTemplateListItemIsAThinPerTenantViewOfACatalogTemplate.from_dict(
                    templates_item_data
                )

                templates.append(templates_item)

        catalog = cls(
            packs=packs,
            templates=templates,
        )

        catalog.additional_properties = d
        return catalog

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
