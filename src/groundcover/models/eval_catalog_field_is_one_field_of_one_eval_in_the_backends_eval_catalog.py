from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog_origin import (
    EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogOrigin,
)
from ..models.eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog_type import (
    EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogType,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog")


@_attrs_define
class EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalog:
    """
    Attributes:
        enabled (bool): Enabled is false for an Eval without a configuration or with its configuration off.
        eval_id (str):
        eval_key (str):
        eval_name (str):
        key (str): Key names the field in filters and results.
        name (str): Name is the display label.
        origin (EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogOrigin): built_in EvalBuiltIn
            user_created EvalUserCreated
        revision (str): Revision is the executable revision whose results are current (64 lowercase hex characters).
        type_ (EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogType): boolean EvalBoolean
            text EvalText
            integer EvalInteger
            float EvalFloat
            enum EvalEnum
        configuration_epoch (int | Unset): ConfigurationEpoch changes each time the Eval's configuration changes.
        definition_version (str | Unset): DefinitionVersion is the version of a built-in Eval definition.
        maximum (float | Unset): Maximum bounds an integer or float field.
        minimum (float | Unset): Minimum bounds an integer or float field.
        namespace (str | Unset): Namespace groups built-in Evals.
        options (list[str] | Unset): Options are the allowed values of an enum field.
    """

    enabled: bool
    eval_id: str
    eval_key: str
    eval_name: str
    key: str
    name: str
    origin: EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogOrigin
    revision: str
    type_: EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogType
    configuration_epoch: int | Unset = UNSET
    definition_version: str | Unset = UNSET
    maximum: float | Unset = UNSET
    minimum: float | Unset = UNSET
    namespace: str | Unset = UNSET
    options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        eval_id = self.eval_id

        eval_key = self.eval_key

        eval_name = self.eval_name

        key = self.key

        name = self.name

        origin = self.origin.value

        revision = self.revision

        type_ = self.type_.value

        configuration_epoch = self.configuration_epoch

        definition_version = self.definition_version

        maximum = self.maximum

        minimum = self.minimum

        namespace = self.namespace

        options: list[str] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "evalId": eval_id,
                "evalKey": eval_key,
                "evalName": eval_name,
                "key": key,
                "name": name,
                "origin": origin,
                "revision": revision,
                "type": type_,
            }
        )
        if configuration_epoch is not UNSET:
            field_dict["configurationEpoch"] = configuration_epoch
        if definition_version is not UNSET:
            field_dict["definitionVersion"] = definition_version
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if options is not UNSET:
            field_dict["options"] = options

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
        enabled = d.pop("enabled")

        eval_id = d.pop("evalId")

        eval_key = d.pop("evalKey")

        eval_name = d.pop("evalName")

        key = d.pop("key")

        name = d.pop("name")

        origin = EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogOrigin(d.pop("origin"))

        revision = d.pop("revision")

        type_ = EvalCatalogFieldIsOneFieldOfOneEvalInTheBackendsEvalCatalogType(d.pop("type"))

        configuration_epoch = d.pop("configurationEpoch", UNSET)

        definition_version = d.pop("definitionVersion", UNSET)

        maximum = d.pop("maximum", UNSET)

        minimum = d.pop("minimum", UNSET)

        namespace = d.pop("namespace", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog = cls(
            enabled=enabled,
            eval_id=eval_id,
            eval_key=eval_key,
            eval_name=eval_name,
            key=key,
            name=name,
            origin=origin,
            revision=revision,
            type_=type_,
            configuration_epoch=configuration_epoch,
            definition_version=definition_version,
            maximum=maximum,
            minimum=minimum,
            namespace=namespace,
            options=options,
        )

        eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog.additional_properties = d
        return eval_catalog_field_is_one_field_of_one_eval_in_the_backends_eval_catalog

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
