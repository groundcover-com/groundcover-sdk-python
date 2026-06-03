from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectionConfiguration")


@_attrs_define
class ConnectionConfiguration:
    """
    Attributes:
        api_key (str): The API key.
        site (str): The site identifier. For Datadog: "us1", "us3", "us5", "eu1", "ap1", "us1-fed". For Coralogix:
            "us1", "us2", "eu1", "eu2", "ap1", "ap2".
        application_key (str | Unset): The Application key (required for Datadog, not used for Coralogix).
    """

    api_key: str
    site: str
    application_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        site = self.site

        application_key = self.application_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "site": site,
            }
        )
        if application_key is not UNSET:
            field_dict["applicationKey"] = application_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        site = d.pop("site")

        application_key = d.pop("applicationKey", UNSET)

        connection_configuration = cls(
            api_key=api_key,
            site=site,
            application_key=application_key,
        )

        connection_configuration.additional_properties = d
        return connection_configuration

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
