"""ConditionSet fluent builder for the groundcover SDK."""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Dict, List

from groundcover.types.conditions import (
    CONDITION_KEY_REASON,
    CONDITION_KEY_TYPE,
    CONDITION_ORIGIN_ROOT,
    CONDITION_TYPE_BOOL,
    CONDITION_TYPE_DATETIME,
    CONDITION_TYPE_FLOAT64,
    CONDITION_TYPE_INT64,
    CONDITION_TYPE_STRING,
    CONDITION_TYPE_STRING_ARRAY,
    CONDITION_VALUE_OOM_KILLED,
    CONDITION_VALUE_TYPE_CONTAINER_CRASH,
    OPERATOR_EQUAL,
)


class ConditionSet:
    """Fluent builder for constructing a list of conditions.

    Uses default values for origin, type, and operator which can be overridden.

    Example::

        from groundcover.utils import ConditionSet

        conditions = (
            ConditionSet()
            .add("namespace", "production")
            .add("reason", "OOMKilled")
            .add_oom_event_conditions()
            .build()
        )
    """

    def __init__(
        self,
        default_origin: str = CONDITION_ORIGIN_ROOT,
        default_cond_type: str = CONDITION_TYPE_STRING,
        default_operator: str = OPERATOR_EQUAL,
    ) -> None:
        self._conditions: List[Dict[str, Any]] = []
        self._default_origin = default_origin
        self._default_cond_type = default_cond_type
        self._default_operator = default_operator

    def add(self, key: str, value: Any) -> ConditionSet:
        """Add a condition, inferring the type from the Python value type.

        Supports: str, list[str], int, float, bool, datetime.
        """
        value_str, cond_type = self._infer_type(value)
        return self._add_internal(key, self._default_origin, cond_type, value_str, self._default_operator)

    def add_full(
        self,
        key: str,
        origin: str,
        cond_type: str,
        value: str,
        operator: str,
    ) -> ConditionSet:
        """Add a condition with explicit origin, type, operator, and value."""
        return self._add_internal(key, origin, cond_type, value, operator)

    def add_raw(self, condition: Dict[str, Any]) -> ConditionSet:
        """Add a pre-constructed condition dict directly."""
        self._conditions.append(condition)
        return self

    def add_oom_event_conditions(self) -> ConditionSet:
        """Add predefined conditions to identify OOM events.

        Adds reason=OOMKilled and type=container_crash.
        """
        self.add(CONDITION_KEY_REASON, CONDITION_VALUE_OOM_KILLED)
        self.add(CONDITION_KEY_TYPE, CONDITION_VALUE_TYPE_CONTAINER_CRASH)
        return self

    def build(self) -> List[Dict[str, Any]]:
        """Return the final list of condition dicts."""
        return list(self._conditions)

    def _add_internal(
        self,
        key: str,
        origin: str,
        cond_type: str,
        value: str,
        operator: str,
    ) -> ConditionSet:
        condition = {
            "key": key,
            "origin": origin,
            "type": cond_type,
            "filters": [{"op": operator, "value": value}],
        }
        self._conditions.append(condition)
        return self

    def _infer_type(self, value: Any) -> tuple:
        """Infer condition type and string value from a Python value.

        Returns (value_str, cond_type).
        """
        if isinstance(value, str):
            return value, CONDITION_TYPE_STRING
        if isinstance(value, bool):
            # Must check bool before int since bool is a subclass of int
            return str(value).lower(), CONDITION_TYPE_BOOL
        if isinstance(value, int):
            return str(value), CONDITION_TYPE_INT64
        if isinstance(value, float):
            return str(value), CONDITION_TYPE_FLOAT64
        if isinstance(value, datetime):
            return value.isoformat(), CONDITION_TYPE_DATETIME
        if isinstance(value, (list, tuple)):
            # Assume list of strings
            return json.dumps(list(value)), CONDITION_TYPE_STRING_ARRAY
        # Fallback
        return str(value), self._default_cond_type
