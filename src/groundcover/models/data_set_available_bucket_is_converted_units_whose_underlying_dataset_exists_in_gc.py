from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count_pct_is_a_count_with_percentage_of_its_parent_total import (
        CountPctIsACountWithPercentageOfItsParentTotal,
    )
    from ..models.no_data_breakdown_drills_into_units_that_did_not_come_back_fully_working import (
        NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking,
    )


T = TypeVar("T", bound="DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC")


@_attrs_define
class DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC:
    """
    Attributes:
        lookback (str | Unset): Lookback is the widest window actually queried, so the report never claims
            a window it did not use.
        no_data (NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking | Unset): A unit lands here when any of
            its queries returned no data, or when a static
            key/value gap was found. For a multi-query unit — a widget with several series,
            a monitor with a formula — that means "not all queries returned data" rather
            than "nothing returned data"; SomeQueriesReturnedData on each entry records
            which of the two it was.
        returns_data (CountPctIsACountWithPercentageOfItsParentTotal | Unset):
        total (int | Unset):
    """

    lookback: str | Unset = UNSET
    no_data: NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking | Unset = UNSET
    returns_data: CountPctIsACountWithPercentageOfItsParentTotal | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookback = self.lookback

        no_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_data, Unset):
            no_data = self.no_data.to_dict()

        returns_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.returns_data, Unset):
            returns_data = self.returns_data.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookback is not UNSET:
            field_dict["lookback"] = lookback
        if no_data is not UNSET:
            field_dict["no_data"] = no_data
        if returns_data is not UNSET:
            field_dict["returns_data"] = returns_data
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.count_pct_is_a_count_with_percentage_of_its_parent_total import (
            CountPctIsACountWithPercentageOfItsParentTotal,
        )
        from ..models.no_data_breakdown_drills_into_units_that_did_not_come_back_fully_working import (
            NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking,
        )

        d = dict(src_dict)
        lookback = d.pop("lookback", UNSET)

        _no_data = d.pop("no_data", UNSET)
        no_data: NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking | Unset
        if isinstance(_no_data, Unset) or _no_data is None:
            no_data = UNSET
        else:
            no_data = NoDataBreakdownDrillsIntoUnitsThatDidNotComeBackFullyWorking.from_dict(_no_data)

        _returns_data = d.pop("returns_data", UNSET)
        returns_data: CountPctIsACountWithPercentageOfItsParentTotal | Unset
        if isinstance(_returns_data, Unset) or _returns_data is None:
            returns_data = UNSET
        else:
            returns_data = CountPctIsACountWithPercentageOfItsParentTotal.from_dict(_returns_data)

        total = d.pop("total", UNSET)

        data_set_available_bucket_is_converted_units_whose_underlying_dataset_exists_in_gc = cls(
            lookback=lookback,
            no_data=no_data,
            returns_data=returns_data,
            total=total,
        )

        data_set_available_bucket_is_converted_units_whose_underlying_dataset_exists_in_gc.additional_properties = d
        return data_set_available_bucket_is_converted_units_whose_underlying_dataset_exists_in_gc

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
