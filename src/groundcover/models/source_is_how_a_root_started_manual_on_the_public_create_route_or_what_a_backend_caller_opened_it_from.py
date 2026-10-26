from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_is_how_a_root_started_manual_on_the_public_create_route_or_what_a_backend_caller_opened_it_from_type import (
    SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFromType,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_source_ref import InvestigationSourceRef


T = TypeVar("T", bound="SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom")


@_attrs_define
class SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom:
    """
    Attributes:
        type_ (SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFromType):
        ref (InvestigationSourceRef | Unset):
    """

    type_: SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFromType
    ref: InvestigationSourceRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_source_ref import InvestigationSourceRef

        d = dict(src_dict)
        type_ = SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFromType(d.pop("type"))

        _ref = d.pop("ref", UNSET)
        ref: InvestigationSourceRef | Unset
        if isinstance(_ref, Unset) or _ref is None:
            ref = UNSET
        else:
            ref = InvestigationSourceRef.from_dict(_ref)

        source_is_how_a_root_started_manual_on_the_public_create_route_or_what_a_backend_caller_opened_it_from = cls(
            type_=type_,
            ref=ref,
        )

        source_is_how_a_root_started_manual_on_the_public_create_route_or_what_a_backend_caller_opened_it_from.additional_properties = d
        return source_is_how_a_root_started_manual_on_the_public_create_route_or_what_a_backend_caller_opened_it_from

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
