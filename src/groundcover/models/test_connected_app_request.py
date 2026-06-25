from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_connected_app_request_type import TestConnectedAppRequestType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_connected_app_request_data import TestConnectedAppRequestData


T = TypeVar("T", bound="TestConnectedAppRequest")


@_attrs_define
class TestConnectedAppRequest:
    """
    Attributes:
        data (TestConnectedAppRequestData): The connected app-specific data. Schema depends on the 'type' field.
        type_ (TestConnectedAppRequestType): The type of the connected app Example: slack-webhook.
        connected_app_id (str | Unset): The ID of an existing connected app (optional).
            When provided, empty secret fields will be filled from the stored app. Example: 1a2b-3c4d.
        name (str | Unset): The name of the connected app (for display purposes in the test notification) Example: my-
            slack-app.
    """

    data: TestConnectedAppRequestData
    type_: TestConnectedAppRequestType
    connected_app_id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        type_ = self.type_.value

        connected_app_id = self.connected_app_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "type": type_,
            }
        )
        if connected_app_id is not UNSET:
            field_dict["connected_app_id"] = connected_app_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_connected_app_request_data import TestConnectedAppRequestData

        d = dict(src_dict)
        data = TestConnectedAppRequestData.from_dict(d.pop("data"))

        type_ = TestConnectedAppRequestType(d.pop("type"))

        connected_app_id = d.pop("connected_app_id", UNSET)

        name = d.pop("name", UNSET)

        test_connected_app_request = cls(
            data=data,
            type_=type_,
            connected_app_id=connected_app_id,
            name=name,
        )

        test_connected_app_request.additional_properties = d
        return test_connected_app_request

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
