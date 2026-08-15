from datetime import datetime, timedelta
from src.utils.date_ops import (
    format_iso_date,
    parse_date_string,
    add_days_to_date,
    calculate_days_between,
    get_relative_time_string,
)

def test_format_iso_date():
    dt = datetime(2026, 8, 15)
    assert format_iso_date(dt) == "2026-08-15"
    assert len(format_iso_date()) == 10

def test_parse_date_string():
    dt = parse_date_string("2026-08-15")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 8 and dt.day == 15
    assert parse_date_string("invalid-date") is None

def test_add_days_and_between():
    dt1 = datetime(2026, 8, 15)
    dt2 = add_days_to_date(dt1, 5)
    assert format_iso_date(dt2) == "2026-08-20"
    assert calculate_days_between(dt1, dt2) == 5

def test_get_relative_time_string():
    now = datetime(2026, 8, 15, 12, 0, 0)
    assert get_relative_time_string(now - timedelta(seconds=30), now) == "방금 전"
    assert get_relative_time_string(now - timedelta(minutes=5), now) == "5분 전"
    assert get_relative_time_string(now - timedelta(hours=2), now) == "2시간 전"
    assert get_relative_time_string(now - timedelta(days=3), now) == "3일 전"
    assert get_relative_time_string(now + timedelta(days=1), now) == "미래"
