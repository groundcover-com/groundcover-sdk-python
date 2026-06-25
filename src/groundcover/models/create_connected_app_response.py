from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CreateConnectedAppResponse")


@_attrs_define
class CreateConnectedAppResponse:
    """
    Attributes:
        data_hash (str | Unset): SHA-256 hash of the stored connected app data, including secret fields Example:
            20b3664454f5b36a20da19805802a369a9f30793fb646a1de9e39b21a004df4e.
        id (str | Unset): The ID of the created connected app Example: 1a2b-3c4d.
        type_ (str | Unset): The type of the connected app Example: slack-webhook.
    """

    data_hash: str | Unset = UNSET
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_hash = self.data_hash

        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_hash is not UNSET:
            field_dict["data_hash"] = data_hash
        if id is not UNSET:
            field_dict["id"] = id
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
        data_hash = d.pop("data_hash", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        create_connected_app_response = cls(
            data_hash=data_hash,
            id=id,
            type_=type_,
        )

        create_connected_app_response.additional_properties = d
        return create_connected_app_response

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
