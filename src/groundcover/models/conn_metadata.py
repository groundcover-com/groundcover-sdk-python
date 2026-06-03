from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnMetadata")


@_attrs_define
class ConnMetadata:
    """
    Attributes:
        backend_id (str | Unset):
        client_id (str | Unset):
    """

    backend_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend_id = self.backend_id

        client_id = self.client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend_id is not UNSET:
            field_dict["BackendID"] = backend_id
        if client_id is not UNSET:
            field_dict["ClientID"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        backend_id = d.pop("BackendID", UNSET)

        client_id = d.pop("ClientID", UNSET)

        conn_metadata = cls(
            backend_id=backend_id,
            client_id=client_id,
        )

        conn_metadata.additional_properties = d
        return conn_metadata

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
