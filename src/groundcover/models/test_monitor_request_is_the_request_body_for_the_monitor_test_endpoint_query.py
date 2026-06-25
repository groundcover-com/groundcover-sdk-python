from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery")


@_attrs_define
class TestMonitorRequestIsTheRequestBodyForTheMonitorTestEndpointQuery:
    """Query metadata from the monitor definition.
    Keys match template variables: expression, data_type, instant_rollup.

        Example:
            {'data_type': 'logs', 'expression': '* | stats count()', 'instant_rollup': '5m'}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

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
        test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_query = cls()

        test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_query.additional_properties = d
        return test_monitor_request_is_the_request_body_for_the_monitor_test_endpoint_query

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
