from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_llm_pricing_response_status import CustomLLMPricingResponseStatus
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_llm_pricing_file_info import CustomLLMPricingFileInfo


T = TypeVar("T", bound="CustomLLMPricingResponse")


@_attrs_define
class CustomLLMPricingResponse:
    """
    Attributes:
        active_revision (str):
        file (CustomLLMPricingFileInfo):
        saved_revision (str):
        status (CustomLLMPricingResponseStatus):
        error (str | Unset):
    """

    active_revision: str
    file: CustomLLMPricingFileInfo
    saved_revision: str
    status: CustomLLMPricingResponseStatus
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_revision = self.active_revision

        file = self.file.to_dict()

        saved_revision = self.saved_revision

        status = self.status.value

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activeRevision": active_revision,
                "file": file,
                "savedRevision": saved_revision,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_llm_pricing_file_info import CustomLLMPricingFileInfo

        d = dict(src_dict)
        active_revision = d.pop("activeRevision")

        file = CustomLLMPricingFileInfo.from_dict(d.pop("file"))

        saved_revision = d.pop("savedRevision")

        status = CustomLLMPricingResponseStatus(d.pop("status"))

        error = d.pop("error", UNSET)

        custom_llm_pricing_response = cls(
            active_revision=active_revision,
            file=file,
            saved_revision=saved_revision,
            status=status,
            error=error,
        )

        custom_llm_pricing_response.additional_properties = d
        return custom_llm_pricing_response

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
