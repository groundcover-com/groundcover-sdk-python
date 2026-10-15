from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_evidence_relation import InvestigationEvidenceRelation

if TYPE_CHECKING:
    from ..models.investigation_finding import InvestigationFinding


T = TypeVar("T", bound="InvestigationEvidence")


@_attrs_define
class InvestigationEvidence:
    """
    Attributes:
        finding (InvestigationFinding):
        relation (InvestigationEvidenceRelation): supports RelationSupports
            contradicts RelationContradicts
    """

    finding: InvestigationFinding
    relation: InvestigationEvidenceRelation
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finding = self.finding.to_dict()

        relation = self.relation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "finding": finding,
                "relation": relation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_finding import InvestigationFinding

        d = dict(src_dict)
        finding = InvestigationFinding.from_dict(d.pop("finding"))

        relation = InvestigationEvidenceRelation(d.pop("relation"))

        investigation_evidence = cls(
            finding=finding,
            relation=relation,
        )

        investigation_evidence.additional_properties = d
        return investigation_evidence

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
