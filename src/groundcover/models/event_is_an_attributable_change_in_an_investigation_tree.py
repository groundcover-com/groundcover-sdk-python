from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_is_an_attributable_change_in_an_investigation_tree_entity_type import (
    EventIsAnAttributableChangeInAnInvestigationTreeEntityType,
)
from ..models.event_is_an_attributable_change_in_an_investigation_tree_type import (
    EventIsAnAttributableChangeInAnInvestigationTreeType,
)

if TYPE_CHECKING:
    from ..models.event_is_an_attributable_change_in_an_investigation_tree_payload import (
        EventIsAnAttributableChangeInAnInvestigationTreePayload,
    )
    from ..models.investigation_author import InvestigationAuthor


T = TypeVar("T", bound="EventIsAnAttributableChangeInAnInvestigationTree")


@_attrs_define
class EventIsAnAttributableChangeInAnInvestigationTree:
    """
    Attributes:
        author (InvestigationAuthor):
        created_at (datetime.datetime):
        entity_id (UUID):
        entity_type (EventIsAnAttributableChangeInAnInvestigationTreeEntityType):
        id (UUID):
        investigation_id (UUID):
        payload (EventIsAnAttributableChangeInAnInvestigationTreePayload): Versioned object with v: 1.
        type_ (EventIsAnAttributableChangeInAnInvestigationTreeType):
    """

    author: InvestigationAuthor
    created_at: datetime.datetime
    entity_id: UUID
    entity_type: EventIsAnAttributableChangeInAnInvestigationTreeEntityType
    id: UUID
    investigation_id: UUID
    payload: EventIsAnAttributableChangeInAnInvestigationTreePayload
    type_: EventIsAnAttributableChangeInAnInvestigationTreeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author.to_dict()

        created_at = self.created_at.isoformat()

        entity_id = str(self.entity_id)

        entity_type = self.entity_type.value

        id = str(self.id)

        investigation_id = str(self.investigation_id)

        payload = self.payload.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "createdAt": created_at,
                "entityId": entity_id,
                "entityType": entity_type,
                "id": id,
                "investigationId": investigation_id,
                "payload": payload,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_is_an_attributable_change_in_an_investigation_tree_payload import (
            EventIsAnAttributableChangeInAnInvestigationTreePayload,
        )
        from ..models.investigation_author import InvestigationAuthor

        d = dict(src_dict)
        author = InvestigationAuthor.from_dict(d.pop("author"))

        created_at = parse_datetime(d.pop("createdAt"))

        entity_id = UUID(d.pop("entityId"))

        entity_type = EventIsAnAttributableChangeInAnInvestigationTreeEntityType(d.pop("entityType"))

        id = UUID(d.pop("id"))

        investigation_id = UUID(d.pop("investigationId"))

        payload = EventIsAnAttributableChangeInAnInvestigationTreePayload.from_dict(d.pop("payload"))

        type_ = EventIsAnAttributableChangeInAnInvestigationTreeType(d.pop("type"))

        event_is_an_attributable_change_in_an_investigation_tree = cls(
            author=author,
            created_at=created_at,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            investigation_id=investigation_id,
            payload=payload,
            type_=type_,
        )

        event_is_an_attributable_change_in_an_investigation_tree.additional_properties = d
        return event_is_an_attributable_change_in_an_investigation_tree

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
