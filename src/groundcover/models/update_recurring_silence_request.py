from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_recurring_silence_request_recurrence_type import UpdateRecurringSilenceRequestRecurrenceType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.silence_matcher import SilenceMatcher
    from ..models.update_recurring_silence_request_timeframes import UpdateRecurringSilenceRequestTimeframes


T = TypeVar("T", bound="UpdateRecurringSilenceRequest")


@_attrs_define
class UpdateRecurringSilenceRequest:
    """
    Attributes:
        comment (str | Unset):
        enabled (bool | Unset):
        matchers (list[SilenceMatcher] | Unset): Matchers is a slice of Matchers that is sortable, implements Stringer,
            and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        recurrence_type (UpdateRecurringSilenceRequestRecurrenceType | Unset):
        timeframes (UpdateRecurringSilenceRequestTimeframes | Unset):
        timezone (str | Unset):
    """

    comment: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    matchers: list[SilenceMatcher] | Unset = UNSET
    recurrence_type: UpdateRecurringSilenceRequestRecurrenceType | Unset = UNSET
    timeframes: UpdateRecurringSilenceRequestTimeframes | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        enabled = self.enabled

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if recurrence_type is not UNSET:
            field_dict["recurrenceType"] = recurrence_type
        if timeframes is not UNSET:
            field_dict["timeframes"] = timeframes
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher
        from ..models.update_recurring_silence_request_timeframes import UpdateRecurringSilenceRequestTimeframes

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        enabled = d.pop("enabled", UNSET)

        _matchers = d.pop("matchers", UNSET)
        matchers: list[SilenceMatcher] | Unset = UNSET
        if _matchers is not UNSET:
            matchers = []
            for componentsschemas_matchers_item_data in _matchers:
                componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

                matchers.append(componentsschemas_matchers_item)

        _recurrence_type = d.pop("recurrenceType", UNSET)
        recurrence_type: UpdateRecurringSilenceRequestRecurrenceType | Unset
        if isinstance(_recurrence_type, Unset) or _recurrence_type is None:
            recurrence_type = UNSET
        else:
            recurrence_type = UpdateRecurringSilenceRequestRecurrenceType(_recurrence_type)

        _timeframes = d.pop("timeframes", UNSET)
        timeframes: UpdateRecurringSilenceRequestTimeframes | Unset
        if isinstance(_timeframes, Unset) or _timeframes is None:
            timeframes = UNSET
        else:
            timeframes = UpdateRecurringSilenceRequestTimeframes.from_dict(_timeframes)

        timezone = d.pop("timezone", UNSET)

        update_recurring_silence_request = cls(
            comment=comment,
            enabled=enabled,
            matchers=matchers,
            recurrence_type=recurrence_type,
            timeframes=timeframes,
            timezone=timezone,
        )

        update_recurring_silence_request.additional_properties = d
        return update_recurring_silence_request

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
