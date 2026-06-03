from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ObjectYamlResponse")


@_attrs_define
class ObjectYamlResponse:
    """
    Attributes:
        object_yaml (str | Unset):
        resource_version (str | Unset):
        uid (str | Unset):
    """

    object_yaml: str | Unset = UNSET
    resource_version: str | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_yaml = self.object_yaml

        resource_version = self.resource_version

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_yaml is not UNSET:
            field_dict["objectYaml"] = object_yaml
        if resource_version is not UNSET:
            field_dict["resourceVersion"] = resource_version
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        object_yaml = d.pop("objectYaml", UNSET)

        resource_version = d.pop("resourceVersion", UNSET)

        uid = d.pop("uid", UNSET)

        object_yaml_response = cls(
            object_yaml=object_yaml,
            resource_version=resource_version,
            uid=uid,
        )

        object_yaml_response.additional_properties = d
        return object_yaml_response

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
