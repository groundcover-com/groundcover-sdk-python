from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_validation_error_details_lists_every_validation_violation import (
        ConnectorValidationErrorDetailsListsEveryValidationViolation,
    )


T = TypeVar("T", bound="ConnectorValidationErrorResponseIsAConnector400ValidationFailuresListEveryViolationInDetails")


@_attrs_define
class ConnectorValidationErrorResponseIsAConnector400ValidationFailuresListEveryViolationInDetails:
    """
    Attributes:
        message (str):
        details (ConnectorValidationErrorDetailsListsEveryValidationViolation | Unset):
        trace_id (str | Unset):
    """

    message: str
    details: ConnectorValidationErrorDetailsListsEveryValidationViolation | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_validation_error_details_lists_every_validation_violation import (
            ConnectorValidationErrorDetailsListsEveryValidationViolation,
        )

        d = dict(src_dict)
        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: ConnectorValidationErrorDetailsListsEveryValidationViolation | Unset
        if isinstance(_details, Unset) or _details is None:
            details = UNSET
        else:
            details = ConnectorValidationErrorDetailsListsEveryValidationViolation.from_dict(_details)

        trace_id = d.pop("trace_id", UNSET)

        connector_validation_error_response_is_a_connector_400_validation_failures_list_every_violation_in_details = (
            cls(
                message=message,
                details=details,
                trace_id=trace_id,
            )
        )

        connector_validation_error_response_is_a_connector_400_validation_failures_list_every_violation_in_details.additional_properties = d
        return (
            connector_validation_error_response_is_a_connector_400_validation_failures_list_every_violation_in_details
        )

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
