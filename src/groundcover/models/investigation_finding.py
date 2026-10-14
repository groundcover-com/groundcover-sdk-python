from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_finding_query_language import InvestigationFindingQueryLanguage
from ..models.investigation_finding_signal import InvestigationFindingSignal
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_retraction import FindingRetraction
    from ..models.investigation_author import InvestigationAuthor
    from ..models.investigation_time_range import InvestigationTimeRange


T = TypeVar("T", bound="InvestigationFinding")


@_attrs_define
class InvestigationFinding:
    """
    Attributes:
        details (str):
        signal (InvestigationFindingSignal): logs SignalLogs
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
        created_at (datetime.datetime | Unset):
        created_by (InvestigationAuthor | Unset):
        id (UUID | Unset):
        investigation_id (UUID | Unset):
        query (str | Unset):
        query_language (InvestigationFindingQueryLanguage | Unset):
        retracted (FindingRetraction | Unset):
        time_range (InvestigationTimeRange | Unset):
        url (str | Unset):
    """

    details: str
    signal: InvestigationFindingSignal
    created_at: datetime.datetime | Unset = UNSET
    created_by: InvestigationAuthor | Unset = UNSET
    id: UUID | Unset = UNSET
    investigation_id: UUID | Unset = UNSET
    query: str | Unset = UNSET
    query_language: InvestigationFindingQueryLanguage | Unset = UNSET
    retracted: FindingRetraction | Unset = UNSET
    time_range: InvestigationTimeRange | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        signal = self.signal.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        investigation_id: str | Unset = UNSET
        if not isinstance(self.investigation_id, Unset):
            investigation_id = str(self.investigation_id)

        query = self.query

        query_language: str | Unset = UNSET
        if not isinstance(self.query_language, Unset):
            query_language = self.query_language.value

        retracted: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retracted, Unset):
            retracted = self.retracted.to_dict()

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if investigation_id is not UNSET:
            field_dict["investigationId"] = investigation_id
        if query is not UNSET:
            field_dict["query"] = query
        if query_language is not UNSET:
            field_dict["queryLanguage"] = query_language
        if retracted is not UNSET:
            field_dict["retracted"] = retracted
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finding_retraction import FindingRetraction
        from ..models.investigation_author import InvestigationAuthor
        from ..models.investigation_time_range import InvestigationTimeRange

        d = dict(src_dict)
        details = d.pop("details")

        signal = InvestigationFindingSignal(d.pop("signal"))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        _created_by = d.pop("createdBy", UNSET)
        created_by: InvestigationAuthor | Unset
        if isinstance(_created_by, Unset) or _created_by is None:
            created_by = UNSET
        else:
            created_by = InvestigationAuthor.from_dict(_created_by)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset) or _id is None:
            id = UNSET
        else:
            id = UUID(_id)

        _investigation_id = d.pop("investigationId", UNSET)
        investigation_id: UUID | Unset
        if isinstance(_investigation_id, Unset) or _investigation_id is None:
            investigation_id = UNSET
        else:
            investigation_id = UUID(_investigation_id)

        query = d.pop("query", UNSET)

        _query_language = d.pop("queryLanguage", UNSET)
        query_language: InvestigationFindingQueryLanguage | Unset
        if isinstance(_query_language, Unset) or _query_language is None:
            query_language = UNSET
        else:
            query_language = InvestigationFindingQueryLanguage(_query_language)

        _retracted = d.pop("retracted", UNSET)
        retracted: FindingRetraction | Unset
        if isinstance(_retracted, Unset) or _retracted is None:
            retracted = UNSET
        else:
            retracted = FindingRetraction.from_dict(_retracted)

        _time_range = d.pop("timeRange", UNSET)
        time_range: InvestigationTimeRange | Unset
        if isinstance(_time_range, Unset) or _time_range is None:
            time_range = UNSET
        else:
            time_range = InvestigationTimeRange.from_dict(_time_range)

        url = d.pop("url", UNSET)

        investigation_finding = cls(
            details=details,
            signal=signal,
            created_at=created_at,
            created_by=created_by,
            id=id,
            investigation_id=investigation_id,
            query=query,
            query_language=query_language,
            retracted=retracted,
            time_range=time_range,
            url=url,
        )

        investigation_finding.additional_properties = d
        return investigation_finding

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
