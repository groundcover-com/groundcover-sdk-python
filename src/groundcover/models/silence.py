from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.silence_matcher import SilenceMatcher


T = TypeVar("T", bound="Silence")


@_attrs_define
class Silence:
    """
    Attributes:
        active (bool | Unset):
        comment (str | Unset):
        created_by (str | Unset):
        created_by_email (str | Unset):
        ends_at (datetime.datetime | Unset):
        id (UUID | Unset):
        matchers (list[SilenceMatcher] | Unset): Matchers is a slice of Matchers that is sortable, implements Stringer,
            and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        recurring_silence_id (UUID | Unset):
        starts_at (datetime.datetime | Unset):
    """

    active: bool | Unset = UNSET
    comment: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_by_email: str | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    matchers: list[SilenceMatcher] | Unset = UNSET
    recurring_silence_id: UUID | Unset = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        comment = self.comment

        created_by = self.created_by

        created_by_email = self.created_by_email

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        matchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matchers, Unset):
            matchers = []
            for componentsschemas_matchers_item_data in self.matchers:
                componentsschemas_matchers_item = componentsschemas_matchers_item_data.to_dict()
                matchers.append(componentsschemas_matchers_item)

        recurring_silence_id: str | Unset = UNSET
        if not isinstance(self.recurring_silence_id, Unset):
            recurring_silence_id = str(self.recurring_silence_id)

        starts_at: str | Unset = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_email is not UNSET:
            field_dict["createdByEmail"] = created_by_email
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if id is not UNSET:
            field_dict["id"] = id
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if recurring_silence_id is not UNSET:
            field_dict["recurringSilenceId"] = recurring_silence_id
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        comment = d.pop("comment", UNSET)

        created_by = d.pop("createdBy", UNSET)

        created_by_email = d.pop("createdByEmail", UNSET)

        _ends_at = d.pop("endsAt", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset) or _ends_at is None:
            ends_at = UNSET
        else:
            ends_at = parse_datetime(_ends_at)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset) or _id is None:
            id = UNSET
        else:
            id = UUID(_id)

        _matchers = d.pop("matchers", UNSET)
        matchers: list[SilenceMatcher] | Unset = UNSET
        if _matchers is not UNSET:
            matchers = []
            for componentsschemas_matchers_item_data in _matchers:
                componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

                matchers.append(componentsschemas_matchers_item)

        _recurring_silence_id = d.pop("recurringSilenceId", UNSET)
        recurring_silence_id: UUID | Unset
        if isinstance(_recurring_silence_id, Unset) or _recurring_silence_id is None:
            recurring_silence_id = UNSET
        else:
            recurring_silence_id = UUID(_recurring_silence_id)

        _starts_at = d.pop("startsAt", UNSET)
        starts_at: datetime.datetime | Unset
        if isinstance(_starts_at, Unset) or _starts_at is None:
            starts_at = UNSET
        else:
            starts_at = parse_datetime(_starts_at)

        silence = cls(
            active=active,
            comment=comment,
            created_by=created_by,
            created_by_email=created_by_email,
            ends_at=ends_at,
            id=id,
            matchers=matchers,
            recurring_silence_id=recurring_silence_id,
            starts_at=starts_at,
        )

        silence.additional_properties = d
        return silence

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
