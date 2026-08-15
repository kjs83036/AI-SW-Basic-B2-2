"""날짜 및 시간 포맷팅/계산 유틸리티 모듈 (팀원 C 담당)."""

from datetime import datetime, timedelta
from typing import Optional


def format_iso_date(dt: Optional[datetime] = None) -> str:
    """datetime 객체를 ISO 8601 형식(YYYY-MM-DD)으로 포맷팅합니다."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d")


def parse_date_string(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[datetime]:
    """문자열을 datetime 객체로 파싱합니다. 실패 시 None을 반환합니다."""
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        return None


def add_days_to_date(dt: datetime, days: int) -> datetime:
    """지정된 날짜에 일(days) 수를 더하거나 뺍니다."""
    return dt + timedelta(days=days)


def calculate_days_between(start_dt: datetime, end_dt: datetime) -> int:
    """두 날짜 사이의 일수 차이를 계산합니다."""
    return abs((end_dt - start_dt).days)


def get_relative_time_string(target_dt: datetime, now_dt: Optional[datetime] = None) -> str:
    """지정된 날짜와 현재 시점 간의 상대적 시간 표현을 반환합니다."""
    if now_dt is None:
        now_dt = datetime.now()

    diff = now_dt - target_dt
    seconds = int(diff.total_seconds())

    if seconds < 0:
        return "미래"
    if seconds < 60:
        return "방금 전"
    if seconds < 3600:
        return f"{seconds // 60}분 전"
    if seconds < 86400:
        return f"{seconds // 3600}시간 전"
    return f"{diff.days}일 전"
