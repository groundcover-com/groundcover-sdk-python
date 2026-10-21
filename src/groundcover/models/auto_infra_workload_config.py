from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AutoInfraWorkloadConfig")


@_attrs_define
class AutoInfraWorkloadConfig:
    """WorkloadConfig is one workload's setting. Env is "" for a cluster installed without one, and
    Namespace is "" for cluster-scoped kinds.

        Attributes:
            cluster (str):
            enabled (bool): Whether Autonomous Infrastructure manages the workload's resources.
            kind (str):
            name (str):
            env (str | Unset):
            namespace (str | Unset):
    """

    cluster: str
    enabled: bool
    kind: str
    name: str
    env: str | Unset = UNSET
    namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        enabled = self.enabled

        kind = self.kind

        name = self.name

        env = self.env

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "enabled": enabled,
                "kind": kind,
                "name": name,
            }
        )
        if env is not UNSET:
            field_dict["env"] = env
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

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
        cluster = d.pop("cluster")

        enabled = d.pop("enabled")

        kind = d.pop("kind")

        name = d.pop("name")

        env = d.pop("env", UNSET)

        namespace = d.pop("namespace", UNSET)

        auto_infra_workload_config = cls(
            cluster=cluster,
            enabled=enabled,
            kind=kind,
            name=name,
            env=env,
            namespace=namespace,
        )

        auto_infra_workload_config.additional_properties = d
        return auto_infra_workload_config

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
