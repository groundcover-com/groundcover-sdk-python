from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProfilingRuleScope")


@_attrs_define
class ProfilingRuleScope:
    """ProfilingRuleScope is where a rule applies: "*" for both env and cluster
    means every cluster; otherwise one env and cluster pair a sensor has
    reported from.

        Attributes:
            cluster (str): The cluster, or "*".
            env (str): The env, or "*". An empty env is a cluster installed without one.
    """

    cluster: str
    env: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        env = self.env

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "env": env,
            }
        )

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

        env = d.pop("env")

        profiling_rule_scope = cls(
            cluster=cluster,
            env=env,
        )

        profiling_rule_scope.additional_properties = d
        return profiling_rule_scope

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
