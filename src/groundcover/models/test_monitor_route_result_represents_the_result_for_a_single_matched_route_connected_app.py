from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_monitor_route_result_represents_the_result_for_a_single_matched_route_connected_app_connected_app_type import (
    TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedAppConnectedAppType,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp")


@_attrs_define
class TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp:
    """
    Attributes:
        connected_app_id (str | Unset): The ID of the connected app that was notified
        connected_app_name (str | Unset): The name of the connected app
        connected_app_type (TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedAppConnectedAppType
            | Unset): The type of the connected app
        message (str | Unset): Optional message with details
        route_id (str | Unset): The ID of the matched notification route
        route_name (str | Unset): The name of the matched notification route
        success (bool | Unset): Whether the test notification was sent successfully
    """

    connected_app_id: str | Unset = UNSET
    connected_app_name: str | Unset = UNSET
    connected_app_type: (
        TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedAppConnectedAppType | Unset
    ) = UNSET
    message: str | Unset = UNSET
    route_id: str | Unset = UNSET
    route_name: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_app_id = self.connected_app_id

        connected_app_name = self.connected_app_name

        connected_app_type: str | Unset = UNSET
        if not isinstance(self.connected_app_type, Unset):
            connected_app_type = self.connected_app_type.value

        message = self.message

        route_id = self.route_id

        route_name = self.route_name

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_app_id is not UNSET:
            field_dict["connected_app_id"] = connected_app_id
        if connected_app_name is not UNSET:
            field_dict["connected_app_name"] = connected_app_name
        if connected_app_type is not UNSET:
            field_dict["connected_app_type"] = connected_app_type
        if message is not UNSET:
            field_dict["message"] = message
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if route_name is not UNSET:
            field_dict["route_name"] = route_name
        if success is not UNSET:
            field_dict["success"] = success

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
        connected_app_id = d.pop("connected_app_id", UNSET)

        connected_app_name = d.pop("connected_app_name", UNSET)

        _connected_app_type = d.pop("connected_app_type", UNSET)
        connected_app_type: (
            TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedAppConnectedAppType | Unset
        )
        if isinstance(_connected_app_type, Unset) or _connected_app_type is None:
            connected_app_type = UNSET
        else:
            connected_app_type = (
                TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedAppConnectedAppType(
                    _connected_app_type
                )
            )

        message = d.pop("message", UNSET)

        route_id = d.pop("route_id", UNSET)

        route_name = d.pop("route_name", UNSET)

        success = d.pop("success", UNSET)

        test_monitor_route_result_represents_the_result_for_a_single_matched_route_connected_app = cls(
            connected_app_id=connected_app_id,
            connected_app_name=connected_app_name,
            connected_app_type=connected_app_type,
            message=message,
            route_id=route_id,
            route_name=route_name,
            success=success,
        )

        test_monitor_route_result_represents_the_result_for_a_single_matched_route_connected_app.additional_properties = d
        return test_monitor_route_result_represents_the_result_for_a_single_matched_route_connected_app

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
