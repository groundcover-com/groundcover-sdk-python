from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_finding_request_uses_signal_and_query_language_to_identify_the_mcp_tool_for_retrieving_evidence_query_language import (
    CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceQueryLanguage,
)
from ..models.create_finding_request_uses_signal_and_query_language_to_identify_the_mcp_tool_for_retrieving_evidence_signal import (
    CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceSignal,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_time_range import InvestigationTimeRange


T = TypeVar("T", bound="CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidence")


@_attrs_define
class CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidence:
    """Queryable signals require a query: metrics uses metricsql, all other queryable signals use gcql.
    Link and other findings require a URL and do not accept queries. A queryable finding may include a supplemental URL.

        Attributes:
            details (str):
            signal (CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceSignal): logs
                SignalLogs
                traces SignalTraces
                metrics SignalMetrics
                events SignalEvents
                entities SignalEntities
                issues SignalIssues
                monitors SignalMonitors
                k8s SignalK8s
                profiling SignalProfiling
                rum SignalRUM
                db_measurements SignalDBMeasurements
                link SignalLink
                other SignalOther
            query (str | Unset):
            query_language
                (CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceQueryLanguage | Unset):
            time_range (InvestigationTimeRange | Unset):
            url (str | Unset):
    """

    details: str
    signal: CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceSignal
    query: str | Unset = UNSET
    query_language: (
        CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceQueryLanguage | Unset
    ) = UNSET
    time_range: InvestigationTimeRange | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        signal = self.signal.value

        query = self.query

        query_language: str | Unset = UNSET
        if not isinstance(self.query_language, Unset):
            query_language = self.query_language.value

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "details": details,
                "signal": signal,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if query_language is not UNSET:
            field_dict["queryLanguage"] = query_language
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_time_range import InvestigationTimeRange

        d = dict(src_dict)
        details = d.pop("details")

        signal = CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceSignal(
            d.pop("signal")
        )

        query = d.pop("query", UNSET)

        _query_language = d.pop("queryLanguage", UNSET)
        query_language: (
            CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceQueryLanguage | Unset
        )
        if isinstance(_query_language, Unset) or _query_language is None:
            query_language = UNSET
        else:
            query_language = (
                CreateFindingRequestUsesSignalAndQueryLanguageToIdentifyTheMCPToolForRetrievingEvidenceQueryLanguage(
                    _query_language
                )
            )

        _time_range = d.pop("timeRange", UNSET)
        time_range: InvestigationTimeRange | Unset
        if isinstance(_time_range, Unset) or _time_range is None:
            time_range = UNSET
        else:
            time_range = InvestigationTimeRange.from_dict(_time_range)

        url = d.pop("url", UNSET)

        create_finding_request_uses_signal_and_query_language_to_identify_the_mcp_tool_for_retrieving_evidence = cls(
            details=details,
            signal=signal,
            query=query,
            query_language=query_language,
            time_range=time_range,
            url=url,
        )

        create_finding_request_uses_signal_and_query_language_to_identify_the_mcp_tool_for_retrieving_evidence.additional_properties = d
        return create_finding_request_uses_signal_and_query_language_to_identify_the_mcp_tool_for_retrieving_evidence

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
