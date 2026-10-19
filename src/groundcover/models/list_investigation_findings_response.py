from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.investigation_finding import InvestigationFinding


T = TypeVar("T", bound="ListInvestigationFindingsResponse")


@_attrs_define
class ListInvestigationFindingsResponse:
    """
    Attributes:
        done (bool): Whether this page exhausts the findings currently stored; not investigation completion.
        findings (list[InvestigationFinding]): Full findings across the root investigation, ordered by createdAt then
            id, ascending.
    """

    done: bool
    findings: list[InvestigationFinding]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "findings": findings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_finding import InvestigationFinding

        d = dict(src_dict)
        done = d.pop("done")

        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = InvestigationFinding.from_dict(findings_item_data)

            findings.append(findings_item)

        list_investigation_findings_response = cls(
            done=done,
            findings=findings,
        )

        list_investigation_findings_response.additional_properties = d
        return list_investigation_findings_response

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
