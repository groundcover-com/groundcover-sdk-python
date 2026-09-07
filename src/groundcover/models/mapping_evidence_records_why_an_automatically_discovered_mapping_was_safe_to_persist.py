from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist")


@_attrs_define
class MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist:
    """
    Attributes:
        kind (str | Unset):
        metric (str | Unset):
        pool_size (int | Unset): PoolSize is the size of the pruned candidate pool the discovery query
            returned, not the size of the tenant's metric catalog.
    """

    kind: str | Unset = UNSET
    metric: str | Unset = UNSET
    pool_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        metric = self.metric

        pool_size = self.pool_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if metric is not UNSET:
            field_dict["metric"] = metric
        if pool_size is not UNSET:
            field_dict["pool_size"] = pool_size

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
        kind = d.pop("kind", UNSET)

        metric = d.pop("metric", UNSET)

        pool_size = d.pop("pool_size", UNSET)

        mapping_evidence_records_why_an_automatically_discovered_mapping_was_safe_to_persist = cls(
            kind=kind,
            metric=metric,
            pool_size=pool_size,
        )

        mapping_evidence_records_why_an_automatically_discovered_mapping_was_safe_to_persist.additional_properties = d
        return mapping_evidence_records_why_an_automatically_discovered_mapping_was_safe_to_persist

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
