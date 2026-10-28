from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_report import ImportReport


T = TypeVar("T", bound="CustomLLMPricingFileInfo")


@_attrs_define
class CustomLLMPricingFileInfo:
    """
    Attributes:
        filename (str):
        model_count (int):
        report (ImportReport):
        uploaded_at (datetime.datetime):
        uploaded_by (str):
    """

    filename: str
    model_count: int
    report: ImportReport
    uploaded_at: datetime.datetime
    uploaded_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        model_count = self.model_count

        report = self.report.to_dict()

        uploaded_at = self.uploaded_at.isoformat()

        uploaded_by = self.uploaded_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "modelCount": model_count,
                "report": report,
                "uploadedAt": uploaded_at,
                "uploadedBy": uploaded_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_report import ImportReport

        d = dict(src_dict)
        filename = d.pop("filename")

        model_count = d.pop("modelCount")

        report = ImportReport.from_dict(d.pop("report"))

        uploaded_at = parse_datetime(d.pop("uploadedAt"))

        uploaded_by = d.pop("uploadedBy")

        custom_llm_pricing_file_info = cls(
            filename=filename,
            model_count=model_count,
            report=report,
            uploaded_at=uploaded_at,
            uploaded_by=uploaded_by,
        )

        custom_llm_pricing_file_info.additional_properties = d
        return custom_llm_pricing_file_info

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
