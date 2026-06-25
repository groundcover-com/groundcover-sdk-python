from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v2_update_silence_request_recurrence_type import V2UpdateSilenceRequestRecurrenceType
from ..models.v2_update_silence_request_type import V2UpdateSilenceRequestType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.silence_matcher import SilenceMatcher
    from ..models.v2_update_silence_request_timeframes import V2UpdateSilenceRequestTimeframes


T = TypeVar("T", bound="V2UpdateSilenceRequest")


@_attrs_define
class V2UpdateSilenceRequest:
    """
    Attributes:
        comment (str | Unset):
        enabled (bool | Unset): Applicable when type=recurring. Whether the recurring silence is active.
        ends_at (datetime.datetime | Unset): Applicable when type=one_time. End time of the silence window.
        matchers (list[SilenceMatcher] | Unset): Matchers is a slice of Matchers that is sortable, implements Stringer,
            and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        recurrence_type (V2UpdateSilenceRequestRecurrenceType | Unset): Applicable when type=recurring. Recurrence
            cadence for the silence.
            daily RecurrenceTypeDaily
            weekly RecurrenceTypeWeekly
            monthly RecurrenceTypeMonthly
        starts_at (datetime.datetime | Unset): Applicable when type=one_time. Start time of the silence window.
        timeframes (V2UpdateSilenceRequestTimeframes | Unset): Applicable when type=recurring. Map of day identifiers to
            time ranges.
        timezone (str | Unset): Applicable when type=recurring. IANA timezone for the recurrence schedule.
        type_ (V2UpdateSilenceRequestType | Unset): Optional. When set to a different type than the existing silence,
            converts between one-time and recurring.
            one_time V2SilenceTypeOneTime
            recurring V2SilenceTypeRecurring
    """

    comment: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    matchers: list[SilenceMatcher] | Unset = UNSET
    recurrence_type: V2UpdateSilenceRequestRecurrenceType | Unset = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    timeframes: V2UpdateSilenceRequestTimeframes | Unset = UNSET
    timezone: str | Unset = UNSET
    type_: V2UpdateSilenceRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        enabled = self.enabled

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        matchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matchers, Unset):
            matchers = []
            for componentsschemas_matchers_item_data in self.matchers:
                componentsschemas_matchers_item = componentsschemas_matchers_item_data.to_dict()
                matchers.append(componentsschemas_matchers_item)

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

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if recurrence_type is not UNSET:
            field_dict["recurrenceType"] = recurrence_type
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if timeframes is not UNSET:
            field_dict["timeframes"] = timeframes
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher
        from ..models.v2_update_silence_request_timeframes import V2UpdateSilenceRequestTimeframes

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        enabled = d.pop("enabled", UNSET)

        _ends_at = d.pop("endsAt", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset) or _ends_at is None:
            ends_at = UNSET
        else:
            ends_at = parse_datetime(_ends_at)

        _matchers = d.pop("matchers", UNSET)
        matchers: list[SilenceMatcher] | Unset = UNSET
        if _matchers is not UNSET:
            matchers = []
            for componentsschemas_matchers_item_data in _matchers:
                componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

                matchers.append(componentsschemas_matchers_item)

        _recurrence_type = d.pop("recurrenceType", UNSET)
        recurrence_type: V2UpdateSilenceRequestRecurrenceType | Unset
        if isinstance(_recurrence_type, Unset) or _recurrence_type is None:
            recurrence_type = UNSET
        else:
            recurrence_type = V2UpdateSilenceRequestRecurrenceType(_recurrence_type)

        _starts_at = d.pop("startsAt", UNSET)
        starts_at: datetime.datetime | Unset
        if isinstance(_starts_at, Unset) or _starts_at is None:
            starts_at = UNSET
        else:
            starts_at = parse_datetime(_starts_at)

        _timeframes = d.pop("timeframes", UNSET)
        timeframes: V2UpdateSilenceRequestTimeframes | Unset
        if isinstance(_timeframes, Unset) or _timeframes is None:
            timeframes = UNSET
        else:
            timeframes = V2UpdateSilenceRequestTimeframes.from_dict(_timeframes)

        timezone = d.pop("timezone", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: V2UpdateSilenceRequestType | Unset
        if isinstance(_type_, Unset) or _type_ is None:
            type_ = UNSET
        else:
            type_ = V2UpdateSilenceRequestType(_type_)

        v2_update_silence_request = cls(
            comment=comment,
            enabled=enabled,
            ends_at=ends_at,
            matchers=matchers,
            recurrence_type=recurrence_type,
            starts_at=starts_at,
            timeframes=timeframes,
            timezone=timezone,
            type_=type_,
        )

        v2_update_silence_request.additional_properties = d
        return v2_update_silence_request

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
