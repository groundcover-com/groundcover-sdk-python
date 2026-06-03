from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TracesErrorVelocityPeak")


@_attrs_define
class TracesErrorVelocityPeak:
    """
    Attributes:
        anomaly_error_trace_count (int | Unset):
        anomaly_normalized_score (float | Unset):
        anomaly_points_count (int | Unset):
        anomaly_rolling_q9 (float | Unset):
        anomaly_rolling_q25 (float | Unset):
        anomaly_rolling_q75 (float | Unset):
        anomaly_score (float | Unset):
        anomaly_score_mean (float | Unset):
        anomaly_score_std (float | Unset):
        anomaly_timestamp (datetime.datetime | Unset):
        cluster (str | Unset):
        container_name (str | Unset):
        env (str | Unset):
        namespace (str | Unset):
        role (str | Unset):
        span_type (str | Unset):
        status_code (str | Unset):
        workload (str | Unset):
    """

    anomaly_error_trace_count: int | Unset = UNSET
    anomaly_normalized_score: float | Unset = UNSET
    anomaly_points_count: int | Unset = UNSET
    anomaly_rolling_q9: float | Unset = UNSET
    anomaly_rolling_q25: float | Unset = UNSET
    anomaly_rolling_q75: float | Unset = UNSET
    anomaly_score: float | Unset = UNSET
    anomaly_score_mean: float | Unset = UNSET
    anomaly_score_std: float | Unset = UNSET
    anomaly_timestamp: datetime.datetime | Unset = UNSET
    cluster: str | Unset = UNSET
    container_name: str | Unset = UNSET
    env: str | Unset = UNSET
    namespace: str | Unset = UNSET
    role: str | Unset = UNSET
    span_type: str | Unset = UNSET
    status_code: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_error_trace_count = self.anomaly_error_trace_count

        anomaly_normalized_score = self.anomaly_normalized_score

        anomaly_points_count = self.anomaly_points_count

        anomaly_rolling_q9 = self.anomaly_rolling_q9

        anomaly_rolling_q25 = self.anomaly_rolling_q25

        anomaly_rolling_q75 = self.anomaly_rolling_q75

        anomaly_score = self.anomaly_score

        anomaly_score_mean = self.anomaly_score_mean

        anomaly_score_std = self.anomaly_score_std

        anomaly_timestamp: str | Unset = UNSET
        if not isinstance(self.anomaly_timestamp, Unset):
            anomaly_timestamp = self.anomaly_timestamp.isoformat()

        cluster = self.cluster

        container_name = self.container_name

        env = self.env

        namespace = self.namespace

        role = self.role

        span_type = self.span_type

        status_code = self.status_code

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly_error_trace_count is not UNSET:
            field_dict["anomaly_error_trace_count"] = anomaly_error_trace_count
        if anomaly_normalized_score is not UNSET:
            field_dict["anomaly_normalized_score"] = anomaly_normalized_score
        if anomaly_points_count is not UNSET:
            field_dict["anomaly_points_count"] = anomaly_points_count
        if anomaly_rolling_q9 is not UNSET:
            field_dict["anomaly_rolling_q9"] = anomaly_rolling_q9
        if anomaly_rolling_q25 is not UNSET:
            field_dict["anomaly_rolling_q25"] = anomaly_rolling_q25
        if anomaly_rolling_q75 is not UNSET:
            field_dict["anomaly_rolling_q75"] = anomaly_rolling_q75
        if anomaly_score is not UNSET:
            field_dict["anomaly_score"] = anomaly_score
        if anomaly_score_mean is not UNSET:
            field_dict["anomaly_score_mean"] = anomaly_score_mean
        if anomaly_score_std is not UNSET:
            field_dict["anomaly_score_std"] = anomaly_score_std
        if anomaly_timestamp is not UNSET:
            field_dict["anomaly_timestamp"] = anomaly_timestamp
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if container_name is not UNSET:
            field_dict["container_name"] = container_name
        if env is not UNSET:
            field_dict["env"] = env
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if role is not UNSET:
            field_dict["role"] = role
        if span_type is not UNSET:
            field_dict["span_type"] = span_type
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        anomaly_error_trace_count = d.pop("anomaly_error_trace_count", UNSET)

        anomaly_normalized_score = d.pop("anomaly_normalized_score", UNSET)

        anomaly_points_count = d.pop("anomaly_points_count", UNSET)

        anomaly_rolling_q9 = d.pop("anomaly_rolling_q9", UNSET)

        anomaly_rolling_q25 = d.pop("anomaly_rolling_q25", UNSET)

        anomaly_rolling_q75 = d.pop("anomaly_rolling_q75", UNSET)

        anomaly_score = d.pop("anomaly_score", UNSET)

        anomaly_score_mean = d.pop("anomaly_score_mean", UNSET)

        anomaly_score_std = d.pop("anomaly_score_std", UNSET)

        _anomaly_timestamp = d.pop("anomaly_timestamp", UNSET)
        anomaly_timestamp: datetime.datetime | Unset
        if isinstance(_anomaly_timestamp, Unset) or _anomaly_timestamp is None:
            anomaly_timestamp = UNSET
        else:
            anomaly_timestamp = parse_datetime(_anomaly_timestamp)

        cluster = d.pop("cluster", UNSET)

        container_name = d.pop("container_name", UNSET)

        env = d.pop("env", UNSET)

        namespace = d.pop("namespace", UNSET)

        role = d.pop("role", UNSET)

        span_type = d.pop("span_type", UNSET)

        status_code = d.pop("status_code", UNSET)

        workload = d.pop("workload", UNSET)

        traces_error_velocity_peak = cls(
            anomaly_error_trace_count=anomaly_error_trace_count,
            anomaly_normalized_score=anomaly_normalized_score,
            anomaly_points_count=anomaly_points_count,
            anomaly_rolling_q9=anomaly_rolling_q9,
            anomaly_rolling_q25=anomaly_rolling_q25,
            anomaly_rolling_q75=anomaly_rolling_q75,
            anomaly_score=anomaly_score,
            anomaly_score_mean=anomaly_score_mean,
            anomaly_score_std=anomaly_score_std,
            anomaly_timestamp=anomaly_timestamp,
            cluster=cluster,
            container_name=container_name,
            env=env,
            namespace=namespace,
            role=role,
            span_type=span_type,
            status_code=status_code,
            workload=workload,
        )

        traces_error_velocity_peak.additional_properties = d
        return traces_error_velocity_peak

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
