from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionReplayVelocityRequestParamsHoldsTheQueryParametersForFetchingSessionReplayEventVelocity")


@_attrs_define
class SessionReplayVelocityRequestParamsHoldsTheQueryParametersForFetchingSessionReplayEventVelocity:
    """
    Attributes:
        bucket_duration (str): BucketDuration is the duration string for time bucketing (e.g. "1m", "5m").
        end (datetime.datetime): End of the time range to query. Must be greater than or equal to Start.
        session_id (str): SessionID is the RUM session identifier.
        start (datetime.datetime): Start of the time range to query.
    """

    bucket_duration: str
    end: datetime.datetime
    session_id: str
    start: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_duration = self.bucket_duration

        end = self.end.isoformat()

        session_id = self.session_id

        start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucketDuration": bucket_duration,
                "end": end,
                "sessionID": session_id,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        bucket_duration = d.pop("bucketDuration")

        end = parse_datetime(d.pop("end"))

        session_id = d.pop("sessionID")

        start = parse_datetime(d.pop("start"))

        session_replay_velocity_request_params_holds_the_query_parameters_for_fetching_session_replay_event_velocity = (
            cls(
                bucket_duration=bucket_duration,
                end=end,
                session_id=session_id,
                start=start,
            )
        )

        session_replay_velocity_request_params_holds_the_query_parameters_for_fetching_session_replay_event_velocity.additional_properties = d
        return (
            session_replay_velocity_request_params_holds_the_query_parameters_for_fetching_session_replay_event_velocity
        )

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
