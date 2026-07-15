from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector")


@_attrs_define
class ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnector:
    """
    Attributes:
        display_name (str): Display name shown for the MCP source.
        server_id (str): Stable identifier for the connector-provided MCP server.
        source_kind (str): Ownership kind for the MCP source.
        auth_state (str | Unset):
        icon (str | Unset):
        org_discovery_path (str | Unset):
        setup_guidance (str | Unset):
        user_proxy_path (str | Unset):
    """

    display_name: str
    server_id: str
    source_kind: str
    auth_state: str | Unset = UNSET
    icon: str | Unset = UNSET
    org_discovery_path: str | Unset = UNSET
    setup_guidance: str | Unset = UNSET
    user_proxy_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        server_id = self.server_id

        source_kind = self.source_kind

        auth_state = self.auth_state

        icon = self.icon

        org_discovery_path = self.org_discovery_path

        setup_guidance = self.setup_guidance

        user_proxy_path = self.user_proxy_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "serverId": server_id,
                "sourceKind": source_kind,
            }
        )
        if auth_state is not UNSET:
            field_dict["authState"] = auth_state
        if icon is not UNSET:
            field_dict["icon"] = icon
        if org_discovery_path is not UNSET:
            field_dict["orgDiscoveryPath"] = org_discovery_path
        if setup_guidance is not UNSET:
            field_dict["setupGuidance"] = setup_guidance
        if user_proxy_path is not UNSET:
            field_dict["userProxyPath"] = user_proxy_path

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
        display_name = d.pop("displayName")

        server_id = d.pop("serverId")

        source_kind = d.pop("sourceKind")

        auth_state = d.pop("authState", UNSET)

        icon = d.pop("icon", UNSET)

        org_discovery_path = d.pop("orgDiscoveryPath", UNSET)

        setup_guidance = d.pop("setupGuidance", UNSET)

        user_proxy_path = d.pop("userProxyPath", UNSET)

        connector_mcp_capability_describes_an_mcp_source_exposed_by_a_first_class_connector = cls(
            display_name=display_name,
            server_id=server_id,
            source_kind=source_kind,
            auth_state=auth_state,
            icon=icon,
            org_discovery_path=org_discovery_path,
            setup_guidance=setup_guidance,
            user_proxy_path=user_proxy_path,
        )

        connector_mcp_capability_describes_an_mcp_source_exposed_by_a_first_class_connector.additional_properties = d
        return connector_mcp_capability_describes_an_mcp_source_exposed_by_a_first_class_connector

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
