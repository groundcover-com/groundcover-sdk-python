from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backend_source_is_the_source_a_backend_caller_opens_a_root_from_type import (
    BackendSourceIsTheSourceABackendCallerOpensARootFromType,
)

if TYPE_CHECKING:
    from ..models.investigation_source_ref import InvestigationSourceRef


T = TypeVar("T", bound="BackendSourceIsTheSourceABackendCallerOpensARootFrom")


@_attrs_define
class BackendSourceIsTheSourceABackendCallerOpensARootFrom:
    """
    Attributes:
        ref (InvestigationSourceRef):
        type_ (BackendSourceIsTheSourceABackendCallerOpensARootFromType):
    """

    ref: InvestigationSourceRef
    type_: BackendSourceIsTheSourceABackendCallerOpensARootFromType
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
        from ..models.investigation_source_ref import InvestigationSourceRef

        d = dict(src_dict)
        ref = InvestigationSourceRef.from_dict(d.pop("ref"))

        type_ = BackendSourceIsTheSourceABackendCallerOpensARootFromType(d.pop("type"))

        backend_source_is_the_source_a_backend_caller_opens_a_root_from = cls(
            ref=ref,
            type_=type_,
        )

        backend_source_is_the_source_a_backend_caller_opens_a_root_from.additional_properties = d
        return backend_source_is_the_source_a_backend_caller_opens_a_root_from

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
