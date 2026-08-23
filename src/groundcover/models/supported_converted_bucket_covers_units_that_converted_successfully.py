from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_set_available_bucket_is_converted_units_whose_underlying_dataset_exists_in_gc import (
        DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC,
    )
    from ..models.missing_data_set_bucket_covers_converted_units_whose_underlying_dataset_is_absent import (
        MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent,
    )
    from ..models.no_data_needed_bucket_counts_units_that_need_no_query_to_render import (
        NoDataNeededBucketCountsUnitsThatNeedNoQueryToRender,
    )


T = TypeVar("T", bound="SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully")


@_attrs_define
class SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully:
    """
    Attributes:
        data_set_available (DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC | Unset):
        missing_underlying_data_set (MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent | Unset):
        no_data_needed (NoDataNeededBucketCountsUnitsThatNeedNoQueryToRender | Unset):
        total (int | Unset):
    """

    data_set_available: DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC | Unset = UNSET
    missing_underlying_data_set: MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent | Unset = UNSET
    no_data_needed: NoDataNeededBucketCountsUnitsThatNeedNoQueryToRender | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_set_available: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_set_available, Unset):
            data_set_available = self.data_set_available.to_dict()

        missing_underlying_data_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.missing_underlying_data_set, Unset):
            missing_underlying_data_set = self.missing_underlying_data_set.to_dict()

        no_data_needed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_data_needed, Unset):
            no_data_needed = self.no_data_needed.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_set_available is not UNSET:
            field_dict["data_set_available"] = data_set_available
        if missing_underlying_data_set is not UNSET:
            field_dict["missing_underlying_data_set"] = missing_underlying_data_set
        if no_data_needed is not UNSET:
            field_dict["no_data_needed"] = no_data_needed
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_set_available_bucket_is_converted_units_whose_underlying_dataset_exists_in_gc import (
            DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC,
        )
        from ..models.missing_data_set_bucket_covers_converted_units_whose_underlying_dataset_is_absent import (
            MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent,
        )
        from ..models.no_data_needed_bucket_counts_units_that_need_no_query_to_render import (
            NoDataNeededBucketCountsUnitsThatNeedNoQueryToRender,
        )

        d = dict(src_dict)
        _data_set_available = d.pop("data_set_available", UNSET)
        data_set_available: DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC | Unset
        if isinstance(_data_set_available, Unset) or _data_set_available is None:
            data_set_available = UNSET
        else:
            data_set_available = DataSetAvailableBucketIsConvertedUnitsWhoseUnderlyingDatasetExistsInGC.from_dict(
                _data_set_available
            )

        _missing_underlying_data_set = d.pop("missing_underlying_data_set", UNSET)
        missing_underlying_data_set: MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent | Unset
        if isinstance(_missing_underlying_data_set, Unset) or _missing_underlying_data_set is None:
            missing_underlying_data_set = UNSET
        else:
            missing_underlying_data_set = (
                MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent.from_dict(
                    _missing_underlying_data_set
                )
            )

        _no_data_needed = d.pop("no_data_needed", UNSET)
        no_data_needed: NoDataNeededBucketCountsUnitsThatNeedNoQueryToRender | Unset
        if isinstance(_no_data_needed, Unset) or _no_data_needed is None:
            no_data_needed = UNSET
        else:
            no_data_needed = NoDataNeededBucketCountsUnitsThatNeedNoQueryToRender.from_dict(_no_data_needed)

        total = d.pop("total", UNSET)

        supported_converted_bucket_covers_units_that_converted_successfully = cls(
            data_set_available=data_set_available,
            missing_underlying_data_set=missing_underlying_data_set,
            no_data_needed=no_data_needed,
            total=total,
        )

        supported_converted_bucket_covers_units_that_converted_successfully.additional_properties = d
        return supported_converted_bucket_covers_units_that_converted_successfully

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
