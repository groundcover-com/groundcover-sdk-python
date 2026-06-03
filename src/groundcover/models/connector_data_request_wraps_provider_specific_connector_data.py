from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_data_request_wraps_provider_specific_connector_data_data import (
        ConnectorDataRequestWrapsProviderSpecificConnectorDataData,
    )


T = TypeVar("T", bound="ConnectorDataRequestWrapsProviderSpecificConnectorData")


@_attrs_define
class ConnectorDataRequestWrapsProviderSpecificConnectorData:
    """
    Attributes:
        data (ConnectorDataRequestWrapsProviderSpecificConnectorDataData | Unset): Provider-specific connector data.
    """

    data: ConnectorDataRequestWrapsProviderSpecificConnectorDataData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_data_request_wraps_provider_specific_connector_data_data import (
            ConnectorDataRequestWrapsProviderSpecificConnectorDataData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ConnectorDataRequestWrapsProviderSpecificConnectorDataData | Unset
        if isinstance(_data, Unset) or _data is None:
            data = UNSET
        else:
            data = ConnectorDataRequestWrapsProviderSpecificConnectorDataData.from_dict(_data)

        connector_data_request_wraps_provider_specific_connector_data = cls(
            data=data,
        )

        connector_data_request_wraps_provider_specific_connector_data.additional_properties = d
        return connector_data_request_wraps_provider_specific_connector_data

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
