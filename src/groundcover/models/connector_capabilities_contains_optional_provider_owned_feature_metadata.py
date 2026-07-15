from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_mcp_capability_describes_an_mcp_source_exposed_by_a_first_class_connector import (
        ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector,
    )


T = TypeVar("T", bound="ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata")


@_attrs_define
class ConnectorCapabilitiesContainsOptionalProviderOwnedFeatureMetadata:
    """
    Attributes:
        mcp (ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector | Unset):
    """

    mcp: ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcp, Unset):
            mcp = self.mcp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mcp is not UNSET:
            field_dict["mcp"] = mcp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_mcp_capability_describes_an_mcp_source_exposed_by_a_first_class_connector import (
            ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector,
        )

        d = dict(src_dict)
        _mcp = d.pop("mcp", UNSET)
        mcp: ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector | Unset
        if isinstance(_mcp, Unset) or _mcp is None:
            mcp = UNSET
        else:
            mcp = ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector.from_dict(_mcp)

        connector_capabilities_contains_optional_provider_owned_feature_metadata = cls(
            mcp=mcp,
        )

        connector_capabilities_contains_optional_provider_owned_feature_metadata.additional_properties = d
        return connector_capabilities_contains_optional_provider_owned_feature_metadata

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
