from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog import (
        EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog,
    )


T = TypeVar("T", bound="EvalCatalogListsTheEvalFieldsOfABackendSortedByEvalID")


@_attrs_define
class EvalCatalogListsTheEvalFieldsOfABackendSortedByEvalID:
    """
    Attributes:
        fields (list[EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog]):
        supported (bool): Supported is always true.
    """

    fields: list[EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog]
    supported: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "supported": supported,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog import (
            EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog,
        )

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog.from_dict(fields_item_data)

            fields.append(fields_item)

        supported = d.pop("supported")

        eval_catalog_lists_the_eval_fields_of_a_backend_sorted_by_eval_id = cls(
            fields=fields,
            supported=supported,
        )

        eval_catalog_lists_the_eval_fields_of_a_backend_sorted_by_eval_id.additional_properties = d
        return eval_catalog_lists_the_eval_fields_of_a_backend_sorted_by_eval_id

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
