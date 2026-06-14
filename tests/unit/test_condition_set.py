"""Tests for groundcover.utils.condition_set."""

from __future__ import annotations

import json
from datetime import datetime

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
from groundcover.utils.condition_set import ConditionSet


class TestConditionSet:
    def test_add_string(self) -> None:
        conditions = ConditionSet().add("namespace", "production").build()
        assert len(conditions) == 1
        assert conditions[0]["key"] == "namespace"
        assert conditions[0]["origin"] == CONDITION_ORIGIN_ROOT
        assert conditions[0]["type"] == CONDITION_TYPE_STRING
        assert conditions[0]["filters"][0]["op"] == OPERATOR_EQUAL
        assert conditions[0]["filters"][0]["value"] == "production"

    def test_add_int(self) -> None:
        conditions = ConditionSet().add("count", 42).build()
        assert conditions[0]["type"] == CONDITION_TYPE_INT64
        assert conditions[0]["filters"][0]["value"] == "42"

    def test_add_float(self) -> None:
        conditions = ConditionSet().add("ratio", 3.14).build()
        assert conditions[0]["type"] == CONDITION_TYPE_FLOAT64
        assert conditions[0]["filters"][0]["value"] == "3.14"

    def test_add_bool(self) -> None:
        conditions = ConditionSet().add("enabled", True).build()
        assert conditions[0]["type"] == CONDITION_TYPE_BOOL
        assert conditions[0]["filters"][0]["value"] == "true"

    def test_add_bool_false(self) -> None:
        conditions = ConditionSet().add("enabled", False).build()
        assert conditions[0]["type"] == CONDITION_TYPE_BOOL
        assert conditions[0]["filters"][0]["value"] == "false"

    def test_add_datetime(self) -> None:
        dt = datetime(2024, 1, 15, 10, 30, 0)
        conditions = ConditionSet().add("timestamp", dt).build()
        assert conditions[0]["type"] == CONDITION_TYPE_DATETIME
        assert "2024-01-15" in conditions[0]["filters"][0]["value"]

    def test_add_string_array(self) -> None:
        conditions = ConditionSet().add("namespaces", ["prod", "staging"]).build()
        assert conditions[0]["type"] == CONDITION_TYPE_STRING_ARRAY
        parsed = json.loads(conditions[0]["filters"][0]["value"])
        assert parsed == ["prod", "staging"]

    def test_chaining(self) -> None:
        conditions = ConditionSet().add("namespace", "production").add("workload", "api-server").build()
        assert len(conditions) == 2
        assert conditions[0]["key"] == "namespace"
        assert conditions[1]["key"] == "workload"

    def test_add_full(self) -> None:
        conditions = ConditionSet().add_full("name", "custom_origin", "string", "test-value", "contains").build()
        assert len(conditions) == 1
        assert conditions[0]["origin"] == "custom_origin"
        assert conditions[0]["type"] == "string"
        assert conditions[0]["filters"][0]["op"] == "contains"

    def test_add_raw(self) -> None:
        raw = {
            "key": "custom",
            "origin": "root",
            "type": "string",
            "filters": [{"op": "eq", "value": "val"}],
        }
        conditions = ConditionSet().add_raw(raw).build()
        assert len(conditions) == 1
        assert conditions[0] == raw

    def test_add_oom_event_conditions(self) -> None:
        conditions = ConditionSet().add_oom_event_conditions().build()
        assert len(conditions) == 2
        assert conditions[0]["key"] == CONDITION_KEY_REASON
        assert conditions[0]["filters"][0]["value"] == CONDITION_VALUE_OOM_KILLED
        assert conditions[1]["key"] == CONDITION_KEY_TYPE
        assert conditions[1]["filters"][0]["value"] == CONDITION_VALUE_TYPE_CONTAINER_CRASH

    def test_build_returns_copy(self) -> None:
        cs = ConditionSet().add("key", "value")
        result1 = cs.build()
        result2 = cs.build()
        assert result1 is not result2
        assert result1 == result2
