from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_finding_suggestion_is_the_top_suggested_fix_carried_on_a_finding import (
        AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding,
    )


T = TypeVar("T", bound="AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset")


@_attrs_define
class AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset:
    """
    Attributes:
        datasource (str | Unset):
        id (str | Unset):
        message (str | Unset):
        metric (str | Unset): Metric a missing key or value belongs to.
        source_datasource (str | Unset):
        source_key (str | Unset): Key a missing value belongs to.
        source_value (str | Unset): Datadog-side value, when a tenant rule already rewrote it.
        subject (str | Unset): The missing or unsupported thing.
        suggestion (AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding | Unset):
        widget_id (str | Unset): Datadog widget the finding belongs to. Empty for monitors and asset-level findings.
        widget_title (str | Unset):
    """

    datasource: str | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    metric: str | Unset = UNSET
    source_datasource: str | Unset = UNSET
    source_key: str | Unset = UNSET
    source_value: str | Unset = UNSET
    subject: str | Unset = UNSET
    suggestion: AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding | Unset = UNSET
    widget_id: str | Unset = UNSET
    widget_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource = self.datasource

        id = self.id

        message = self.message

        metric = self.metric

        source_datasource = self.source_datasource

        source_key = self.source_key

        source_value = self.source_value

        subject = self.subject

        suggestion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggestion, Unset):
            suggestion = self.suggestion.to_dict()

        widget_id = self.widget_id

        widget_title = self.widget_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if metric is not UNSET:
            field_dict["metric"] = metric
        if source_datasource is not UNSET:
            field_dict["source_datasource"] = source_datasource
        if source_key is not UNSET:
            field_dict["source_key"] = source_key
        if source_value is not UNSET:
            field_dict["source_value"] = source_value
        if subject is not UNSET:
            field_dict["subject"] = subject
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion
        if widget_id is not UNSET:
            field_dict["widget_id"] = widget_id
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_finding_suggestion_is_the_top_suggested_fix_carried_on_a_finding import (
            AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding,
        )

        d = dict(src_dict)
        datasource = d.pop("datasource", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        metric = d.pop("metric", UNSET)

        source_datasource = d.pop("source_datasource", UNSET)

        source_key = d.pop("source_key", UNSET)

        source_value = d.pop("source_value", UNSET)

        subject = d.pop("subject", UNSET)

        _suggestion = d.pop("suggestion", UNSET)
        suggestion: AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding | Unset
        if isinstance(_suggestion, Unset) or _suggestion is None:
            suggestion = UNSET
        else:
            suggestion = AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFinding.from_dict(_suggestion)

        widget_id = d.pop("widget_id", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        asset_finding_is_one_finding_or_warning_of_an_evaluated_asset = cls(
            datasource=datasource,
            id=id,
            message=message,
            metric=metric,
            source_datasource=source_datasource,
            source_key=source_key,
            source_value=source_value,
            subject=subject,
            suggestion=suggestion,
            widget_id=widget_id,
            widget_title=widget_title,
        )

        asset_finding_is_one_finding_or_warning_of_an_evaluated_asset.additional_properties = d
        return asset_finding_is_one_finding_or_warning_of_an_evaluated_asset

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
