"""Date and time utility functions."""
from datetime import datetime, timedelta
from typing import Optional

def format_iso_date(dt: Optional[datetime] = None) -> str:
    """날짜를 ISO 포맷(YYYY-MM-DD)으로 변환합니다."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d")

def parse_date_string(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[datetime]:
    """문자열을 datetime 객체로 파싱합니다."""
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        return None

def add_days_to_date(dt: datetime, days: int) -> datetime:
    """날짜에 일수를 더하거나 뺍니다."""
    return dt + timedelta(days=days)

def calculate_days_between(start_dt: datetime, end_dt: datetime) -> int:
    """두 날짜 사이의 일수 차이를 계산합니다."""
    return abs((end_dt - start_dt).days)

def get_relative_time_string(target_dt: datetime, now_dt: Optional[datetime] = None) -> str:
    """상대 시간 문자열을 반환합니다 (예: '방금 전', '5분 전', '2시간 전', '3일 전')."""
    if now_dt is None:
        now_dt = datetime.now()
    diff = now_dt - target_dt
    seconds = int(diff.total_seconds())
    if seconds < 0:
        return "미래"
    if seconds < 60:
        return "방금 전"
    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes}분 전"
    hours = minutes // 60
    if hours < 24:
        return f"{hours}시간 전"
    days = hours // 24
    return f"{days}일 전"
