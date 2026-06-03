from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SlackManifestResponseContainsTheSlackAppManifestAndAppCreationURL")


@_attrs_define
class SlackManifestResponseContainsTheSlackAppManifestAndAppCreationURL:
    """
    Attributes:
        manifest_json (str | Unset): Raw Slack app manifest JSON.
        manifest_url (str | Unset): Slack app creation URL with the manifest embedded as a query parameter.
    """

    manifest_json: str | Unset = UNSET
    manifest_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest_json = self.manifest_json

        manifest_url = self.manifest_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manifest_json is not UNSET:
            field_dict["manifest_json"] = manifest_json
        if manifest_url is not UNSET:
            field_dict["manifest_url"] = manifest_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        manifest_json = d.pop("manifest_json", UNSET)

        manifest_url = d.pop("manifest_url", UNSET)

        slack_manifest_response_contains_the_slack_app_manifest_and_app_creation_url = cls(
            manifest_json=manifest_json,
            manifest_url=manifest_url,
        )

        slack_manifest_response_contains_the_slack_app_manifest_and_app_creation_url.additional_properties = d
        return slack_manifest_response_contains_the_slack_app_manifest_and_app_creation_url

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
