"""Custom Duration type for the groundcover SDK.

Handles Go-style duration string parsing and serialization (e.g., '5m', '1h30m', '10s').
"""

from __future__ import annotations

import re
from datetime import timedelta
from typing import Any

# Regex for parsing Go-style duration strings.
# Supports optional leading '-' for negative durations and units: h, m, s, ms, us/µs, ns.
_DURATION_RE = re.compile(
    r"^(-)?(?:(\d+)h)?(?:(\d+)m)?(?:(\d+(?:\.\d+)?)s)?(?:(\d+)ms)?(?:(\d+)(?:us|µs))?(?:(\d+)ns)?$"
)


def _parse_go_duration(s: str) -> timedelta:
    """Parse a Go-style duration string like '5m0s', '1h30m', '500ms', '-1s' into timedelta."""
    s = s.strip()
    if s == "0" or s == "0s":
        return timedelta()

    match = _DURATION_RE.match(s)
    if not match:
        raise ValueError(f"Invalid Go duration string: {s!r}")

    negative = match.group(1) is not None
    hours = int(match.group(2) or 0)
    minutes = int(match.group(3) or 0)
    seconds = float(match.group(4) or 0)
    milliseconds = int(match.group(5) or 0)
    microseconds = int(match.group(6) or 0)
    nanoseconds = int(match.group(7) or 0)

    td = timedelta(
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        milliseconds=milliseconds,
        microseconds=microseconds + nanoseconds / 1000,
    )
    return -td if negative else td


def _format_go_duration(td: timedelta) -> str:
    """Format a timedelta as a Go-style duration string.

    Preserves sub-second components (ms, us) like Go's time.Duration.String().
    """
    total_us = round(td / timedelta(microseconds=1))
    if total_us == 0:
        return "0s"

    parts: list[str] = []
    if total_us < 0:
        parts.append("-")
        total_us = -total_us

    hours, total_us = divmod(total_us, 3_600_000_000)
    minutes, total_us = divmod(total_us, 60_000_000)
    seconds, total_us = divmod(total_us, 1_000_000)
    milliseconds, microseconds = divmod(total_us, 1_000)

    if hours:
        parts.append(f"{hours}h")
    if minutes or hours:
        parts.append(f"{minutes}m")
    if seconds or minutes or hours:
        parts.append(f"{seconds}s")
    if milliseconds:
        parts.append(f"{milliseconds}ms")
    if microseconds:
        parts.append(f"{microseconds}us")

    return "".join(parts)


class Duration(timedelta):
    """Custom Duration type that serializes to/from Go-style duration strings.

    Used in monitor models for PendingFor, etc.

    Examples:
        >>> Duration.from_string("5m0s")
        Duration(seconds=300)
        >>> str(Duration(minutes=5))
        '5m0s'
    """

    @classmethod
    def from_string(cls, s: str) -> Duration:
        """Parse a Go-style duration string."""
        td = _parse_go_duration(s)
        return cls(seconds=td.total_seconds())

    def __str__(self) -> str:
        return _format_go_duration(self)

    def __repr__(self) -> str:
        return f"Duration({super().__repr__()})"

    @classmethod
    def from_value(cls, value: Any) -> Duration:
        """Convert various types to Duration."""
        if isinstance(value, cls):
            return value
        if isinstance(value, timedelta):
            return cls(seconds=value.total_seconds())
        if isinstance(value, str):
            return cls.from_string(value)
        if isinstance(value, (int, float)):
            return cls(seconds=value)
        raise ValueError(f"Cannot convert {type(value).__name__} to Duration")
