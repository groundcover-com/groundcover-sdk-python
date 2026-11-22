from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs_finding_type import (
    IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsFindingType,
)

if TYPE_CHECKING:
    from ..models.issue_context_finding_contains_the_stored_query_pair_for_one_issue_occurrence import (
        IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence,
    )
    from ..models.issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs_evidence_type_0 import (
        IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0,
    )
    from ..models.issue_subject_identifies_the_subject_on_both_sides_of_the_migration import (
        IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration,
    )
    from ..models.issue_suggestion_is_a_candidate_mapping_for_a_migration_issue import (
        IssueSuggestionIsACandidateMappingForAMigrationIssue,
    )


T = TypeVar("T", bound="IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs")


@_attrs_define
class IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairs:
    """
    Attributes:
        asset_count (int):
        category (str):
        context (list[IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence]): Up to 3,000 eligible
            findings ordered by finding UUID.
        datasource (str):
        evidence (IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0 | None):
        field_name (str):
        finding_type (IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsFindingType):
        integration (str):
        issue_id (UUID):
        label_key (str):
        label_key_dd (str):
        label_value (str):
        label_value_dd (str):
        message (str):
        returned_findings (int):
        severity (str):
        subject (IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration):
        suggestions (list[IssueSuggestionIsACandidateMappingForAMigrationIssue]):
        total_findings (int): Count of all eligible findings for the issue.
        truncated (bool): True when the finding limit was reached and additional findings exist.
    """

    asset_count: int
    category: str
    context: list[IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence]
    datasource: str
    evidence: IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0 | None
    field_name: str
    finding_type: IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsFindingType
    integration: str
    issue_id: UUID
    label_key: str
    label_key_dd: str
    label_value: str
    label_value_dd: str
    message: str
    returned_findings: int
    severity: str
    subject: IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration
    suggestions: list[IssueSuggestionIsACandidateMappingForAMigrationIssue]
    total_findings: int
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs_evidence_type_0 import (
            IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0,
        )

        asset_count = self.asset_count

        category = self.category

        context = []
        for context_item_data in self.context:
            context_item = context_item_data.to_dict()
            context.append(context_item)

        datasource = self.datasource

        evidence: dict[str, Any] | None
        if isinstance(
            self.evidence, IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0
        ):
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

        returned_findings = self.returned_findings

        severity = self.severity

        subject = self.subject.to_dict()

        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        total_findings = self.total_findings

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_count": asset_count,
                "category": category,
                "context": context,
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
                "returned_findings": returned_findings,
                "severity": severity,
                "subject": subject,
                "suggestions": suggestions,
                "total_findings": total_findings,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_context_finding_contains_the_stored_query_pair_for_one_issue_occurrence import (
            IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence,
        )
        from ..models.issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs_evidence_type_0 import (
            IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0,
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

        context = []
        _context = d.pop("context")
        for context_item_data in _context:
            context_item = IssueContextFindingContainsTheStoredQueryPairForOneIssueOccurrence.from_dict(
                context_item_data
            )

            context.append(context_item)

        datasource = d.pop("datasource")

        def _parse_evidence(
            data: object,
        ) -> IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evidence_type_0 = (
                    IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0.from_dict(data)
                )

                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsEvidenceType0 | None, data
            )

        evidence = _parse_evidence(d.pop("evidence"))

        field_name = d.pop("field_name")

        finding_type = IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsFindingType(
            d.pop("finding_type")
        )

        integration = d.pop("integration")

        issue_id = UUID(d.pop("issue_id"))

        label_key = d.pop("label_key")

        label_key_dd = d.pop("label_key_dd")

        label_value = d.pop("label_value")

        label_value_dd = d.pop("label_value_dd")

        message = d.pop("message")

        returned_findings = d.pop("returned_findings")

        severity = d.pop("severity")

        subject = IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration.from_dict(d.pop("subject"))

        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = IssueSuggestionIsACandidateMappingForAMigrationIssue.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        total_findings = d.pop("total_findings")

        truncated = d.pop("truncated")

        issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs = cls(
            asset_count=asset_count,
            category=category,
            context=context,
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
            returned_findings=returned_findings,
            severity=severity,
            subject=subject,
            suggestions=suggestions,
            total_findings=total_findings,
            truncated=truncated,
        )

        issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs.additional_properties = d
        return issue_context_response_extends_the_migration_issue_with_stored_member_query_pairs

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
