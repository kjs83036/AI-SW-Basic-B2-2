from datetime import datetime, timedelta
import pytest
from src.utils.date_ops import (
    add_days_to_date,
    calculate_days_between,
    format_iso_date,
    get_relative_time_string,
    parse_date_string,
)


def test_format_iso_date():
    dt = datetime(2026, 8, 14, 15, 30, 0)
    assert format_iso_date(dt) == "2026-08-14"


def test_parse_date_string():
    parsed = parse_date_string("2026-08-14")
    assert parsed is not None
    assert parsed.year == 2026
    assert parsed.month == 8
    assert parsed.day == 14
    assert parse_date_string("invalid-date") is None


def test_add_days_and_between():
    start = datetime(2026, 8, 1)
    end = add_days_to_date(start, 10)
    assert end.day == 11
    assert calculate_days_between(start, end) == 10


def test_get_relative_time_string():
    now = datetime(2026, 8, 14, 12, 0, 0)
    past_10s = now - timedelta(seconds=10)
    past_5m = now - timedelta(minutes=5)
    past_2h = now - timedelta(hours=2)
    past_3d = now - timedelta(days=3)
    future = now + timedelta(minutes=10)

    assert get_relative_time_string(past_10s, now) == "방금 전"
    assert get_relative_time_string(past_5m, now) == "5분 전"
    assert get_relative_time_string(past_2h, now) == "2시간 전"
    assert get_relative_time_string(past_3d, now) == "3일 전"
    assert get_relative_time_string(future, now) == "미래"
