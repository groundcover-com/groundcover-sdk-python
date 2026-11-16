from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profiling_rule_response_is_a_stored_profiling_rule_origin import (
    ProfilingRuleResponseIsAStoredProfilingRuleOrigin,
)
from ..models.profiling_rule_response_is_a_stored_profiling_rule_status import (
    ProfilingRuleResponseIsAStoredProfilingRuleStatus,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profiling_rule_response_is_a_stored_profiling_rule_tags import (
        ProfilingRuleResponseIsAStoredProfilingRuleTags,
    )
    from ..models.profiling_rule_scope import ProfilingRuleScope


T = TypeVar("T", bound="ProfilingRuleResponseIsAStoredProfilingRule")


@_attrs_define
class ProfilingRuleResponseIsAStoredProfilingRule:
    """
    Attributes:
        created_at (datetime.datetime | Unset):
        created_by (str | Unset):
        description (str | Unset):
        expires_at (datetime.datetime | Unset): Absent when the rule applies until deleted.
        filter_ (str | Unset):
        id (str | Unset):
        origin (ProfilingRuleResponseIsAStoredProfilingRuleOrigin | Unset): How the rule was created: ui, api, terraform
            or agent.
        scope (ProfilingRuleScope | Unset): ProfilingRuleScope is where a rule applies: "*" for both env and cluster
            means every cluster; otherwise one env and cluster pair a sensor has
            reported from.
        status (ProfilingRuleResponseIsAStoredProfilingRuleStatus | Unset): active or expired.
        tags (ProfilingRuleResponseIsAStoredProfilingRuleTags | Unset):
        updated_at (datetime.datetime | Unset):
        updated_by (str | Unset):
    """

    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    description: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    filter_: str | Unset = UNSET
    id: str | Unset = UNSET
    origin: ProfilingRuleResponseIsAStoredProfilingRuleOrigin | Unset = UNSET
    scope: ProfilingRuleScope | Unset = UNSET
    status: ProfilingRuleResponseIsAStoredProfilingRuleStatus | Unset = UNSET
    tags: ProfilingRuleResponseIsAStoredProfilingRuleTags | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        filter_ = self.filter_

        id = self.id

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.value

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if id is not UNSET:
            field_dict["id"] = id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if scope is not UNSET:
            field_dict["scope"] = scope
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profiling_rule_response_is_a_stored_profiling_rule_tags import (
            ProfilingRuleResponseIsAStoredProfilingRuleTags,
        )
        from ..models.profiling_rule_scope import ProfilingRuleScope

        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        created_by = d.pop("createdBy", UNSET)

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset) or _expires_at is None:
            expires_at = UNSET
        else:
            expires_at = parse_datetime(_expires_at)

        filter_ = d.pop("filter", UNSET)

        id = d.pop("id", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: ProfilingRuleResponseIsAStoredProfilingRuleOrigin | Unset
        if isinstance(_origin, Unset) or _origin is None:
            origin = UNSET
        else:
            origin = ProfilingRuleResponseIsAStoredProfilingRuleOrigin(_origin)

        _scope = d.pop("scope", UNSET)
        scope: ProfilingRuleScope | Unset
        if isinstance(_scope, Unset) or _scope is None:
            scope = UNSET
        else:
            scope = ProfilingRuleScope.from_dict(_scope)

        _status = d.pop("status", UNSET)
        status: ProfilingRuleResponseIsAStoredProfilingRuleStatus | Unset
        if isinstance(_status, Unset) or _status is None:
            status = UNSET
        else:
            status = ProfilingRuleResponseIsAStoredProfilingRuleStatus(_status)

        _tags = d.pop("tags", UNSET)
        tags: ProfilingRuleResponseIsAStoredProfilingRuleTags | Unset
        if isinstance(_tags, Unset) or _tags is None:
            tags = UNSET
        else:
            tags = ProfilingRuleResponseIsAStoredProfilingRuleTags.from_dict(_tags)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        updated_by = d.pop("updatedBy", UNSET)

        profiling_rule_response_is_a_stored_profiling_rule = cls(
            created_at=created_at,
            created_by=created_by,
            description=description,
            expires_at=expires_at,
            filter_=filter_,
            id=id,
            origin=origin,
            scope=scope,
            status=status,
            tags=tags,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        profiling_rule_response_is_a_stored_profiling_rule.additional_properties = d
        return profiling_rule_response_is_a_stored_profiling_rule

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
