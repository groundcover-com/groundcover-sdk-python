from __future__ import annotations

from enum import Enum


class TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressionsType(
    str, Enum
):
    DATETIME_EXTRACT = "datetime_extract"
    JSON_UNPACK = "json_unpack"

    def __str__(self) -> str:
        return str(self.value)
