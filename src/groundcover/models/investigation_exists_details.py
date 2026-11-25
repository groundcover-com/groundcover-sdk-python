from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="InvestigationExistsDetails")


@_attrs_define
class InvestigationExistsDetails:
    """InvestigationExistsDetails is the details of a 409 INVESTIGATION_EXISTS, the root to join, or of a 409
    TRIGGER_IN_COOLDOWN, the trigger's root of the issue from within its cooldown.

        Attributes:
            investigation_id (UUID):
            issue_timestamp (datetime.datetime | Unset): The issue timestamp of the root to join, which names its firing
                cycle; only on INVESTIGATION_EXISTS.
    """

    investigation_id: UUID
    issue_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investigation_id = str(self.investigation_id)

        issue_timestamp: str | Unset = UNSET
        if not isinstance(self.issue_timestamp, Unset):
            issue_timestamp = self.issue_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investigationId": investigation_id,
            }
        )
        if issue_timestamp is not UNSET:
            field_dict["issueTimestamp"] = issue_timestamp

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
        investigation_id = UUID(d.pop("investigationId"))

        _issue_timestamp = d.pop("issueTimestamp", UNSET)
        issue_timestamp: datetime.datetime | Unset
        if isinstance(_issue_timestamp, Unset) or _issue_timestamp is None:
            issue_timestamp = UNSET
        else:
            issue_timestamp = parse_datetime(_issue_timestamp)

        investigation_exists_details = cls(
            investigation_id=investigation_id,
            issue_timestamp=issue_timestamp,
        )

        investigation_exists_details.additional_properties = d
        return investigation_exists_details

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
