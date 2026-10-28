from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigator_run_is_the_start_of_a_roots_investigator_pending_until_agent_service_accepts_or_refuses_it_status import (
    InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesItStatus,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_error_is_agent_services_answer_to_a_refused_run_start import (
        RunErrorIsAgentServicesAnswerToARefusedRunStart,
    )


T = TypeVar("T", bound="InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesIt")


@_attrs_define
class InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesIt:
    """
    Attributes:
        status (InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesItStatus): pending
            InvestigatorPending
            started InvestigatorStarted
            failed InvestigatorFailed
        error (RunErrorIsAgentServicesAnswerToARefusedRunStart | Unset):
        finished_at (datetime.datetime | Unset): When agent-service accepted or refused the start.
    """

    status: InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesItStatus
    error: RunErrorIsAgentServicesAnswerToARefusedRunStart | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_error_is_agent_services_answer_to_a_refused_run_start import (
            RunErrorIsAgentServicesAnswerToARefusedRunStart,
        )

        d = dict(src_dict)
        status = InvestigatorRunIsTheStartOfARootsInvestigatorPendingUntilAgentServiceAcceptsOrRefusesItStatus(
            d.pop("status")
        )

        _error = d.pop("error", UNSET)
        error: RunErrorIsAgentServicesAnswerToARefusedRunStart | Unset
        if isinstance(_error, Unset) or _error is None:
            error = UNSET
        else:
            error = RunErrorIsAgentServicesAnswerToARefusedRunStart.from_dict(_error)

        _finished_at = d.pop("finishedAt", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset) or _finished_at is None:
            finished_at = UNSET
        else:
            finished_at = parse_datetime(_finished_at)

        investigator_run_is_the_start_of_a_roots_investigator_pending_until_agent_service_accepts_or_refuses_it = cls(
            status=status,
            error=error,
            finished_at=finished_at,
        )

        investigator_run_is_the_start_of_a_roots_investigator_pending_until_agent_service_accepts_or_refuses_it.additional_properties = d
        return investigator_run_is_the_start_of_a_roots_investigator_pending_until_agent_service_accepts_or_refuses_it

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
