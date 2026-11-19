from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count_finding_type import (
    IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountFindingType,
)

if TYPE_CHECKING:
    from ..models.issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count_evidence_type_0 import (
        IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0,
    )
    from ..models.issue_subject_identifies_the_subject_on_both_sides_of_the_migration import (
        IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration,
    )
    from ..models.issue_suggestion_is_a_candidate_mapping_for_a_migration_issue import (
        IssueSuggestionIsACandidateMappingForAMigrationIssue,
    )


T = TypeVar("T", bound="IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount")


@_attrs_define
class IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount:
    """
    Attributes:
        asset_count (int):
        category (str):
        datasource (str):
        evidence (IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0 | None):
        field_name (str):
        finding_type (IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountFindingType):
        integration (str):
        issue_id (UUID):
        label_key (str):
        label_key_dd (str):
        label_value (str):
        label_value_dd (str):
        message (str):
        severity (str):
        subject (IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration):
        suggestions (list[IssueSuggestionIsACandidateMappingForAMigrationIssue]):
    """

    asset_count: int
    category: str
    datasource: str
    evidence: IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0 | None
    field_name: str
    finding_type: IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountFindingType
    integration: str
    issue_id: UUID
    label_key: str
    label_key_dd: str
    label_value: str
    label_value_dd: str
    message: str
    severity: str
    subject: IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration
    suggestions: list[IssueSuggestionIsACandidateMappingForAMigrationIssue]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count_evidence_type_0 import (
            IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0,
        )

        asset_count = self.asset_count

        category = self.category

        datasource = self.datasource

        evidence: dict[str, Any] | None
        if isinstance(self.evidence, IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0):
            evidence = self.evidence.to_dict()
        else:
            evidence = self.evidence

        field_name = self.field_name

        finding_type = self.finding_type.value

        integration = self.integration

        issue_id = str(self.issue_id)

        label_key = self.label_key

        label_key_dd = self.label_key_dd

        label_value = self.label_value

        label_value_dd = self.label_value_dd

        message = self.message

        severity = self.severity

        subject = self.subject.to_dict()

        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_count": asset_count,
                "category": category,
                "datasource": datasource,
                "evidence": evidence,
                "field_name": field_name,
                "finding_type": finding_type,
                "integration": integration,
                "issue_id": issue_id,
                "label_key": label_key,
                "label_key_dd": label_key_dd,
                "label_value": label_value,
                "label_value_dd": label_value_dd,
                "message": message,
                "severity": severity,
                "subject": subject,
                "suggestions": suggestions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count_evidence_type_0 import (
            IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0,
        )
        from ..models.issue_subject_identifies_the_subject_on_both_sides_of_the_migration import (
            IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration,
        )
        from ..models.issue_suggestion_is_a_candidate_mapping_for_a_migration_issue import (
            IssueSuggestionIsACandidateMappingForAMigrationIssue,
        )

        d = dict(src_dict)
        asset_count = d.pop("asset_count")

        category = d.pop("category")

        datasource = d.pop("datasource")

        def _parse_evidence(
            data: object,
        ) -> IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evidence_type_0 = IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0.from_dict(
                    data
                )

                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountEvidenceType0 | None, data)

        evidence = _parse_evidence(d.pop("evidence"))

        field_name = d.pop("field_name")

        finding_type = IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCountFindingType(d.pop("finding_type"))

        integration = d.pop("integration")

        issue_id = UUID(d.pop("issue_id"))

        label_key = d.pop("label_key")

        label_key_dd = d.pop("label_key_dd")

        label_value = d.pop("label_value")

        label_value_dd = d.pop("label_value_dd")

        message = d.pop("message")

        severity = d.pop("severity")

        subject = IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration.from_dict(d.pop("subject"))

        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = IssueSuggestionIsACandidateMappingForAMigrationIssue.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count = cls(
            asset_count=asset_count,
            category=category,
            datasource=datasource,
            evidence=evidence,
            field_name=field_name,
            finding_type=finding_type,
            integration=integration,
            issue_id=issue_id,
            label_key=label_key,
            label_key_dd=label_key_dd,
            label_value=label_value,
            label_value_dd=label_value_dd,
            message=message,
            severity=severity,
            subject=subject,
            suggestions=suggestions,
        )

        issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count.additional_properties = d
        return issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count

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
