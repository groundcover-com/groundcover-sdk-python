from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_finding import InvestigationFinding


T = TypeVar("T", bound="ListInvestigationFindingsResponse")


@_attrs_define
class ListInvestigationFindingsResponse:
    """
    Attributes:
        done (bool): Whether this page exhausts the findings currently stored; not investigation completion.
        findings (list[InvestigationFinding]): Full findings across the root investigation, ordered by createdAt,
            ascending.
        next_after_timestamp (datetime.datetime | Unset): Last returned finding's createdAt, to send as afterTimestamp;
            an empty page retains afterTimestamp.
    """

    done: bool
    findings: list[InvestigationFinding]
    next_after_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        next_after_timestamp: str | Unset = UNSET
        if not isinstance(self.next_after_timestamp, Unset):
            next_after_timestamp = self.next_after_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "findings": findings,
            }
        )
        if next_after_timestamp is not UNSET:
            field_dict["nextAfterTimestamp"] = next_after_timestamp

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

        _next_after_timestamp = d.pop("nextAfterTimestamp", UNSET)
        next_after_timestamp: datetime.datetime | Unset
        if isinstance(_next_after_timestamp, Unset) or _next_after_timestamp is None:
            next_after_timestamp = UNSET
        else:
            next_after_timestamp = parse_datetime(_next_after_timestamp)

        list_investigation_findings_response = cls(
            done=done,
            findings=findings,
            next_after_timestamp=next_after_timestamp,
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
