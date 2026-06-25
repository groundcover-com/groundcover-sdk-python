from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_policy_defines_model_for_execution_policy import (
        ExecutionPolicyDefinesModelForExecutionPolicy,
    )
    from ..models.metadata_defines_model_for_metadata import MetadataDefinesModelForMetadata
    from ..models.request_check_request_configuration_only_one_field_should_be_set_based_on_the_check_kind import (
        RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind,
    )
    from ..models.tracing_defines_model_for_tracing import TracingDefinesModelForTracing


T = TypeVar("T", bound="WorkerRequestDefinesModelForWorkerRequest")


@_attrs_define
class WorkerRequestDefinesModelForWorkerRequest:
    """
    Attributes:
        execution_policy (ExecutionPolicyDefinesModelForExecutionPolicy | Unset):
        kind (str | Unset): WorkerRequestKind Type of synthetic check to perform
        metadata (MetadataDefinesModelForMetadata | Unset):
        request (RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind | Unset):
        tracing (TracingDefinesModelForTracing | Unset):
    """

    execution_policy: ExecutionPolicyDefinesModelForExecutionPolicy | Unset = UNSET
    kind: str | Unset = UNSET
    metadata: MetadataDefinesModelForMetadata | Unset = UNSET
    request: RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind | Unset = UNSET
    tracing: TracingDefinesModelForTracing | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_policy, Unset):
            execution_policy = self.execution_policy.to_dict()

        kind = self.kind

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        tracing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tracing, Unset):
            tracing = self.tracing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_policy is not UNSET:
            field_dict["executionPolicy"] = execution_policy
        if kind is not UNSET:
            field_dict["kind"] = kind
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if request is not UNSET:
            field_dict["request"] = request
        if tracing is not UNSET:
            field_dict["tracing"] = tracing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_policy_defines_model_for_execution_policy import (
            ExecutionPolicyDefinesModelForExecutionPolicy,
        )
        from ..models.metadata_defines_model_for_metadata import MetadataDefinesModelForMetadata
        from ..models.request_check_request_configuration_only_one_field_should_be_set_based_on_the_check_kind import (
            RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind,
        )
        from ..models.tracing_defines_model_for_tracing import TracingDefinesModelForTracing

        d = dict(src_dict)
        _execution_policy = d.pop("executionPolicy", UNSET)
        execution_policy: ExecutionPolicyDefinesModelForExecutionPolicy | Unset
        if isinstance(_execution_policy, Unset) or _execution_policy is None:
            execution_policy = UNSET
        else:
            execution_policy = ExecutionPolicyDefinesModelForExecutionPolicy.from_dict(_execution_policy)

        kind = d.pop("kind", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: MetadataDefinesModelForMetadata | Unset
        if isinstance(_metadata, Unset) or _metadata is None:
            metadata = UNSET
        else:
            metadata = MetadataDefinesModelForMetadata.from_dict(_metadata)

        _request = d.pop("request", UNSET)
        request: RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind | Unset
        if isinstance(_request, Unset) or _request is None:
            request = UNSET
        else:
            request = RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind.from_dict(_request)

        _tracing = d.pop("tracing", UNSET)
        tracing: TracingDefinesModelForTracing | Unset
        if isinstance(_tracing, Unset) or _tracing is None:
            tracing = UNSET
        else:
            tracing = TracingDefinesModelForTracing.from_dict(_tracing)

        worker_request_defines_model_for_worker_request = cls(
            execution_policy=execution_policy,
            kind=kind,
            metadata=metadata,
            request=request,
            tracing=tracing,
        )

        worker_request_defines_model_for_worker_request.additional_properties = d
        return worker_request_defines_model_for_worker_request

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
