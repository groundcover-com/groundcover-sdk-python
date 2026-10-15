from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invalid_citation_is_one_entry_of_the_error_details_when_cited_findings_cant_be_used_code import (
    InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsedCode,
)

T = TypeVar("T", bound="InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsed")


@_attrs_define
class InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsed:
    """
    Attributes:
        code (InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsedCode):
        finding_id (UUID):
    """

    code: InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsedCode
    finding_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        finding_id = str(self.finding_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "findingId": finding_id,
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
        code = InvalidCitationIsOneEntryOfTheErrorDetailsWhenCitedFindingsCantBeUsedCode(d.pop("code"))

        finding_id = UUID(d.pop("findingId"))

        invalid_citation_is_one_entry_of_the_error_details_when_cited_findings_cant_be_used = cls(
            code=code,
            finding_id=finding_id,
        )

        invalid_citation_is_one_entry_of_the_error_details_when_cited_findings_cant_be_used.additional_properties = d
        return invalid_citation_is_one_entry_of_the_error_details_when_cited_findings_cant_be_used

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
