from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SessionMetrics")


@_attrs_define
class SessionMetrics:
    """
    Attributes:
        cls (float | Unset):
        fcp (float | Unset):
        inp (float | Unset):
        lcp (float | Unset):
        page_load_time (float | Unset):
        ttfb (float | Unset):
    """

    cls: float | Unset = UNSET
    fcp: float | Unset = UNSET
    inp: float | Unset = UNSET
    lcp: float | Unset = UNSET
    page_load_time: float | Unset = UNSET
    ttfb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cls = self.cls

        fcp = self.fcp

        inp = self.inp

        lcp = self.lcp

        page_load_time = self.page_load_time

        ttfb = self.ttfb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cls is not UNSET:
            field_dict["cls"] = cls
        if fcp is not UNSET:
            field_dict["fcp"] = fcp
        if inp is not UNSET:
            field_dict["inp"] = inp
        if lcp is not UNSET:
            field_dict["lcp"] = lcp
        if page_load_time is not UNSET:
            field_dict["pageLoadTime"] = page_load_time
        if ttfb is not UNSET:
            field_dict["ttfb"] = ttfb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        cls = d.pop("cls", UNSET)

        fcp = d.pop("fcp", UNSET)

        inp = d.pop("inp", UNSET)

        lcp = d.pop("lcp", UNSET)

        page_load_time = d.pop("pageLoadTime", UNSET)

        ttfb = d.pop("ttfb", UNSET)

        session_metrics = cls(
            cls=cls,
            fcp=fcp,
            inp=inp,
            lcp=lcp,
            page_load_time=page_load_time,
            ttfb=ttfb,
        )

        session_metrics.additional_properties = d
        return session_metrics

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
