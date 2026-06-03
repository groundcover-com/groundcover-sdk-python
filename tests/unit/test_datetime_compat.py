"""Tests for _datetime_compat.parse_datetime."""

from __future__ import annotations

import datetime

from groundcover._datetime_compat import parse_datetime


class TestParseDatetime:
    """Tests for fractional-second normalization and Z suffix handling."""

    def test_six_digit_fraction_passthrough(self):
        result = parse_datetime("2024-01-15T10:30:00.123456+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123456, tzinfo=datetime.timezone.utc)

    def test_three_digit_fraction_padded(self):
        result = parse_datetime("2024-01-15T10:30:00.123+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123000, tzinfo=datetime.timezone.utc)

    def test_one_digit_fraction_padded(self):
        result = parse_datetime("2024-01-15T10:30:00.1+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 100000, tzinfo=datetime.timezone.utc)

    def test_two_digit_fraction_padded(self):
        result = parse_datetime("2024-01-15T10:30:00.12+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 120000, tzinfo=datetime.timezone.utc)

    def test_four_digit_fraction_padded(self):
        result = parse_datetime("2024-01-15T10:30:00.1234+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123400, tzinfo=datetime.timezone.utc)

    def test_five_digit_fraction_padded(self):
        result = parse_datetime("2024-01-15T10:30:00.12345+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123450, tzinfo=datetime.timezone.utc)

    def test_seven_digit_fraction_truncated(self):
        result = parse_datetime("2024-01-15T10:30:00.1234567+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123456, tzinfo=datetime.timezone.utc)

    def test_nine_digit_fraction_truncated(self):
        result = parse_datetime("2024-01-15T10:30:00.123456789+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123456, tzinfo=datetime.timezone.utc)

    def test_no_fraction(self):
        result = parse_datetime("2024-01-15T10:30:00+00:00")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 0, tzinfo=datetime.timezone.utc)

    def test_z_suffix_replaced(self):
        result = parse_datetime("2024-01-15T10:30:00.123456Z")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123456, tzinfo=datetime.timezone.utc)

    def test_z_suffix_with_short_fraction(self):
        result = parse_datetime("2024-01-15T10:30:00.1234Z")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123400, tzinfo=datetime.timezone.utc)

    def test_z_suffix_with_long_fraction(self):
        result = parse_datetime("2024-01-15T10:30:00.123456789Z")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 123456, tzinfo=datetime.timezone.utc)

    def test_z_suffix_no_fraction(self):
        result = parse_datetime("2024-01-15T10:30:00Z")
        assert result == datetime.datetime(2024, 1, 15, 10, 30, 0, 0, tzinfo=datetime.timezone.utc)
