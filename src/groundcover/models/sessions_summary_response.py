from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SessionsSummaryResponse")


@_attrs_define
class SessionsSummaryResponse:
    """
    Attributes:
        cls (float | Unset):
        error_rate (float | Unset):
        inp (float | Unset):
        page_load_time (float | Unset):
        total_sessions (int | Unset):
        unique_users (int | Unset):
    """

    cls: float | Unset = UNSET
    error_rate: float | Unset = UNSET
    inp: float | Unset = UNSET
    page_load_time: float | Unset = UNSET
    total_sessions: int | Unset = UNSET
    unique_users: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cls = self.cls

        error_rate = self.error_rate

        inp = self.inp

        page_load_time = self.page_load_time

        total_sessions = self.total_sessions

        unique_users = self.unique_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cls is not UNSET:
            field_dict["cls"] = cls
        if error_rate is not UNSET:
            field_dict["errorRate"] = error_rate
        if inp is not UNSET:
            field_dict["inp"] = inp
        if page_load_time is not UNSET:
            field_dict["pageLoadTime"] = page_load_time
        if total_sessions is not UNSET:
            field_dict["totalSessions"] = total_sessions
        if unique_users is not UNSET:
            field_dict["uniqueUsers"] = unique_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        cls = d.pop("cls", UNSET)

        error_rate = d.pop("errorRate", UNSET)

        inp = d.pop("inp", UNSET)

        page_load_time = d.pop("pageLoadTime", UNSET)

        total_sessions = d.pop("totalSessions", UNSET)

        unique_users = d.pop("uniqueUsers", UNSET)

        sessions_summary_response = cls(
            cls=cls,
            error_rate=error_rate,
            inp=inp,
            page_load_time=page_load_time,
            total_sessions=total_sessions,
            unique_users=unique_users,
        )

        sessions_summary_response.additional_properties = d
        return sessions_summary_response

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
