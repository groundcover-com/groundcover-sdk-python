from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
        InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
    )


T = TypeVar("T", bound="ListInvestigationsResponse")


@_attrs_define
class ListInvestigationsResponse:
    """
    Attributes:
        done (bool): Whether this is the last page.
        investigations (list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]): Page of
            root investigations, newest first.
    """

    done: bool
    investigations: list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        investigations = []
        for investigations_item_data in self.investigations:
            investigations_item = investigations_item_data.to_dict()
            investigations.append(investigations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "investigations": investigations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
            InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
        )

        d = dict(src_dict)
        done = d.pop("done")

        investigations = []
        _investigations = d.pop("investigations")
        for investigations_item_data in _investigations:
            investigations_item = (
                InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion.from_dict(
                    investigations_item_data
                )
            )

            investigations.append(investigations_item)

        list_investigations_response = cls(
            done=done,
            investigations=investigations,
        )

        list_investigations_response.additional_properties = d
        return list_investigations_response

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
