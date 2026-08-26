from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    """
    Attributes:
        app_version (str | Unset): AppVersion is the mobile application version. Empty for web sessions, which
            report ReleaseID instead.
        browser (str | Unset):
        country (str | Unset):
        device_brand (str | Unset):
        device_model (str | Unset):
        duration_milli (int | Unset):
        end_time (datetime.datetime | Unset):
        has_session_replay (int | Unset):
        is_mobile (str | Unset):
        os_name (str | Unset): Mobile RUM. Empty for web sessions, which report browser.* instead. The client
            platform is not returned: it is a filter dimension only.
        os_version (str | Unset):
        page_count (int | Unset):
        release_id (str | Unset):
        service_name (str | Unset):
        session_errors (int | Unset):
        session_id (str | Unset):
        start_time (datetime.datetime | Unset):
        user_email (str | Unset):
        user_id (str | Unset):
        user_organization (str | Unset):
    """

    app_version: str | Unset = UNSET
    browser: str | Unset = UNSET
    country: str | Unset = UNSET
    device_brand: str | Unset = UNSET
    device_model: str | Unset = UNSET
    duration_milli: int | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    has_session_replay: int | Unset = UNSET
    is_mobile: str | Unset = UNSET
    os_name: str | Unset = UNSET
    os_version: str | Unset = UNSET
    page_count: int | Unset = UNSET
    release_id: str | Unset = UNSET
    service_name: str | Unset = UNSET
    session_errors: int | Unset = UNSET
    session_id: str | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    user_email: str | Unset = UNSET
    user_id: str | Unset = UNSET
    user_organization: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_version = self.app_version

        browser = self.browser

        country = self.country

        device_brand = self.device_brand

        device_model = self.device_model

        duration_milli = self.duration_milli

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        has_session_replay = self.has_session_replay

        is_mobile = self.is_mobile

        os_name = self.os_name

        os_version = self.os_version

        page_count = self.page_count

        release_id = self.release_id

        service_name = self.service_name

        session_errors = self.session_errors

        session_id = self.session_id

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        user_email = self.user_email

        user_id = self.user_id

        user_organization = self.user_organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if browser is not UNSET:
            field_dict["browser"] = browser
        if country is not UNSET:
            field_dict["country"] = country
        if device_brand is not UNSET:
            field_dict["deviceBrand"] = device_brand
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if duration_milli is not UNSET:
            field_dict["durationMilli"] = duration_milli
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if has_session_replay is not UNSET:
            field_dict["hasSessionReplay"] = has_session_replay
        if is_mobile is not UNSET:
            field_dict["isMobile"] = is_mobile
        if os_name is not UNSET:
            field_dict["osName"] = os_name
        if os_version is not UNSET:
            field_dict["osVersion"] = os_version
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if session_errors is not UNSET:
            field_dict["sessionErrors"] = session_errors
        if session_id is not UNSET:
            field_dict["sessionID"] = session_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_organization is not UNSET:
            field_dict["userOrganization"] = user_organization

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
        app_version = d.pop("appVersion", UNSET)

        browser = d.pop("browser", UNSET)

        country = d.pop("country", UNSET)

        device_brand = d.pop("deviceBrand", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        duration_milli = d.pop("durationMilli", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset) or _end_time is None:
            end_time = UNSET
        else:
            end_time = parse_datetime(_end_time)

        has_session_replay = d.pop("hasSessionReplay", UNSET)

        is_mobile = d.pop("isMobile", UNSET)

        os_name = d.pop("osName", UNSET)

        os_version = d.pop("osVersion", UNSET)

        page_count = d.pop("pageCount", UNSET)

        release_id = d.pop("releaseId", UNSET)

        service_name = d.pop("serviceName", UNSET)

        session_errors = d.pop("sessionErrors", UNSET)

        session_id = d.pop("sessionID", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset) or _start_time is None:
            start_time = UNSET
        else:
            start_time = parse_datetime(_start_time)

        user_email = d.pop("userEmail", UNSET)

        user_id = d.pop("userId", UNSET)

        user_organization = d.pop("userOrganization", UNSET)

        session = cls(
            app_version=app_version,
            browser=browser,
            country=country,
            device_brand=device_brand,
            device_model=device_model,
            duration_milli=duration_milli,
            end_time=end_time,
            has_session_replay=has_session_replay,
            is_mobile=is_mobile,
            os_name=os_name,
            os_version=os_version,
            page_count=page_count,
            release_id=release_id,
            service_name=service_name,
            session_errors=session_errors,
            session_id=session_id,
            start_time=start_time,
            user_email=user_email,
            user_id=user_id,
            user_organization=user_organization,
        )

        session.additional_properties = d
        return session

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
