from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.evidence_request import EvidenceRequest


T = TypeVar("T", bound="SetAssessmentRequestReplacesTheCallersAssessmentOnTheNode")


@_attrs_define
class SetAssessmentRequestReplacesTheCallersAssessmentOnTheNode:
    """
    Attributes:
        details (str):
        evidence (list[EvidenceRequest]): The full set of citations, each finding at most once; [] means none.
    """

    details: str
    evidence: list[EvidenceRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "details": details,
                "evidence": evidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evidence_request import EvidenceRequest

        d = dict(src_dict)
        details = d.pop("details")

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = EvidenceRequest.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        set_assessment_request_replaces_the_callers_assessment_on_the_node = cls(
            details=details,
            evidence=evidence,
        )

        set_assessment_request_replaces_the_callers_assessment_on_the_node.additional_properties = d
        return set_assessment_request_replaces_the_callers_assessment_on_the_node

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
