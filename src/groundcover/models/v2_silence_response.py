from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v2_silence_response_recurrence_type import V2SilenceResponseRecurrenceType
from ..models.v2_silence_response_type import V2SilenceResponseType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.silence_matcher import SilenceMatcher
    from ..models.v2_silence_response_timeframes import V2SilenceResponseTimeframes


T = TypeVar("T", bound="V2SilenceResponse")


@_attrs_define
class V2SilenceResponse:
    """
    Attributes:
        active (bool | Unset):
        comment (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by (str | Unset):
        created_by_email (str | Unset):
        enabled (bool | Unset):
        ends_at (datetime.datetime | Unset):
        id (UUID | Unset):
        matchers (list[SilenceMatcher] | Unset): Matchers is a slice of Matchers that is sortable, implements Stringer,
            and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        recurrence_type (V2SilenceResponseRecurrenceType | Unset): Recurring silence fields
            daily RecurrenceTypeDaily
            weekly RecurrenceTypeWeekly
            monthly RecurrenceTypeMonthly
        recurring_silence_id (UUID | Unset):
        starts_at (datetime.datetime | Unset): One-time silence fields
        timeframes (V2SilenceResponseTimeframes | Unset):
        timezone (str | Unset):
        type_ (V2SilenceResponseType | Unset):
        updated_at (datetime.datetime | Unset):
    """

    active: bool | Unset = UNSET
    comment: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    created_by_email: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    matchers: list[SilenceMatcher] | Unset = UNSET
    recurrence_type: V2SilenceResponseRecurrenceType | Unset = UNSET
    recurring_silence_id: UUID | Unset = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    timeframes: V2SilenceResponseTimeframes | Unset = UNSET
    timezone: str | Unset = UNSET
    type_: V2SilenceResponseType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        comment = self.comment

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        created_by_email = self.created_by_email

        enabled = self.enabled

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

        recurrence_type: str | Unset = UNSET
        if not isinstance(self.recurrence_type, Unset):
            recurrence_type = self.recurrence_type.value

        recurring_silence_id: str | Unset = UNSET
        if not isinstance(self.recurring_silence_id, Unset):
            recurring_silence_id = str(self.recurring_silence_id)

        starts_at: str | Unset = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        timeframes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeframes, Unset):
            timeframes = self.timeframes.to_dict()

        timezone = self.timezone

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_email is not UNSET:
            field_dict["createdByEmail"] = created_by_email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if id is not UNSET:
            field_dict["id"] = id
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if recurrence_type is not UNSET:
            field_dict["recurrenceType"] = recurrence_type
        if recurring_silence_id is not UNSET:
            field_dict["recurringSilenceId"] = recurring_silence_id
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if timeframes is not UNSET:
            field_dict["timeframes"] = timeframes
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher
        from ..models.v2_silence_response_timeframes import V2SilenceResponseTimeframes

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        comment = d.pop("comment", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        created_by = d.pop("createdBy", UNSET)

        created_by_email = d.pop("createdByEmail", UNSET)

        enabled = d.pop("enabled", UNSET)

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

        _recurrence_type = d.pop("recurrenceType", UNSET)
        recurrence_type: V2SilenceResponseRecurrenceType | Unset
        if isinstance(_recurrence_type, Unset) or _recurrence_type is None:
            recurrence_type = UNSET
        else:
            recurrence_type = V2SilenceResponseRecurrenceType(_recurrence_type)

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

        _timeframes = d.pop("timeframes", UNSET)
        timeframes: V2SilenceResponseTimeframes | Unset
        if isinstance(_timeframes, Unset) or _timeframes is None:
            timeframes = UNSET
        else:
            timeframes = V2SilenceResponseTimeframes.from_dict(_timeframes)

        timezone = d.pop("timezone", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: V2SilenceResponseType | Unset
        if isinstance(_type_, Unset) or _type_ is None:
            type_ = UNSET
        else:
            type_ = V2SilenceResponseType(_type_)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        v2_silence_response = cls(
            active=active,
            comment=comment,
            created_at=created_at,
            created_by=created_by,
            created_by_email=created_by_email,
            enabled=enabled,
            ends_at=ends_at,
            id=id,
            matchers=matchers,
            recurrence_type=recurrence_type,
            recurring_silence_id=recurring_silence_id,
            starts_at=starts_at,
            timeframes=timeframes,
            timezone=timezone,
            type_=type_,
            updated_at=updated_at,
        )

        v2_silence_response.additional_properties = d
        return v2_silence_response

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
