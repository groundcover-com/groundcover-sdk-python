from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_represents_a_single_preflight_validation_finding_evidence import (
        FindingRepresentsASinglePreflightValidationFindingEvidence,
    )
    from ..models.finding_represents_a_single_preflight_validation_finding_labels_used import (
        FindingRepresentsASinglePreflightValidationFindingLabelsUsed,
    )
    from ..models.subject_holds_both_datadog_and_gc_names_for_explainability import (
        SubjectHoldsBothDatadogAndGCNamesForExplainability,
    )
    from ..models.suggestion_proposes_an_alternative_for_a_missing_resource import (
        SuggestionProposesAnAlternativeForAMissingResource,
    )


T = TypeVar("T", bound="FindingRepresentsASinglePreflightValidationFinding")


@_attrs_define
class FindingRepresentsASinglePreflightValidationFinding:
    """
    Attributes:
        asset_id (str | Unset):
        asset_name (str | Unset):
        asset_type (str | Unset):
        datasource (str | Unset):
        evidence (FindingRepresentsASinglePreflightValidationFindingEvidence | Unset):
        field_name (str | Unset):
        integration (str | Unset):
        issue_type (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_values (list[str] | Unset):
        labels_used (FindingRepresentsASinglePreflightValidationFindingLabelsUsed | Unset):
        message (str | Unset):
        query_id (str | Unset):
        subject (SubjectHoldsBothDatadogAndGCNamesForExplainability | Unset):
        suggestions (list[SuggestionProposesAnAlternativeForAMissingResource] | Unset):
        values_used (list[str] | Unset):
        widget_id (str | Unset):
        widget_title (str | Unset):
    """

    asset_id: str | Unset = UNSET
    asset_name: str | Unset = UNSET
    asset_type: str | Unset = UNSET
    datasource: str | Unset = UNSET
    evidence: FindingRepresentsASinglePreflightValidationFindingEvidence | Unset = UNSET
    field_name: str | Unset = UNSET
    integration: str | Unset = UNSET
    issue_type: str | Unset = UNSET
    label_key: str | Unset = UNSET
    label_value: str | Unset = UNSET
    label_values: list[str] | Unset = UNSET
    labels_used: FindingRepresentsASinglePreflightValidationFindingLabelsUsed | Unset = UNSET
    message: str | Unset = UNSET
    query_id: str | Unset = UNSET
    subject: SubjectHoldsBothDatadogAndGCNamesForExplainability | Unset = UNSET
    suggestions: list[SuggestionProposesAnAlternativeForAMissingResource] | Unset = UNSET
    values_used: list[str] | Unset = UNSET
    widget_id: str | Unset = UNSET
    widget_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type = self.asset_type

        datasource = self.datasource

        evidence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = self.evidence.to_dict()

        field_name = self.field_name

        integration = self.integration

        issue_type = self.issue_type

        label_key = self.label_key

        label_value = self.label_value

        label_values: list[str] | Unset = UNSET
        if not isinstance(self.label_values, Unset):
            label_values = self.label_values

        labels_used: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels_used, Unset):
            labels_used = self.labels_used.to_dict()

        message = self.message

        query_id = self.query_id

        subject: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        suggestions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()
                suggestions.append(suggestions_item)

        values_used: list[str] | Unset = UNSET
        if not isinstance(self.values_used, Unset):
            values_used = self.values_used

        widget_id = self.widget_id

        widget_title = self.widget_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if integration is not UNSET:
            field_dict["integration"] = integration
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type
        if label_key is not UNSET:
            field_dict["label_key"] = label_key
        if label_value is not UNSET:
            field_dict["label_value"] = label_value
        if label_values is not UNSET:
            field_dict["label_values"] = label_values
        if labels_used is not UNSET:
            field_dict["labels_used"] = labels_used
        if message is not UNSET:
            field_dict["message"] = message
        if query_id is not UNSET:
            field_dict["query_id"] = query_id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if values_used is not UNSET:
            field_dict["values_used"] = values_used
        if widget_id is not UNSET:
            field_dict["widget_id"] = widget_id
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finding_represents_a_single_preflight_validation_finding_evidence import (
            FindingRepresentsASinglePreflightValidationFindingEvidence,
        )
        from ..models.finding_represents_a_single_preflight_validation_finding_labels_used import (
            FindingRepresentsASinglePreflightValidationFindingLabelsUsed,
        )
        from ..models.subject_holds_both_datadog_and_gc_names_for_explainability import (
            SubjectHoldsBothDatadogAndGCNamesForExplainability,
        )
        from ..models.suggestion_proposes_an_alternative_for_a_missing_resource import (
            SuggestionProposesAnAlternativeForAMissingResource,
        )

        d = dict(src_dict)
        asset_id = d.pop("asset_id", UNSET)

        asset_name = d.pop("asset_name", UNSET)

        asset_type = d.pop("asset_type", UNSET)

        datasource = d.pop("datasource", UNSET)

        _evidence = d.pop("evidence", UNSET)
        evidence: FindingRepresentsASinglePreflightValidationFindingEvidence | Unset
        if isinstance(_evidence, Unset) or _evidence is None:
            evidence = UNSET
        else:
            evidence = FindingRepresentsASinglePreflightValidationFindingEvidence.from_dict(_evidence)

        field_name = d.pop("field_name", UNSET)

        integration = d.pop("integration", UNSET)

        issue_type = d.pop("issue_type", UNSET)

        label_key = d.pop("label_key", UNSET)

        label_value = d.pop("label_value", UNSET)

        label_values = cast(list[str], d.pop("label_values", UNSET))

        _labels_used = d.pop("labels_used", UNSET)
        labels_used: FindingRepresentsASinglePreflightValidationFindingLabelsUsed | Unset
        if isinstance(_labels_used, Unset) or _labels_used is None:
            labels_used = UNSET
        else:
            labels_used = FindingRepresentsASinglePreflightValidationFindingLabelsUsed.from_dict(_labels_used)

        message = d.pop("message", UNSET)

        query_id = d.pop("query_id", UNSET)

        _subject = d.pop("subject", UNSET)
        subject: SubjectHoldsBothDatadogAndGCNamesForExplainability | Unset
        if isinstance(_subject, Unset) or _subject is None:
            subject = UNSET
        else:
            subject = SubjectHoldsBothDatadogAndGCNamesForExplainability.from_dict(_subject)

        _suggestions = d.pop("suggestions", UNSET)
        suggestions: list[SuggestionProposesAnAlternativeForAMissingResource] | Unset = UNSET
        if _suggestions is not UNSET:
            suggestions = []
            for suggestions_item_data in _suggestions:
                suggestions_item = SuggestionProposesAnAlternativeForAMissingResource.from_dict(suggestions_item_data)

                suggestions.append(suggestions_item)

        values_used = cast(list[str], d.pop("values_used", UNSET))

        widget_id = d.pop("widget_id", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        finding_represents_a_single_preflight_validation_finding = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
            datasource=datasource,
            evidence=evidence,
            field_name=field_name,
            integration=integration,
            issue_type=issue_type,
            label_key=label_key,
            label_value=label_value,
            label_values=label_values,
            labels_used=labels_used,
            message=message,
            query_id=query_id,
            subject=subject,
            suggestions=suggestions,
            values_used=values_used,
            widget_id=widget_id,
            widget_title=widget_title,
        )

        finding_represents_a_single_preflight_validation_finding.additional_properties = d
        return finding_represents_a_single_preflight_validation_finding

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
