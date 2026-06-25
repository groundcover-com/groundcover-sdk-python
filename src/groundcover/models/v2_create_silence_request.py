from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v2_create_silence_request_recurrence_type import V2CreateSilenceRequestRecurrenceType
from ..models.v2_create_silence_request_type import V2CreateSilenceRequestType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.silence_matcher import SilenceMatcher
    from ..models.v2_create_silence_request_timeframes import V2CreateSilenceRequestTimeframes


T = TypeVar("T", bound="V2CreateSilenceRequest")


@_attrs_define
class V2CreateSilenceRequest:
    """
    Attributes:
        matchers (list[SilenceMatcher]): Matchers is a slice of Matchers that is sortable, implements Stringer, and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        type_ (V2CreateSilenceRequestType): one_time V2SilenceTypeOneTime
            recurring V2SilenceTypeRecurring
        comment (str | Unset): Optional comment
        enabled (bool | Unset): Optional when type=recurring. Whether the recurring silence is active.
        ends_at (datetime.datetime | Unset): Required when type=one_time. End time of the silence window.
        recurrence_type (V2CreateSilenceRequestRecurrenceType | Unset): Required when type=recurring. Recurrence cadence
            for the silence.
            daily RecurrenceTypeDaily
            weekly RecurrenceTypeWeekly
            monthly RecurrenceTypeMonthly
        starts_at (datetime.datetime | Unset): Required when type=one_time. Start time of the silence window.
        timeframes (V2CreateSilenceRequestTimeframes | Unset): Required when type=recurring. Map of day identifiers to
            time ranges.
        timezone (str | Unset): Required when type=recurring. IANA timezone for the recurrence schedule.
    """

    matchers: list[SilenceMatcher]
    type_: V2CreateSilenceRequestType
    comment: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    recurrence_type: V2CreateSilenceRequestRecurrenceType | Unset = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    timeframes: V2CreateSilenceRequestTimeframes | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matchers = []
        for componentsschemas_matchers_item_data in self.matchers:
            componentsschemas_matchers_item = componentsschemas_matchers_item_data.to_dict()
            matchers.append(componentsschemas_matchers_item)

        type_ = self.type_.value

        comment = self.comment

        enabled = self.enabled

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        recurrence_type: str | Unset = UNSET
        if not isinstance(self.recurrence_type, Unset):
            recurrence_type = self.recurrence_type.value

        starts_at: str | Unset = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        timeframes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeframes, Unset):
            timeframes = self.timeframes.to_dict()

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matchers": matchers,
                "type": type_,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if recurrence_type is not UNSET:
            field_dict["recurrenceType"] = recurrence_type
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if timeframes is not UNSET:
            field_dict["timeframes"] = timeframes
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher
        from ..models.v2_create_silence_request_timeframes import V2CreateSilenceRequestTimeframes

        d = dict(src_dict)
        matchers = []
        _matchers = d.pop("matchers")
        for componentsschemas_matchers_item_data in _matchers:
            componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

            matchers.append(componentsschemas_matchers_item)

        type_ = V2CreateSilenceRequestType(d.pop("type"))

        comment = d.pop("comment", UNSET)

        enabled = d.pop("enabled", UNSET)

        _ends_at = d.pop("endsAt", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset) or _ends_at is None:
            ends_at = UNSET
        else:
            ends_at = parse_datetime(_ends_at)

        _recurrence_type = d.pop("recurrenceType", UNSET)
        recurrence_type: V2CreateSilenceRequestRecurrenceType | Unset
        if isinstance(_recurrence_type, Unset) or _recurrence_type is None:
            recurrence_type = UNSET
        else:
            recurrence_type = V2CreateSilenceRequestRecurrenceType(_recurrence_type)

        _starts_at = d.pop("startsAt", UNSET)
        starts_at: datetime.datetime | Unset
        if isinstance(_starts_at, Unset) or _starts_at is None:
            starts_at = UNSET
        else:
            starts_at = parse_datetime(_starts_at)

        _timeframes = d.pop("timeframes", UNSET)
        timeframes: V2CreateSilenceRequestTimeframes | Unset
        if isinstance(_timeframes, Unset) or _timeframes is None:
            timeframes = UNSET
        else:
            timeframes = V2CreateSilenceRequestTimeframes.from_dict(_timeframes)

        timezone = d.pop("timezone", UNSET)

        v2_create_silence_request = cls(
            matchers=matchers,
            type_=type_,
            comment=comment,
            enabled=enabled,
            ends_at=ends_at,
            recurrence_type=recurrence_type,
            starts_at=starts_at,
            timeframes=timeframes,
            timezone=timezone,
        )

        v2_create_silence_request.additional_properties = d
        return v2_create_silence_request

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
