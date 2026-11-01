from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TriggerOpensARootInvestigationWhenAMonitorIssueItsQuerySelectsStartsFiring")


@_attrs_define
class TriggerOpensARootInvestigationWhenAMonitorIssueItsQuerySelectsStartsFiring:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        id (str):
        instructions (str): What the trigger's investigations are asked to do after their statement; empty for none.
        max_concurrent (int): At most this many of the trigger's investigations are open at once.
        modified_at (datetime.datetime):
        modified_by (str): The last editor; the trigger's investigations act as this user.
        name (str):
        query (str): The gcQL issue selector notification routes use.
        cooldown_interval (str | Unset): A still-firing issue is investigated again at most once per interval; empty:
            once per firing cycle.
    """

    created_at: datetime.datetime
    created_by: str
    id: str
    instructions: str
    max_concurrent: int
    modified_at: datetime.datetime
    modified_by: str
    name: str
    query: str
    cooldown_interval: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = self.id

        instructions = self.instructions

        max_concurrent = self.max_concurrent

        modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by

        name = self.name

        query = self.query

        cooldown_interval = self.cooldown_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "createdBy": created_by,
                "id": id,
                "instructions": instructions,
                "maxConcurrent": max_concurrent,
                "modifiedAt": modified_at,
                "modifiedBy": modified_by,
                "name": name,
                "query": query,
            }
        )
        if cooldown_interval is not UNSET:
            field_dict["cooldownInterval"] = cooldown_interval

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
        created_at = parse_datetime(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        id = d.pop("id")

        instructions = d.pop("instructions")

        max_concurrent = d.pop("maxConcurrent")

        modified_at = parse_datetime(d.pop("modifiedAt"))

        modified_by = d.pop("modifiedBy")

        name = d.pop("name")

        query = d.pop("query")

        cooldown_interval = d.pop("cooldownInterval", UNSET)

        trigger_opens_a_root_investigation_when_a_monitor_issue_its_query_selects_starts_firing = cls(
            created_at=created_at,
            created_by=created_by,
            id=id,
            instructions=instructions,
            max_concurrent=max_concurrent,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            query=query,
            cooldown_interval=cooldown_interval,
        )

        trigger_opens_a_root_investigation_when_a_monitor_issue_its_query_selects_starts_firing.additional_properties = d
        return trigger_opens_a_root_investigation_when_a_monitor_issue_its_query_selects_starts_firing

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
