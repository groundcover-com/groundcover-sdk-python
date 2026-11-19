from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count import (
        IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount,
    )


T = TypeVar("T", bound="ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters")


@_attrs_define
class ListIssuesResponseIsAnOrderedPageAndTheExactTotalUnderTheFilters:
    """
    Attributes:
        has_more (bool):
        issues (list[IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount]):
        limit (int):
        offset (int):
        total (int):
    """

    has_more: bool
    issues: list[IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount]
    limit: int
    offset: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        limit = self.limit

        offset = self.offset

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_more": has_more,
                "issues": issues,
                "limit": limit,
                "offset": offset,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_is_an_open_migration_issue_with_its_distinct_eligible_asset_count import (
            IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount,
        )

        d = dict(src_dict)
        has_more = d.pop("has_more")

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = IssueIsAnOpenMigrationIssueWithItsDistinctEligibleAssetCount.from_dict(issues_item_data)

            issues.append(issues_item)

        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        list_issues_response_is_an_ordered_page_and_the_exact_total_under_the_filters = cls(
            has_more=has_more,
            issues=issues,
            limit=limit,
            offset=offset,
            total=total,
        )

        list_issues_response_is_an_ordered_page_and_the_exact_total_under_the_filters.additional_properties = d
        return list_issues_response_is_an_ordered_page_and_the_exact_total_under_the_filters

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
