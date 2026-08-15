"""문자열 변환 및 파싱 유틸리티 모듈 (팀원 B 담당)."""

import re


def capitalize_words(text: str) -> str:
    """각 단어의 첫 글자를 대문자로 변환합니다."""
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split(" "))


def reverse_string(text: str) -> str:
    """문자열을 역순으로 뒤집습니다."""
    return text[::-1]


def strip_all_whitespace(text: str) -> str:
    """문자열 내 모든 공백(스페이스, 탭, 줄바꿈)을 제거합니다."""
    if not text:
        return ""
    return "".join(text.split())


def to_snake_case(text: str) -> str:
    """CamelCase 또는 일반 문장을 snake_case로 변환합니다."""
    if not text:
        return ""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    s3 = re.sub(r"[\s\-]+", "_", s2)
    return s3.lower()


def slugify(text: str) -> str:
    """URL 친화적인 slug 문자열로 변환합니다."""
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """지정된 단어 수를 초과하는 문자열을 축약합니다."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + suffix
