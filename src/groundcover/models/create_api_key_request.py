from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CreateApiKeyRequest")


@_attrs_define
class CreateApiKeyRequest:
    """
    Attributes:
        name (str): User-defined name for the API key.
        service_account_id (str): The UUID of the service account this key belongs to.
        description (str | Unset): Optional description for the API key.
        expiration_date (datetime.datetime | Unset): Optional expiration date for the API key.
            Format: date-time
    """

    name: str
    service_account_id: str
    description: str | Unset = UNSET
    expiration_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_account_id = self.service_account_id

        description = self.description

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "serviceAccountId": service_account_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        name = d.pop("name")

        service_account_id = d.pop("serviceAccountId")

        description = d.pop("description", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.datetime | Unset
        if isinstance(_expiration_date, Unset) or _expiration_date is None:
            expiration_date = UNSET
        else:
            expiration_date = parse_datetime(_expiration_date)

        create_api_key_request = cls(
            name=name,
            service_account_id=service_account_id,
            description=description,
            expiration_date=expiration_date,
        )

        create_api_key_request.additional_properties = d
        return create_api_key_request

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
