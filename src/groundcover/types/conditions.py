"""Condition constants for the groundcover SDK."""

# Condition fields
CONDITION_ORIGIN_ROOT = "root"

# Condition keys
CONDITION_KEY_NAMESPACE = "namespace"
CONDITION_KEY_WORKLOAD = "workload"
CONDITION_KEY_POD_NAME = "podName"
CONDITION_KEY_REASON = "reason"
CONDITION_KEY_TYPE = "type"
CONDITION_KEY_ENV = "env"
CONDITION_KEY_INSTANCE = "instance"

# Condition values
CONDITION_VALUE_OOM_KILLED = "OOMKilled"
CONDITION_VALUE_TYPE_CONTAINER_CRASH = "container_crash"

# Filter operators
OPERATOR_EQUAL = "eq"
OPERATOR_NOT_EQUAL = "ne"
OPERATOR_CONTAINS = "contains"
OPERATOR_NOT_CONTAINS = "notcontains"
OPERATOR_CONTAINS_IGNORE_CASE = "icontains"
OPERATOR_NOT_CONTAINS_IGNORE_CASE = "inotcontains"
OPERATOR_STARTS_WITH = "startswith"
OPERATOR_STARTS_WITH_IGNORE_CASE = "istartswith"

# Condition types
CONDITION_TYPE_STRING = "string"
CONDITION_TYPE_INT64 = "int64"
CONDITION_TYPE_FLOAT64 = "float64"
CONDITION_TYPE_BOOL = "bool"
CONDITION_TYPE_DATETIME = "datetime"
CONDITION_TYPE_STRING_ARRAY = "string_array"
