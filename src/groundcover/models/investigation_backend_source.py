from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_backend_source_type import InvestigationBackendSourceType

if TYPE_CHECKING:
    from ..models.source_ref_holds_the_fields_of_every_source_type_each_type_requires_its_own_and_refuses_the_others import (
        SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers,
    )


T = TypeVar("T", bound="InvestigationBackendSource")


@_attrs_define
class InvestigationBackendSource:
    """BackendSource is the source a backend caller opens a root from: an automation trigger, or the Slack thread whose
    Investigate button was clicked.

        Attributes:
            ref (SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers):
            type_ (InvestigationBackendSourceType):
    """

    ref: SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers
    type_: InvestigationBackendSourceType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_ref_holds_the_fields_of_every_source_type_each_type_requires_its_own_and_refuses_the_others import (
            SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers,
        )

        d = dict(src_dict)
        ref = SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers.from_dict(d.pop("ref"))

        type_ = InvestigationBackendSourceType(d.pop("type"))

        investigation_backend_source = cls(
            ref=ref,
            type_=type_,
        )

        investigation_backend_source.additional_properties = d
        return investigation_backend_source

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
