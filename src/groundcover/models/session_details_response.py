from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_details import EventDetails
    from ..models.session_metrics import SessionMetrics


T = TypeVar("T", bound="SessionDetailsResponse")


@_attrs_define
class SessionDetailsResponse:
    """
    Attributes:
        events (list[EventDetails] | Unset):
        metrics (SessionMetrics | Unset):
    """

    events: list[EventDetails] | Unset = UNSET
    metrics: SessionMetrics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_details import EventDetails
        from ..models.session_metrics import SessionMetrics

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[EventDetails] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = EventDetails.from_dict(events_item_data)

                events.append(events_item)

        _metrics = d.pop("metrics", UNSET)
        metrics: SessionMetrics | Unset
        if isinstance(_metrics, Unset) or _metrics is None:
            metrics = UNSET
        else:
            metrics = SessionMetrics.from_dict(_metrics)

        session_details_response = cls(
            events=events,
            metrics=metrics,
        )

        session_details_response.additional_properties = d
        return session_details_response

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
