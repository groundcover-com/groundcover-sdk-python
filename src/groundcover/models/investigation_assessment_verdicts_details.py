from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assessment_revision_names_an_assessment_at_one_revision import (
        AssessmentRevisionNamesAnAssessmentAtOneRevision,
    )


T = TypeVar("T", bound="InvestigationAssessmentVerdictsDetails")


@_attrs_define
class InvestigationAssessmentVerdictsDetails:
    """AssessmentVerdictsDetails are the INVALID_ARGUMENT details when a conclusion's verdicts don't match the node's
    open assessments.

        Attributes:
            missing (list[AssessmentRevisionNamesAnAssessmentAtOneRevision] | Unset): Open assessments without a verdict, at
                their current revision.
            stale (list[AssessmentRevisionNamesAnAssessmentAtOneRevision] | Unset): Assessments graded at an older revision,
                with their current revision.
            unexpected (list[UUID] | Unset): Graded ids that are not open assessments on the node.
    """

    missing: list[AssessmentRevisionNamesAnAssessmentAtOneRevision] | Unset = UNSET
    stale: list[AssessmentRevisionNamesAnAssessmentAtOneRevision] | Unset = UNSET
    unexpected: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        missing: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = []
            for missing_item_data in self.missing:
                missing_item = missing_item_data.to_dict()
                missing.append(missing_item)

        stale: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stale, Unset):
            stale = []
            for stale_item_data in self.stale:
                stale_item = stale_item_data.to_dict()
                stale.append(stale_item)

        unexpected: list[str] | Unset = UNSET
        if not isinstance(self.unexpected, Unset):
            unexpected = []
            for unexpected_item_data in self.unexpected:
                unexpected_item = str(unexpected_item_data)
                unexpected.append(unexpected_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if missing is not UNSET:
            field_dict["missing"] = missing
        if stale is not UNSET:
            field_dict["stale"] = stale
        if unexpected is not UNSET:
            field_dict["unexpected"] = unexpected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assessment_revision_names_an_assessment_at_one_revision import (
            AssessmentRevisionNamesAnAssessmentAtOneRevision,
        )

        d = dict(src_dict)
        _missing = d.pop("missing", UNSET)
        missing: list[AssessmentRevisionNamesAnAssessmentAtOneRevision] | Unset = UNSET
        if _missing is not UNSET:
            missing = []
            for missing_item_data in _missing:
                missing_item = AssessmentRevisionNamesAnAssessmentAtOneRevision.from_dict(missing_item_data)

                missing.append(missing_item)

        _stale = d.pop("stale", UNSET)
        stale: list[AssessmentRevisionNamesAnAssessmentAtOneRevision] | Unset = UNSET
        if _stale is not UNSET:
            stale = []
            for stale_item_data in _stale:
                stale_item = AssessmentRevisionNamesAnAssessmentAtOneRevision.from_dict(stale_item_data)

                stale.append(stale_item)

        _unexpected = d.pop("unexpected", UNSET)
        unexpected: list[UUID] | Unset = UNSET
        if _unexpected is not UNSET:
            unexpected = []
            for unexpected_item_data in _unexpected:
                unexpected_item = UUID(unexpected_item_data)

                unexpected.append(unexpected_item)

        investigation_assessment_verdicts_details = cls(
            missing=missing,
            stale=stale,
            unexpected=unexpected,
        )

        investigation_assessment_verdicts_details.additional_properties = d
        return investigation_assessment_verdicts_details

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
