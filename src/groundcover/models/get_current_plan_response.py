from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="GetCurrentPlanResponse")


@_attrs_define
class GetCurrentPlanResponse:
    """
    Attributes:
        billing_frequency (str | Unset):
        has_denied_users (bool | Unset):
        is_current_user_denied (bool | Unset):
        seats (int | Unset):
        subscription (str | Unset):
        trial_enabled (bool | Unset):
        trial_end_date (datetime.datetime | Unset):
        trial_start_date (datetime.datetime | Unset):
        used (int | Unset):
    """

    billing_frequency: str | Unset = UNSET
    has_denied_users: bool | Unset = UNSET
    is_current_user_denied: bool | Unset = UNSET
    seats: int | Unset = UNSET
    subscription: str | Unset = UNSET
    trial_enabled: bool | Unset = UNSET
    trial_end_date: datetime.datetime | Unset = UNSET
    trial_start_date: datetime.datetime | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_frequency = self.billing_frequency

        has_denied_users = self.has_denied_users

        is_current_user_denied = self.is_current_user_denied

        seats = self.seats

        subscription = self.subscription

        trial_enabled = self.trial_enabled

        trial_end_date: str | Unset = UNSET
        if not isinstance(self.trial_end_date, Unset):
            trial_end_date = self.trial_end_date.isoformat()

        trial_start_date: str | Unset = UNSET
        if not isinstance(self.trial_start_date, Unset):
            trial_start_date = self.trial_start_date.isoformat()

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_frequency is not UNSET:
            field_dict["billingFrequency"] = billing_frequency
        if has_denied_users is not UNSET:
            field_dict["hasDeniedUsers"] = has_denied_users
        if is_current_user_denied is not UNSET:
            field_dict["isCurrentUserDenied"] = is_current_user_denied
        if seats is not UNSET:
            field_dict["seats"] = seats
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if trial_enabled is not UNSET:
            field_dict["trialEnabled"] = trial_enabled
        if trial_end_date is not UNSET:
            field_dict["trialEndDate"] = trial_end_date
        if trial_start_date is not UNSET:
            field_dict["trialStartDate"] = trial_start_date
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        billing_frequency = d.pop("billingFrequency", UNSET)

        has_denied_users = d.pop("hasDeniedUsers", UNSET)

        is_current_user_denied = d.pop("isCurrentUserDenied", UNSET)

        seats = d.pop("seats", UNSET)

        subscription = d.pop("subscription", UNSET)

        trial_enabled = d.pop("trialEnabled", UNSET)

        _trial_end_date = d.pop("trialEndDate", UNSET)
        trial_end_date: datetime.datetime | Unset
        if isinstance(_trial_end_date, Unset) or _trial_end_date is None:
            trial_end_date = UNSET
        else:
            trial_end_date = parse_datetime(_trial_end_date)

        _trial_start_date = d.pop("trialStartDate", UNSET)
        trial_start_date: datetime.datetime | Unset
        if isinstance(_trial_start_date, Unset) or _trial_start_date is None:
            trial_start_date = UNSET
        else:
            trial_start_date = parse_datetime(_trial_start_date)

        used = d.pop("used", UNSET)

        get_current_plan_response = cls(
            billing_frequency=billing_frequency,
            has_denied_users=has_denied_users,
            is_current_user_denied=is_current_user_denied,
            seats=seats,
            subscription=subscription,
            trial_enabled=trial_enabled,
            trial_end_date=trial_end_date,
            trial_start_date=trial_start_date,
            used=used,
        )

        get_current_plan_response.additional_properties = d
        return get_current_plan_response

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
