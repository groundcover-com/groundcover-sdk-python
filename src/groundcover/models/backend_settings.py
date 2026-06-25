from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backend_settings_gcp_pubsub_topic import BackendSettingsGcpPubsubTopic
    from ..models.endpoint import Endpoint
    from ..models.integrations import Integrations


T = TypeVar("T", bound="BackendSettings")


@_attrs_define
class BackendSettings:
    """
    Attributes:
        cloud (str | Unset):
        endpoints (list[Endpoint] | Unset):
        gcp_pubsub_topic (BackendSettingsGcpPubsubTopic | Unset):
        integrations (Integrations | Unset):
        nat_ips (list[str] | Unset):
        region (str | Unset):
    """

    cloud: str | Unset = UNSET
    endpoints: list[Endpoint] | Unset = UNSET
    gcp_pubsub_topic: BackendSettingsGcpPubsubTopic | Unset = UNSET
    integrations: Integrations | Unset = UNSET
    nat_ips: list[str] | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud = self.cloud

        endpoints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = []
            for endpoints_item_data in self.endpoints:
                endpoints_item = endpoints_item_data.to_dict()
                endpoints.append(endpoints_item)

        gcp_pubsub_topic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_pubsub_topic, Unset):
            gcp_pubsub_topic = self.gcp_pubsub_topic.to_dict()

        integrations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = self.integrations.to_dict()

        nat_ips: list[str] | Unset = UNSET
        if not isinstance(self.nat_ips, Unset):
            nat_ips = self.nat_ips

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud is not UNSET:
            field_dict["cloud"] = cloud
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if gcp_pubsub_topic is not UNSET:
            field_dict["gcp_pubsub_topic"] = gcp_pubsub_topic
        if integrations is not UNSET:
            field_dict["integrations"] = integrations
        if nat_ips is not UNSET:
            field_dict["nat_ips"] = nat_ips
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backend_settings_gcp_pubsub_topic import BackendSettingsGcpPubsubTopic
        from ..models.endpoint import Endpoint
        from ..models.integrations import Integrations

        d = dict(src_dict)
        cloud = d.pop("cloud", UNSET)

        _endpoints = d.pop("endpoints", UNSET)
        endpoints: list[Endpoint] | Unset = UNSET
        if _endpoints is not UNSET:
            endpoints = []
            for endpoints_item_data in _endpoints:
                endpoints_item = Endpoint.from_dict(endpoints_item_data)

                endpoints.append(endpoints_item)

        _gcp_pubsub_topic = d.pop("gcp_pubsub_topic", UNSET)
        gcp_pubsub_topic: BackendSettingsGcpPubsubTopic | Unset
        if isinstance(_gcp_pubsub_topic, Unset) or _gcp_pubsub_topic is None:
            gcp_pubsub_topic = UNSET
        else:
            gcp_pubsub_topic = BackendSettingsGcpPubsubTopic.from_dict(_gcp_pubsub_topic)

        _integrations = d.pop("integrations", UNSET)
        integrations: Integrations | Unset
        if isinstance(_integrations, Unset) or _integrations is None:
            integrations = UNSET
        else:
            integrations = Integrations.from_dict(_integrations)

        nat_ips = cast(list[str], d.pop("nat_ips", UNSET))

        region = d.pop("region", UNSET)

        backend_settings = cls(
            cloud=cloud,
            endpoints=endpoints,
            gcp_pubsub_topic=gcp_pubsub_topic,
            integrations=integrations,
            nat_ips=nat_ips,
            region=region,
        )

        backend_settings.additional_properties = d
        return backend_settings

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
