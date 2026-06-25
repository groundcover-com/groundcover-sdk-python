from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workloads_list_item_identifiers import WorkloadsListItemIdentifiers


T = TypeVar("T", bound="WorkloadsListItem")


@_attrs_define
class WorkloadsListItem:
    """
    Attributes:
        cluster (str | Unset):
        cpu_limit (float | Unset):
        cpu_usage (float | Unset):
        env (str | Unset):
        env_type (str | Unset):
        error_rate (float | Unset):
        identifiers (WorkloadsListItemIdentifiers | Unset):
        issue_count (int | Unset):
        kind (str | Unset):
        memory_limit (float | Unset):
        memory_usage (float | Unset):
        namespace (str | Unset):
        p50 (float | Unset):
        p95 (float | Unset):
        p99 (float | Unset):
        pods_count (int | Unset):
        ready (bool | Unset):
        resource_version (str | Unset):
        rps (float | Unset):
        uid (str | Unset):
        workload (str | Unset):
    """

    cluster: str | Unset = UNSET
    cpu_limit: float | Unset = UNSET
    cpu_usage: float | Unset = UNSET
    env: str | Unset = UNSET
    env_type: str | Unset = UNSET
    error_rate: float | Unset = UNSET
    identifiers: WorkloadsListItemIdentifiers | Unset = UNSET
    issue_count: int | Unset = UNSET
    kind: str | Unset = UNSET
    memory_limit: float | Unset = UNSET
    memory_usage: float | Unset = UNSET
    namespace: str | Unset = UNSET
    p50: float | Unset = UNSET
    p95: float | Unset = UNSET
    p99: float | Unset = UNSET
    pods_count: int | Unset = UNSET
    ready: bool | Unset = UNSET
    resource_version: str | Unset = UNSET
    rps: float | Unset = UNSET
    uid: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        cpu_limit = self.cpu_limit

        cpu_usage = self.cpu_usage

        env = self.env

        env_type = self.env_type

        error_rate = self.error_rate

        identifiers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers.to_dict()

        issue_count = self.issue_count

        kind = self.kind

        memory_limit = self.memory_limit

        memory_usage = self.memory_usage

        namespace = self.namespace

        p50 = self.p50

        p95 = self.p95

        p99 = self.p99

        pods_count = self.pods_count

        ready = self.ready

        resource_version = self.resource_version

        rps = self.rps

        uid = self.uid

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if cpu_limit is not UNSET:
            field_dict["cpuLimit"] = cpu_limit
        if cpu_usage is not UNSET:
            field_dict["cpuUsage"] = cpu_usage
        if env is not UNSET:
            field_dict["env"] = env
        if env_type is not UNSET:
            field_dict["envType"] = env_type
        if error_rate is not UNSET:
            field_dict["errorRate"] = error_rate
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if issue_count is not UNSET:
            field_dict["issueCount"] = issue_count
        if kind is not UNSET:
            field_dict["kind"] = kind
        if memory_limit is not UNSET:
            field_dict["memoryLimit"] = memory_limit
        if memory_usage is not UNSET:
            field_dict["memoryUsage"] = memory_usage
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if p50 is not UNSET:
            field_dict["p50"] = p50
        if p95 is not UNSET:
            field_dict["p95"] = p95
        if p99 is not UNSET:
            field_dict["p99"] = p99
        if pods_count is not UNSET:
            field_dict["podsCount"] = pods_count
        if ready is not UNSET:
            field_dict["ready"] = ready
        if resource_version is not UNSET:
            field_dict["resourceVersion"] = resource_version
        if rps is not UNSET:
            field_dict["rps"] = rps
        if uid is not UNSET:
            field_dict["uid"] = uid
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workloads_list_item_identifiers import WorkloadsListItemIdentifiers

        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        cpu_limit = d.pop("cpuLimit", UNSET)

        cpu_usage = d.pop("cpuUsage", UNSET)

        env = d.pop("env", UNSET)

        env_type = d.pop("envType", UNSET)

        error_rate = d.pop("errorRate", UNSET)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: WorkloadsListItemIdentifiers | Unset
        if isinstance(_identifiers, Unset) or _identifiers is None:
            identifiers = UNSET
        else:
            identifiers = WorkloadsListItemIdentifiers.from_dict(_identifiers)

        issue_count = d.pop("issueCount", UNSET)

        kind = d.pop("kind", UNSET)

        memory_limit = d.pop("memoryLimit", UNSET)

        memory_usage = d.pop("memoryUsage", UNSET)

        namespace = d.pop("namespace", UNSET)

        p50 = d.pop("p50", UNSET)

        p95 = d.pop("p95", UNSET)

        p99 = d.pop("p99", UNSET)

        pods_count = d.pop("podsCount", UNSET)

        ready = d.pop("ready", UNSET)

        resource_version = d.pop("resourceVersion", UNSET)

        rps = d.pop("rps", UNSET)

        uid = d.pop("uid", UNSET)

        workload = d.pop("workload", UNSET)

        workloads_list_item = cls(
            cluster=cluster,
            cpu_limit=cpu_limit,
            cpu_usage=cpu_usage,
            env=env,
            env_type=env_type,
            error_rate=error_rate,
            identifiers=identifiers,
            issue_count=issue_count,
            kind=kind,
            memory_limit=memory_limit,
            memory_usage=memory_usage,
            namespace=namespace,
            p50=p50,
            p95=p95,
            p99=p99,
            pods_count=pods_count,
            ready=ready,
            resource_version=resource_version,
            rps=rps,
            uid=uid,
            workload=workload,
        )

        workloads_list_item.additional_properties = d
        return workloads_list_item

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
