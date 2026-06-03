from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_attributes_response_attributes import LogAttributesResponseAttributes
    from ..models.log_attributes_response_tags import LogAttributesResponseTags


T = TypeVar("T", bound="LogAttributesResponse")


@_attrs_define
class LogAttributesResponse:
    """
    Attributes:
        attributes (LogAttributesResponseAttributes | Unset):
        guid (str | Unset):
        raw_log (str | Unset):
        tags (LogAttributesResponseTags | Unset):
    """

    attributes: LogAttributesResponseAttributes | Unset = UNSET
    guid: str | Unset = UNSET
    raw_log: str | Unset = UNSET
    tags: LogAttributesResponseTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        guid = self.guid

        raw_log = self.raw_log

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if guid is not UNSET:
            field_dict["guid"] = guid
        if raw_log is not UNSET:
            field_dict["rawLog"] = raw_log
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_attributes_response_attributes import LogAttributesResponseAttributes
        from ..models.log_attributes_response_tags import LogAttributesResponseTags

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: LogAttributesResponseAttributes | Unset
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = LogAttributesResponseAttributes.from_dict(_attributes)

        guid = d.pop("guid", UNSET)

        raw_log = d.pop("rawLog", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: LogAttributesResponseTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = LogAttributesResponseTags.from_dict(_tags)

        log_attributes_response = cls(
            attributes=attributes,
            guid=guid,
            raw_log=raw_log,
            tags=tags,
        )

        log_attributes_response.additional_properties = d
        return log_attributes_response

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
