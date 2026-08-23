from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_funnel_is_the_wet_mode_hierarchical_breakdown_for_one_asset_type import (
        AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType,
    )
    from ..models.assets_summary_holds_asset_counts_for_the_unified_summary import (
        AssetsSummaryHoldsAssetCountsForTheUnifiedSummary,
    )
    from ..models.queries_summary_holds_query_level_statistics_for_the_unified_summary import (
        QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary,
    )
    from ..models.unified_summary_is_the_single_hierarchical_summary_included_in_json_output_assets_by_finding_type import (
        UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAssetsByFindingType,
    )
    from ..models.unsupported_counts_for_the_unified_summary import UnsupportedCountsForTheUnifiedSummary
    from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary import (
        WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary,
    )


T = TypeVar("T", bound="UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput")


@_attrs_define
class UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutput:
    """
    Attributes:
        assets (AssetsSummaryHoldsAssetCountsForTheUnifiedSummary | Unset):
        assets_by_finding_type (UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAssetsByFindingType |
            Unset): AssetsByFindingType is the distribution of affected assets per finding
            type, keyed by asset type.
        conversion (UnsupportedCountsForTheUnifiedSummary | Unset):
        dashboards (AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType | Unset): Unit names what Total counts:
            monitors are counted whole, dashboards are
            counted per widget.
        monitors (AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType | Unset): Unit names what Total counts:
            monitors are counted whole, dashboards are
            counted per widget.
        queries (QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary | Unset):
        wet_validation (WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary | Unset): Two "with data"
            rates provide different perspectives:
            WithDataPct: of tested queries only (denominator = wet-tested, including dedup fan-out)
            WithDataOfTotalPct: of all extractable queries from supported assets (broadest available
            denominator; note this undercounts because queries inside unsupported widgets and
            unsupported asset types are not included)
    """

    assets: AssetsSummaryHoldsAssetCountsForTheUnifiedSummary | Unset = UNSET
    assets_by_finding_type: (
        UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAssetsByFindingType | Unset
    ) = UNSET
    conversion: UnsupportedCountsForTheUnifiedSummary | Unset = UNSET
    dashboards: AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType | Unset = UNSET
    monitors: AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType | Unset = UNSET
    queries: QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary | Unset = UNSET
    wet_validation: WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = self.assets.to_dict()

        assets_by_finding_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assets_by_finding_type, Unset):
            assets_by_finding_type = self.assets_by_finding_type.to_dict()

        conversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversion, Unset):
            conversion = self.conversion.to_dict()

        dashboards: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dashboards, Unset):
            dashboards = self.dashboards.to_dict()

        monitors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = self.monitors.to_dict()

        queries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = self.queries.to_dict()

        wet_validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wet_validation, Unset):
            wet_validation = self.wet_validation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if assets_by_finding_type is not UNSET:
            field_dict["assets_by_finding_type"] = assets_by_finding_type
        if conversion is not UNSET:
            field_dict["conversion"] = conversion
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards
        if monitors is not UNSET:
            field_dict["monitors"] = monitors
        if queries is not UNSET:
            field_dict["queries"] = queries
        if wet_validation is not UNSET:
            field_dict["wet_validation"] = wet_validation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_funnel_is_the_wet_mode_hierarchical_breakdown_for_one_asset_type import (
            AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType,
        )
        from ..models.assets_summary_holds_asset_counts_for_the_unified_summary import (
            AssetsSummaryHoldsAssetCountsForTheUnifiedSummary,
        )
        from ..models.queries_summary_holds_query_level_statistics_for_the_unified_summary import (
            QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary,
        )
        from ..models.unified_summary_is_the_single_hierarchical_summary_included_in_json_output_assets_by_finding_type import (
            UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAssetsByFindingType,
        )
        from ..models.unsupported_counts_for_the_unified_summary import UnsupportedCountsForTheUnifiedSummary
        from ..models.wet_validation_summary_holds_wet_mode_validation_results_for_the_unified_summary import (
            WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary,
        )

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: AssetsSummaryHoldsAssetCountsForTheUnifiedSummary | Unset
        if isinstance(_assets, Unset) or _assets is None:
            assets = UNSET
        else:
            assets = AssetsSummaryHoldsAssetCountsForTheUnifiedSummary.from_dict(_assets)

        _assets_by_finding_type = d.pop("assets_by_finding_type", UNSET)
        assets_by_finding_type: (
            UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAssetsByFindingType | Unset
        )
        if isinstance(_assets_by_finding_type, Unset) or _assets_by_finding_type is None:
            assets_by_finding_type = UNSET
        else:
            assets_by_finding_type = (
                UnifiedSummaryIsTheSingleHierarchicalSummaryIncludedInJSONOutputAssetsByFindingType.from_dict(
                    _assets_by_finding_type
                )
            )

        _conversion = d.pop("conversion", UNSET)
        conversion: UnsupportedCountsForTheUnifiedSummary | Unset
        if isinstance(_conversion, Unset) or _conversion is None:
            conversion = UNSET
        else:
            conversion = UnsupportedCountsForTheUnifiedSummary.from_dict(_conversion)

        _dashboards = d.pop("dashboards", UNSET)
        dashboards: AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType | Unset
        if isinstance(_dashboards, Unset) or _dashboards is None:
            dashboards = UNSET
        else:
            dashboards = AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType.from_dict(_dashboards)

        _monitors = d.pop("monitors", UNSET)
        monitors: AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType | Unset
        if isinstance(_monitors, Unset) or _monitors is None:
            monitors = UNSET
        else:
            monitors = AssetFunnelIsTheWetModeHierarchicalBreakdownForOneAssetType.from_dict(_monitors)

        _queries = d.pop("queries", UNSET)
        queries: QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary | Unset
        if isinstance(_queries, Unset) or _queries is None:
            queries = UNSET
        else:
            queries = QueriesSummaryHoldsQueryLevelStatisticsForTheUnifiedSummary.from_dict(_queries)

        _wet_validation = d.pop("wet_validation", UNSET)
        wet_validation: WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary | Unset
        if isinstance(_wet_validation, Unset) or _wet_validation is None:
            wet_validation = UNSET
        else:
            wet_validation = WetValidationSummaryHoldsWetModeValidationResultsForTheUnifiedSummary.from_dict(
                _wet_validation
            )

        unified_summary_is_the_single_hierarchical_summary_included_in_json_output = cls(
            assets=assets,
            assets_by_finding_type=assets_by_finding_type,
            conversion=conversion,
            dashboards=dashboards,
            monitors=monitors,
            queries=queries,
            wet_validation=wet_validation,
        )

        unified_summary_is_the_single_hierarchical_summary_included_in_json_output.additional_properties = d
        return unified_summary_is_the_single_hierarchical_summary_included_in_json_output

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
