from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.excluded_bucket import ExcludedBucket
    from ..models.not_supported_bucket_covers_unsupported_types_bucketed_by_type import (
        NotSupportedBucketCoversUnsupportedTypesBucketedByType,
    )
    from ..models.supported_converted_bucket_covers_units_that_converted_successfully import (
        SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully,
    )
    from ..models.supported_not_converted_bucket_covers_supported_types_that_failed_conversion import (
        SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion,
    )


T = TypeVar("T", bound="AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType")


@_attrs_define
class AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType:
    """Unit names what Total counts: monitors are counted whole, dashboards are
    counted per widget.

        Attributes:
            excluded (ExcludedBucket | Unset): ExcludedBucket counts units held out of the funnel because their only unmet
                dependency is Datadog's own telemetry: a self-observability metric, or one
                already inactive in Datadog. Migration quality has no bearing on either —
                they were never going to return data — so they are reported separately
                rather than weighing on supported/unsupported like a real gap would.
            not_supported (NotSupportedBucketCoversUnsupportedTypesBucketedByType | Unset):
            supported_converted (SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully | Unset):
            supported_not_converted (SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion | Unset):
            total (int | Unset):
            unit (str | Unset):
    """

    excluded: ExcludedBucket | Unset = UNSET
    not_supported: NotSupportedBucketCoversUnsupportedTypesBucketedByType | Unset = UNSET
    supported_converted: SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully | Unset = UNSET
    supported_not_converted: SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion | Unset = UNSET
    total: int | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.excluded, Unset):
            excluded = self.excluded.to_dict()

        not_supported: dict[str, Any] | Unset = UNSET
        if not isinstance(self.not_supported, Unset):
            not_supported = self.not_supported.to_dict()

        supported_converted: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supported_converted, Unset):
            supported_converted = self.supported_converted.to_dict()

        supported_not_converted: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supported_not_converted, Unset):
            supported_not_converted = self.supported_not_converted.to_dict()

        total = self.total

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded is not UNSET:
            field_dict["excluded"] = excluded
        if not_supported is not UNSET:
            field_dict["not_supported"] = not_supported
        if supported_converted is not UNSET:
            field_dict["supported_converted"] = supported_converted
        if supported_not_converted is not UNSET:
            field_dict["supported_not_converted"] = supported_not_converted
        if total is not UNSET:
            field_dict["total"] = total
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.excluded_bucket import ExcludedBucket
        from ..models.not_supported_bucket_covers_unsupported_types_bucketed_by_type import (
            NotSupportedBucketCoversUnsupportedTypesBucketedByType,
        )
        from ..models.supported_converted_bucket_covers_units_that_converted_successfully import (
            SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully,
        )
        from ..models.supported_not_converted_bucket_covers_supported_types_that_failed_conversion import (
            SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion,
        )

        d = dict(src_dict)
        _excluded = d.pop("excluded", UNSET)
        excluded: ExcludedBucket | Unset
        if isinstance(_excluded, Unset) or _excluded is None:
            excluded = UNSET
        else:
            excluded = ExcludedBucket.from_dict(_excluded)

        _not_supported = d.pop("not_supported", UNSET)
        not_supported: NotSupportedBucketCoversUnsupportedTypesBucketedByType | Unset
        if isinstance(_not_supported, Unset) or _not_supported is None:
            not_supported = UNSET
        else:
            not_supported = NotSupportedBucketCoversUnsupportedTypesBucketedByType.from_dict(_not_supported)

        _supported_converted = d.pop("supported_converted", UNSET)
        supported_converted: SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully | Unset
        if isinstance(_supported_converted, Unset) or _supported_converted is None:
            supported_converted = UNSET
        else:
            supported_converted = SupportedConvertedBucketCoversUnitsThatConvertedSuccessfully.from_dict(
                _supported_converted
            )

        _supported_not_converted = d.pop("supported_not_converted", UNSET)
        supported_not_converted: SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion | Unset
        if isinstance(_supported_not_converted, Unset) or _supported_not_converted is None:
            supported_not_converted = UNSET
        else:
            supported_not_converted = SupportedNotConvertedBucketCoversSupportedTypesThatFailedConversion.from_dict(
                _supported_not_converted
            )

        total = d.pop("total", UNSET)

        unit = d.pop("unit", UNSET)

        asset_funnel_is_the_wet_mode_hierarchical_breakdown_for_one_asset_type = cls(
            excluded=excluded,
            not_supported=not_supported,
            supported_converted=supported_converted,
            supported_not_converted=supported_not_converted,
            total=total,
            unit=unit,
        )

        asset_funnel_is_the_wet_mode_hierarchical_breakdown_for_one_asset_type.additional_properties = d
        return asset_funnel_is_the_wet_mode_hierarchical_breakdown_for_one_asset_type

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
