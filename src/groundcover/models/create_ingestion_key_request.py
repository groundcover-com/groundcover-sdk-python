from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_ingestion_key_request_type import CreateIngestionKeyRequestType
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CreateIngestionKeyRequest")


@_attrs_define
class CreateIngestionKeyRequest:
    """
    Attributes:
        name (str): The desired name for the ingestion key.
        type_ (CreateIngestionKeyRequestType): The type of the ingestion key.
        remote_config (bool | Unset): Indicates whether the key is explicitly for remote configuration or not.
        tags (list[str] | Unset): A list of tags to associate with the key.
    """

    name: str
    type_: CreateIngestionKeyRequestType
    remote_config: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        remote_config = self.remote_config

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if remote_config is not UNSET:
            field_dict["remoteConfig"] = remote_config
        if tags is not UNSET:
            field_dict["tags"] = tags

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
        name = d.pop("name")

        type_ = CreateIngestionKeyRequestType(d.pop("type"))

        remote_config = d.pop("remoteConfig", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        create_ingestion_key_request = cls(
            name=name,
            type_=type_,
            remote_config=remote_config,
            tags=tags,
        )

        create_ingestion_key_request.additional_properties = d
        return create_ingestion_key_request

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
