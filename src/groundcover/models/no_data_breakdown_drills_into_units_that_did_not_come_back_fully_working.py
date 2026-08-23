from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_missing_breakdown_groups_units_with_missing_keys import (
        KeyMissingBreakdownGroupsUnitsWithMissingKeys,
    )
    from ..models.positive_no_data_bucket import PositiveNoDataBucket
    from ..models.value_missing_bucket_lists_units_whose_filter_values_are_absent_in_groundcover import (
        ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover,
    )


T = TypeVar("T", bound="NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking")


@_attrs_define
class NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking:
    """A unit lands here when any of its queries returned no data, or when a static
    key/value gap was found. For a multi-query unit — a widget with several series,
    a monitor with a formula — that means "not all queries returned data" rather
    than "nothing returned data"; SomeQueriesReturnedData on each entry records
    which of the two it was.

        Attributes:
            count (int | Unset):
            negative_key_missing (KeyMissingBreakdownGroupsUnitsWithMissingKeys | Unset): Metric label gaps and search field
                gaps are reported separately: a log or event
                field gap has no metric to attribute it to, and folding both into a by-metric
                view produced a meaningless "unknown" bucket.
            negative_value_missing (ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover | Unset):
            pct (float | Unset):
            positive_all_keys_values_exist (PositiveNoDataBucket | Unset): PositiveNoDataBucket covers units where every
                dependency resolves yet no data
                came back, broken down by the reason we could establish.
    """

    count: int | Unset = UNSET
    negative_key_missing: KeyMissingBreakdownGroupsUnitsWithMissingKeys | Unset = UNSET
    negative_value_missing: ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover | Unset = UNSET
    pct: float | Unset = UNSET
    positive_all_keys_values_exist: PositiveNoDataBucket | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        negative_key_missing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.negative_key_missing, Unset):
            negative_key_missing = self.negative_key_missing.to_dict()

        negative_value_missing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.negative_value_missing, Unset):
            negative_value_missing = self.negative_value_missing.to_dict()

        pct = self.pct

        positive_all_keys_values_exist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positive_all_keys_values_exist, Unset):
            positive_all_keys_values_exist = self.positive_all_keys_values_exist.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if negative_key_missing is not UNSET:
            field_dict["negative_key_missing"] = negative_key_missing
        if negative_value_missing is not UNSET:
            field_dict["negative_value_missing"] = negative_value_missing
        if pct is not UNSET:
            field_dict["pct"] = pct
        if positive_all_keys_values_exist is not UNSET:
            field_dict["positive_all_keys_values_exist"] = positive_all_keys_values_exist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_missing_breakdown_groups_units_with_missing_keys import (
            KeyMissingBreakdownGroupsUnitsWithMissingKeys,
        )
        from ..models.positive_no_data_bucket import PositiveNoDataBucket
        from ..models.value_missing_bucket_lists_units_whose_filter_values_are_absent_in_groundcover import (
            ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover,
        )

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _negative_key_missing = d.pop("negative_key_missing", UNSET)
        negative_key_missing: KeyMissingBreakdownGroupsUnitsWithMissingKeys | Unset
        if isinstance(_negative_key_missing, Unset) or _negative_key_missing is None:
            negative_key_missing = UNSET
        else:
            negative_key_missing = KeyMissingBreakdownGroupsUnitsWithMissingKeys.from_dict(_negative_key_missing)

        _negative_value_missing = d.pop("negative_value_missing", UNSET)
        negative_value_missing: ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover | Unset
        if isinstance(_negative_value_missing, Unset) or _negative_value_missing is None:
            negative_value_missing = UNSET
        else:
            negative_value_missing = ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover.from_dict(
                _negative_value_missing
            )

        pct = d.pop("pct", UNSET)

        _positive_all_keys_values_exist = d.pop("positive_all_keys_values_exist", UNSET)
        positive_all_keys_values_exist: PositiveNoDataBucket | Unset
        if isinstance(_positive_all_keys_values_exist, Unset) or _positive_all_keys_values_exist is None:
            positive_all_keys_values_exist = UNSET
        else:
            positive_all_keys_values_exist = PositiveNoDataBucket.from_dict(_positive_all_keys_values_exist)

        no_data_breakdown_drills_into_units_that_did_not_come_back_fully_working = cls(
            count=count,
            negative_key_missing=negative_key_missing,
            negative_value_missing=negative_value_missing,
            pct=pct,
            positive_all_keys_values_exist=positive_all_keys_values_exist,
        )

        no_data_breakdown_drills_into_units_that_did_not_come_back_fully_working.additional_properties = d
        return no_data_breakdown_drills_into_units_that_did_not_come_back_fully_working

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
