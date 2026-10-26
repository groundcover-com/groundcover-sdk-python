from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time_type import (
    SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATimeType,
)

if TYPE_CHECKING:
    from ..models.investigation_subject_ref import InvestigationSubjectRef


T = TypeVar("T", bound="SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime")


@_attrs_define
class SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime:
    """
    Attributes:
        ref (InvestigationSubjectRef):
        type_ (SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATimeType):
    """

    ref: InvestigationSubjectRef
    type_: SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATimeType
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
        from ..models.investigation_subject_ref import InvestigationSubjectRef

        d = dict(src_dict)
        ref = InvestigationSubjectRef.from_dict(d.pop("ref"))

        type_ = SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATimeType(d.pop("type"))

        subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time = cls(
            ref=ref,
            type_=type_,
        )

        subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time.additional_properties = d
        return subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time

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
