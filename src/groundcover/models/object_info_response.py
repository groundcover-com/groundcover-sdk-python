from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.object_info_response_data import ObjectInfoResponseData
    from ..models.toleration import Toleration


T = TypeVar("T", bound="ObjectInfoResponse")


@_attrs_define
class ObjectInfoResponse:
    """
    Attributes:
        annotations (list[str] | Unset):
        available (int | Unset):
        completed_at (datetime.datetime | Unset):
        completions (int | Unset):
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        creation_time (datetime.datetime | Unset):
        data (ObjectInfoResponseData | Unset):
        desired (int | Unset):
        desired_completions (int | Unset):
        duration (int | Unset):
        labels (list[str] | Unset):
        name (str | Unset):
        namespace (str | Unset):
        owner_kind (str | Unset):
        owner_name (str | Unset):
        owner_uid (str | Unset):
        ready (int | Unset):
        replicas (int | Unset):
        resource_version (str | Unset):
        selector (list[str] | Unset):
        started_at (datetime.datetime | Unset):
        status (str | Unset):
        tolerations (list[Toleration] | Unset):
        uid (str | Unset):
        workload (str | Unset):
    """

    annotations: list[str] | Unset = UNSET
    available: int | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    completions: int | Unset = UNSET
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    data: ObjectInfoResponseData | Unset = UNSET
    desired: int | Unset = UNSET
    desired_completions: int | Unset = UNSET
    duration: int | Unset = UNSET
    labels: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    owner_kind: str | Unset = UNSET
    owner_name: str | Unset = UNSET
    owner_uid: str | Unset = UNSET
    ready: int | Unset = UNSET
    replicas: int | Unset = UNSET
    resource_version: str | Unset = UNSET
    selector: list[str] | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    tolerations: list[Toleration] | Unset = UNSET
    uid: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: list[str] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations

        available = self.available

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        completions = self.completions

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        desired = self.desired

        desired_completions = self.desired_completions

        duration = self.duration

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        name = self.name

        namespace = self.namespace

        owner_kind = self.owner_kind

        owner_name = self.owner_name

        owner_uid = self.owner_uid

        ready = self.ready

        replicas = self.replicas

        resource_version = self.resource_version

        selector: list[str] | Unset = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        status = self.status

        tolerations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tolerations, Unset):
            tolerations = []
            for tolerations_item_data in self.tolerations:
                tolerations_item = tolerations_item_data.to_dict()
                tolerations.append(tolerations_item)

        uid = self.uid

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if available is not UNSET:
            field_dict["available"] = available
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if completions is not UNSET:
            field_dict["completions"] = completions
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if data is not UNSET:
            field_dict["data"] = data
        if desired is not UNSET:
            field_dict["desired"] = desired
        if desired_completions is not UNSET:
            field_dict["desiredCompletions"] = desired_completions
        if duration is not UNSET:
            field_dict["duration"] = duration
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if owner_kind is not UNSET:
            field_dict["ownerKind"] = owner_kind
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if owner_uid is not UNSET:
            field_dict["ownerUid"] = owner_uid
        if ready is not UNSET:
            field_dict["ready"] = ready
        if replicas is not UNSET:
            field_dict["replicas"] = replicas
        if resource_version is not UNSET:
            field_dict["resourceVersion"] = resource_version
        if selector is not UNSET:
            field_dict["selector"] = selector
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if uid is not UNSET:
            field_dict["uid"] = uid
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.object_info_response_data import ObjectInfoResponseData
        from ..models.toleration import Toleration

        d = dict(src_dict)
        annotations = cast(list[str], d.pop("annotations", UNSET))

        available = d.pop("available", UNSET)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset) or _completed_at is None:
            completed_at = UNSET
        else:
            completed_at = parse_datetime(_completed_at)

        completions = d.pop("completions", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: datetime.datetime | Unset
        if isinstance(_creation_time, Unset) or _creation_time is None:
            creation_time = UNSET
        else:
            creation_time = parse_datetime(_creation_time)

        _data = d.pop("data", UNSET)
        data: ObjectInfoResponseData | Unset
        if isinstance(_data, Unset) or _data is None:
            data = UNSET
        else:
            data = ObjectInfoResponseData.from_dict(_data)

        desired = d.pop("desired", UNSET)

        desired_completions = d.pop("desiredCompletions", UNSET)

        duration = d.pop("duration", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        owner_kind = d.pop("ownerKind", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        owner_uid = d.pop("ownerUid", UNSET)

        ready = d.pop("ready", UNSET)

        replicas = d.pop("replicas", UNSET)

        resource_version = d.pop("resourceVersion", UNSET)

        selector = cast(list[str], d.pop("selector", UNSET))

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset) or _started_at is None:
            started_at = UNSET
        else:
            started_at = parse_datetime(_started_at)

        status = d.pop("status", UNSET)

        _tolerations = d.pop("tolerations", UNSET)
        tolerations: list[Toleration] | Unset = UNSET
        if _tolerations is not UNSET:
            tolerations = []
            for tolerations_item_data in _tolerations:
                tolerations_item = Toleration.from_dict(tolerations_item_data)

                tolerations.append(tolerations_item)

        uid = d.pop("uid", UNSET)

        workload = d.pop("workload", UNSET)

        object_info_response = cls(
            annotations=annotations,
            available=available,
            completed_at=completed_at,
            completions=completions,
            conditions=conditions,
            creation_time=creation_time,
            data=data,
            desired=desired,
            desired_completions=desired_completions,
            duration=duration,
            labels=labels,
            name=name,
            namespace=namespace,
            owner_kind=owner_kind,
            owner_name=owner_name,
            owner_uid=owner_uid,
            ready=ready,
            replicas=replicas,
            resource_version=resource_version,
            selector=selector,
            started_at=started_at,
            status=status,
            tolerations=tolerations,
            uid=uid,
            workload=workload,
        )

        object_info_response.additional_properties = d
        return object_info_response

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
