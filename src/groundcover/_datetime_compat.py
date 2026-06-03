"""Python <3.11 compatible datetime parsing."""

from __future__ import annotations

import datetime
import re


def parse_datetime(value: str) -> datetime.datetime:
    """Parse an ISO 8601 datetime string, compatible with Python 3.9+.

    Handles two issues with Python <3.11's fromisoformat():
    - Doesn't accept 'Z' UTC suffix (only +00:00)
    - Only accepts 0, 3, or 6 fractional second digits (normalizes to 6)
    """
    value = value.replace("Z", "+00:00")
    value = re.sub(r"\.(\d+)", lambda m: "." + m.group(1)[:6].ljust(6, "0"), value)
    return datetime.datetime.fromisoformat(value)
