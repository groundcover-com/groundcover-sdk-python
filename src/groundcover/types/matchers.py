"""Match type enum for the groundcover SDK."""

from enum import Enum


class MatchType(str, Enum):
    """Match types for silence matchers."""

    EQUAL = "="
    NOT_EQUAL = "!="
    REGEX = "=~"
    NOT_REGEX = "!~"
