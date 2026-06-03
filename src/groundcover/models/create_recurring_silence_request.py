from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_recurring_silence_request_recurrence_type import CreateRecurringSilenceRequestRecurrenceType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_recurring_silence_request_timeframes import CreateRecurringSilenceRequestTimeframes
    from ..models.silence_matcher import SilenceMatcher


T = TypeVar("T", bound="CreateRecurringSilenceRequest")


@_attrs_define
class CreateRecurringSilenceRequest:
    """
    Attributes:
        matchers (list[SilenceMatcher]): Matchers is a slice of Matchers that is sortable, implements Stringer, and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        recurrence_type (CreateRecurringSilenceRequestRecurrenceType): Recurrence type: daily, weekly, or monthly
            daily RecurrenceTypeDaily
            weekly RecurrenceTypeWeekly
            monthly RecurrenceTypeMonthly
        timeframes (CreateRecurringSilenceRequestTimeframes): Timeframes map: keys depend on recurrenceType (every_day /
            weekday names / day-of-month strings)
        timezone (str): IANA timezone name (e.g. "America/New_York")
        comment (str | Unset): Optional comment for the recurring silence
        enabled (bool | Unset): Whether the recurring silence is enabled. Defaults to true.
    """

    matchers: list[SilenceMatcher]
    recurrence_type: CreateRecurringSilenceRequestRecurrenceType
    timeframes: CreateRecurringSilenceRequestTimeframes
    timezone: str
    comment: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matchers = []
        for componentsschemas_matchers_item_data in self.matchers:
            componentsschemas_matchers_item = componentsschemas_matchers_item_data.to_dict()
            matchers.append(componentsschemas_matchers_item)

        recurrence_type = self.recurrence_type.value

        timeframes = self.timeframes.to_dict()

        timezone = self.timezone

        comment = self.comment

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matchers": matchers,
                "recurrenceType": recurrence_type,
                "timeframes": timeframes,
                "timezone": timezone,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_recurring_silence_request_timeframes import CreateRecurringSilenceRequestTimeframes
        from ..models.silence_matcher import SilenceMatcher

        d = dict(src_dict)
        matchers = []
        _matchers = d.pop("matchers")
        for componentsschemas_matchers_item_data in _matchers:
            componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

            matchers.append(componentsschemas_matchers_item)

        recurrence_type = CreateRecurringSilenceRequestRecurrenceType(d.pop("recurrenceType"))

        timeframes = CreateRecurringSilenceRequestTimeframes.from_dict(d.pop("timeframes"))

        timezone = d.pop("timezone")

        comment = d.pop("comment", UNSET)

        enabled = d.pop("enabled", UNSET)

        create_recurring_silence_request = cls(
            matchers=matchers,
            recurrence_type=recurrence_type,
            timeframes=timeframes,
            timezone=timezone,
            comment=comment,
            enabled=enabled,
        )

        create_recurring_silence_request.additional_properties = d
        return create_recurring_silence_request

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
