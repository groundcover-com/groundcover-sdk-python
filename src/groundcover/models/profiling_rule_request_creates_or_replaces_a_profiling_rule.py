from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profiling_rule_request_creates_or_replaces_a_profiling_rule_tags import (
        ProfilingRuleRequestCreatesOrReplacesAProfilingRuleTags,
    )
    from ..models.profiling_rule_scope import ProfilingRuleScope


T = TypeVar("T", bound="ProfilingRuleRequestCreatesOrReplacesAProfilingRule")


@_attrs_define
class ProfilingRuleRequestCreatesOrReplacesAProfilingRule:
    """
    Attributes:
        filter_ (str): gcQL over namespace, workload, container_name, pod_name, node and
            node_pool, such as `namespace:shop workload:checkout-*` or
            `pod_name:checkout-7d9f8-*`. `*` selects every container.
        scope (ProfilingRuleScope): ProfilingRuleScope is where a rule applies: "*" for both env and cluster
            means every cluster; otherwise one env and cluster pair a sensor has
            reported from.
        description (str | Unset): Why the rule exists; at most 500 characters.
        duration (str | Unset): How long the rule applies from this request, as a Go duration such as
            "30m" or "2h"; at least 5m. Mutually exclusive with expiresAt.
        expires_at (datetime.datetime | Unset): When the rule stops applying; at least 5m from now. Mutually exclusive
            with duration; with neither, the rule applies until deleted.
        tags (ProfilingRuleRequestCreatesOrReplacesAProfilingRuleTags | Unset): At most 20 tags.
    """

    filter_: str
    scope: ProfilingRuleScope
    description: str | Unset = UNSET
    duration: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    tags: ProfilingRuleRequestCreatesOrReplacesAProfilingRuleTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        scope = self.scope.to_dict()

        description = self.description

        duration = self.duration

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
                "scope": scope,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profiling_rule_request_creates_or_replaces_a_profiling_rule_tags import (
            ProfilingRuleRequestCreatesOrReplacesAProfilingRuleTags,
        )
        from ..models.profiling_rule_scope import ProfilingRuleScope

        d = dict(src_dict)
        filter_ = d.pop("filter")

        scope = ProfilingRuleScope.from_dict(d.pop("scope"))

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset) or _expires_at is None:
            expires_at = UNSET
        else:
            expires_at = parse_datetime(_expires_at)

        _tags = d.pop("tags", UNSET)
        tags: ProfilingRuleRequestCreatesOrReplacesAProfilingRuleTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = ProfilingRuleRequestCreatesOrReplacesAProfilingRuleTags.from_dict(_tags)

        profiling_rule_request_creates_or_replaces_a_profiling_rule = cls(
            filter_=filter_,
            scope=scope,
            description=description,
            duration=duration,
            expires_at=expires_at,
            tags=tags,
        )

        profiling_rule_request_creates_or_replaces_a_profiling_rule.additional_properties = d
        return profiling_rule_request_creates_or_replaces_a_profiling_rule

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
