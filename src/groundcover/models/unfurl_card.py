from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unfurl_card_field import UnfurlCardField


T = TypeVar("T", bound="UnfurlCard")


@_attrs_define
class UnfurlCard:
    """UnfurlCard is the provider-agnostic card POST /api/unfurl resolves a shared
    link to. ExternalRefID is the resolved asset's stable identity — not
    necessarily anything present verbatim in the URL. Fields is display-ordered:
    the slice order IS the order a renderer shows them in.

        Attributes:
            display_type (str | Unset):
            external_ref_id (str | Unset):
            fields (list[UnfurlCardField] | Unset):
            title (str | Unset):
            type_ (str | Unset):
    """

    display_type: str | Unset = UNSET
    external_ref_id: str | Unset = UNSET
    fields: list[UnfurlCardField] | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_type = self.display_type

        external_ref_id = self.external_ref_id

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_type is not UNSET:
            field_dict["displayType"] = display_type
        if external_ref_id is not UNSET:
            field_dict["externalRefId"] = external_ref_id
        if fields is not UNSET:
            field_dict["fields"] = fields
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unfurl_card_field import UnfurlCardField

        d = dict(src_dict)
        display_type = d.pop("displayType", UNSET)

        external_ref_id = d.pop("externalRefId", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[UnfurlCardField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = UnfurlCardField.from_dict(fields_item_data)

                fields.append(fields_item)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        unfurl_card = cls(
            display_type=display_type,
            external_ref_id=external_ref_id,
            fields=fields,
            title=title,
            type_=type_,
        )

        unfurl_card.additional_properties = d
        return unfurl_card

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
