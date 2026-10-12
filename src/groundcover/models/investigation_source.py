from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_source_ref import InvestigationSourceRef


T = TypeVar("T", bound="InvestigationSource")


@_attrs_define
class InvestigationSource:
    """
    Attributes:
        type_ (str):
        ref (InvestigationSourceRef | Unset): JSON object whose serialized representation is at most 8192 bytes.
    """

    type_: str
    ref: InvestigationSourceRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

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
        type_ = d.pop("type")

        _ref = d.pop("ref", UNSET)
        ref: InvestigationSourceRef | Unset
        if isinstance(_ref, Unset) or _ref is None:
            ref = UNSET
        else:
            ref = InvestigationSourceRef.from_dict(_ref)

        investigation_source = cls(
            type_=type_,
            ref=ref,
        )

        investigation_source.additional_properties = d
        return investigation_source

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
