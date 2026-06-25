from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_defines_model_for_metadata_labels import MetadataDefinesModelForMetadataLabels


T = TypeVar("T", bound="MetadataDefinesModelForMetadata")


@_attrs_define
class MetadataDefinesModelForMetadata:
    """
    Attributes:
        execution_id (str | Unset):
        labels (MetadataDefinesModelForMetadataLabels | Unset):
        synthetic_id (str | Unset):
        synthetic_name (str | Unset):
        target (str | Unset):
    """

    execution_id: str | Unset = UNSET
    labels: MetadataDefinesModelForMetadataLabels | Unset = UNSET
    synthetic_id: str | Unset = UNSET
    synthetic_name: str | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        synthetic_id = self.synthetic_id

        synthetic_name = self.synthetic_name

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if synthetic_id is not UNSET:
            field_dict["syntheticId"] = synthetic_id
        if synthetic_name is not UNSET:
            field_dict["syntheticName"] = synthetic_name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_defines_model_for_metadata_labels import MetadataDefinesModelForMetadataLabels

        d = dict(src_dict)
        execution_id = d.pop("executionId", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: MetadataDefinesModelForMetadataLabels | Unset
        if isinstance(_labels, Unset) or _labels is None:
            labels = UNSET
        else:
            labels = MetadataDefinesModelForMetadataLabels.from_dict(_labels)

        synthetic_id = d.pop("syntheticId", UNSET)

        synthetic_name = d.pop("syntheticName", UNSET)

        target = d.pop("target", UNSET)

        metadata_defines_model_for_metadata = cls(
            execution_id=execution_id,
            labels=labels,
            synthetic_id=synthetic_id,
            synthetic_name=synthetic_name,
            target=target,
        )

        metadata_defines_model_for_metadata.additional_properties = d
        return metadata_defines_model_for_metadata

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
