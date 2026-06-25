from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CheckoutSessionRequest")


@_attrs_define
class CheckoutSessionRequest:
    """
    Attributes:
        billing_frequency (str | Unset):
        email (str | Unset):
        plan_name (str | Unset):
        tenant_uuid (str | Unset):
    """

    billing_frequency: str | Unset = UNSET
    email: str | Unset = UNSET
    plan_name: str | Unset = UNSET
    tenant_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_frequency = self.billing_frequency

        email = self.email

        plan_name = self.plan_name

        tenant_uuid = self.tenant_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_frequency is not UNSET:
            field_dict["billingFrequency"] = billing_frequency
        if email is not UNSET:
            field_dict["email"] = email
        if plan_name is not UNSET:
            field_dict["planName"] = plan_name
        if tenant_uuid is not UNSET:
            field_dict["tenantUUID"] = tenant_uuid

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
        billing_frequency = d.pop("billingFrequency", UNSET)

        email = d.pop("email", UNSET)

        plan_name = d.pop("planName", UNSET)

        tenant_uuid = d.pop("tenantUUID", UNSET)

        checkout_session_request = cls(
            billing_frequency=billing_frequency,
            email=email,
            plan_name=plan_name,
            tenant_uuid=tenant_uuid,
        )

        checkout_session_request.additional_properties = d
        return checkout_session_request

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
