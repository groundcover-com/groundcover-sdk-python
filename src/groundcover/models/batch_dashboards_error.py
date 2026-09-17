from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="BatchDashboardsError")


@_attrs_define
class BatchDashboardsError:
    """
    Attributes:
        code (str | Unset): Code mirrors the single-route ErrorResponse.code contract so the UI can
            branch the same way: set to VIEW_REVISION_CONFLICT when the item lost a
            write race (retry the item), empty for permanent per-item failures.
        id (str | Unset):
        reason (str | Unset):
    """

    code: str | Unset = UNSET
    id: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        id = self.id

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if reason is not UNSET:
            field_dict["reason"] = reason

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
        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        reason = d.pop("reason", UNSET)

        batch_dashboards_error = cls(
            code=code,
            id=id,
            reason=reason,
        )

        batch_dashboards_error.additional_properties = d
        return batch_dashboards_error

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
