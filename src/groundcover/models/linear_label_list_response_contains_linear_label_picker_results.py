from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linear_label_is_a_linear_issue_label_for_a_team import LinearLabelIsALinearIssueLabelForATeam


T = TypeVar("T", bound="LinearLabelListResponseContainsLinearLabelPickerResults")


@_attrs_define
class LinearLabelListResponseContainsLinearLabelPickerResults:
    """
    Attributes:
        labels (list[LinearLabelIsALinearIssueLabelForATeam] | Unset):
        truncated (bool | Unset):
    """

    labels: list[LinearLabelIsALinearIssueLabelForATeam] | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linear_label_is_a_linear_issue_label_for_a_team import LinearLabelIsALinearIssueLabelForATeam

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: list[LinearLabelIsALinearIssueLabelForATeam] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LinearLabelIsALinearIssueLabelForATeam.from_dict(labels_item_data)

                labels.append(labels_item)

        truncated = d.pop("truncated", UNSET)

        linear_label_list_response_contains_linear_label_picker_results = cls(
            labels=labels,
            truncated=truncated,
        )

        linear_label_list_response_contains_linear_label_picker_results.additional_properties = d
        return linear_label_list_response_contains_linear_label_picker_results

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
