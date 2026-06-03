from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TenantResponse")


@_attrs_define
class TenantResponse:
    """
    Attributes:
        clusters_limit (int | Unset):
        org_name (str | Unset):
        public (bool | Unset):
        seats (int | Unset):
        subscription (str | Unset):
        tenant_name (str | Unset):
        used (int | Unset):
    """

    clusters_limit: int | Unset = UNSET
    org_name: str | Unset = UNSET
    public: bool | Unset = UNSET
    seats: int | Unset = UNSET
    subscription: str | Unset = UNSET
    tenant_name: str | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clusters_limit = self.clusters_limit

        org_name = self.org_name

        public = self.public

        seats = self.seats

        subscription = self.subscription

        tenant_name = self.tenant_name

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clusters_limit is not UNSET:
            field_dict["ClustersLimit"] = clusters_limit
        if org_name is not UNSET:
            field_dict["OrgName"] = org_name
        if public is not UNSET:
            field_dict["Public"] = public
        if seats is not UNSET:
            field_dict["Seats"] = seats
        if subscription is not UNSET:
            field_dict["Subscription"] = subscription
        if tenant_name is not UNSET:
            field_dict["TenantName"] = tenant_name
        if used is not UNSET:
            field_dict["Used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        clusters_limit = d.pop("ClustersLimit", UNSET)

        org_name = d.pop("OrgName", UNSET)

        public = d.pop("Public", UNSET)

        seats = d.pop("Seats", UNSET)

        subscription = d.pop("Subscription", UNSET)

        tenant_name = d.pop("TenantName", UNSET)

        used = d.pop("Used", UNSET)

        tenant_response = cls(
            clusters_limit=clusters_limit,
            org_name=org_name,
            public=public,
            seats=seats,
            subscription=subscription,
            tenant_name=tenant_name,
            used=used,
        )

        tenant_response.additional_properties = d
        return tenant_response

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
