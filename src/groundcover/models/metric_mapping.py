from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mapping_evidence_records_why_an_automatically_discovered_mapping_was_safe_to_persist import (
        MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist,
    )


T = TypeVar("T", bound="MetricMapping")


@_attrs_define
class MetricMapping:
    """
    Attributes:
        evidence (MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist | Unset):
        groundcover_metric (str | Unset):
        origin (str | Unset): Origin is server-owned normalization provenance.
        source_metric (str | Unset):
    """

    evidence: MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist | Unset = UNSET
    groundcover_metric: str | Unset = UNSET
    origin: str | Unset = UNSET
    source_metric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evidence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = self.evidence.to_dict()

        groundcover_metric = self.groundcover_metric

        origin = self.origin

        source_metric = self.source_metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if groundcover_metric is not UNSET:
            field_dict["groundcover_metric"] = groundcover_metric
        if origin is not UNSET:
            field_dict["origin"] = origin
        if source_metric is not UNSET:
            field_dict["source_metric"] = source_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mapping_evidence_records_why_an_automatically_discovered_mapping_was_safe_to_persist import (
            MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist,
        )

        d = dict(src_dict)
        _evidence = d.pop("evidence", UNSET)
        evidence: MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist | Unset
        if isinstance(_evidence, Unset) or _evidence is None:
            evidence = UNSET
        else:
            evidence = MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist.from_dict(_evidence)

        groundcover_metric = d.pop("groundcover_metric", UNSET)

        origin = d.pop("origin", UNSET)

        source_metric = d.pop("source_metric", UNSET)

        metric_mapping = cls(
            evidence=evidence,
            groundcover_metric=groundcover_metric,
            origin=origin,
            source_metric=source_metric,
        )

        metric_mapping.additional_properties = d
        return metric_mapping

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
