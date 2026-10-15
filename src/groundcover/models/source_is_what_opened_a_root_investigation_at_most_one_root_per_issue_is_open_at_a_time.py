from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_is_what_opened_a_root_investigation_at_most_one_root_per_issue_is_open_at_a_time_type import (
    SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATimeType,
)

if TYPE_CHECKING:
    from ..models.investigation_source_ref import InvestigationSourceRef


T = TypeVar("T", bound="SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATime")


@_attrs_define
class SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATime:
    """
    Attributes:
        ref (InvestigationSourceRef):
        type_ (SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATimeType):
    """

    ref: InvestigationSourceRef
    type_: SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATimeType
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

        type_ = SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATimeType(d.pop("type"))

        source_is_what_opened_a_root_investigation_at_most_one_root_per_issue_is_open_at_a_time = cls(
            ref=ref,
            type_=type_,
        )

        source_is_what_opened_a_root_investigation_at_most_one_root_per_issue_is_open_at_a_time.additional_properties = d
        return source_is_what_opened_a_root_investigation_at_most_one_root_per_issue_is_open_at_a_time

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
