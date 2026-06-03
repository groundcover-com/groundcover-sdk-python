from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clusters_list_result_pods import ClustersListResultPods


T = TypeVar("T", bound="ClustersListResult")


@_attrs_define
class ClustersListResult:
    """
    Attributes:
        cloud_provider (str | Unset):
        cpu_allocatable (float | Unset):
        cpu_limit (float | Unset):
        cpu_limit_allocatable_percent (float | Unset):
        cpu_request (float | Unset):
        cpu_request_allocatable_percent (float | Unset):
        cpu_usage (float | Unset):
        cpu_usage_allocatable_percent (float | Unset):
        cpu_usage_limit_percent (float | Unset):
        cpu_usage_request_percent (float | Unset):
        env (str | Unset):
        issue_count (int | Unset):
        kubernetes_version (str | Unset):
        memory_allocatable (float | Unset):
        memory_limit (float | Unset):
        memory_limit_allocatable_percent (float | Unset):
        memory_request (float | Unset):
        memory_request_allocatable_percent (float | Unset):
        memory_usage (float | Unset):
        memory_usage_allocatable_percent (float | Unset):
        memory_usage_limit_percent (float | Unset):
        memory_usage_request_percent (float | Unset):
        name (str | Unset):
        nodes_count (int | Unset):
        pods (ClustersListResultPods | Unset):
    """

    cloud_provider: str | Unset = UNSET
    cpu_allocatable: float | Unset = UNSET
    cpu_limit: float | Unset = UNSET
    cpu_limit_allocatable_percent: float | Unset = UNSET
    cpu_request: float | Unset = UNSET
    cpu_request_allocatable_percent: float | Unset = UNSET
    cpu_usage: float | Unset = UNSET
    cpu_usage_allocatable_percent: float | Unset = UNSET
    cpu_usage_limit_percent: float | Unset = UNSET
    cpu_usage_request_percent: float | Unset = UNSET
    env: str | Unset = UNSET
    issue_count: int | Unset = UNSET
    kubernetes_version: str | Unset = UNSET
    memory_allocatable: float | Unset = UNSET
    memory_limit: float | Unset = UNSET
    memory_limit_allocatable_percent: float | Unset = UNSET
    memory_request: float | Unset = UNSET
    memory_request_allocatable_percent: float | Unset = UNSET
    memory_usage: float | Unset = UNSET
    memory_usage_allocatable_percent: float | Unset = UNSET
    memory_usage_limit_percent: float | Unset = UNSET
    memory_usage_request_percent: float | Unset = UNSET
    name: str | Unset = UNSET
    nodes_count: int | Unset = UNSET
    pods: ClustersListResultPods | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_provider = self.cloud_provider

        cpu_allocatable = self.cpu_allocatable

        cpu_limit = self.cpu_limit

        cpu_limit_allocatable_percent = self.cpu_limit_allocatable_percent

        cpu_request = self.cpu_request

        cpu_request_allocatable_percent = self.cpu_request_allocatable_percent

        cpu_usage = self.cpu_usage

        cpu_usage_allocatable_percent = self.cpu_usage_allocatable_percent

        cpu_usage_limit_percent = self.cpu_usage_limit_percent

        cpu_usage_request_percent = self.cpu_usage_request_percent

        env = self.env

        issue_count = self.issue_count

        kubernetes_version = self.kubernetes_version

        memory_allocatable = self.memory_allocatable

        memory_limit = self.memory_limit

        memory_limit_allocatable_percent = self.memory_limit_allocatable_percent

        memory_request = self.memory_request

        memory_request_allocatable_percent = self.memory_request_allocatable_percent

        memory_usage = self.memory_usage

        memory_usage_allocatable_percent = self.memory_usage_allocatable_percent

        memory_usage_limit_percent = self.memory_usage_limit_percent

        memory_usage_request_percent = self.memory_usage_request_percent

        name = self.name

        nodes_count = self.nodes_count

        pods: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pods, Unset):
            pods = self.pods.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if cpu_allocatable is not UNSET:
            field_dict["cpuAllocatable"] = cpu_allocatable
        if cpu_limit is not UNSET:
            field_dict["cpuLimit"] = cpu_limit
        if cpu_limit_allocatable_percent is not UNSET:
            field_dict["cpuLimitAllocatablePercent"] = cpu_limit_allocatable_percent
        if cpu_request is not UNSET:
            field_dict["cpuRequest"] = cpu_request
        if cpu_request_allocatable_percent is not UNSET:
            field_dict["cpuRequestAllocatablePercent"] = cpu_request_allocatable_percent
        if cpu_usage is not UNSET:
            field_dict["cpuUsage"] = cpu_usage
        if cpu_usage_allocatable_percent is not UNSET:
            field_dict["cpuUsageAllocatablePercent"] = cpu_usage_allocatable_percent
        if cpu_usage_limit_percent is not UNSET:
            field_dict["cpuUsageLimitPercent"] = cpu_usage_limit_percent
        if cpu_usage_request_percent is not UNSET:
            field_dict["cpuUsageRequestPercent"] = cpu_usage_request_percent
        if env is not UNSET:
            field_dict["env"] = env
        if issue_count is not UNSET:
            field_dict["issueCount"] = issue_count
        if kubernetes_version is not UNSET:
            field_dict["kubernetesVersion"] = kubernetes_version
        if memory_allocatable is not UNSET:
            field_dict["memoryAllocatable"] = memory_allocatable
        if memory_limit is not UNSET:
            field_dict["memoryLimit"] = memory_limit
        if memory_limit_allocatable_percent is not UNSET:
            field_dict["memoryLimitAllocatablePercent"] = memory_limit_allocatable_percent
        if memory_request is not UNSET:
            field_dict["memoryRequest"] = memory_request
        if memory_request_allocatable_percent is not UNSET:
            field_dict["memoryRequestAllocatablePercent"] = memory_request_allocatable_percent
        if memory_usage is not UNSET:
            field_dict["memoryUsage"] = memory_usage
        if memory_usage_allocatable_percent is not UNSET:
            field_dict["memoryUsageAllocatablePercent"] = memory_usage_allocatable_percent
        if memory_usage_limit_percent is not UNSET:
            field_dict["memoryUsageLimitPercent"] = memory_usage_limit_percent
        if memory_usage_request_percent is not UNSET:
            field_dict["memoryUsageRequestPercent"] = memory_usage_request_percent
        if name is not UNSET:
            field_dict["name"] = name
        if nodes_count is not UNSET:
            field_dict["nodesCount"] = nodes_count
        if pods is not UNSET:
            field_dict["pods"] = pods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clusters_list_result_pods import ClustersListResultPods

        d = dict(src_dict)
        cloud_provider = d.pop("cloudProvider", UNSET)

        cpu_allocatable = d.pop("cpuAllocatable", UNSET)

        cpu_limit = d.pop("cpuLimit", UNSET)

        cpu_limit_allocatable_percent = d.pop("cpuLimitAllocatablePercent", UNSET)

        cpu_request = d.pop("cpuRequest", UNSET)

        cpu_request_allocatable_percent = d.pop("cpuRequestAllocatablePercent", UNSET)

        cpu_usage = d.pop("cpuUsage", UNSET)

        cpu_usage_allocatable_percent = d.pop("cpuUsageAllocatablePercent", UNSET)

        cpu_usage_limit_percent = d.pop("cpuUsageLimitPercent", UNSET)

        cpu_usage_request_percent = d.pop("cpuUsageRequestPercent", UNSET)

        env = d.pop("env", UNSET)

        issue_count = d.pop("issueCount", UNSET)

        kubernetes_version = d.pop("kubernetesVersion", UNSET)

        memory_allocatable = d.pop("memoryAllocatable", UNSET)

        memory_limit = d.pop("memoryLimit", UNSET)

        memory_limit_allocatable_percent = d.pop("memoryLimitAllocatablePercent", UNSET)

        memory_request = d.pop("memoryRequest", UNSET)

        memory_request_allocatable_percent = d.pop("memoryRequestAllocatablePercent", UNSET)

        memory_usage = d.pop("memoryUsage", UNSET)

        memory_usage_allocatable_percent = d.pop("memoryUsageAllocatablePercent", UNSET)

        memory_usage_limit_percent = d.pop("memoryUsageLimitPercent", UNSET)

        memory_usage_request_percent = d.pop("memoryUsageRequestPercent", UNSET)

        name = d.pop("name", UNSET)

        nodes_count = d.pop("nodesCount", UNSET)

        _pods = d.pop("pods", UNSET)
        pods: ClustersListResultPods | Unset
        if isinstance(_pods, Unset) or _pods is None:
            pods = UNSET
        else:
            pods = ClustersListResultPods.from_dict(_pods)

        clusters_list_result = cls(
            cloud_provider=cloud_provider,
            cpu_allocatable=cpu_allocatable,
            cpu_limit=cpu_limit,
            cpu_limit_allocatable_percent=cpu_limit_allocatable_percent,
            cpu_request=cpu_request,
            cpu_request_allocatable_percent=cpu_request_allocatable_percent,
            cpu_usage=cpu_usage,
            cpu_usage_allocatable_percent=cpu_usage_allocatable_percent,
            cpu_usage_limit_percent=cpu_usage_limit_percent,
            cpu_usage_request_percent=cpu_usage_request_percent,
            env=env,
            issue_count=issue_count,
            kubernetes_version=kubernetes_version,
            memory_allocatable=memory_allocatable,
            memory_limit=memory_limit,
            memory_limit_allocatable_percent=memory_limit_allocatable_percent,
            memory_request=memory_request,
            memory_request_allocatable_percent=memory_request_allocatable_percent,
            memory_usage=memory_usage,
            memory_usage_allocatable_percent=memory_usage_allocatable_percent,
            memory_usage_limit_percent=memory_usage_limit_percent,
            memory_usage_request_percent=memory_usage_request_percent,
            name=name,
            nodes_count=nodes_count,
            pods=pods,
        )

        clusters_list_result.additional_properties = d
        return clusters_list_result

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
