from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Trace")


@_attrs_define
class Trace:
    """Trace represents a trace record for graph transformation

    Attributes:
        client (str):
        client_is_external (bool):
        client_namespace (str):
        protocol_type (str):
        server (str):
        server_is_external (bool):
        server_namespace (str):
        source (str):
        status (str):
        cluster (str | Unset):
        env (str | Unset):
    """

    client: str
    client_is_external: bool
    client_namespace: str
    protocol_type: str
    server: str
    server_is_external: bool
    server_namespace: str
    source: str
    status: str
    cluster: str | Unset = UNSET
    env: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client = self.client

        client_is_external = self.client_is_external

        client_namespace = self.client_namespace

        protocol_type = self.protocol_type

        server = self.server

        server_is_external = self.server_is_external

        server_namespace = self.server_namespace

        source = self.source

        status = self.status

        cluster = self.cluster

        env = self.env

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client": client,
                "client_is_external": client_is_external,
                "client_namespace": client_namespace,
                "protocol_type": protocol_type,
                "server": server,
                "server_is_external": server_is_external,
                "server_namespace": server_namespace,
                "source": source,
                "status": status,
            }
        )
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if env is not UNSET:
            field_dict["env"] = env

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
        client = d.pop("client")

        client_is_external = d.pop("client_is_external")

        client_namespace = d.pop("client_namespace")

        protocol_type = d.pop("protocol_type")

        server = d.pop("server")

        server_is_external = d.pop("server_is_external")

        server_namespace = d.pop("server_namespace")

        source = d.pop("source")

        status = d.pop("status")

        cluster = d.pop("cluster", UNSET)

        env = d.pop("env", UNSET)

        trace = cls(
            client=client,
            client_is_external=client_is_external,
            client_namespace=client_namespace,
            protocol_type=protocol_type,
            server=server,
            server_is_external=server_is_external,
            server_namespace=server_namespace,
            source=source,
            status=status,
            cluster=cluster,
            env=env,
        )

        trace.additional_properties = d
        return trace

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
