from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CatalogInstallRequestIsTheOptionalBodyForACatalogInstall")


@_attrs_define
class CatalogInstallRequestIsTheOptionalBodyForACatalogInstall:
    """
    Attributes:
        client_id (str | Unset): Pre-registered OAuth client id. Required for entries whose auth_mode is
            `oauth_static` (servers without dynamic client registration); not accepted
            for `oauth` entries. For `token_or_oauth` entries it is optional: supply it
            to install in OAuth mode, omit it to install in token mode.
        client_secret (str | Unset): Pre-registered OAuth client secret; requires client_id. Omit for public
            clients (PKCE only).
        name (str | Unset): Optional distinct name for an additional named instance; when omitted the
            catalog entry's display name is used.
        software_statement (str | Unset): Overrides the configured DCR software statement (RFC 7591 §2.3) for this
            install. Valid only for `oauth` entries.
    """

    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    name: str | Unset = UNSET
    software_statement: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        name = self.name

        software_statement = self.software_statement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if name is not UNSET:
            field_dict["name"] = name
        if software_statement is not UNSET:
            field_dict["software_statement"] = software_statement

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
        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        name = d.pop("name", UNSET)

        software_statement = d.pop("software_statement", UNSET)

        catalog_install_request_is_the_optional_body_for_a_catalog_install = cls(
            client_id=client_id,
            client_secret=client_secret,
            name=name,
            software_statement=software_statement,
        )

        catalog_install_request_is_the_optional_body_for_a_catalog_install.additional_properties = d
        return catalog_install_request_is_the_optional_body_for_a_catalog_install

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
