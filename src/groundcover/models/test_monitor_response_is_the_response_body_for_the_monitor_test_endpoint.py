from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_monitor_route_result_represents_the_result_for_a_single_matched_route_connected_app import (
        TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp,
    )


T = TypeVar("T", bound="TestMonitorResponseIsTheResponseBodyForTheMonitorTestEndpoint")


@_attrs_define
class TestMonitorResponseIsTheResponseBodyForTheMonitorTestEndpoint:
    """
    Attributes:
        matched_routes (list[TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp] | Unset):
            Results for each matched route + connected app combination
    """

    matched_routes: list[TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched_routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matched_routes, Unset):
            matched_routes = []
            for matched_routes_item_data in self.matched_routes:
                matched_routes_item = matched_routes_item_data.to_dict()
                matched_routes.append(matched_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matched_routes is not UNSET:
            field_dict["matched_routes"] = matched_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_monitor_route_result_represents_the_result_for_a_single_matched_route_connected_app import (
            TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp,
        )

        d = dict(src_dict)
        _matched_routes = d.pop("matched_routes", UNSET)
        matched_routes: list[TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp] | Unset = (
            UNSET
        )
        if _matched_routes is not UNSET:
            matched_routes = []
            for matched_routes_item_data in _matched_routes:
                matched_routes_item = (
                    TestMonitorRouteResultRepresentsTheResultForASingleMatchedRouteConnectedApp.from_dict(
                        matched_routes_item_data
                    )
                )

                matched_routes.append(matched_routes_item)

        test_monitor_response_is_the_response_body_for_the_monitor_test_endpoint = cls(
            matched_routes=matched_routes,
        )

        test_monitor_response_is_the_response_body_for_the_monitor_test_endpoint.additional_properties = d
        return test_monitor_response_is_the_response_body_for_the_monitor_test_endpoint

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
