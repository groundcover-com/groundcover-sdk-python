from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor


T = TypeVar("T", bound="FindingRetraction")


@_attrs_define
class FindingRetraction:
    """
    Attributes:
        at (datetime.datetime | Unset):
        by (InvestigationAuthor | Unset):
        reason (str | Unset):
    """

    at: datetime.datetime | Unset = UNSET
    by: InvestigationAuthor | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by, Unset):
            by = self.by.to_dict()

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor

        d = dict(src_dict)
        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset) or _at is None:
            at = UNSET
        else:
            at = parse_datetime(_at)

        _by = d.pop("by", UNSET)
        by: InvestigationAuthor | Unset
        if isinstance(_by, Unset) or _by is None:
            by = UNSET
        else:
            by = InvestigationAuthor.from_dict(_by)

        reason = d.pop("reason", UNSET)

        finding_retraction = cls(
            at=at,
            by=by,
            reason=reason,
        )

        finding_retraction.additional_properties = d
        return finding_retraction

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
