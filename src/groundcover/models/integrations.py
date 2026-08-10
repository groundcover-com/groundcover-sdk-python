from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Integrations")


@_attrs_define
class Integrations:
    """
    Attributes:
        identity (str | Unset): Identity is the principal of the backend's own cloud (an AWS role ARN, a GCP
            service account email, or an Azure client id). Customers grant it access when the
            integration target lives in the same cloud as the backend.
        oidc_issuer_url (str | Unset): OIDCIssuerURL and ServiceAccountSubject describe the backend cluster's Kubernetes
            OIDC identity. They are what a customer must trust to federate an integration
            whose target is on a different cloud than the backend, where Identity is not
            usable: the customer configures their own IAM/WIF/Entra trust against this issuer
            and subject, then derives the principal to grant themselves.

            Empty when the backend's cluster has no publicly reachable OIDC issuer, in which
            case cross-cloud federation is unavailable and static credentials remain the only
            option.
        service_account_subject (str | Unset):
    """

    identity: str | Unset = UNSET
    oidc_issuer_url: str | Unset = UNSET
    service_account_subject: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity = self.identity

        oidc_issuer_url = self.oidc_issuer_url

        service_account_subject = self.service_account_subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity is not UNSET:
            field_dict["identity"] = identity
        if oidc_issuer_url is not UNSET:
            field_dict["oidc_issuer_url"] = oidc_issuer_url
        if service_account_subject is not UNSET:
            field_dict["service_account_subject"] = service_account_subject

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
        identity = d.pop("identity", UNSET)

        oidc_issuer_url = d.pop("oidc_issuer_url", UNSET)

        service_account_subject = d.pop("service_account_subject", UNSET)

        integrations = cls(
            identity=identity,
            oidc_issuer_url=oidc_issuer_url,
            service_account_subject=service_account_subject,
        )

        integrations.additional_properties = d
        return integrations

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
