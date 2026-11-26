from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.explain_response_is_an_explains_state_result_is_set_once_the_status_is_succeeded_status import (
    ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceededStatus,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.explain_result import ExplainResult


T = TypeVar("T", bound="ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceeded")


@_attrs_define
class ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceeded:
    """
    Attributes:
        id (str):
        status (ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceededStatus):
        error (str | Unset): Why the command failed, when the agent could not ask the database.
        result (ExplainResult | Unset): ExplainResult is the database's answer as it gave it: a plan, or the error it
            returned instead. Every engine's
            explain answers with it.
    """

    id: str
    status: ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceededStatus
    error: str | Unset = UNSET
    result: ExplainResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        error = self.error

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.explain_result import ExplainResult

        d = dict(src_dict)
        id = d.pop("id")

        status = ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceededStatus(d.pop("status"))

        error = d.pop("error", UNSET)

        _result = d.pop("result", UNSET)
        result: ExplainResult | Unset
        if isinstance(_result, Unset) or _result is None:
            result = UNSET
        else:
            result = ExplainResult.from_dict(_result)

        explain_response_is_an_explains_state_result_is_set_once_the_status_is_succeeded = cls(
            id=id,
            status=status,
            error=error,
            result=result,
        )

        explain_response_is_an_explains_state_result_is_set_once_the_status_is_succeeded.additional_properties = d
        return explain_response_is_an_explains_state_result_is_set_once_the_status_is_succeeded

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
