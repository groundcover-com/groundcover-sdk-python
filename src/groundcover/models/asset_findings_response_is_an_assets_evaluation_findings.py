from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_findings_groups_are_the_findings_that_count_toward_needs_review_by_type import (
        AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType,
    )
    from ..models.asset_findings_warnings_are_shown_to_the_user_but_never_count_toward_needs_review import (
        AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview,
    )


T = TypeVar("T", bound="AssetFindingsResponseIsAnAssetsEvaluationFindings")


@_attrs_define
class AssetFindingsResponseIsAnAssetsEvaluationFindings:
    """
    Attributes:
        evaluated_at (datetime.datetime | Unset): When the asset was last evaluated. Absent when it has not been
            evaluated.
        findings (AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType | Unset):
        warnings (AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview | Unset):
    """

    evaluated_at: datetime.datetime | Unset = UNSET
    findings: AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType | Unset = UNSET
    warnings: AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluated_at: str | Unset = UNSET
        if not isinstance(self.evaluated_at, Unset):
            evaluated_at = self.evaluated_at.isoformat()

        findings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.findings, Unset):
            findings = self.findings.to_dict()

        warnings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluated_at is not UNSET:
            field_dict["evaluated_at"] = evaluated_at
        if findings is not UNSET:
            field_dict["findings"] = findings
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_findings_groups_are_the_findings_that_count_toward_needs_review_by_type import (
            AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType,
        )
        from ..models.asset_findings_warnings_are_shown_to_the_user_but_never_count_toward_needs_review import (
            AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview,
        )

        d = dict(src_dict)
        _evaluated_at = d.pop("evaluated_at", UNSET)
        evaluated_at: datetime.datetime | Unset
        if isinstance(_evaluated_at, Unset) or _evaluated_at is None:
            evaluated_at = UNSET
        else:
            evaluated_at = parse_datetime(_evaluated_at)

        _findings = d.pop("findings", UNSET)
        findings: AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType | Unset
        if isinstance(_findings, Unset) or _findings is None:
            findings = UNSET
        else:
            findings = AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType.from_dict(_findings)

        _warnings = d.pop("warnings", UNSET)
        warnings: AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview | Unset
        if isinstance(_warnings, Unset) or _warnings is None:
            warnings = UNSET
        else:
            warnings = AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview.from_dict(_warnings)

        asset_findings_response_is_an_assets_evaluation_findings = cls(
            evaluated_at=evaluated_at,
            findings=findings,
            warnings=warnings,
        )

        asset_findings_response_is_an_assets_evaluation_findings.additional_properties = d
        return asset_findings_response_is_an_assets_evaluation_findings

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
