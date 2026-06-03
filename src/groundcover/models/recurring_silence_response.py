from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recurring_silence_response_recurrence_type import RecurringSilenceResponseRecurrenceType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recurring_silence_response_timeframes import RecurringSilenceResponseTimeframes
    from ..models.silence_matcher import SilenceMatcher


T = TypeVar("T", bound="RecurringSilenceResponse")


@_attrs_define
class RecurringSilenceResponse:
    """
    Attributes:
        comment (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by (str | Unset):
        created_by_email (str | Unset):
        enabled (bool | Unset):
        id (UUID | Unset):
        matchers (list[SilenceMatcher] | Unset): Matchers is a slice of Matchers that is sortable, implements Stringer,
            and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        recurrence_type (RecurringSilenceResponseRecurrenceType | Unset):
        timeframes (RecurringSilenceResponseTimeframes | Unset):
        timezone (str | Unset):
        updated_at (datetime.datetime | Unset):
    """

    comment: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    created_by_email: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    matchers: list[SilenceMatcher] | Unset = UNSET
    recurrence_type: RecurringSilenceResponseRecurrenceType | Unset = UNSET
    timeframes: RecurringSilenceResponseTimeframes | Unset = UNSET
    timezone: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        created_by_email = self.created_by_email

        enabled = self.enabled

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

        timeframes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeframes, Unset):
            timeframes = self.timeframes.to_dict()

        timezone = self.timezone

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if id is not UNSET:
            field_dict["id"] = id
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if recurrence_type is not UNSET:
            field_dict["recurrenceType"] = recurrence_type
        if timeframes is not UNSET:
            field_dict["timeframes"] = timeframes
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recurring_silence_response_timeframes import RecurringSilenceResponseTimeframes
        from ..models.silence_matcher import SilenceMatcher

        d = dict(src_dict)
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
        recurrence_type: RecurringSilenceResponseRecurrenceType | Unset
        if isinstance(_recurrence_type, Unset) or _recurrence_type is None:
            recurrence_type = UNSET
        else:
            recurrence_type = RecurringSilenceResponseRecurrenceType(_recurrence_type)

        _timeframes = d.pop("timeframes", UNSET)
        timeframes: RecurringSilenceResponseTimeframes | Unset
        if isinstance(_timeframes, Unset) or _timeframes is None:
            timeframes = UNSET
        else:
            timeframes = RecurringSilenceResponseTimeframes.from_dict(_timeframes)

        timezone = d.pop("timezone", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        recurring_silence_response = cls(
            comment=comment,
            created_at=created_at,
            created_by=created_by,
            created_by_email=created_by_email,
            enabled=enabled,
            id=id,
            matchers=matchers,
            recurrence_type=recurrence_type,
            timeframes=timeframes,
            timezone=timezone,
            updated_at=updated_at,
        )

        recurring_silence_response.additional_properties = d
        return recurring_silence_response

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
