from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ListIngestionKeysRequest")


@_attrs_define
class ListIngestionKeysRequest:
    """
    Attributes:
        name (str | Unset): Name of the ingestion key to filter by
        remote_config (bool | Unset): RemoteConfig indicates if the key is for remote config
        type_ (str | Unset): Type of the ingestion key to filter by
    """

    name: str | Unset = UNSET
    remote_config: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        remote_config = self.remote_config

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if remote_config is not UNSET:
            field_dict["remoteConfig"] = remote_config
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        name = d.pop("name", UNSET)

        remote_config = d.pop("remoteConfig", UNSET)

        type_ = d.pop("type", UNSET)

        list_ingestion_keys_request = cls(
            name=name,
            remote_config=remote_config,
            type_=type_,
        )

        list_ingestion_keys_request.additional_properties = d
        return list_ingestion_keys_request

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
