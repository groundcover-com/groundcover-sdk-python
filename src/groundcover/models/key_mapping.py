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


T = TypeVar("T", bound="KeyMapping")


@_attrs_define
class KeyMapping:
    """
    Attributes:
        evidence (MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist | Unset):
        groundcover_key (str | Unset):
        metric_pattern (str | Unset): MetricPattern optionally scopes this mapping to groundcover metric names (not
            source metric names).
        origin (str | Unset): Origin is server-owned normalization provenance.
        source_key (str | Unset):
    """

    evidence: MappingEvidenceRecordsWhyAnAutomaticallyDiscoveredMappingWasSafeToPersist | Unset = UNSET
    groundcover_key: str | Unset = UNSET
    metric_pattern: str | Unset = UNSET
    origin: str | Unset = UNSET
    source_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evidence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = self.evidence.to_dict()

        groundcover_key = self.groundcover_key

        metric_pattern = self.metric_pattern

        origin = self.origin

        source_key = self.source_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if groundcover_key is not UNSET:
            field_dict["groundcover_key"] = groundcover_key
        if metric_pattern is not UNSET:
            field_dict["metric_pattern"] = metric_pattern
        if origin is not UNSET:
            field_dict["origin"] = origin
        if source_key is not UNSET:
            field_dict["source_key"] = source_key

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

        groundcover_key = d.pop("groundcover_key", UNSET)

        metric_pattern = d.pop("metric_pattern", UNSET)

        origin = d.pop("origin", UNSET)

        source_key = d.pop("source_key", UNSET)

        key_mapping = cls(
            evidence=evidence,
            groundcover_key=groundcover_key,
            metric_pattern=metric_pattern,
            origin=origin,
            source_key=source_key,
        )

        key_mapping.additional_properties = d
        return key_mapping

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
