from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin")


@_attrs_define
class InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin:
    """
    Attributes:
        investigation_id (UUID):
    """

    investigation_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investigation_id = str(self.investigation_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investigationId": investigation_id,
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
        investigation_id = UUID(d.pop("investigationId"))

        investigation_exists_details_is_the_details_of_a409investigationexists_the_root_to_join = cls(
            investigation_id=investigation_id,
        )

        investigation_exists_details_is_the_details_of_a409investigationexists_the_root_to_join.additional_properties = d
        return investigation_exists_details_is_the_details_of_a409investigationexists_the_root_to_join

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
