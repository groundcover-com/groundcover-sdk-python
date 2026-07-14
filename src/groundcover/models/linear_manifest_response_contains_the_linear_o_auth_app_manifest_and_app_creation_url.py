from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LinearManifestResponseContainsTheLinearOAuthAppManifestAndAppCreationURL")


@_attrs_define
class LinearManifestResponseContainsTheLinearOAuthAppManifestAndAppCreationURL:
    """
    Attributes:
        icon_url (str): Absolute icon URL embedded in the Linear OAuth app manifest.
        manifest_json (str): JSON manifest for creating the Linear OAuth app.
        manifest_url (str): Linear URL that opens the OAuth app creation form prefilled with the manifest.
    """

    icon_url: str
    manifest_json: str
    manifest_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon_url = self.icon_url

        manifest_json = self.manifest_json

        manifest_url = self.manifest_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon_url": icon_url,
                "manifest_json": manifest_json,
                "manifest_url": manifest_url,
            }
        )

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
        icon_url = d.pop("icon_url")

        manifest_json = d.pop("manifest_json")

        manifest_url = d.pop("manifest_url")

        linear_manifest_response_contains_the_linear_o_auth_app_manifest_and_app_creation_url = cls(
            icon_url=icon_url,
            manifest_json=manifest_json,
            manifest_url=manifest_url,
        )

        linear_manifest_response_contains_the_linear_o_auth_app_manifest_and_app_creation_url.additional_properties = d
        return linear_manifest_response_contains_the_linear_o_auth_app_manifest_and_app_creation_url

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
