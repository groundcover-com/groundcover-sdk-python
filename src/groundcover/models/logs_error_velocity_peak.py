from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LogsErrorVelocityPeak")


@_attrs_define
class LogsErrorVelocityPeak:
    """
    Attributes:
        anomaly_error_log_count (int | Unset):
        anomaly_normalized_score (float | Unset):
        anomaly_points_count (int | Unset):
        anomaly_rolling_q25 (float | Unset):
        anomaly_rolling_q75 (float | Unset):
        anomaly_score (float | Unset):
        anomaly_score_mean (float | Unset):
        anomaly_score_std (float | Unset):
        anomaly_timestamp (datetime.datetime | Unset):
        avg_anomaly_score (float | Unset):
        cluster (str | Unset):
        container (str | Unset):
        env (str | Unset):
        namespace (str | Unset):
        std_anomaly_score (float | Unset):
        workload (str | Unset):
    """

    anomaly_error_log_count: int | Unset = UNSET
    anomaly_normalized_score: float | Unset = UNSET
    anomaly_points_count: int | Unset = UNSET
    anomaly_rolling_q25: float | Unset = UNSET
    anomaly_rolling_q75: float | Unset = UNSET
    anomaly_score: float | Unset = UNSET
    anomaly_score_mean: float | Unset = UNSET
    anomaly_score_std: float | Unset = UNSET
    anomaly_timestamp: datetime.datetime | Unset = UNSET
    avg_anomaly_score: float | Unset = UNSET
    cluster: str | Unset = UNSET
    container: str | Unset = UNSET
    env: str | Unset = UNSET
    namespace: str | Unset = UNSET
    std_anomaly_score: float | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_error_log_count = self.anomaly_error_log_count

        anomaly_normalized_score = self.anomaly_normalized_score

        anomaly_points_count = self.anomaly_points_count

        anomaly_rolling_q25 = self.anomaly_rolling_q25

        anomaly_rolling_q75 = self.anomaly_rolling_q75

        anomaly_score = self.anomaly_score

        anomaly_score_mean = self.anomaly_score_mean

        anomaly_score_std = self.anomaly_score_std

        anomaly_timestamp: str | Unset = UNSET
        if not isinstance(self.anomaly_timestamp, Unset):
            anomaly_timestamp = self.anomaly_timestamp.isoformat()

        avg_anomaly_score = self.avg_anomaly_score

        cluster = self.cluster

        container = self.container

        env = self.env

        namespace = self.namespace

        std_anomaly_score = self.std_anomaly_score

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly_error_log_count is not UNSET:
            field_dict["anomaly_error_log_count"] = anomaly_error_log_count
        if anomaly_normalized_score is not UNSET:
            field_dict["anomaly_normalized_score"] = anomaly_normalized_score
        if anomaly_points_count is not UNSET:
            field_dict["anomaly_points_count"] = anomaly_points_count
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
        if avg_anomaly_score is not UNSET:
            field_dict["avg_anomaly_score"] = avg_anomaly_score
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if container is not UNSET:
            field_dict["container"] = container
        if env is not UNSET:
            field_dict["env"] = env
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if std_anomaly_score is not UNSET:
            field_dict["std_anomaly_score"] = std_anomaly_score
        if workload is not UNSET:
            field_dict["workload"] = workload

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
        anomaly_error_log_count = d.pop("anomaly_error_log_count", UNSET)

        anomaly_normalized_score = d.pop("anomaly_normalized_score", UNSET)

        anomaly_points_count = d.pop("anomaly_points_count", UNSET)

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

        avg_anomaly_score = d.pop("avg_anomaly_score", UNSET)

        cluster = d.pop("cluster", UNSET)

        container = d.pop("container", UNSET)

        env = d.pop("env", UNSET)

        namespace = d.pop("namespace", UNSET)

        std_anomaly_score = d.pop("std_anomaly_score", UNSET)

        workload = d.pop("workload", UNSET)

        logs_error_velocity_peak = cls(
            anomaly_error_log_count=anomaly_error_log_count,
            anomaly_normalized_score=anomaly_normalized_score,
            anomaly_points_count=anomaly_points_count,
            anomaly_rolling_q25=anomaly_rolling_q25,
            anomaly_rolling_q75=anomaly_rolling_q75,
            anomaly_score=anomaly_score,
            anomaly_score_mean=anomaly_score_mean,
            anomaly_score_std=anomaly_score_std,
            anomaly_timestamp=anomaly_timestamp,
            avg_anomaly_score=avg_anomaly_score,
            cluster=cluster,
            container=container,
            env=env,
            namespace=namespace,
            std_anomaly_score=std_anomaly_score,
            workload=workload,
        )

        logs_error_velocity_peak.additional_properties = d
        return logs_error_velocity_peak

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
